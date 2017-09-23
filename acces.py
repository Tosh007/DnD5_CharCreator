
def initializeTables(ui):
    from ValueTable import ValueTable
    from ChoiceTable import ActiveChoiceTable, StateTable
    from ProficiencyTable import ProficiencyTable
    from ConfigTable import ConfigTable
    from ModifierTable import ModifierTable
    global UI,Value,Modifier,Config,Proficiency,State,ActiveState
    UI = ui
    Config = ConfigTable
    Modifier = ModifierTable()
    Value = ValueTable()
    Proficiency = ProficiencyTable()
    State = StateTable
    ActiveState = ActiveChoiceTable()
    print("global table initialization complete!")

def getValueTable():
    return Value
def getProficiencyTable():
    return Proficiency
def getActiveStateTable():
    return ActiveState


# returns a list of objects as result of a list of strings
# returns a list with one object if a string is given
def _get(obj,name,err):
    try:
        if type(name) is str:
            return ((getattr(obj,name)),)
        else:
            return (getattr(obj,n) for n in name)
    except KeyError as e:
        raise KeyError(err.format(name)) from e

def getUI(name):
    return _get(UI,name,"getUI({0}) failed")[0]

def getValues(name):
    return _get(Value,name,"getValues({0}) failed")

def getValue(name):
    return getValues(name)[0]

def getModifier(name):
    return _get(Modifier,name,"getModifier({0}) failed")[0]

def getConfig(name):
    return _get(Config,name,"getConfig({0}) failed")[0]

def getProficiency(name):
    return _get(Proficiency,name,"getProficiency({0}) failed")[0]

def getState(name):
    return _get(State, name,"getState({0}) failed")[0]

def getActiveState(name):
    return _get(ActiveState,name,"getActiveState({0}) failed")[0]
