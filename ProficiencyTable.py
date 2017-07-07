import yaml

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
        if sname[-4:]==".UI.":
            sname = sname[:-4]
            ui = getUI("checkBox_"+sname)
            c = getConfig("ProficiencyConfig")(sname, parent)
        else:
            c = getConfig("ProficiencyListConfig")(sname, parent)
            ui = getUI("listWidget_proficiencies")


        valueref = ValueReference(ui, c, name)
        vt=getValueTable()
        vt.newValue("prof_"+sname,valueref)
        if initial>0:
            getModifier("plus1").connect(valueref)
        if parent:
            parentLearn = "prof_"+parent+"_learnChildren"
            getValue(parentLearn).connect(valueref)
        if hasChildren:
            learn = ValueReference(None, getConfig("AllowNone"))
            vt.newValue("prof_"+sname+"_learnChildren",learn)
            if parent:
                getValue(parentLearn).connect(learn)
                self._createPropagateModifier(parentLearn).connect(learn)

        #self.table[sname] = Proficiency(name, parent, valueref)  # now longer use seperate proficiency storage
        return sname

    def _createPropagateModifier(self,parentLearn):
        return ValueModifier(lambda x,parent=parentLearn:x+getValue(parent).get(),"",0)

    def __getattr__(self,name):
        return self.table[name]

    def addChoice(self, choice):
        name = str(choice)
        assert name not in self.table.keys()
        self.table[name] = choice

    def removeChoice(self,name):
        del self.table[name]
