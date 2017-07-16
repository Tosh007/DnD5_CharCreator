with open("spellList.yaml", "a") as output:
    category = input("category: ")
    output.write('- "'+category+'":\n')
    abort=False
    while not abort:
        spell = input("spell: ")
        output.write('    - "'+spell+'.SPELL."\n')
        abort = spell==""
