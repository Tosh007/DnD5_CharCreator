from PyQt5.QtWidgets import *
from acces import*
from CharacterCore import *
from menu_human import Ui_Human
from menu_wizard import Ui_Wizard
from menu_warlock import Ui_Warlock
from menu_sorcerer import Ui_Sorcerer
from menu_twoCombobox import Ui_twoCombobox
from menu_singleCombobox import Ui_singleCombobox
from menu_singleCheckableCombobox import Ui_singleCheckableCombobox
from menu_halfElf import Ui_halfElf

class StateTable:
    class Classes(ChoiceReference):
        stateFile = "data/character/state_Classes.yaml"
        def enterWarlock(self):
            getActiveStateTable().addChoice(StateTable.WarlockPatron(getUI("ComboBox_Subclass")))
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_warlock = QWidget()
            self.extra_ui = Ui_Warlock()
            self.extra_ui.setupUi(self.tab_warlock)
            self.tab = tabRoot.addTab(self.tab_warlock, "warlock")
            getValueTable().newValue("warlock_spellSlotLevel", ValueReference(self.extra_ui.label_spellSlotLevel, getConfig("AllowNone"), "your spell slots are of level {2}"))
            getValueTable().newValue("warlock_spellSlots", ValueReference(self.extra_ui.label_spellSlots, getConfig("AllowNone"), "you have {2} spell slots"))
            getModifier("warlock_spellSlotLevel").connect(getValue("warlock_spellSlotLevel"))
            getModifier("warlock_spellSlots").connect(getValue("warlock_spellSlots"))


        def exitWarlock(self):
            getActiveStateTable().removeChoice(StateTable.WarlockPatron)
            getValueTable().destroyValue("warlock_spellSlots")
            getValueTable().destroyValue("warlock_spellSlotLevel")
            self.tab_warlock.setParent(None)

        def enterCleric(self):
            getActiveStateTable().addChoice(StateTable.ClericDomain(getUI("ComboBox_Subclass")))

        def exitCleric(self):
            getActiveStateTable().removeChoice(StateTable.ClericDomain)

        def enterWizard(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_wizard = QWidget()
            self.extra_ui = Ui_Wizard()
            self.extra_ui.setupUi(self.tab_wizard)
            self.tab = tabRoot.addTab(self.tab_wizard, "wizard")
            getValueTable().newValue("wizard_numPreparedSpells", ValueReference(self.extra_ui.label_numPreparedSpells, getConfig("AllowNone"), "You can prepare {2} spells at a time"))
            getModifier("wizard_numPreparedSpells").connect(getValue("wizard_numPreparedSpells"))

        def exitWizard(self):
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_wizard.setParent(None)
            del self.tab_wizard
            del self.extra_ui
            del self.tab
            getValueTable().destroyValue("wizard_numPreparedSpells")

        def enterSorcerer(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_sorcerer = QWidget()
            self.extra_ui = Ui_Sorcerer()
            self.extra_ui.setupUi(self.tab_sorcerer)
            self.tab = tabRoot.addTab(self.tab_sorcerer, "sorcerer")
            getActiveStateTable().addChoice(StateTable.SorcerousOrigin(getUI("ComboBox_Subclass")))

        def exitSorcerer(self):
            getActiveStateTable().removeChoice(StateTable.SorcerousOrigin)
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_sorcerer.setParent(None)
            del self.tab_sorcerer
            del self.extra_ui
            del self.tab

    class ClericDomain(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_clericDomain.yaml"

    class WarlockPatron(ChoiceReference):
        loadLevel = 4
        stateFile = "data/character/state_warlockPatron.yaml"

    class SorcerousOrigin(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_sorcerousOrigin.yaml"
        def enterBloodline(self):
            getActiveStateTable().addChoice(StateTable.SorcerousOrigin_bloodline(getActiveState(StateTable.Classes).extra_ui.comboBox1))
        def exitBloodline(self):
            getActiveStateTable().removeChoice(StateTable.SorcerousOrigin_bloodline)
        def enterDivine_Magic(self):
            getActiveStateTable().addChoice(StateTable.SorcerousOrigin_divine(getActiveState(StateTable.Classes).extra_ui.comboBox1))
        def exitDivine_Magic(self):
            getActiveStateTable().removeChoice(StateTable.SorcerousOrigin_divine)

    class SorcerousOrigin_divine(ChoiceReference):
        loadLevel = 3
        stateFile = "data/character/state_sorcerousOrigin_divine.yaml"

    class SorcerousOrigin_bloodline(ChoiceReference):
        loadLevel = 3
        stateFile = "data/character/state_sorcerousOrigin_bloodline.yaml"

    class Choice2AbilityScore(MultiChoiceReference):
        loadLevel = 4
        n = 2
        def __init__(self, w, items, mod):
            MultiChoiceReference.__init__(self,w,items)
            self.mod = mod

        def activate(self, args):
            self.mod.connect(getValues(args))

        def deactivate(self, args):
            self.mod.disconnect(getValues(args),True)

    class FeatChoice(ChoiceReference):
        loadLevel = 4
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
        def enterObservant(self):
            self._enterSubmenu("Observant", StateTable.IntelligenceOrWisdom1)
        exitObservant = _exitSubmenu

    class StrengthOrDex1(ChoiceReference):
        loadLevel = 4
        stateFile = "data/character/strengthOrDex1.yaml"

    class IntelligenceOrWisdom1(ChoiceReference):
        loadLevel = 4
        stateFile = "data/character/intOrWis1.yaml"

    class Feat_Resilient(ChoiceReference):
        loadLevel = 3
        stateFile = "data/character/feat_resilient.yaml"

    class Subrace_Genasi(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_Subrace_Genasi.yaml"

    class Subrace_Aasimar(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_Subrace_Aasimar.yaml"

    class Subrace_Dragonborn(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/dragonborn_ancestry.yaml"

    class Subrace_Dwarf(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_Subrace_Dwarf.yaml"

    class Subrace_Elf(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_Subrace_Elf.yaml"

    class Subrace_Halfling(ChoiceReference):
        stateFile = "data/character/state_Subrace_Halfling.yaml"

    class Subrace_Gnome(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_Subrace_Gnome.yaml"

    class Subrace_Half_Elf(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_Subrace_HalfElf.yaml"
        def enterHalfWoodElf(self):
            getActiveStateTable().addChoice(StateTable.HalfWoodElf(getActiveState("Races").extra_ui.comboBox))

        def exitHalfWoodElf(self):
            getActiveStateTable().removeChoice(StateTable.HalfWoodElf)

        def enterHalfHighElf(self):
            getActiveStateTable().addChoice(StateTable.HalfHighElf(getActiveState("Races").extra_ui.comboBox))

        def exitHalfHighElf(self):
            getActiveStateTable().removeChoice(StateTable.HalfHighElf)

    class HalfWoodElf(ChoiceReference):
        loadLevel = 3
        stateFile = "data/character/state_HalfWoodElf.yaml"

    class HalfHighElf(ChoiceReference):
        loadLevel = 3
        stateFile = "data/character/state_HalfHighElf.yaml"

    class HumanTraitToggle(ChoiceReference):
        loadLevel = 2
        stateFile = "data/character/state_HumanTrait.yaml"

        def enterChecked(self):
            getActiveStateTable().addChoice(StateTable.FeatChoice(getActiveState("Races").extra_ui.comboBox_feat))
            getValue("anythingChanged").connect(getActiveState(StateTable.FeatChoice)) # cannot be handled by state, because target value is a ChoiceRef
            self.score = getActiveMultiStateTable().addChoice(StateTable.Choice2AbilityScore(getActiveState("Races").extra_ui.comboBox_abilityScore,("strength","dexterity","constitution","wisdom","intelligence","charisma"),getModifier("Human_plus1")))

        def exitChecked(self):
            getValue("anythingChanged").disconnect(getActiveState(StateTable.FeatChoice))
            getActiveMultiStateTable().removeChoice(StateTable.Choice2AbilityScore)
            getActiveStateTable().removeChoice(StateTable.FeatChoice)

    class Races(ChoiceReference):
        stateFile = "data/character/state_Races.yaml"
        def enter(self,state):
            if state=="Off":return
            try:
                choice = getState("Subrace_"+state)
            except:return
            getActiveStateTable().addChoice(choice(getUI("ComboBox_Subrace")))

        def exit(self,state):
            try:
                subrace = getState("Subrace_"+state)
            except:
                return
            getActiveStateTable().removeChoice(subrace)

        def enterHuman(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_human = QWidget()
            self.extra_ui = Ui_Human()
            self.extra_ui.setupUi(self.tab_human)
            self.tab = tabRoot.addTab(self.tab_human, "Human")
            getActiveStateTable().addChoice(StateTable.HumanTraitToggle(self.extra_ui.checkBox_variantTraits))

        def exitHuman(self):
            getActiveStateTable().removeChoice(StateTable.HumanTraitToggle)
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_human.setParent(None)
            del self.tab_human
            del self.extra_ui
            del self.tab

        def enterHalf_Elf(self):
            tabRoot = getUI("tabWidget_specialProperties")
            self.tab_halfelf = QWidget()
            self.extra_ui = Ui_halfElf()
            self.extra_ui.setupUi(self.tab_halfelf)
            self.tab = tabRoot.addTab(self.tab_halfelf, "Half-Elf")
            getActiveMultiStateTable().addChoice(StateTable.Choice2AbilityScore(self.extra_ui.comboBox1,("strength","dexterity","constitution","wisdom","intelligence"),getModifier("HalfElf_plus1")))
        def exitHalf_Elf(self):
            getUI("tabWidget_specialProperties").removeTab(self.tab)
            self.tab_halfelf.setParent(None)
            getActiveMultiStateTable().removeChoice(StateTable.Choice2AbilityScore)

    class PrimaryState(FiniteStateMachine):
        stateFile = "data/character/state_ValueTable.yaml"

    class Backgrounds(ChoiceReference):
        stateFile = "data/character/state_Background.yaml"

class _ChoiceTableBase(dict):
    def addChoice(self,choice):
        name = type(choice).__name__
        assert name not in self.keys()
        self[name] = choice
        return name

    def removeChoice(self,type_):
        self[type_.__name__].destroy()
        del self[type_.__name__]

    def __getattr__(self,name):
        return self[name]

class ActiveChoiceTable(_ChoiceTableBase):
    def __init__(self):
        dict.__init__(self)
        # always existing fsm
        self.addChoice(StateTable.Races(getUI("ComboBox_Race")))
        self.addChoice(StateTable.Classes(getUI("ComboBox_Class")))
        self.addChoice(StateTable.Backgrounds(getUI("ComboBox_Background")))
        self.addChoice(StateTable.PrimaryState())
        self.PrimaryState.initFSM()
        self.PrimaryState.request("On")
        # acces via dict or argument, set only as dict
        self.update(self.__dict__)
        self.__dict__.clear()

class ActiveMultiChoiceTable(_ChoiceTableBase):pass
