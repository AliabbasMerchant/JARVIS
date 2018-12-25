import pyautogui
import os
import time


# pyautogui.PAUSE = 0


def automate(sequence: str, *args):
    args_index = 0
    if sequence.strip() == "":
        raise Exception("Sequence name cannot be a whitespace")
    seq_dir = str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "automated_sequences"
    if os.path.exists(seq_dir + os.sep + sequence):
        with open(seq_dir + os.sep + sequence, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    line = " ".join(line.split())
                    try:
                        line = line[:line.index("#")].strip()
                    except ValueError:
                        pass
                    if line == "~arg~":
                        try:
                            print("Type (arg):", args[args_index])
                            pyautogui.typewrite(args[args_index])
                        except IndexError:
                            print("Type: ")
                            pyautogui.typewrite("")
                        args_index += 1
                    elif line.startswith("~sleep~"):
                        milliseconds = line[line.rindex("~") + 1:].strip()
                        try:
                            milliseconds = int(milliseconds)
                            if milliseconds >= 0:
                                print("Sleep Milliseconds:", milliseconds)
                                time.sleep(milliseconds // 1000)
                            else:
                                raise ValueError()
                        except ValueError:
                            raise Exception("The number of milliseconds to sleep must be a whole number.")
                    elif line.startswith("~~"):
                        seq = line[2:].strip()
                        automate(seq.split()[0], *seq.split()[1:])
                    elif line.startswith("~"):
                        keys = line[1:].split()
                        for k in keys:
                            if k not in pyautogui.KEY_NAMES:
                                raise Exception("No such key found:", k)
                        print("Press:", keys)
                        pyautogui.hotkey(*keys)
                    else:
                        print("Type:", line)
                        pyautogui.typewrite(line)
    else:
        raise Exception("No such automated sequence has been saved:", sequence)
