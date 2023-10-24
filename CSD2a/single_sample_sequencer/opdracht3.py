import simpleaudio as sa #sa = SimpleAudio
import time
import random


#   load audio files, defining location of
hihat = sa.WaveObject.from_wave_file("hihat.wav"),
snare  = sa.WaveObject.from_wave_file("snare.wav"),
kick  = sa.WaveObject.from_wave_file("kick.wav")


#   variables & values
BPM                     = 120 
measures                = 4  
beats_16th              = 0
beats_16th_total        = 0 
beats_16th_left         = 0
beat_4th_duration       = 60 / BPM          # 1/4th  measure
beat_16th_duration      = 60 / BPM / 4      # 1/16th measure


#   lists
sequence = []
timestamps16th = []
timestamps = []


#   setting BPM
while True:
    # ask for input
    inp = input("Enter a new BPM or press enter for default of 120: ")

    # if no input, default value
    if not inp:
        inp = BPM
        print("BPM of", inp, "set")
        BPM = inp
        break
    
    # else ask for integer, if not an integer repeat till it is
    else:
        try:
            inp = int(inp)
        except ValueError:
            print("Please enter a valid integer")
            continue
        print("BPM of", inp, "set")
        break


#   asking for measures
while True: 
    try:
        measures = int(input("How many measures should the sequence consist of?: "))
    except ValueError:
        print("Please enter a valid integer")
        continue
    break

#   calculating the amount of 16th notes within the measures
beats_16th_total = measures * 16
print(measures, "measures or a total of", beats_16th_total, "16th notes")


#   user input for creating the sequence
while (beats_16th < beats_16th_total):
    while True:
        try:
            user_input = int(input())
        except ValueError:
            print("Please enter a valid integer", end = " ")
            continue
        break

    beats_16th = beats_16th + user_input
    beats_16th_left = beats_16th_total - beats_16th

    # when to play sample
    sequence.append(1)
    
    add_zero_for = user_input - 1

    # 16th beats rest
    for j in range(add_zero_for):
        sequence.append(0)

    print(sequence, beats_16th_left, "notes left to use")

# shorten list
sequence = sequence[:beats_16th_total]
print(len(sequence))


for i in range(len(sequence)):
    if (sequence[i] == 1):
        timestamps16th.append(i)

print(timestamps16th)

# from timestamps to duration in seconds
for timestamp in timestamps16th:
    timestamps.append(timestamp * beat_16th_duration)

# get the first element
timestamp = timestamps.pop(0)

# define start position
startTime = time.time()

while True:
    currentTime = time.time()
    
    if(currentTime - startTime >= timestamp):
        kick.play()

        if timestamps:
            timestamp = timestamps.pop(0)
        else:
            break
    
    else:
        time.sleep(0.001)

time.sleep(1) # end buffer for last note 



