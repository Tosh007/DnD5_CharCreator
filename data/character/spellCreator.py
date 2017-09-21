with open("spellList.yaml", "a") as output:
    category = input("category: ")
    output.write('- "'+category+'":\n')
    while True:
        spell = input("spell: ")
        if spell:
            output.write('    - "'+spell+'.SPELL."\n')
        else:
            break
