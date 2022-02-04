import sys
import os

path, skills = sys.argv[1], sys.argv[2]

if len(skills) != 10:
    print('Error: Provide 10 skills!')
    exit()


for filename in os.listdir(path):
    for name, keyword in [('(WindowMSButtonShared)', '.(BackgroundSimpleScallingTexture)'), ('(WindowSimple)', '.(WindowSimpleShared)')]:
        if name in filename:
            index = filename.split(name)[0][-2]
            if index not in "123456789X": continue
            index = int(index) if index != 'X' else 10
            data = open(f'{path}/{filename}', 'r').read().split(keyword)
            with open(f'{path}/{filename}', 'w') as file:
                for d in data[:-1]:
                    file.write(f'{d[:-1]}{skills[index-1]}{keyword}')
                file.write(data[-1])
    

# python .\switch.py .\UI\Doc\SkillWheel\Skills\Destructive\    123486759X
# python .\switch.py .\UI\Doc\SkillWheel\Skills\Enlightenment\  123756489X
# python .\switch.py .\UI\Doc\SkillWheel\Skills\Sorcery         1234X57689       
# python .\switch.py .\UI\Doc\SkillWheel\Skills\Offense\        12354679X8
# python .\switch.py .\UI\Doc\SkillWheel\Skills\Defense\        1234567X98
# python .\switch.py .\UI\Doc\SkillWheel\Skills\Leadership\     123945X867
# python .\switch.py .\UI\Doc\SkillWheel\Skills\Combat\         123486975X