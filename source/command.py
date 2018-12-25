from .automate.automate import automate
from .automate.gen_sequence import gen_sequence
from .text_to_speech import text_to_speech
import os
import json


def do(command: str):
    commands = json.load(open(str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "commands.json", 'r'))
    command_args = " ".join(command.split()[1:])
    if command.split()[0].lower() in commands["Execute Automated Sequence"]:
        automate(command_args.split()[0], *command_args.split()[1:])
    elif command.split()[0].lower() in commands["Generate Automate Sequence"]:
        gen_sequence(command_args)
    else:
        raise AttributeError("No such command exists:", command)
    print("Command Successfully Executed!")
    text_to_speech("Command Successfully Executed!")
