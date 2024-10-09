import sys
from process_image import process_image
from elementary.operations import negative, brightness, contrast
from geometric.operations import paint, hflip

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
        process_image(args, brightness)
    elif command == '--contrast':
        process_image(args, contrast)
    elif command == '--negative':
        process_image(args, negative)
    elif command == '--hflip':
        process_image(args, hflip)
    elif command == '--test':
        process_image(args, paint)
    else:
        print("Unknown command: " + command)

main()