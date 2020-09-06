# gcc4jupyter
This is an adaptation of the nvcc4jupyter plugin at https://smoolak.com/git/Smoolak/nvcc4jupyter.git
The goal is to compile and run C programs from Colab notebooks with minimal overhead. It suffices to prefix the program with <%%c>.

To use, run the following in a Python kernel:
```
!pip install git+git://github.com/frehseg/gcc4jupyter
%load_ext gcc_plugin
```

After this, any cell with prefix <%%c> is compiled and run as a C program.
