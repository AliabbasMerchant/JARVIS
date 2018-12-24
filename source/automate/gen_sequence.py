import pyautogui
import os

seq_dir = str(__file__)[:str(__file__).index("source")] + "config" + os.sep + "automated_sequences"


def correct(seq: str):
    global seq_dir
    if seq == "~arg~":
        return True
    if seq.startswith("~sleep~"):
        milliseconds = seq[seq.rindex("~") + 1:].strip()
        try:
            milliseconds = int(milliseconds)
            if milliseconds >= 0:
                return True
            else:
                raise ValueError()
        except ValueError:
            raise Exception("The number of milliseconds to sleep must be a whole number.")
    if seq.startswith("~~"):
        seq = seq[2:].strip().split()[0]
        if os.path.exists(seq_dir + os.sep + seq):
            return True
        else:
            raise Exception("No such sequence found:", seq)
    if seq.startswith("~"):
        t = seq[1:].strip()
        for s in t.split():
            if s not in pyautogui.KEY_NAMES:
                raise Exception("No such key found:", s)
        return True
    return True


def gen_sequence(seq_name: str):
    global seq_dir
    if seq_name.strip() == "":
        raise Exception("Sequence name cannot be a whitespace")
    if os.path.exists(seq_dir + os.sep + seq_name):
        raise Exception("Sequence " + seq_name + " already exists")
    print('Generating Sequence', seq_name)
    print('Instructions(Currently does not support mouse functions):')
    print('Available key names:', pyautogui.KEY_NAMES)
    print('For normal text, type on a new line: "<text to be typed><enter>"')
    print('For simultaneous key press(es), type on a new line: "~<space separated key name(s)><enter>"')
    print('To reuse an existing automation sequence, type on a new line: "'
          '~~<existing sequence name> <space separated optional arguments>"')
    print('To add a placeholder for a text argument, type on a new line: "~arg~<enter>"')
    print('To add a comment, type "#<comment><enter>"')
    print('To make JARVIS wait for some time, type on a new line: "~sleep~<milliseconds to sleep><enter>"')
    print('To complete sequence generation, type on a new line: "~exit<enter>"')
    sequence = []
    while True:
        i = input().strip()
        if i != "":
            if i == "~exit":
                break
            i = " ".join(i.split())
            try:
                t = i[:i.index("#")].strip()
            except ValueError:
                t = i
            if correct(t):
                sequence.append(i)
    if len(sequence) > 0:
        with open(seq_dir + os.sep + seq_name, "w+") as f:
            for s in sequence:
                f.write(s.strip() + "\n")
