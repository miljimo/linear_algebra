import math;
from linear_algebra.vector3f import Vector3f;


class Quaternion(Vector3f):

    def __init__(self, x , y , z , w):
        super().__init__(x, y,z);
        self.__W  = float(w);
        
    @property
    def W(self):
        return self.__W;

    @W.setter
    def W(self, value):
        if((type(value) == float) or
           (type(value) == int)):
            self.__W  = value;
        else:
            raise TypeError("@Expecting a floating value");

    def __str__(self):
        return "({0},{1},{2},{3})".format(self.X, self.Y, self.Z, self.W);


    def __add__(self, other):
       if(isinstance(other, Quaternion) != True):
           raise TypeError("@Expecting a Quaternion object");
       v3 = super().__add__(other);
       return Quaternion(v3.X, v3.Y, v3.Z, other.W + self.W);

    def __iadd__(self, other):
        self = self.__add__(other);
        return self;

    def __sub__(self, other):
       if(isinstance(other, Quaternion) != True):
           raise TypeError("@Expecting a Quaternion object");
       v3 = super().__sub__(other);
       return Quaternion(v3.X, v3.Y, v3.Z,  self.W - other.W);

    def __isub__(self, other):
        self = self.__sub__(other);
        return self;

    def __mul__(self, other):
        if(isinstance(other, Quaternion) != True):
            scale  =  float(other);
            return Quaternion(self.X * scale , self.Y * scale, self.Z * scale, self.W * scale);
        return Quaternion(self.X * other.X , self.Y * other.Y, self.Z * self.Z, self.W * self.W);

    def __imul__(self, other):
        self  = self.__mul__(other);
        return self;
    

    def Cross(self , other):
        if(isinstance(other,Quaternion) != True):
            if(isinstance(other, Vector3f) != True):
               raise TypeError("Expecting a vector3f or quaternion object");
            other  = Quaternion(other.X, other.Y, other.Z, 0);
        return self.__CrossQuaternion(other);


    def __CrossQuaternion(self, other):
        if(isinstance(other,Quaternion) != True):
            raise TypeError("Expecting a quaternion object");
        
        w =  (self.W * other.W) - (self.X * other.X) - (self.Y * other.Y) - (self.Z * other.Z);
        x =  (self.W * other.X) + (self.X * other.W) + (self.Y * other.Z) - (self.Z * other.Y);
        y =  (self.W * other.Y) - (self.X * other.Z) + (self.Y * other.W) + (self.Z * other.X);
        z =  (self.W * other.Z) + (self.X * other.Y) - (self.Y * other.X) + (self.Z * other.W);
        return Quaternion(x,y,z,w);
        
        
    
    @property
    def Length(self):
        return (math.sqrt((self.X *self.X) + (self.Y * self.Y) + (self.Z * self.Z) + (self.W * self.W)));

    def Dot(self, other):
        if(isinstance(other, Quaternion) != True):
            raise TypeError("Expecting a Quaternion object");
        return ((self.X * other.X ) + (self.Y * other.Y) + (self.Z * other.Z) + (self.W * other.W));
    
    @property
    def Conjugate(self):
      return Quaternion(-1 * self.X, -1 * self.Y, -1 * self.Z, self.W);

    @property
    def Normalise(self):
        # This is also called versor
        length = self.Length;
        return Quaternion(self.X / length, self.Y / length, self.Z / length, self.W/length);
    
    @property
    def Inverse(self):
        conjugate = self.Conjugate;
        sqtNorm   = self.Length * self.Length;
    
        x = conjugate.X / sqtNorm;
        y = conjugate.Y / sqtNorm;
        z = conjugate.Z / sqtNorm;
        w = conjugate.W / sqtNorm;
        return Quaternion(x, y,z,w);

    def __truediv__(self, other):
        result  = self;
        if(isinstance(other, Quaternion) != True):
            raise TypeError("@Expecting a Quaternion object");
        if(other.IsZero != True):
            result  = self.Cross(other.Inverse);
        return result;

    def __idiv__(self, other):
        self =  self.__truediv__(other);
        return self;

    @property
    def IsZero(self):
       return ((self.X  == 0) and  (self.Y ==0) and (self.Z == 0) and (self.W == 0));
     



if(__name__ =="__main__"):
    q  = Quaternion(12,0.4, 2.0,1);
    w  = Quaternion(12,0.4, 2.0,1);
    v  = Vector3f(12, 0.4,6.9);
    print(q + q - w);
    print(w.Dot(q));
    print(w.Cross(q) * q);
    print(w.Conjugate);
    print(w.Length);
    wx = w.Normalise;
    print(wx.Length);
    print(w.Cross(v));
    print(w.Inverse);
    print(q/ w);
            
        
