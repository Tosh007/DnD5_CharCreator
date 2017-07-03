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
            if "language" in self.name and vmod!=self.vmod:
                self.vmod = vmod
                print(self.name,vmod)

    class ProficiencyConfig(ValueConfig):
        def __init__(self, root):
            self.root = root    # name of parent proficiency

        def checkRequirements(self,value,lastValue):
            #print ("proficiency requirement check:")
            if value<0 or (not self.root):return 0
            learn = getValue("prof_"+self.root+"_learnChildren")
            """if value>1:return 1
            #print(value,oldvalue,learn.get())
            mod = learn.get()-learn.get(True)
            diffmod = learn.get()-value+oldvalue
            if value == oldvalue and value<=self.getMaxValue(oldvalue):
                return value
            if value == oldvalue:
                return value
            if diffmod>=0:

                #print ("possible",diffmod)
                learn.set(diffmod-mod)
                learn.changeSignal.emit()
                return value
            else:
                #print("impossible",diffmod,diffmod+value)
                if oldvalue<=self.getMaxValue(oldvalue):
                    return oldvalue
                learn.set(diffmod-mod+value)
                #learn.changeSignal.emit()  # do not notify here !recursion!
                return 0"""
            maxValue = self.getMaxValue(lastValue)
            if value==lastValue:
                if value>maxValue:
                    learn+=lastValue-maxValue
                    getValue("listWidget_proficiencies_VisualUpdate").changeSignal.emit()
                    return maxValue
                else:
                    return value
            else:
                if value>maxValue:
                    assert lastValue<=maxValue
                    return lastValue
                else:
                    learn += lastValue - value
                    getValue("listWidget_proficiencies_VisualUpdate").changeSignal.emit()
                    return value

        def getMaxValue(self, lastValue):
            if self.root:
                return max(0,getValue("prof_"+self.root+"_learnChildren").get()+lastValue)
            else:
                return 0
        hide = lambda self,v,vmod,maxValue:False
        specialSetup = lambda self,widget,v,vmod,mdesc,maxValue: None

    class ProficiencyListConfig(ProficiencyConfig):
        hide = lambda self,v,vmod,maxValue:(v==0) and (vmod==0) and (maxValue==0)
        VisualUpdateSignal = "listWidget_proficiencies_VisualUpdate"
        forceCheckbox = True
        def specialSetup(self,widget,v,vmod,mdesc,maxValue):
            return
            if "standart_language" in self.root:
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
