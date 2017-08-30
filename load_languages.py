# utility script loading language who speaks what and converts to mod yaml
langs = {}
l = []
whitespace = "\r\n\t"
with open("Sprachen.csv","r") as input:
    line1 = input.readline()
    line1 = line1.split(",")
    for language in line1:
        language = language.strip(whitespace)
        langs[language]=[]
        l.append(language)
    s = input.readline()
    while s:
        s = s.split(",")
        assert len(s)==len(l)#always as many entries as language
        for i in range(len(s)):
            race = s[i]
            race = race.strip(whitespace)
            if race:#csv has empty entries
                langs[l[i]].append(race)
        s = input.readline()
import yaml
with open("data/character/language.yaml","w") as out:
    yaml.dump(langs,out)
