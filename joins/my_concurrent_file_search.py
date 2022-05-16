import os
from os.path import isdir, join
from threading import Lock, Thread

mutex = Lock()
matches = []

def file_search(root, filename):
    print("Searching in:", root)
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        #-- Recursive Search
        if isdir(file):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)
    for t in child_threads:
        t.join()


def main():
    Thread(target=file_search, args=("./", "thread")).start()
    #-- Al usar join nos aseguramos que, una vez llegamos aquí, todos los hilos lanzados hayan terminado.
    for m in matches:
        print("Matched:", m)

main()