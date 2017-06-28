import yaml

from acces import*
from CharacterCore import *

class ModifierTable:
    def __init__(self):
        f = open(getDirectoryPrefix()+"data/character/modifier.yaml")
        data = yaml.load(f)
        f.close()
        for d in data:
            name = tuple(d.keys())[0]
            meta = tuple(d.values())[0]
            l = lambda x:x
            text = "default modifier text"
            order = 0
            for key in meta:
                if key=="lambda":
                    l = "lambda x:"+meta[key]
                    l = eval(l)
                if key=="order":
                    order = meta[key]
                if key=="text":
                    text = meta[key]
            self.__dict__[name] = ValueModifier(l, text, order)
