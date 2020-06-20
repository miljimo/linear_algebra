import setuptools
long_description = "Linear algebra module for matrix, transformation and scale";
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(name = "linear_algebra-jimobama",
      version="0.0.1",
      description="Mathematic linear algebra module for calculation and matrix malipulation",
      long_description =long_description,
      url="https://github.com/miljimo/linear_algebra.git",
      long_description_content_type="text/markdown",
      author="Obaro I. Johnson",
      author_email="johnson.obaro@hotmail.com",
      packages=setuptools.find_packages(),
      install_requires=['mpi4py>=2.0',
                        
                       ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
         
    ],python_requires='>=3');

      
