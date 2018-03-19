from distutils.core import setup, Extension

yescryptr16_module = Extension('yescryptr16',
                            sources = ['yescrypt.c'],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'yescryptr16',
       version = '1.0',
       description = 'Bindings for yescryptr16 proof of work used by Yenten',
       ext_modules = [yescryptr16_module])
