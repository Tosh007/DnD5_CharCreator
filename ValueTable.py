try:
    from CharacterCore import *
    from acces import *
except ImportError:
    from program.CharacterCore import *
    from program.acces import *
import yaml
class ValueTable:
    def __init__(self):
        f = open(getDirectoryPrefix()+"data/character/values.yaml")
        data = yaml.load(f)
        f.close()
        for obj in data:
            name = tuple(obj.keys())[0]
            meta = tuple(obj.values())[0]
            ui=None
            config = ValueConfig
            format = None
            initial=0
            #print (meta)
            for key in meta:
                if key=="ui":
                    ui=getUI(meta[key])
                    #print (ui)
                if key=="config":
                    config = getConfig(meta[key])
                if key=="format":
                    format = meta[key]
                if key=="initial":
                    initial = meta[key]
            self.__dict__[name] = ValueReference(ui, config,format)
            self.__dict__[name].set(initial)
            self.__dict__[name].lastValue = initial
            #print(name,"=ValueReference(",ui,config, format,")")
    def flushChanges(self):
        for obj in self.__dict__.values():
            obj.changeSignal.emit()
