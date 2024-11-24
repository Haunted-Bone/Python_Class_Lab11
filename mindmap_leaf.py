from textwrap import indent
Shapes = {}

Shapes ["circle"] = "(({}))"
Shapes ["oval"] = "({})"
Shapes ["square"] = "[{}]"
Shapes ["cloud"] = "){}("
Shapes ["hexagon"] = "{{{{{}}}}}"
Shapes ["bang"] = ")){}(("

class MindMapLeaf:
    def __init__(self,name,shape):
        self.name = name
        self.shape = shape
    def get_shape_representation(self):
        s = format(Shapes.get(self.shape))
        return s
    def __str__(self):
      return f'{self.name}'

    def display(self, indent=0):
         print(f" " * indent + str(self))





tEST = MindMapLeaf('tEST','square')


#tEST.display(3)
#print(tEST.get_shape_representation())

#print(str(tEST))