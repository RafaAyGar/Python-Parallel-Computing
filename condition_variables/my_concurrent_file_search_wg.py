import os
from os.path import isdir, join
from threading import Lock, Thread

from wait_group import WaitGroup

matches = []
wg = WaitGroup()

def file_search(root, filename):
    print("Searching in:", root)
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            matches.append(full_path)
        #-- Recursive Search
        if isdir(file):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            wg.add(1)
    wg.done()


def main():
    Thread(target=file_search, args=("./", "thread")).start()
    #-- Al usar join nos aseguramos que, una vez llegamos aquí, todos los hilos lanzados hayan terminado.
    wg.wait()
    for m in matches:
        print("Matched:", m)

main()

