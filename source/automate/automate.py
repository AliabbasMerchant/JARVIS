import pyautogui
import os


def automate(sequence: str):
    if sequence.strip() == "":
        raise Exception("Sequence name cannot be a whitespace")
    seq_dir = str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "automated_sequences"
    if sequence in os.listdir(seq_dir):
        with open(seq_dir + os.sep + sequence, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                if line.startswith("~~"):
                    seq = line[2:].strip()
                    automate(seq)
                if line.startswith("~"):
                    keys = line[1:].split()
                    pyautogui.hotkey(*keys)
                else:
                    pyautogui.typewrite(line)
    else:
        print("No such automated sequence has been saved.")
