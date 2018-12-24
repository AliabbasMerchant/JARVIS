from source import command
import sys


def display_help():
    print("JARVIS: A virtual voice and text based assistant for Windows.")


def do(text: str):
    if text.lower() == "help":
        display_help()
    elif text.startswith("!"):
        command.do(text[1:])
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    args = sys.argv
    args = args[1:]
    arguments = " ".join(args)
    do(arguments)
