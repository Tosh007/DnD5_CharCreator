import yaml
f=open("spellList.yaml","r")
data = yaml.load(f)
f.close()
# all cantrips, remove duplicates
cantrips = set()
spells1  = set()

for group in data:
    c = tuple(group.values())[0]
    c = set(c)
    if "cantrip" in tuple(group.keys())[0]:
        cantrips |= c
    else:
        assert "spells" in tuple(group.keys())[0]
        spells1 |= c

out = ({"cantrips":tuple(cantrips)},{"spells":tuple(spells1)})
with open("spellListGroups.yaml","w") as f:
    yaml.dump(out,f,default_flow_style=False)
