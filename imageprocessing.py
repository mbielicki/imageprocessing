from cli.help_message import help_message
from cli.process_cli_args import process_cli_args
from exceptions import ApplicationError, ArgumentError

def main():
    try:
        process_cli_args()
    except ArgumentError as e:
        print(e)
        print(help_message)
    except ApplicationError as e:
        print(e)


if __name__ == "__main__":
    main()