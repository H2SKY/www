import time, random

print("Progress bar simulation, by Dominik Rutkowski, Iza Czwórnóg, Lukas Dabroś.\n")
print("Our network is a little bit old. The downstream bandwidth is 6Mbps.")
print("It means that the maximum download speed is limited to roughly 750kB/s.\n")
print("This program simulates a downloading file of a given size.\n")
print("What is the file size in kilobytes[kB]? 1024 = 1MB, 1048576 = 1GB")

size = input()
filling = 0

while True:
    if size.isdigit():
        break
    elif size == "quit":
        exit()
    else:
        print("Please enter only numbers.")
        size = input()

size = int(size)
while filling < size:
    percentage = filling/size
    bar = percentage * 40
    percentage = percentage * 100
    percentage = float('%.1f' % percentage)
    bar = int(bar)
    empty = 40 - bar
    print('[', chr(9608) * bar, chr(32) * empty, '] ', percentage, '% ', filling, '/', size, sep='', end='\r')
    filling += random.randint(0, 750)
    time.sleep(1)
print('[', chr(9608) * 40, '] 100.0% ', size, '/', size, sep='')