import pyautogui
import os


def gen_sequence(seq_name: str):
    if seq_name.strip() == "":
        raise Exception("Sequence name cannot be a whitespace")
    seq_dir = str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "automated_sequences"
    if seq_name in os.listdir(seq_dir):
        raise Exception("Sequence", seq_name, "already exists")
    print('Generating Sequence', seq_name)
    print('Instructions(Currently does not support mouse functions):')
    print('Available key names:', pyautogui.KEY_NAMES)
    print('For normal text, type "<text to be typed><enter>"')
    print('For simultaneous key press(es), type "~<space separated key name(s)><enter>"')
    print('To complete sequence generation, type "~~<enter>"')
    sequence = []
    while True:
        i = input()
        if i != "":
            if i == "~~":
                break
            elif i.strip().startswith("~"):
                t = i.strip()[1:].split()
                print(t)
                for s in t:
                    if s not in pyautogui.KEY_NAMES:
                        raise Exception("No such key found:", s)
                sequence.append('~'+" ".join(t))
            else:
                sequence.append(i)
    with open(seq_dir + os.sep + seq_name, "w+") as f:
        for s in sequence:
            f.write(s+"\n")
