import pyautogui
import os


def gen_sequence(seq_name: str):
    if seq_name.strip() == "":
        raise Exception("Sequence name cannot be a whitespace")
    seq_dir = str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "automated_sequences"
    if os.path.exists(seq_dir + os.sep + seq_name):
        raise Exception("Sequence " + seq_name + " already exists")
    print('Generating Sequence', seq_name)
    print('Instructions(Currently does not support mouse functions):')
    print('Available key names:', pyautogui.KEY_NAMES)
    print('For normal text, type "<text to be typed><enter>"')
    print('For simultaneous key press(es), type "~<space separated key name(s)><enter>"')
    print('To reuse an existing automation sequence, type "~~<existing sequence name>"')
    print('To complete sequence generation, type "~exit<enter>"')
    sequence = []
    while True:
        i = input().strip()
        if i != "":
            if i == "~exit":
                break
            elif i.startswith("~~"):
                seq = i.lstrip()[2:].strip()
                if os.path.exists(seq_dir + os.sep + seq):
                    sequence.append("~~"+seq)
                else:
                    raise Exception("No such sequence found:", seq)
            elif i.startswith("~"):
                t = i.strip()[1:].split()
                for s in t:
                    if s not in pyautogui.KEY_NAMES:
                        raise Exception("No such key found:", s)
                sequence.append('~' + " ".join(t))
            else:
                sequence.append(i)
    if len(sequence) > 0:
        with open(seq_dir + os.sep + seq_name, "w+") as f:
            for s in sequence:
                f.write(s.strip() + "\n")
