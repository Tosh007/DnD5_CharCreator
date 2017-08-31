import yaml
from collections import *
from CharacterCore import*
from acces import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class ProficiencyTable:
    def __init__(self):
        self.table = {}
        f = open(getDirectoryPrefix()+"data/character/proficiency.yaml")
        y = yaml.load(f)
        f.close()
        self.table = {}
        self.childTable = defaultdict(list)
        self.loadProficiency(y)
        f = open(getDirectoryPrefix()+"data/character/spellList.yaml")
        y = yaml.load(f)
        f.close()
        self.loadProficiency(y)
        l = open(getDirectoryPrefix()+"data/character/language.yaml")
        whoSpeaksWhat = yaml.load(l)
        l.close()
        self.whoSpeaksWhat={}
        for key in whoSpeaksWhat:
            value = whoSpeaksWhat[key]
            key= key.replace(" ","_").lower()
            self.whoSpeaksWhat[key]=value

    def loadProficiency(self, data, parent=None):
        # always a list as toplevel structure
        for obj in data:
            if type(obj) is str:
                # just a new proficiency
                self.newProficiency(obj,parent)
            elif type(obj) is dict:
                # a new category with subproficiencies
                assert len(obj.keys())==1
                name = tuple(obj.keys())[0]
                attr=self.newProficiency(name, parent, True)
                self.loadProficiency(obj[name],attr)

    def newProficiency(self, name, parent, hasChildren=False):
        if name[-1]=="!":
            initial = 1
            name  = name[:-1]
        else:
            initial=0
        sname=name.replace(" ", "_")
        if sname[-6:]==".SKIL.":
            sname = sname[:-6]
            ui = getUI("checkBox_"+sname)   # QCheckBox
            c = getConfig("ProficiencyConfig")(sname, parent)
        else:
            if sname[-6:]==".LANG.":
                sname = sname[:-6]
                name = name[:-6]
                ui = getUI("treeWidget_languages")
            elif sname[-7:]==".SPELL.":
                sname = sname[:-7]
                name = name[:-7]
                ui = getUI("treeWidget_spells")
            else:
                ui = getUI("treeWidget_proficiencies")
            c = getConfig("ProficiencyListConfig")(sname, parent)
        if hasChildren:
            c = getConfig("ProficiencyCategoryConfig")(sname, parent)
            if sname == "skills" or sname == "saving_throws":
                c = getConfig("HiddenValue")
        if isinstance(ui, QtWidgets.QTreeWidget):
            widget=ui
            if parent:
                ui = QtWidgets.QTreeWidgetItem()
                getValue("prof_"+parent).widget.addChild(ui)
            else:
                ui = QtWidgets.QTreeWidgetItem()
                widget.addTopLevelItem(ui)
        valueref = ValueReference(ui, c, name)
        getValue("listWidget_proficiencies_update").connect(valueref)
        vt=getValueTable()
        vt.newValue("prof_"+sname,valueref)
        if initial>0:
            getModifier("plus1").connect(valueref)
        if parent:
            self.childTable[parent].append(sname)
            self._createPropagateModifier(parent).connect(valueref)
            pv = getValue("prof_"+parent)
            pv.connect(valueref)
            valueref.changeSignal.connect(pv.on_visual_update)
        return sname

    def _createPropagateModifier(self,parentLearn):
        return ValueModifier(lambda x,parent=parentLearn:x+getValue("prof_"+parent).get(),"proficient in category "+parentLearn,0)

    def __getattr__(self,name):
        return self.table[name]

    def addChoice(self, choice):
        name = str(choice)
        assert name not in self.table.keys()
        self.table[name] = choice
        getValue("listWidget_proficiencies_update").changeSignal.emit()

    def removeChoice(self,name, try_=False):
        if try_:
            try:
                del self.table[name]
            except:pass
        else:
            del self.table[name]
        getValue("listWidget_proficiencies_update").changeSignal.emit()

    def getChildProficiencies(self,name):
        if name in self.childTable:
            for child in self.childTable[name]:
                yield child
                for i in self.getChildProficiencies(child):
                    yield i
