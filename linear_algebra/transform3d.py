from linear_algebra.matrix4f import Matrix4f;
from linear_algebra.vector3f import Vector3f;


class Transform3D(object):

    def __init__(self, **kwargs):

        self.__Position =  kwargs['position']  if(('position' in kwargs) and
                                                 (isinstance(kwargs['position'], Vector3f))) else Vector3f(0,0,0);
        self.__Rotation =  kwargs['rotation'] if(('rotation' in kwargs) and
                                                 (isinstance(kwargs['rotation'], Vector3f))) else Vector3f(0,0,0);
        self.__Scale    =  kwargs['scale']    if(('scale' in kwargs) and
                                                 (isinstance(kwargs['scale'], Vector3f))) else Vector3f(0,0,0);
        self.__Matrix   =  Matrix4f();
        self.__Matrix   =  self.__Matrix.Identity;
        

    @property
    def Matrix(self):
        traslationMatrix  =  self.__GetTranslationMatrix(self.Position);
        rotationMatrix    =  self.__GetRotationMatrix(self.Rotation);
        scaleMatrix       =  self.__GetScaleMatrix(self.Scale);
        # translate , rotation , then scale 
        # traslate matrix, rotate matrix , scale matrix
        self.__Matrix =   (((self.__Matrix * translationMatrix) *  rotationMatrix)  *  scaleMatrix);
        return self.__Matrix;


    def __GetTranslationMatrix (self, pos):
        pass;

    def __GetRotationMatrix(self, rotation):
        pass;

    def __GetScaleMatrix(self,scale):
        pass;
    
    @property
    def Scale(self):
        return self.__Scale;

    @Scale.setter
    def Scale(self, other):
        if(isinstance(other, Vector3f) != True):
            raise TypeError("@Scale: expecting an vector3f object.");
        self.__Scale  = other;

    @property
    def Rotation(self):
        return self.__Rotation;
    
    @Rotation.setter
    def Rotation(self, value):
        if(isinstance(value, Vector3f) != True):
            raise TypeError("Expecting a vector3f object");
        self.__Rotation  = value;
        

    @property
    def Position(self):
        return self.__Position;
    
    @Position.setter
    def Position(self, position):
        if(isinstance(position, Vector3f) != True):
            raise TypeError("@Position: expecting a Vector3f object");
        self.__Position  = position;
            
