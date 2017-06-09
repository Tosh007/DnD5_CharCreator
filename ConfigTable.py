from acces import *
from CharacterCore import *

class ConfigTable:
    AllowNone = ValueConfig
    AllowAll  = ValueConfig_allow
    class ProficiencyListConfig(ValueConfig):
        hide = lambda v: not bool(v)
    class HiddenValue(ValueConfig):
        hide = lambda v: True
    class AbilityScoreConfig(ValueConfig):
        points = None
        text = "Ability Score Points"
        @classmethod
        def checkRequirements(self, value, oldvalue):
            total = getValue("abilityScorePoints").get() - self.getReqPoints(value) + self.getReqPoints(oldvalue)
            #print(total if total>0 else 0)
            if (total>=0):
                getValue("abilityScorePoints").set(total)
                return True
            return False
        @staticmethod
        def getReqPoints(value):
            #assert (value>=8)
            if (value>15):return 100
            return (0,1,2,3,4,5,7,9)[value-8]

    class AbilityModConfig(ValueConfig):
        def __init__(self, score):
            self.score = score

        def getMaxValue(self):
            score = getValues(self.score)[0]
            return (score.get()//2)-5

    strengthMod = AbilityModConfig("strength")
    dextMod = AbilityModConfig("dexterity")
    constMod = AbilityModConfig("constitution")
    intelMod = AbilityModConfig("intelligence")
    wisdomMod = AbilityModConfig("wisdom")
    charismaMod = AbilityModConfig("charisma")

    class MaxHPConfig(ValueConfig):
        def getMaxValue():
            return getValue("constMod").get()