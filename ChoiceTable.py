from PyQt5.QtWidgets import *
from acces import*
from CharacterCore import *
from menu_human import Ui_Human
from menu_singleCombobox import Ui_singleCombobox
from menu_singleCheckableCombobox import Ui_singleCheckableCombobox

class StateTable:
    class Classes(ChoiceReference):
        stateFile = "data/character/state_Classes.yaml"

    class Choice2AbilityScore(DependentObject):
        def __init__(self, w, items, mod):
            self.activeMod = set()
            DependentObject.__init__(self,w)
            self.widget.addItems(items)
            self.mod = mod
            for i in range(self.widget.count()):
                self.widget.setItemChecked(i, False)

        def on_changed(self):
            items = self.widget.checkedItems()
            if len(items)>2:
                uncheck = items - self.activeMod
                for i in uncheck:
                    self.widget.setItemWithNameChecked(i,False)
                items = self.widget.checkedItems()
            activate = items - self.activeMod
            self.mod.connect(getValues(activate))
            deactivate = self.activeMod - items
            self.mod.disconnect(getValues(deactivate))
            self.activeMod = items

        def destroy(self):
            DependentObject.destroy(self)
            self.widget.clear()
            self.on_changed()

    class FeatChoice(ChoiceReference):
        stateFile = "data/character/feats.yaml"
        usePrerequisite = True
        def _enterSubmenu(self, name, choice):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tabWidget = QWidget()
            self.extra_ui = Ui_singleCombobox()
            self.extra_ui.setupUi(self.tabWidget)
            self.tab = tabRoot.addTab(self.tabWidget, name)
            self.choice1 = choice(self.extra_ui.comboBox1)
        def _exitSubmenu(self):
            self.choice1.destroy()
            del self.choice1
            getUI("tabWidget_specialProperties").removeTab(self.tab)

        def enterAthlete(self):
            self._enterSubmenu("Athlete", StateTable.StrengthOrDex1)
        exitAthlete = _exitSubmenu
        def enterLightly_Armored(self):
            self._enterSubmenu("Lightly Armored", StateTable.StrengthOrDex1)
        exitLightly_Armored = _exitSubmenu
        def enterModerately_Armored(self):
            self._enterSubmenu("Moderately Armored", StateTable.StrengthOrDex1)
        exitModerately_Armored = _exitSubmenu
        def enterObservant(self):
            self._enterSubmenu("Observant", StateTable.IntelligenceOrWisdom1)
        exitObservant = _exitSubmenu
        def enterResilient(self):
            self._enterSubmenu("Resilient", StateTable.Feat_Resilient)
        exitResilient = _exitSubmenu
        def enterWeapon_Master(self):
            self._enterSubmenu("Weapon Master", StateTable.StrengthOrDex1)
        exitWeapon_Master = _exitSubmenu

    class StrengthOrDex1(ChoiceReference):
        stateFile = "data/character/strengthOrDex1.yaml"

    class IntelligenceOrWisdom1(ChoiceReference):
        stateFile = "data/character/intOrWis1.yaml"

    class Feat_Resilient(ChoiceReference):
        stateFile = "data/character/feat_resilient.yaml"

    class Subrace_Genasi(ChoiceReference):
        stateFile = "data/character/state_Subrace_Genasi.yaml"

    class Subrace_Aasimar(ChoiceReference):
        stateFile = "data/character/state_Subrace_Aasimar.yaml"

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
            getModifier("Human_plus1").connect(getValues(("strength", "dexterity", "constitution", "intelligence","wisdom","charisma")))

        def exitHuman(self):
            self.extra_ui.checkBox_variantTraits.setCheckState(False)
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_human.setParent(None)
            del self.tab_human
            del self.extra_ui
            del self.tab
            getModifier("Human_plus1").disconnect(getValues(("strength", "dexterity", "constitution", "intelligence","wisdom","charisma")),True)
            try:
                getProficiencyTable().removeChoice(self.Human_SkillChoice)
            except:pass

        def altHumanTrait(self):
            b = self.extra_ui.checkBox_variantTraits.checkState()
            if b:
                getModifier("Human_plus1").disconnect(getValues(("strength", "dexterity", "constitution", "intelligence","wisdom","charisma")),True)
                choice = ProficiencyChoice(1,("skills",))
                self.Human_SkillChoice = str(choice)
                getProficiencyTable().addChoice(choice)
                self.feat = StateTable.FeatChoice(self.extra_ui.comboBox_feat)
                getValue("anythingChanged").connect(self.feat)
                self.score = StateTable.Choice2AbilityScore(self.extra_ui.comboBox_abilityScore,("strength","dexterity","constitution","wisdom","intelligence","charisma"),getModifier("Human_plus1"))
            else:
                getModifier("Human_plus1").connect(getValues(("strength", "dexterity", "constitution", "intelligence","wisdom","charisma")))
                try:
                    getValue("anythingChanged").disconnect(self.feat)
                except:pass
                try:
                    getProficiencyTable().removeChoice(self.Human_SkillChoice)
                except BaseException as e:pass
                self.score.destroy()
                self.feat.destroy()
                del self.score
                del self.feat
        def enterHalf_Elf(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_halfelf = QWidget()
            self.extra_ui = Ui_singleCheckableCombobox()
            self.extra_ui.setupUi(self.tab_halfelf)
            self.tab = tabRoot.addTab(self.tab_halfelf, "Half-Elf")
            self.score = StateTable.Choice2AbilityScore(self.extra_ui.comboBox1,("strength","dexterity","constitution","wisdom","intelligence"),getModifier("HalfElf_plus1"))
        def exitHalf_Elf(self):
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_halfelf.setParent(None)
            self.score.destroy()
            del self.score

    class PrimaryState(FiniteStateMachine):
        stateFile = "data/character/state_ValueTable.yaml"

class ActiveChoiceTable(dict):
    def __init__(self):
        dict.__init__(self)
        self.raceSelect = StateTable.Races(getUI("ComboBox_Race"))
        self.classSelect = StateTable.Classes(getUI("ComboBox_Class"))
        self.baseState = StateTable.PrimaryState()
        self.baseState.initFSM()
        self.baseState.request("On")

    def __getattr__(self,name):
        return self[name]
