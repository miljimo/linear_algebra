import math;

class Vector3f(object):

    def __init__(self, xpos, ypos, zpos):
        self.__X = float(xpos);
        self.__Y = float(ypos);
        self.__Z = float(zpos);
        pass;
    
    @property
    def X(self):
        return self.__X;
    
    @X.setter
    def X(self, xpos):
        self.__X   = float(xpos);

    @property
    def Y(self):
        return self.__Y;

    @Y.setter
    def Y(self, ypos):
        self.__Y  = float(ypos);

    @property
    def Z(self):
        return self.__Z;
    
    @Z.setter
    def Z(self, value):
        self.__Z  = float(value);
        
    def Dot(self):
        return ((self.X * self.X) + (self.Y * self.Y) + (self.Z * self.Z));
        
        
    @property
    def Length(self):
        return (math.sqrt((self.X * self.X) + (self.Y * self.Y) + (self.Z * self.Z)));

    @property
    def Normalise(self):
        if(self.Length == 0):
            return Vector3f(0,0,0);
        return Vector3f(self.X / self.Length, self.Y / self.Length, self.Z / self.Y);

    def __str__(self):
        return "({0},{1},{2})".format(self.X, self.Y, self.Z);

    def __add__(self, other):
        if(isinstance(other, Vector3f) != True):
           raise TypeError("@__add__ : unable to add {0} to vector3f".format(type(other)));
        return Vector3f(other.X + self.X , self.Y + other.Y, self.Z + other.Z);

    def __iadd__(self, other):
        self = self.__add__(other);
        return self;

    def __sub__(self, other):
        if(isinstance(other, Vector3f) != True):
            raise TypeError("@Vector3f.__sub__: expecting a Vector3f");
        return Vector3f(self.X - other.X, self.Y - other.Y, self.Z - other.Z);

    def __isub__(self, other):
        self  = self.__sub__(other);
        return self;

    def __mul__(self, other):
        result = None;
        if(isinstance(other, Vector3f)):
            result  = Vector3f(self.X * other.X, self.Y * other.Y, self.Z * other.Z);
        else:
            other  =  float(other);
            result  = Vector3f(other * self.X , self.Y * other, self.Z * other);
        if(result == None):
            raise TypeError("Expecting a floating number or Vector3f object");
        return result;

    def __imul__(self, other):
        self  = self.__mul__(other);
        return self;
    
    @property
    def Negate(self):
        return self * -1;

    def Cross(self, other):
        if(isinstance(other,Vector3f) != True):
            raise TypeError("@Cross : expecting a vector3f object");
   
        x = self.X * self.Z  - self.Z * other.Y;
        y = self.Z * other.X - self.X * other.Z;
        z = self.X * other.Y - self.Y * other.X;
        return Vector3f(x,y,z);


    def __eq__(self,other):
        status = False;
        if(isinstance(other, Vector3f)):
            if((self.X == other.X) and
               (self.Y == other.Y) and
               (self.Z == other.Z)):
                status = True;
        return status;

   
    @staticmethod
    def Unit():
        return Vector3f(1,1,1);



if(__name__ == "__main__"):
    position  = Vector3f(10,2, 3);
    print(position + Vector3f(0,1, 0) + Vector3f(12,4,10));
    print(position.Length);
    pos = position.Normalise;
    print(pos.Length);
    print("unit vector  = {0}".format(pos));
    print(position.Dot());
    print(pos.Dot());
    print(pos * position * 1);
    print(pos.Negate);
    print(pos.Cross(position));
    print(pos  == pos);
    print(Vector3f.Unit());
  
    
    
    




        
        
