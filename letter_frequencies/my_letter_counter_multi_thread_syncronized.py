import json
import urllib.request as req
import time
from threading import Thread, Lock

finished_count = 0

def count_letters(url, frequency, mutex):
    response = req.urlopen(url)
    txt = str(response.read())

    mutex.acquire() #-- Lock shared memory

    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1

    mutex.release() #-- Free shared memory
        
def main():
    frequency = {}
    mutex = Lock()

    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0

    start = time.time()

    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()
    
    while True:
        mutex.acquire() #-- También hay que bloquear aquí ya que leemos una variable compartida
        if finished_count == 20:
            break
        mutex.release()
        time.sleep(0.5) # Chequeamos cada medio segundo si han terminado, o no, todos los hilos.


    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done!, time taken:", end-start)

main()


"""
    
    - Ahora que hemos aplicado algoritmos de mutua exclusión (mutex) para sincronizar los hilos al acceder a la
    memoria compartida, los resultados salen consistentes, iguales a los de la versión ordinal.

    OUTPUT:

        {
            "a": 80014,
            "b": 16998,
            "c": 48003,
            "d": 40501,
            "e": 140093,
            "f": 26074,
            "g": 19010,
            "h": 36316,
            "i": 79913,
            "j": 2170,
            "k": 6614,
            "l": 38305,
            "m": 31176,
            "n": 135371,
            "o": 84258,
            "p": 32270,
            "q": 2835,
            "r": 75326,
            "s": 79790,
            "t": 103557,
            "u": 27572,
            "v": 10580,
            "w": 14195,
            "x": 4719,
            "y": 13914,
            "z": 1115
        }
        Done!, time taken: 2.04266619682312
"""
