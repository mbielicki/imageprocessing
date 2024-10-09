from cli.process_cli_args import process_cli_args
from exceptions import ApplicationError

def main():
    try:
        process_cli_args()
    except ApplicationError as e:
        print(e)


if __name__ == "__main__":
    main()