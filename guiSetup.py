from PyQt5.QtCore import*
# disable proficiency checkboxes
def setup_main_window(ui):
    return
    l = (ui.checkBox_strength_saves,ui.checkBox_athletics,
        ui.checkBox_dexterity_saves,ui.checkBox_sleight_of_hand,ui.checkBox_stealth,ui.checkBox_acrobatics,
        ui.checkBox_constitution_saves,ui.checkBox_intelligence_saves,ui.checkBox_investigation,ui.checkBox_religion,
        ui.checkBox_arcana,ui.checkBox_nature,ui.checkBox_history,
        ui.checkBox_insight,ui.checkBox_medicine,ui.checkBox_wisdom_saves,ui.checkBox_animal_handling,ui.checkBox_survival,
        ui.checkBox_perception,ui.checkBox_charisma_saves,ui.checkBox_deception,ui.checkBox_intimidation,ui.checkBox_performance,
        ui.checkBox_persuation)
    for w in l:
        w.setAttribute(Qt.WA_TransparentForMouseEvents)