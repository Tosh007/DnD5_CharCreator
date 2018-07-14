from PyQt5 import QtCore
from acces import *
from CharacterCore import *

class ConfigTable:
    AllowNone = ValueConfig
    AllowAll  = ValueConfig_allow

    class ProficiencyConfig(ValueConfig):
        forceCheckbox = True
        def __init__(self, name, root):
            self.name = name
            self.root = root    # name of parent proficiency
            self.choice = None  # choice from which value is drawn

        def checkRequirements(self,value,lastValue):
            if value<0 or (not self.root):return 0
            try:
                choices = getProficiencyTable().table.values()
            except:
                return lastValue
            try:
                maxValue = self.getMaxValue(lastValue)
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
            except BaseException as e:
                print("checkReq failed for "+self.name)
                print("value:"+str(value)+"\nlast value:"+str(lastValue))
                raise e

        def getMaxValue(self, lastValue):
            try:
                choices = getProficiencyTable().table.values()
            except:
                return 0
            for choice in choices:
                v=max(0,choice.possible(self.name,1))
                if v:
                    return 1
                else:
                    pass
            return 0
        hide = lambda self,v,vmod,maxValue:False
        specialSetup = lambda self,widget,v,vmod,mdesc,maxValue: None

    class ProficiencyListConfig(ProficiencyConfig):
        hide = lambda self,v,vmod,maxValue:(v==0) and (vmod==0) and (maxValue==0)
        VisualUpdateSignal = "listWidget_proficiencies_VisualUpdate"
        setToolTip = False
        def __init__(self,name,root):
            ConfigTable.ProficiencyConfig.__init__(self,name,root)
            self.toolTipText = ""

        def specialSetup(self,widget,v,vmod,mdesc,maxValue):
            try:
                races = getProficiencyTable().whoSpeaksWhat[self.name]
            except BaseException as e:pass#if we would return in any case, we kill tooltips for anything but languages
            else:
                mdesc += "\n<b>spoken by:</b>"
                for race in races:
                    mdesc += "\n"+race+","
                mdesc = mdesc[:-1]
            if mdesc != self.toolTipText:
                self.toolTipText = mdesc
                widget.widget.setToolTip(0,mdesc)   # note:  setToolTip(int,str) only for QTreeWidget!

    class ProficiencyCategoryConfig(ProficiencyListConfig):
        forceCheckbox=False
        def checkRequirements(self,value,lastValue):
            return lastValue
        def hide(self,v,vmod,maxValue:False):
            try:
                pt = getProficiencyTable()
                vt = getValueTable()
            except NameError:
                return True
            for prof in pt.getChildProficiencies(self.name):
                if not getValue("prof_"+prof).widget.isHidden():
                    return False
            return True


    class HiddenValue(ValueConfig): #can be achieved by setting ui element to none
        hide = lambda v,vmod,maxV: True

    class AbilityScoreConfig(ValueConfig):
        points = None
        @classmethod
        def checkRequirements(self, value, oldvalue):
            total = getValue("abilityScorePoints").get() - self.getReqPoints(value) + self.getReqPoints(oldvalue)
            if (total>=0):
                getValue("abilityScorePoints").set(total)
                return value
            return oldvalue
        @staticmethod
        def getReqPoints(value):
            #assert (value>=8)
            if (value>15):return 100
            return (0,1,2,3,4,5,7,9)[value-8]
