import json
import urllib.request as req
import time

def count_letters(url, frequency):
    response = req.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
        
def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done!, time taken:", end-start)

main()


"""
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
    Done!, time taken: 18.8845157623291
"""
