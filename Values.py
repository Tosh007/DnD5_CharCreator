from CharacterCore import ValueReference, ValueConfig, ValueModifier, DependantValueReference, ChoiceReference


"""
------------------------------------------------------------------
Ability Score & Ability Modifier
------------------------------------------------------------------
"""
class AbilityScoreHardCap(ValueModifier):
    text = ""
    mod = lambda x: min(20,x)
    order = 10 #executed after all other modifiers


class AbilityScoreConfig(ValueConfig):
    points = None
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

class AbilityModConfig(ValueConfig):
    def __init__(self, score):
        self.score = score
        self.dependant_value_change = score.changeSignal

    def getMaxValue(self):
        return (self.score.get()//2)-5


"""
------------------------------------------------------------------
Races
------------------------------------------------------------------
"""
class Human_AbilityScoreIncrease(ValueModifier):
    text = "Human: +1"
    mod = lambda x: x+1

class Races(ChoiceReference):
    def __init__(self, widget, values):
        self.values = values
        races = ("Human", "Dwarf", "Elf", "Halfling", "Dragonborn",
                 "Gnome", "Half-Elf", "Half-Orc", "Orc", "Tiefling")
        ChoiceReference.__init__(self, widget, races)
        
    def enterHuman(self):
        Human_AbilityScoreIncrease.connect((self.values.strength,self.values.dexterity,self.values.constitution,self.values.intelligence,self.values.wisdom,self.values.charisma))
    def exitHuman(self):
        Human_AbilityScoreIncrease.disconnect((self.values.strength,self.values.dexterity,self.values.constitution,self.values.intelligence,self.values.wisdom,self.values.charisma))

    def enterDwarf(self):pass
    def exitDwarf(self):pass

    def enterElf(self):pass
    def exitElf(self):pass

    def enterHalfling(self):pass
    def exitHalfling(self):pass

    def enterDragonborn(self):pass
    def exitDragonborn(self):pass

    def enterGnome(self):pass
    def exitGnome(self):pass

    def enterHalf_Elf(self):pass
    def exitHalf_Elf(self):pass

    def enterHalf_Orc(self):pass
    def exitHalf_Orc(self):pass

    def enterOrc(self):pass
    def exitOrc(self):pass

    def enterTiefling(self):pass
    def exitTiefling(self):pass



class Values:
    def __init__(self, ui):
        # Ability Scores
        AbilityScoreConfig.points = ValueReference(ui.Label_AbilityScore, ValueConfig, "Ability Score Points: {0}")
        AbilityScoreConfig.points.set(27)
        self.strength     = ValueReference(ui.SpinBox_StrengthScore, AbilityScoreConfig)
        self.dexterity    = ValueReference(ui.SpinBox_DextScore, AbilityScoreConfig)
        self.constitution = ValueReference(ui.SpinBox_ConstScore, AbilityScoreConfig)
        self.intelligence = ValueReference(ui.SpinBox_IntelScore, AbilityScoreConfig)
        self.wisdom       = ValueReference(ui.SpinBox_WisdomScore, AbilityScoreConfig)
        self.charisma     = ValueReference(ui.SpinBox_CharismaScore,AbilityScoreConfig)

        AbilityScoreHardCap.connect((self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma))

        self.strengthMod  = DependantValueReference(ui.label_EchoStrengthMod, AbilityModConfig(self.strength),"{0}")
        self.dextMod  = DependantValueReference(ui.label_EchoDextMod, AbilityModConfig(self.dexterity),"{0}")
        self.constMod  = DependantValueReference(ui.label_EchoConstMod, AbilityModConfig(self.constitution),"{0}")
        self.intelMod  = DependantValueReference(ui.label_EchoIntelMod, AbilityModConfig(self.intelligence),"{0}")
        self.wisdomMod  = DependantValueReference(ui.label_EchoWisdomMod, AbilityModConfig(self.wisdom),"{0}")
        self.charismaMod  = DependantValueReference(ui.label_EchoCharismaMod, AbilityModConfig(self.charisma),"{0}")

        # Races
        self.raceSelect = Races(ui.comboBox_Race,self)

        