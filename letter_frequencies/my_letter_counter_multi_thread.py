import json
import urllib.request as req
import time
from threading import Thread

finished_count = 0

def count_letters(url, frequency):
    response = req.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1
        
def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0

    start = time.time()

    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start()
    while finished_count < 20:
        time.sleep(0.5) # Chequeamos cada medio segundo si han terminado, o no, todos los hilos.

    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done!, time taken:", end-start)

main()


"""
    
    - Nos fijamos en que en esta versión multihilo el conteo de cada letra es diferente que en la versión secuencial, esto es 
    debido a problemas de sincronización de memoria con los hilos.

    OUTPUT:

        {
        "a": 80014,
        "b": 16998,
        "c": 48003,
        "d": 40501,
        "e": 139296,
        "f": 25893,
        "g": 18726,
        "h": 36045,
        "i": 79159,
        "j": 2170,
        "k": 6614,
        "l": 37978,
        "m": 31176,
        "n": 135371,
        "o": 82724,
        "p": 32270,
        "q": 2835,
        "r": 75326,
        "s": 77525,
        "t": 96253,
        "u": 27572,
        "v": 10580,
        "w": 14195,
        "x": 4719,
        "y": 13914,
        "z": 1115
    }
    Done!, time taken: 2.0337467193603516
"""
