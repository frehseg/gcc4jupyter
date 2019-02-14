import os
import uuid
import timeit
import argparse
import tempfile
import subprocess
import IPython.core.magic as ipym

compiler = '/usr/local/cuda/bin/nvcc'
compiler_options = '-I /usr/local/cuda/samples/common/inc/ -L/usr/local/cuda/include -lcublas -lcusolver'
ext = '.cu'


def get_argparser():
    parser = argparse.ArgumentParser(description='NVCCPlugin params')
    parser.add_argument("-t", "--timeit", action='store_true',
                        help='flag to return timeit result instead of stdout')
    return parser

@ipym.magics_class
class NVCCPlugin(ipym.Magics):

    def __init__(self, shell):
        super(NVCCPlugin, self).__init__(shell)
        self.argparser = get_argparser()

    def run(self, file_path, timeit=False):
        if timeit:
            stmt = "subprocess.check_output(['{}'], stderr=subprocess.STDOUT)".format(file_path + ".out")
            return self.shell.run_cell_magic(magic_name="timeit", line="-q -o import subprocess", cell=stmt)
        else:
            return subprocess.check_output([file_path + ".out"], stderr=subprocess.STDOUT).decode("utf-8")

    @ipym.cell_magic
    def cu(self, line, cell):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit as e:
            self.argparser.print_help()
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ext, "w") as f:
                f.write(cell)
            try:
                subprocess.check_output([compiler, compiler_options, file_path + ext, "-o", file_path + ".out"], stderr=subprocess.STDOUT)
                print(self.run(file_path, timeit=args.timeit))
            except subprocess.CalledProcessError as e:
                print(e.output.decode("utf8"))

def load_ipython_extension(ip):
    nvcc_plugin = NVCCPlugin(ip)
    ip.register_magics(nvcc_plugin)
