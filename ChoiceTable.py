from acces import*
from CharacterCore import ChoiceReference, FiniteStateMachine

class Classes(ChoiceReference):
    stateFile = "data/character/state_Classes.yaml"

class Subrace_Dwarf(ChoiceReference):
    stateFile = "data/character/state_Subrace_Dwarf.yaml"

class Races(ChoiceReference):
    stateFile = "data/character/state_Races.yaml"
    
    def enterDwarf(self):
        self.subrace = Subrace_Dwarf(getUI("ComboBox_Subrace"))
    def exitDwarf(self):
        self.subrace.destroy()
        del self.subrace

class PrimaryState(FiniteStateMachine):
    stateFile = "data/character/state_ValueTable.yaml"


class ChoiceTable:
    def __init__(self):
        self.raceSelect = Races(getUI("ComboBox_Race"))
        self.classSelect = Classes(getUI("ComboBox_Class"))
        self.baseState = PrimaryState()
        self.baseState.initFSM()
        self.baseState.request("On")
