
class Matrix4f(object):

    def __init__(self):
        """
          row 1  =  a11 a12 a13 a14
          row 2  =  a21 a22 a23 a24
          row 3  =  a31 a32 a33 a44
          row 4  =  a41 a42 a43 a44
        """
        self.__mat  = [
                            [0,0,0,0],  # 1
                            [0,0,0,0],  # 2
                            [0,0,0,0],  # 3
                            [0,0,0,0]]; # 4


    @property
    def Identity(self):
        mat4f  = Matrix4f();
        mat4f.__mat[0][0] = 1 ;self.__mat[0][1]  = 0; self.__mat[0][2]  = 0;self.__mat[0][3]  = 0;
        mat4f.__mat[1][0] = 0 ;self.__mat[1][1]  = 1; self.__mat[1][2]  = 0;self.__mat[1][3]  = 0;
        mat4f.__mat[2][0] = 0 ;self.__mat[2][1]  = 0; self.__mat[2][2]  = 1;self.__mat[2][3]  = 0;
        mat4f.__mat[3][0] = 0 ;self.__mat[3][1]  = 0; self.__mat[3][2]  = 0;self.__mat[3][3]  = 1;       
        return mat4f;



if(__name__ =="__main__"):
    mat  = Matrix4f();
    print(mat);
    print(mat.Identity);
    
