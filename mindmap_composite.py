import os
import mindmap_leaf



#Global Variables
Shapes = {}

Shapes ["circle"] = "(({}))"
Shapes ["oval"] = "({})"
Shapes ["square"] = "[{}]"
Shapes ["cloud"] = "){}("
Shapes ["hexagon"] = "{{{{{}}}}}"
Shapes ["bang"] = ")){}(("



class MindMapComposite:
    def __init__(self,name,shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add_child(self, child):
        self.children.append(child)


    def remove_child(self,child):
        self.children.remove(child)


    def get_shape_representation(self):
        s = format(Shapes.get(self.shape), format(self.name))
        return s
    def __str__(self):
        return f'{self.name}, {Shapes.get(self.shape)}'

    def display(self, indent=0):
        print(f'{self.name}')
        for child in self.children:
            child.display(indent + 2)

newtest = MindMapComposite("new test", 'hexagon')

