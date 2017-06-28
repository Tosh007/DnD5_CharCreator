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
        if parent:
            parent = self.table[parent]
        if sname[-4:]==".UI.":
            sname = sname[:-4]
            ui = getUI("checkBox_"+sname)
            c = ValueConfig
        else:
            c = getConfig("ProficiencyListConfig")
            ui = getUI("listWidget_proficiencies")
        if hasChildren:
            c = getConfig("HiddenValue")

        valueref = ValueReference(ui, c, name)
        valueref.set(initial)
        getValueTable().__dict__["prof_"+sname] = valueref
        self.table[sname] = Proficiency(name, parent, valueref)
        return sname

    def __getattr__(self,name):
        return self.table[name]
