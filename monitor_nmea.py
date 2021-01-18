import sys
import time
import threading

thisdict={}
print_thread=None

def read_nmea_thread():
    global thisdict
    for line in sys.stdin:
        items = line.rstrip().split(',')
        tuplet = { "timestamp": time.time(), "line": line.rstrip() }
        thisdict[items[0]]=tuplet

def print_nmea_data():
    global thisdict
    global print_thread
    print("\033c", end="") # clear the linux screen
    right_now = time.time()
    for sentence in thisdict:
        age = round(right_now - thisdict[sentence]["timestamp"], 1)
        if age < 2:
            print (thisdict[sentence]["line"], "({}s)".format(age))
    for sentence in thisdict:
        age = round(right_now - thisdict[sentence]["timestamp"], 1)
        if age >= 2:
            print (thisdict[sentence]["line"], "({}s)".format(age), "***** STALE *****")
    print_thread = threading.Timer(1, print_nmea_data)
    print_thread.start()


nmea_thread = threading.Thread(target = read_nmea_thread, daemon=True)
nmea_thread.start()

print_thread = threading.Timer(1, print_nmea_data)
print_thread.start()

try:
    nmea_thread.join()
except:
    print_thread.cancel()

