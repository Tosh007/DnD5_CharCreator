from PyQt5 import QtCore
from acces import *
from CharacterCore import *

class ConfigTable:
    AllowNone = ValueConfig
    AllowAll  = ValueConfig_allow
    class AllowNone_debug(AllowNone):
        def __init__(self, name):
            self.name=name
            self.vmod=0
        def specialSetup(self,widget,v,vmod,mdesc,maxValue):
            pass
        #    if "language" in self.name and vmod!=self.vmod:
        #        self.vmod = vmod
        #        print(self.name,vmod)

    class ProficiencyConfig(ValueConfig):
        def __init__(self, name, root):
            self.name = name
            self.root = root    # name of parent proficiency
            self.choice = None  # choice from which value is drawn

        def checkRequirements(self,value,lastValue):
            #print ("proficiency requirement check:")
            if value<0 or (not self.root):return 0
            #learn = getValue("prof_"+self.root+"_learnChildren")
            try:
                choices = getProficiencyTable().table.values()
            except:
                return lastValue
            maxValue = self.getMaxValue(lastValue)
            #if value==lastValue:
            #    if value>maxValue:
            #        learn+=lastValue-maxValue
            #        getValue("listWidget_proficiencies_VisualUpdate").changeSignal.emit()
            #        return maxValue
            #    else:
            #        return value
            #else:
            #    if value>maxValue:
            #        assert lastValue<=maxValue
            #        return lastValue
            #    else:
            #        learn += lastValue - value
            #        getValue("listWidget_proficiencies_VisualUpdate").changeSignal.emit()
            #        return value
            if value==lastValue:
                if value>0:
                    assert self.choice
                    v=self.choice.proficient(self.name, value) #dont search for other choices for takeover
                    if not v:self.choice=None
                    return v
                #else: value==lastValue==0
            else:
                #value!=lastValue
                if value>0:
                    assert lastValue==0
                    #assert not self.choice
                    for choice in getProficiencyTable().table.values():
                        v = choice.proficient(self.name, value)
                        if v:
                            self.choice=choice
                            return v
                else:
                    # value=0
                    assert lastValue>0
                    assert self.choice
                    return self.choice.proficient(self.name,0)
                    self.choice = None
            return 0

        def getMaxValue(self, lastValue):
            try:
                choices = getProficiencyTable().table.values()
            except:
                #print("fail")
                return 0
            for choice in choices:
                v=max(0,choice.possible(self.name,1))
                if v:
                    #print("1")
                    return 1
                else:
                    pass
                    #print(v)
            return 0



        hide = lambda self,v,vmod,maxValue:False
        specialSetup = lambda self,widget,v,vmod,mdesc,maxValue: None

    class ProficiencyListConfig(ProficiencyConfig):
        hide = lambda self,v,vmod,maxValue:(v==0) and (vmod==0) and (maxValue==0)
        VisualUpdateSignal = "listWidget_proficiencies_VisualUpdate"
        forceCheckbox = True
        def specialSetup(self,widget,v,vmod,mdesc,maxValue):
            if self.root and "standart_language" in self.root:
                print(widget.widget.text(),v,vmod,maxValue,self.hide(v,vmod,maxValue))



    class HiddenValue(ValueConfig): #can be achieved by setting ui element to none
        hide = lambda v,vmod,maxV: True

    class AbilityScoreConfig(ValueConfig):
        points = None
        @classmethod
        def checkRequirements(self, value, oldvalue):
            total = getValue("abilityScorePoints").get() - self.getReqPoints(value) + self.getReqPoints(oldvalue)
            #print(total if total>0 else 0)
            if (total>=0):
                getValue("abilityScorePoints").set(total)
                return value
            return oldvalue
        @staticmethod
        def getReqPoints(value):
            #assert (value>=8)
            if (value>15):return 100
            return (0,1,2,3,4,5,7,9)[value-8]

    class AbilityModConfig(ValueConfig):
        def __init__(self, score):
            self.score = score

        def getMaxValue(self,lastValue):
            score = getValues(self.score)[0]
            return (score.get()//2)-5
        hide = lambda self,v,vmod,maxV:False
        specialSetup = lambda self,widget,v,vmod,mdesc,maxValue: None
        alwaysMax = True

    strengthMod = AbilityModConfig("strength")
    dextMod = AbilityModConfig("dexterity")
    constMod = AbilityModConfig("constitution")
    intelMod = AbilityModConfig("intelligence")
    wisdomMod = AbilityModConfig("wisdom")
    charismaMod = AbilityModConfig("charisma")

    class MaxHPConfig(ValueConfig):
        def getMaxValue(lastValue):
            return getValue("constMod").get()
