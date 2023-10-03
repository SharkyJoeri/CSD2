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
quarterNoteDuration     = 60 / BPM          # 1/4th  measure
sixteenthNoteDuration   = 60 / BPM / 4      # 1/16th measure


#   lists, t = time
t_stamps      = []
t_stamps16th  = []

#INPUTS FROM USER  - measures, sequence
#CALCULATE TIME
#START SEQUENCE

inputs()
getTime()


def inputs()
    print("How many measures should the sequence consist of?")
    measures = int(input())

    sequenceLength16th = measures * 16

    for i in range(sequenceLength16th -):
        
        user_input = input()

        beat.append(float(user_input))



def getTime():
    # from time intervals in seconds to 16th note durations
    for t_stamp in t_stamps16th:
        t_stamps.append(t_stamp * sixteenthNoteDuration)

    # get the first element from the time stamps list
    t_stamp = t_stamps.pop(0)

    # set basetime
    startTime = time.time()







#   playback certain audio file from samples list
def playBack(sound_object):
    samplePlay = (sound_object).play() 
    samplePlay.wait_done()

 
for sample in samples:
    print(sample)
    playBack(sample)


    randomIndex = random.randint(0, 2)
    print("waiting: " + str(timeIntervals[randomIndex]) + " seconds.")
    time.sleep(timeIntervals[randomIndex])



# timeIntervals = [0.25, 0.5, 1]


#Defining variables

# timestamps16th = [] #Timestamps at which to play the sample

# noteDurations = [] 

# durationsToTimestamps16th = []

# BPM = 120

# # print("BPM:", BPM)
# print("Please enter BPM")
# BPM = int(input())

# print("BPM of", BPM, "confirmed")

# print("How long should the sequence be?")
# numPlaybackTimes = int(input())

# for i in range(numPlaybackTimes):
#     noteDurations.append(int(input()))

# print(noteDurations)







# sequence = [kick, hihat, snare, hihat]

# samples = [
#     (sa.WaveObject.from_wave_file("hihat.wav")),
#     (sa.WaveObject.from_wave_file("snare.wav")),
#     (sa.WaveObject.from_wave_file("kick.wav"))
# ]

# t_stamps8th   = []
# eightNoteDuration       = 60 / BPM / 2      # 1/8th  measure