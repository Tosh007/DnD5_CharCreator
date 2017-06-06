#class ModifierTable_:
#    Human_plus1 = VMod(lambda x:x+1, "Human: {2:+d}")
#    HalfOrc_plus1 = VMod(lambda x:x+1, "Half Orc: {2:+d}")
#    HalfOrc_plus2 = VMod(lambda x:x+2, "Half Orc: {2:+d}")
#    Barbarian_HP = VMod(lambda x:x+12, "Barbarian: {2:+d}")
#    AbilityScoreHardCap = VMod(lambda x: min(20,x), "Hardcap at 20", 8)
import yaml
from acces import*
from CharacterCore import *
class ModifierTable:
    def __init__(self):
        f = open("data/character/modifier.yaml")
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
