from vector3f import Vector3f;
from vector2f import Vector2f;

class Vertex(object):

    def __init__(self, **kwargs):
        self.__Position =  kwargs['position'] if('position' in kwargs) else Vector3f(0,0,0);
        self.__Normal   =  kwargs['normal'] if('normal' in kwargs)     else Vector3f(0,0,0);
        self.__Coord    =  kwargs['coord'] if('coord' in kwargs)       else Vector2f(0,0)

    @property
    def Position(self):
        return self.__Position;

    @Position.setter
    def Position(self, pos):
        if(isinstance(pos, Vector3f) != True):
            raise TypeError("@Expecting a vector3f object");
        self.__Position  = pos;

    @property
    def Normal(self):
        return self.__Normal;

    @Normal.setter
    def Normal(self, value):
        if(isinstance(value, Vector3f) != True):
            raise TypeError("@Expecting a vector3f object.");
        self.__Normal  = value;
        
    @property
    def Coord(self):
        # the coordinte for the texture of the vertex;
        return self.__Coord;

    @Coord.setter
    def Coord(self, coord):
        if(isinstance(coord, Vector2f) != True):
            raise TypeError("Expecting a Vector2f object ");
        self.__Coord = coord;



if(__name__=="__main__"):

    vertex  = Vertex(position= Vector3f(10,2,3), coord=Vector2f(1,-1), normal=Vector3f(1,82,1.9));
    print(vertex);
    print(vertex.Position);
    print(vertex.Normal);
    print(vertex.Coord);

    pass;
