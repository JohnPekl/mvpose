from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy  # Ensure NumPy is imported to get the include path

ext_modules=[ Extension("pictorial",
              ["pictorial.pyx"],
              libraries=["m"],
              include_dirs=[numpy.get_include()],  # Add NumPy headers
              extra_compile_args = ["-ffast-math", "-O3"])]

setup(
  name = "pictorial",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules)