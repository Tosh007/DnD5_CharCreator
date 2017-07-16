import yaml
from collections import *
from CharacterCore import*
from acces import *
from PyQt5.QtCore import Qt

class ProficiencyTable:
    def __init__(self):
        self.table = {}
        f = open(getDirectoryPrefix()+"data/character/proficiency.yaml")
        y = yaml.load(f)
        f.close()
        self.table = {}
        self.childTable = defaultdict(list)
        self.loadProficiency(y)

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
            ui = getUI("checkBox_"+sname)
            c = getConfig("ProficiencyConfig")(sname, parent)
        else:
            if sname[-6:]==".LANG.":
                sname = sname[:-6]
                name = name[:-6]
                ui = getUI("listWidget_languages")
            else:
                ui = getUI("listWidget_proficiencies")
            c = getConfig("ProficiencyListConfig")(sname, parent)
        if hasChildren:
            c = getConfig("ProficiencyCategoryConfig")(sname, parent)
        valueref = ValueReference(ui, c, name)
        getValue("listWidget_proficiencies_update").connect(valueref)
        vt=getValueTable()
        vt.newValue("prof_"+sname,valueref)
        if initial>0:
            getModifier("plus1").connect(valueref)
        if parent:
            self.childTable[parent].append(sname)
        return sname

    def _createPropagateModifier(self,parentLearn):
        return ValueModifier(lambda x,parent=parentLearn:x+getValue(parent).get(),"",0)

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
