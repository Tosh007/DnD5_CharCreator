from CharacterCore import ValueReference, ValueConfig, ValueModifier, ChoiceReference, FiniteStateMachine
import yaml
from acces import *

class ValueTable:
    def __init__(self):
        f = open("data/character/values.yaml")
        data = yaml.load(f)
        f.close()
        for obj in data:
            name = tuple(obj.keys())[0]
            meta = tuple(obj.values())[0]
            ui=None
            config = ValueConfig
            format = None
            initial=None
            print (meta)
            for key in meta:
                if key=="ui":
                    ui=getUI(meta[key])
                    print (ui)
                if key=="config":
                    config = getConfig(meta[key])
                if key=="format":
                    format = meta[key]
                if key=="initial":
                    initial = meta[key]
            self.__dict__[name] = ValueReference(ui, config,format)
            if initial:
                self.__dict__[name].set(initial)
            print(name,"=ValueReference(",ui,config, format,")")
