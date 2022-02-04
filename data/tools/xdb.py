from xml.etree import cElementTree as ET
import os

class XDB:
    def __init__(self, tree) -> None:
        self.tree = tree
        self.tags = {c.tag: (ix, c) for ix, c in enumerate(tree)}

    @classmethod
    def new(Self, tag, content, attributes = None):
        tree = ET.Element(tag, attributes or {})
        if type(content) == str:
            tree.text = content
        else:
            tree.extend(c.tree for c in content)
        return Self(tree)

    @classmethod
    def load(Self, path):
        # print(path)
        return Self(ET.parse(path).getroot())

    def save(self, path, encoding='UTF-8'):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        ET.indent(self.tree, '\t')
        ET.ElementTree(self.tree).write(path, xml_declaration=True, encoding=encoding)

    @property
    def txt(self): return self.tree.text
    @txt.setter
    def txt(self, txt): self.tree.text = txt
        
    @property
    def int(self): return int(self.tree.text)
    @int.setter
    def int(self, txt): self.tree.text = str(txt)
    
    @property
    def atr(self): return self.tree.attrib

    @property
    def tag(self): return self.tree.tag
    
    def __getitem__(self, tag):
        if type(tag) == int:
            return XDB(self.tree[tag])
        else:
            return XDB(self.tags[tag][1])
    
    def __setitem__(self, tag, value):        
        index = tag if type(tag) == int else self.tags[tag][0]
        value = XDB.new(self.tree[index].tag, value)
        self.tags[value.tag] = index, value.tree
        self.tree.remove(self.tree[index])
        self.tree.insert(index, value.tree)

    def findall(self, tag):
        return (XDB(t) for t in self.tree.iter(tag))

    def find(self, tag):
        return next(self.findall(tag))

    def __iter__(self):
        return (XDB(tree) for tree in self.tree)
