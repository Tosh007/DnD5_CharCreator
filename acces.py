
def initializeTables(ui):
    from ValueTable import ValueTable
    from ChoiceTable import ChoiceTable
    from ProficiencyTable import ProficiencyTable
    from ConfigTable import ConfigTable
    from ModifierTable import ModifierTable
    global UI,Value,Modifier,Config,Proficiency,Choice
    UI = ui
    Config = ConfigTable
    Modifier = ModifierTable()
    Value = ValueTable()
    Proficiency = ProficiencyTable()
    Choice = ChoiceTable()
    print("global table initialization complete!")

def getValueTable():
    return Value


# returns a list of objects as result of a list of strings
# returns a list with one object if a string is given
def _get(obj,name):
    if type(name) is str:
        return ((getattr(obj,name)),)
    else:
        return (getattr(obj,n) for n in name)

def getUI(name):
    return _get(UI,name)[0]

def getValues(name):
    return _get(Value,name)

def getValue(name):
    return getValues(name)[0]

def getModifier(name):
    return _get(Modifier,name)[0]

def getConfig(name):
    return _get(Config,name)[0]

def getProficiency(name):
    return _get(Proficiency,name)[0]

def getChoice(name):
    return _get(Choice,name)[0]
