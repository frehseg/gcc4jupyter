from distutils.core import setup

setup(
    name='GCCPlugin',
    version='0.0.8',
    author='Goran Frehse',
    author_email='goranf@gmail.com',
    py_modules=['gcc_plugin','add_cpp_magic','solution_toggle'],
    url='htpps://github.com/frehseg/gcc4jupyter',
    license='LICENSE',
    description='Jupyter notebook plugin to run C/C++ code',
    # long_description=open('README.md').read(),
)
