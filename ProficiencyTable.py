import yaml
from collections import *
from CharacterCore import*
from acces import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class ProficiencyTable:
    def __init__(self):
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
        f = open(getDirectoryPrefix()+"data/character/spellGroups.yaml")
        y = yaml.load(f)
        f.close()
        self.loadProficiency(y,virtualParent=True)
        l = open(getDirectoryPrefix()+"data/character/language.yaml")
        whoSpeaksWhat = yaml.load(l)
        l.close()
        self.whoSpeaksWhat={}
        for key in whoSpeaksWhat:
            value = whoSpeaksWhat[key]
            key= key.replace(" ","_").lower()
            self.whoSpeaksWhat[key]=value
        # special: spellcasting ability is shown in proficiency/magical ability category, so we need to define this here
        ui = QtWidgets.QTreeWidgetItem()
        getValue("prof_magical_ability").widget.addChild(ui)
        getValueTable().newValue("spellSaveDC", ValueReference(ui, getConfig("AllowNone"),"spell save DC: {2}"))
        ui = QtWidgets.QTreeWidgetItem()
        getValue("prof_magical_ability").widget.addChild(ui)
        getValueTable().newValue("spellAttackMod", ValueReference(ui, getConfig("AllowNone"),"spell attack mod: {2}"))
        getValue("spellSaveDC").set(8)      # because this value is always based on 8 + class.mod
        getValue("spellSaveDC").initial = 8

    def loadProficiency(self, data, parent=None, virtualParent=False):  # "virtual" parent => category only for ProfChoice
        # always a list as toplevel structure
        for obj in data:
            if type(obj) is str:
                # just a new proficiency
                #print(obj)
                if not virtualParent:
                    self.newProficiency(obj,parent)
                else:
                    self.newVirtualProfParent(obj,parent)
            elif type(obj) is dict:
                # a new category with subproficiencies
                assert len(obj.keys())==1
                name = tuple(obj.keys())[0]
                if not virtualParent:   # only if we are actually creating a prof tree
                    attr=self.newProficiency(name, parent, True)
                else:
                    attr = self.newVirtualProfParent(name,parent)
                self.loadProficiency(obj[name],attr,virtualParent)

    def newVirtualProfParent(self,name,parent):
        if name[-1]=="!":
            initial = 1
            name  = name[:-1]
        else:
            initial=0
        sname=name.replace(" ", "_")
        if sname[-6:]==".SKIL.":
            sname = sname[:-6]
        else:
            if sname[-6:]==".LANG.":
                sname = sname[:-6]
            elif sname[-7:]==".SPELL.":
                sname = sname[:-7]
        if parent:
            self.childTable[parent].append(sname)
        return sname

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
                c = getConfig("LanguageProfConfig")(sname, parent)
            elif sname[-7:]==".SPELL.":
                sname = sname[:-7]
                name = name[:-7]
                ui = getUI("treeWidget_spells")
                c = getConfig("ProficiencyListConfig")(sname, parent)
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
            valueref.changeSignal.connect(Signal(pv.on_visual_update))
        return sname

    def _createPropagateModifier(self,parentLearn):
        return ValueModifier(lambda x,parent=parentLearn:x+getValue("prof_"+parent).get(),"proficient in category "+parentLearn,0)

    def __getattr__(self,name):
        return self.table[name]

    def addChoice(self, choice):
        name = choice.name
        if name in self.table.keys():raise KeyError("addChoice({0}) duplicate".format(choice))
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
