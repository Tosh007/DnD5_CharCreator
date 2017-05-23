from CharacterCore import ValueReference, ValueConfig, ValueModifier, ChoiceReference, FiniteStateMachine, Proficiency
import yaml

class ProficiencyTable:
    def __init__(self,Values,UI):
        global values,ui
        values = Values
        ui = UI
        self.table = {}
        f = open("proficiency.yaml")
        y = yaml.load(f)
        f.close()
        self.loadProficiency(y)
        
    def loadProficiency(self, data, parent=None):
        # always a list as toplevel structure
        for obj in data:
            if type(obj) is str:
                # just a new proficiency
                self.newProficiency(obj,parent, obj.replace(" ","_"))
                print(obj)
            elif type(obj) is dict:
                # a new proficiency with at least one subcategory
                assert len(obj.keys())==1
                name = tuple(obj.keys())[0]
                print(name+":")
                sname=name.replace(" ", "_")
                self.newProficiency(name, parent, sname)
                self.loadProficiency(obj[name],parent=sname)

    def newProficiency(self, name, parent, attrName, valueref=None):
        if parent:
            parent = self.table[parent]
        self.table[attrName] = Proficiency(name, parent, valueref)

    def __getattr__(self,name):
        return self.table[name]

if __name__=="__main__":
    p=ProficiencyTable(None,None)