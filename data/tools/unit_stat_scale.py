import sys
import os
from xml.etree import cElementTree as ET

path, tag, amount = sys.argv[1], sys.argv[2], float(sys.argv[3])

def scale(path):
    for filename in os.listdir(path):
        filepath = f'{path}/{filename}'
        if os.path.isdir(filepath): scale(filepath)
        if filename[-4:] != ".xdb": continue
        # try:
        data = ET.parse(filepath)
        print(data.getroot()[0])
        for t in data.iter(tag):
            t.text = str(int(int(t.text)*amount))
        ET.indent(data, '\t')
        data.write(filepath, xml_declaration=True, encoding='UTF-8', )
        # except:
        #     print(filepath)

scale(path)