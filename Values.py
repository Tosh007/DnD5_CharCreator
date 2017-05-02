from CharacterCore import ValueReference, ValueConfig, ValueModifier, DependantValueReference

class AbilityScoreHardCap(ValueModifier):
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
        self.dependant_value_change = score._changeSignal

    def getMaxValue(self):
        return (self.score.get()//2)-5




class Values:
    def __init__(self, ui):
        AbilityScoreConfig.points = ValueReference("AbilityScorePoints", ui.Label_AbilityScore, ValueConfig, 27, "Ability Score Points: {0}")
        self.strength     = ValueReference("StrengthScore", ui.SpinBox_StrengthScore, AbilityScoreConfig)
        self.dexterity    = ValueReference("DexterityScore", ui.SpinBox_DextScore, AbilityScoreConfig)
        self.constitution = ValueReference("ConstitutionScore", ui.SpinBox_ConstScore, AbilityScoreConfig)
        self.intelligence = ValueReference("IntelligenceScore", ui.SpinBox_IntelScore, AbilityScoreConfig)
        self.wisdom       = ValueReference("WisdomScore", ui.SpinBox_WisdomScore, AbilityScoreConfig)
        self.charisma     = ValueReference("CharismaScore", ui.SpinBox_CharismaScore,AbilityScoreConfig)

        AbilityScoreHardCap.connect((self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma))

        self.strengthMod  = DependantValueReference("StrengthMod", ui.label_EchoStrengthMod, AbilityModConfig(self.strength), -1,"{0}")
        self.dextMod  = DependantValueReference("DexterityMod", ui.label_EchoDextMod, AbilityModConfig(self.dexterity), -1,"{0}")
        self.constMod  = DependantValueReference("ConstitutionMod", ui.label_EchoConstMod, AbilityModConfig(self.constitution), -1,"{0}")
        self.intelMod  = DependantValueReference("IntelligenceMod", ui.label_EchoIntelMod, AbilityModConfig(self.intelligence), -1,"{0}")
        self.wisdomMod  = DependantValueReference("WisdomMod", ui.label_EchoWisdomMod, AbilityModConfig(self.wisdom), -1,"{0}")
        self.charismaMod  = DependantValueReference("CharismaMod", ui.label_EchoCharismaMod, AbilityModConfig(self.charisma), -1,"{0}")