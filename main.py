import subprocess
import sys

from parser import parse_input_file
from file_generator import create_prolog_program

def parse_command_line_args(args):
    conf = {"input": "input.txt", "output": "output.pl"}
    if len(args) == 0:
        return conf
    if len(args) == 2:
        if args[0][1:] not in conf.keys():
            sys.exit("Unknown flag")
        conf[args[0][1:]] = args[1]
        return conf
                       
    if len(args) == 4:
        if args[0][1:] not in conf.keys() or args[2][1:] not in conf.keys():
            sys.exit("Unknown flag")
        conf[args[0][1:]] = args[1]
        conf[args[2][1:]] = args[3]
        return conf
    sys.exit("Incorrect number of command line arguments (must be 0, 2 or 4, including flags)")
    
def main():
    args = sys.argv[1:]
    input_output_conf = parse_command_line_args(args)
    
    input_file = input_output_conf["input"]
    try:
        graph = parse_input_file(input_file)
    except:
        sys.exit("Error during the parsing of the input file")
    
    output_file = input_output_conf["output"]
    create_prolog_program(graph, output_file)
    
    try:
        subprocess.run(["powershell", f"swipl {input_output_conf["output"]}"], shell=True)
    except:
        sys.exit("Could not run the Prolog program")

if __name__ == "__main__":
    main()