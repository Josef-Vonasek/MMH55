import sys
import os
from xdb import XDB
from skillwheel import camel_case

path = sys.argv[1]

masteries = {'MASTERY_BASIC':1, 'MASTERY_ADVANCED':2, 'MASTERY_EXPERT':3}
table = {
    'Voice': 'Shouting',
    'Artificier': 'Artificer',
    'ShatterSummoning': 'Stamina',
    'ShatterDestructive': 'Rush',
    'ShatterDark': 'Faith',
}
def skillname(name, mastery=''):
    name = camel_case(name[10:])
    if name in table: return mastery[8:].capitalize() + ' ' + table[name]
    if mastery: name = f'{name}/{masteries[mastery]}'
    for file in ['Common', 'Unique']:
        path = f'Text/Game/Skills/{file}/{name}/Name.txt'
        if os.path.exists(path):
            return open(path, encoding='utf-16').read()
    return name

names = []
def start_skills(path):
    for filename in os.listdir(path):
        filepath = f'{path}/{filename}'
        if os.path.isdir(filepath): start_skills(filepath)
        if filename[-4:] != ".xdb": continue
        try:
            data  = XDB.load(filepath)
            perk = [skillname(perk.txt) for perk in data['Editable']['perkIDs']]
            skil = zip(data.findall('SkillID'), data.findall('Mastery'))
            skil = [skillname(s.txt, m.txt) for s, m in skil]
            text = '<br><color=yellow>Starts with:<br>'+'<br>'.join(skil+perk)

            for name in ['SpecializationNameFileRef', 'SpecializationDescFileRef']:
                name = '.' + data[name].atr['href']
                if name not in names:
                    names.append(name)
                    open(name, 'a', encoding='utf-16').write(text)
        except Exception as e:
            print(filename)
            print(e)


start_skills(path)