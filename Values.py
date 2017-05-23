from CharacterCore import ValueReference, ValueConfig, ValueModifier, ChoiceReference, FiniteStateMachine
from proficiencies import ProficiencyTable

VRef = ValueReference
VConf = ValueConfig
VMod = ValueModifier
CRef = ChoiceReference

"""
------------------------------------------------------------------
Ability Score & Ability Modifier
------------------------------------------------------------------
"""
AbilityScoreHardCap = VMod(lambda x: min(20,x), "Hardcap at 20", 8)


class AbilityScoreConfig(VConf):
    points = None
    text = "Ability Score Points"
    @staticmethod
    def checkRequirements(value, oldvalue):
        total = AbilityScoreConfig.points.get() - AbilityScoreConfig.getReqPoints(value) + AbilityScoreConfig.getReqPoints(oldvalue)
        #print(total if total>0 else 0)
        if (total>=0):
            AbilityScoreConfig.points.set(total)
            return True
        return False
    @staticmethod
    def getReqPoints(value):
        assert (value>=8)
        if (value>15):return 100
        return (0,1,2,3,4,5,7,9)[value-8]

class AbilityModConfig(VConf):
    def __init__(self, score):
        self.score = score

    def getMaxValue(self):
        return (self.score.get()//2)-5

class MaxHPConfig(VConf):
    def getMaxValue():
        return values.constMod.get()

"""
------------------------------------------------------------------
Races
------------------------------------------------------------------
"""
Human_plus1 = VMod(lambda x:x+1, "Human: {2:+d}")
HalfOrc_plus1 = VMod(lambda x:x+1, "Half Orc: {2:+d}")
HalfOrc_plus2 = VMod(lambda x:x+2, "Half Orc: {2:+d}")


class Subrace_Dwarf(CRef):
    states = {"Hill Dwarf":{},"Mountain Dwarf":{}}

class Races(CRef):
    states = {"Human":{"mod":{Human_plus1:("strength","dexterity","constitution","intelligence","wisdom","charisma")}}, 
            "Dwarf":{}, 
            "Elf":{}, 
            "Halfling":{}, 
            "Dragonborn":{},
            "Gnome":{}, 
            "Half-Elf":{}, 
            "Half-Orc":{}, 
            "Orc":{}, 
            "Tiefling":{}}
    
    def enterDwarf(self):
        self.subrace = Subrace_Dwarf(ui.ComboBox_Subrace,values)
    def exitDwarf(self):
        self.subrace.destroy()
        del self.subrace

"""
------------------------------------------------------------------
Classes
------------------------------------------------------------------
"""
Barbarian_HP = VMod(lambda x:x+12, "Barbarian: {2:+d}")
class Classes(CRef):
    states = {"Barbarian":{"mod":{Barbarian_HP:"maxHP"}}, "Bard":{}, "Cleric":{}, "Monk":{}, "Druid":{}, "Fighter":{},
        "Paladin":{}, "Ranger":{}, "Rogue":{}, "Sorcerer":{},"Warlock":{}, "Wizard":{}}

class Values(FiniteStateMachine):
    states = \
   {"On":{"mod":{AbilityScoreHardCap:("strength","dexterity","constitution","intelligence","wisdom","charisma")},
    "depend":{"strength":"strengthMod",
              "constitution":"constMod",
              "dexterity":"dextMod",
              "intelligence":"intelMod",
              "wisdom":"wisdomMod",
              "charisma":"charismaMod",

              "constMod":"maxHP"}}}
    def __init__(self, ui_):
        global ui, values
        ui = ui_
        values = self
        FiniteStateMachine.__init__(self,self)
        self.initFSM()
        self.level = VRef(ui.Label_CharLevel, ValueConfig, "Level: {0}")
        self.level.set(1)
        self.proficiencyBonus = VRef(ui.Label_ProficiencyBonus, ValueConfig, "Proficiency Bonus: {0}")
        self.proficiencyBonus.set(2)
        # Ability Scores
        AbilityScoreConfig.points = VRef(ui.Label_AbilityScore, ValueConfig, "Ability Score Points: {0}")
        AbilityScoreConfig.points.set(27)
        self.strength     = VRef(ui.SpinBox_StrengthScore, AbilityScoreConfig)
        self.dexterity    = VRef(ui.SpinBox_DextScore, AbilityScoreConfig)
        self.constitution = VRef(ui.SpinBox_ConstScore, AbilityScoreConfig)
        self.intelligence = VRef(ui.SpinBox_IntelScore, AbilityScoreConfig)
        self.wisdom       = VRef(ui.SpinBox_WisdomScore, AbilityScoreConfig)
        self.charisma     = VRef(ui.SpinBox_CharismaScore,AbilityScoreConfig)

        self.strengthMod  = VRef(ui.Label_EchoStrengthMod, AbilityModConfig(self.strength),"{0}")
        self.dextMod  = VRef(ui.Label_EchoDextMod, AbilityModConfig(self.dexterity),"{0}")
        self.constMod  = VRef(ui.Label_EchoConstMod, AbilityModConfig(self.constitution),"{0}")
        self.intelMod  = VRef(ui.Label_EchoIntelMod, AbilityModConfig(self.intelligence),"{0}")
        self.wisdomMod  = VRef(ui.Label_EchoWisdomMod, AbilityModConfig(self.wisdom),"{0}")
        self.charismaMod  = VRef(ui.Label_EchoCharismaMod, AbilityModConfig(self.charisma),"{0}")

        # Speed, ArmorClass, Initiative, max HP
        self.speed      = VRef(ui.Label_Speed, ValueConfig, "Speed: {0}")
        self.armorClass = VRef(ui.Label_ArmorClass, ValueConfig, "Armor Class: {0}")
        self.initiative = VRef(ui.Label_Initiative, ValueConfig, "Initiative: {0}")
        self.maxHP      = VRef(ui.Label_MaxHP, MaxHPConfig, "Hit Point Maximum: {2}")
        self.speed.set(30)
        self.armorClass.set(0)
        self.initiative.set(0)

        # Races
        self.raceSelect = Races(ui.ComboBox_Race,self)
        self.classSelect = Classes(ui.ComboBox_Class,self)

    # returns a list of objects as result of a list of strings
    # returns a list with one object if a string is given
    def get(self,name):
        if type(name) is str:
            return ((getattr(self,name)),)
        else:
            return (getattr(self,n) for n in name)



        