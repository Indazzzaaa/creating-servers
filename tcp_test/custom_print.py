from pathlib import Path

path = Path(__file__)

file = open(f"{path.parent}\output.txt", 'w')


def printF(*arg, **kwargs):
    if len(arg):
        print(arg, file=file,flush=True)
    if len(kwargs):
        print(kwargs, file=file,flush=True)
