import math;

class Vector2f(object):

    def __init__(self, xpos, ypos):
        self.__x  = xpos if((type(xpos) == float) or (type(xpos) == int)) else 0.0;
        self.__y  = ypos if((type(ypos) == float) or (type(ypos) == int)) else 0.0;

    @property
    def X(self):
        return self.__x;
    
    @property
    def Y(self):
        return self.__y;

    @X.setter
    def X(self, value):
        if ( (type(value) == float) or
             (type(value) == int)):
            self.__x = value;
    @Y.setter
    def Y(self, value):
        if((type(value) == float) or
           (type(value) == int)):
            self.__y = value;

    @property
    def Length(self):
        return math.sqrt((self.X * self.X) + (self.Y * self.Y));

    @property
    def Normalise(self):
     x  = 0;
     y  = 0;
     if(self.X !=0):
         x = self.X / self.Length;
     if(self.Y  != 0):
         y = self.Y / self.Length;
     self.X  = x;
     self.Y  = y;
     return self;

    def __add__(self, other):
        if(isinstance(other, Vector2f) != True):
            raise TypeError("expecting a Vector2f type");
        return Vector2f(other.X + self.X , other.Y + self.Y);

    def __iadd__(self, other):
        if(isinstance(other, Vector2f)):
            self.X  += other.X;
            self.Y  += other.Y;
        return self;
    
    def __sub__(self, other):
        return Vector2f(self.X - other.X, self.Y - other.Y)

    def __isub__(self, other):
        self  =  self.__sub__(other);
        return self;
    
    @property
    def Negate(self):
     xPos = self.X * -1;
     yPos = self.Y * -1;
     return Vector2f(xPos, yPos);

    def Dot(self, other):
        x = self.X * other.X;
        y = self.Y * other.Y;
        return x + y;

    def Cross(self, other):
        x = self.X * other.X - self.Y * self.Y;
        y = self.X * other.Y + self.Y * other.X;
        return Vector2f(x,y);


    def __mul__(self, other):
         result = None;
         if((type(other) == float) or
            (type(other) == int)):
             result  = Vector2f(self.X * other, self.Y * other);
         else:
             if(isinstance(other, Vector2f) != True):
                 raise TypeError("@Vector2f.scale: expecting parameter 1 to be Vector2f or float");
             result  = Vector2f(self.X * other.X , self.Y * other.Y);
         return  result;
        

    def __imul__(self, other):
        self = self.__mul__(other);
        return self;
    
    @property
    def Conjugate(self):
        return Vector2f(self.X, self.Y * -1);
    
    def __truediv__(self, other):
         status= isinstance(other,Vector2f);
         if(status != True):
             raise TypeError("@Vector2f : expecting an a Vector2f parameter");
         conjugate      = other.Conjugate;
         numerator      = self.Cross(conjugate);
         demonumerator  = other.Cross(conjugate);
       
         x = numerator.X / (demonumerator.X + demonumerator.Y);
         y = numerator.Y / (demonumerator.X + demonumerator.Y);
         
         return Vector2f(x,y);
    
    def __idiv__(self, other):
        self  = self.__truediv__(other);
        return self;
    
    def __str__(self):
        return "({0},{1})".format(self.X, self.Y);





if(__name__ == "__main__"):

    v  =  Vector2f(8.0,10);
    v2 = Vector2f(12,19);
    v3  = v * v2 - v2 / v2;
    print(v3.Length);
    v4 =v3.Normalise;
    print(v4);
    print(v4.Length);
    print(v3.Normalise.Length);
    print(v2.Cross(v).Normalise);
    print(v.Conjugate);
    print(v /v2 );
    print((v *90).Normalise);
            
