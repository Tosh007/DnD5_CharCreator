from PyQt5.QtWidgets import *
from acces import*
from CharacterCore import *
from menu_human import Ui_Human
class StateTable:
    class Classes(ChoiceReference):
        stateFile = "data/character/state_Classes.yaml"

    class Choice2AbilityScore(DependentObject):
        def __init__(self, w):
            self.activeMod = set()
            DependentObject.__init__(self,w)
            self.widget.addItems(("strength","dexterity","constitution","wisdom","intelligence","charisma"))

        def on_changed(self):
            items = self.widget.checkedItems()
            if len(items)>2:
                uncheck = items - self.activeMod
                for i in uncheck:
                    self.widget.setItemWithNameChecked(i,False)
                items = self.widget.checkedItems()
            activate = items - self.activeMod
            getModifier("Human_plus").connect(getValues(activate))
            deactivate = self.activeMod - items
            getModifier("Human_plus").disconnect(getValues(deactivate))
            self.activeMod = items

        def destroy(self):
            self.widget.clear()
            self.on_changed()

    class FeatChoice(ChoiceReference):
        stateFile = "data/character/feats.yaml"

    class Human_SkillChoice(ChoiceReference):
        stateFile = "data/character/skills.yaml"

    class Subrace_Dragonborn(ChoiceReference):
        stateFile = "data/character/dragonborn_ancestry.yaml"

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

        def enter(self,state):
            if state=="Off":return
            try:
                choice = getState("Subrace_"+state)
            except:return
            self.subrace = choice(getUI("ComboBox_Subrace"))
        def exit(self,state):
            if hasattr(self,"subrace"):
                self.subrace.destroy()
                del self.subrace

        def enterHuman(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_human = QWidget()
            self.extra_ui = Ui_Human()
            self.extra_ui.setupUi(self.tab_human)
            self.tab = tabRoot.addTab(self.tab_human, "Human")
            self.extra_ui.checkBox_variantTraits.stateChanged.connect(self.altHumanTrait)

        def exitHuman(self):
            self.extra_ui.checkBox_variantTraits.setCheckState(False)
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_human.setParent(None)
            del self.tab_human
            del self.extra_ui
            del self.tab

        def altHumanTrait(self):
            b = self.extra_ui.checkBox_variantTraits.checkState()
            if b:
                self.skill = StateTable.Human_SkillChoice(self.extra_ui.comboBox_skill)
                self.feat = StateTable.FeatChoice(self.extra_ui.comboBox_feat)
                self.score = StateTable.Choice2AbilityScore(self.extra_ui.comboBox_abilityScore)
                for i in range(self.extra_ui.comboBox_abilityScore.count()):
                    self.extra_ui.comboBox_abilityScore.setItemChecked(i, False)
            else:
                self.score.destroy()
                self.skill.destroy()
                self.feat.destroy()
                del self.score
                del self.feat
                del self.skill

    class PrimaryState(FiniteStateMachine):
        stateFile = "data/character/state_ValueTable.yaml"

class ActiveChoiceTable:
    def __init__(self):
        self.raceSelect = StateTable.Races(getUI("ComboBox_Race"))
        self.classSelect = StateTable.Classes(getUI("ComboBox_Class"))
        self.baseState = StateTable.PrimaryState()
        self.baseState.initFSM()
        self.baseState.request("On")
