import pyautogui
import os


def automate(sequence: str):
    if sequence.strip() == "":
        raise Exception("Sequence name cannot be a whitespace")
    seq_dir = str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "automated_sequences"
    if os.path.exists(seq_dir + os.sep + sequence):
        with open(seq_dir + os.sep + sequence, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                if line.startswith("~~"):
                    seq = line[2:].strip()
                    automate(seq)
                elif line.startswith("~"):
                    keys = line[1:].split()
                    for k in keys:
                        if k not in pyautogui.KEY_NAMES:
                            raise Exception("No such key found:", k)
                    # print("hotkey:", keys)
                    pyautogui.hotkey(*keys)
                else:
                    # print("typewrite:", line)
                    pyautogui.typewrite(line)
    else:
        raise Exception("No such automated sequence has been saved:", sequence)
