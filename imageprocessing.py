import sys
from brightness import brightness

def args_to_dict(args):
    return dict(arg.split('=') for arg in args)

def main():

    if len(sys.argv) == 1:
        print("No command line parameters given.\n")
        sys.exit()

    if len(sys.argv) == 2:
        print("Too few command line parameters given.\n")
        sys.exit()

    command = sys.argv[1]
    args = args_to_dict(sys.argv[2:])
    
    if command == '--brightness':
        brightness(args)
    else:
        print("Unknown command: " + command)

main()