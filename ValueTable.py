from CharacterCore import *
from acces import *
import yaml
class ValueTable:
    def __init__(self):
        f = open(getDirectoryPrefix()+"data/character/values.yaml")
        data = yaml.load(f)
        f.close()
        self._data = {}
        self.custom()
        for obj in data:
            name = tuple(obj.keys())[0]
            meta = tuple(obj.values())[0]
            ui=None
            config = ValueConfig
            format = None
            initial=0
            for key in meta:
                if key=="ui":
                    ui=getUI(meta[key])
                if key=="config":
                    config = getConfig(meta[key])
                if key=="format":
                    format = meta[key]
                if key=="initial":
                    initial = meta[key]
            self._data[name] = ValueReference(ui, config,format)
            self._data[name].set(initial)
            self._data[name].lastValue = initial
            self._data[name].connect(self._data["anythingChanged"])
    def newValue(self,name,value):
        if name in self._data.keys():raise ValueError("value '"+name+"' exists")
        self._data[name] = value
    def __getattr__(self, name):
        return self._data[name]
    def flushChanges(self):
        for obj in self._data.values():
            obj.changeSignal.emit()
    def custom(self):
        self._data["listWidget_proficiencies_VisualUpdate"] = DependentObject(None)
        self._data["listWidget_proficiencies_update"] = DependentObject(None)
        self._data["anythingChanged"] = DependentObject(None)
