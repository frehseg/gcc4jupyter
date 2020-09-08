def add_cpp_to_input(lines):
    if lines:
        if lines[0][0:2]!='%%':
            lines.insert(0,'%%c\n')
    return lines

def load_ipython_extension(ipython):
    ipython.input_transformers_cleanup.append(add_cpp_to_input)

