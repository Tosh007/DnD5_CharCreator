try:
    from acces import*
    from CharacterCore import ChoiceReference, FiniteStateMachine
except ImportError:
    from program.acces import*
    from program.CharacterCore import*
class StateTable:
    class Classes(ChoiceReference):
        stateFile = "data/character/state_Classes.yaml"

    class Subrace_Dwarf(ChoiceReference):
        stateFile = "data/character/state_Subrace_Dwarf.yaml"

    class Subrace_Elf(ChoiceReference):
        stateFile = "data/character/state_Subrace_Elf.yaml"

    class Races(ChoiceReference):
        stateFile = "data/character/state_Races.yaml"
        #def enterDwarf(self):
        #    self.subrace = Subrace_Dwarf(getUI("ComboBox_Subrace"))
        #def exitDwarf(self):
        #    self.subrace.destroy()
        #    del self.subrace
        def enter(self,state):
            if state=="Off":return
            try:
                choice = getChoice("Subrace_"+state)
            except:return
            self.subrace = choice(getUI("ComboBox_Subrace"))
        def exit(self,state):
            if hasattr(self,"subrace"):
                self.subrace.destroy()
                del self.subrace

    class PrimaryState(FiniteStateMachine):
        stateFile = "data/character/state_ValueTable.yaml"

class ChoiceTable:
    def __init__(self):
        self.raceSelect = StateTable.Races(getUI("ComboBox_Race"))
        self.classSelect = StateTable.Classes(getUI("ComboBox_Class"))
        self.baseState = StateTable.PrimaryState()
        self.baseState.initFSM()
        self.baseState.request("On")
    def __getattr__(self,name):
        return getattr(StateTable,name)
