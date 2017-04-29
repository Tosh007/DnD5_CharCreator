from CharacterCore import ValueReference, ValueConfig, ValueModifier
class AbilityScoreConfig(ValueConfig):
    points = None
    @staticmethod
    def checkRequirements(value, oldvalue):
        total = AbilityScoreConfig.points.get() - AbilityScoreConfig.getReqPoints(value) + AbilityScoreConfig.getReqPoints(oldvalue)
        print(total if total>0 else 0)
        if (total>=0):
            AbilityScoreConfig.points.set(total)
            return True
        return False
    @staticmethod
    def getReqPoints(value):
        assert (value>=8)
        if (value>15):return 100
        return (0,1,2,3,4,5,7,9)[value-8]

class Values:
    def __init__(self, ui):
        AbilityScoreConfig.points = ValueReference("AbilityScorePoints", ui.Label_AbilityScore, ValueConfig, 27, "Ability Score Points: {0}")
        self.strength     = ValueReference("StrengthScore", ui.SpinBox_StrengthScore, AbilityScoreConfig)
        self.dexterity    = ValueReference("DexterityScore", ui.SpinBox_DextScore, AbilityScoreConfig)
        self.constitution = ValueReference("ConstitutionScore", ui.SpinBox_ConstScore, AbilityScoreConfig)
        self.intelligence = ValueReference("IntelligenceScore", ui.SpinBox_IntelScore, AbilityScoreConfig)
        self.wisdom       = ValueReference("WisdomScore", ui.SpinBox_WisdomScore, AbilityScoreConfig)
        self.charisma     = ValueReference("CharismaScore", ui.SpinBox_CharismaScore,AbilityScoreConfig)