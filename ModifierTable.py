import yaml

from acces import*
from CharacterCore import *

class ModifierTable:
    def __init__(self):
        f = open(getDirectoryPrefix()+"data/character/modifier.yaml")
        data = yaml.load(f)
        f.close()
        self._data = {}
        for d in data:
            name = tuple(d.keys())[0]
            meta = tuple(d.values())[0]
            l = lambda x:x
            text = "default modifier text"
            order = 0
            dependsOn = ()
            for key in meta:
                if key=="lambda":
                    l = "lambda x:"+meta[key]
                    l = eval(l)
                if key=="order":
                    order = meta[key]
                if key=="text":
                    text = meta[key]
                if key=="dependsOn":
                    dependsOn = meta[key]
            self.newModifier(name, ValueModifier(l, text, order, dependsOn))
        for auto in (AutoModRace,AutoModClass):
            c = auto()
            self.autoModInit(c)

    def newModifier(self,name,modifier):
        assert modifier not in self._data.values()
        assert name not in self._data.keys()
        self._data[name] = modifier

    def __getattr__(self,name):
        return self._data[name]

    def autoModInit(self,r):
        for name, mod in r.getMods():
            self.newModifier(name,mod)


class AutoModBase:
    lambdaBase = "x"
    textBase = "AutoModBase"
    nameBase = "AutoModName"
    def __init__(self):
        self.values=()
    def createFromList(self,values):
        for value in values:
            for v in self.new(value):
                yield v
    def newFromFormat(self,lambda_args=(),text_args=(),name_args=(),order=0):
        l = self.lambdaBase.format(*lambda_args)
        l=eval("lambda x:"+l)
        text = self.textBase.format(*text_args)
        name = self.nameBase.format(*name_args)
        order=int(order)
        return name, ValueModifier(l,text,order)
    def new(self,value):
        yield self.newFromFormat(value,value)
    def getMods(self):
        for mod in self.createFromList(self.values):
            yield mod

class AutoModRace(AutoModBase):
    lambdaBase = "x{0}"
    textBase = "{0}"
    nameBase = "{0}_{1}"
    def __init__(self):
        f = open(getDirectoryPrefix()+"data/character/automod_races.yaml")
        self.values = yaml.load(f)
        f.close()
    def new(self,value):
        yield self.newFromFormat(("+1",), (value+": +1",), (value, "plus1"))
        yield self.newFromFormat(("+2",), (value+": +2",), (value, "plus2"))
        yield self.newFromFormat(("+1",), (value,), (value, "proficient"))

class AutoModClass(AutoModBase):
    lambdaBase = "x{0}"
    textBase = "{0}"
    nameBase = "{0}_proficient"
    def __init__(self):
        f = open(getDirectoryPrefix()+"data/character/automod_classes.yaml")
        self.values = yaml.load(f)
        f.close()
    def new(self,value):
        yield self.newFromFormat(("+1",), (value,), (value,))
