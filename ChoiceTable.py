from PyQt5.QtWidgets import *
try:
    from acces import*
    from CharacterCore import ChoiceReference, FiniteStateMachine, ValueReference,ValueConfig_allow
    from menu_human import Ui_Human
except ImportError:
    from program.acces import*
    from program.CharacterCore import*
    from program.menu_human import Ui_Human
class StateTable:
    class Classes(ChoiceReference):
        stateFile = "data/character/state_Classes.yaml"

    class FeatChoice(ChoiceReference):
        stateFile = "data/character/feats.yaml"

    class Subrace_Dwarf(ChoiceReference):
        stateFile = "data/character/state_Subrace_Dwarf.yaml"

    class Subrace_Elf(ChoiceReference):
        stateFile = "data/character/state_Subrace_Elf.yaml"

    class Subrace_Halfling(ChoiceReference):
        stateFile = "data/character/state_Subrace_Halfling.yaml"

    class Subrace_Gnome(ChoiceReference):
        stateFile = "data/character/state_Subrace_Gnome.yaml"

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

        def enterHuman(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_human = QWidget()
            self.ui_human = Ui_Human()
            self.ui_human.setupUi(self.tab_human)
            self.tab = tabRoot.addTab(self.tab_human, "Human")
            self.ui_human.checkBox_variantTraits.stateChanged.connect(self.altHumanTrait)

        def exitHuman(self):
            self.ui_human.checkBox_variantTraits.setCheckState(False)
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_human.setParent(None)
            del self.tab_human
            del self.ui_human
            del self.tab

        def altHumanTrait(self):
            b = self.ui_human.checkBox_variantTraits.checkState()
            if b:
                self.skill = StateTable.FeatChoice(self.ui_human.comboBox_feat)
            else:
                self.skill.destroy()
                del self.skill

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
