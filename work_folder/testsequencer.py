import simpleaudio as sa #sa = SimpleAudio
import time
import random

#   load audio files, defining location of
hihat = sa.WaveObject.from_wave_file("hihat.wav"),
snare  = sa.WaveObject.from_wave_file("snare.wav"),
kick  = sa.WaveObject.from_wave_file("kick.wav")


#   variables & values
BPM                     = 160 
measures                = 4  
beats_16th              = 0
beats_16th_total        = 0 
beats_16th_left         = 0
beat_4th_duration       = 60 / BPM          # 1/4th  measure
beat_16th_duration      = 60 / BPM / 4      # 1/16th measure

#   lists
kick_list = []
snare_list = []
hihat_list = []

#   user input
print("How many measures should the sequence consist of?")
measures = int(input())
beats_16th_total = measures * 16
print(measures, "measures or", beats_16th_total, "16th notes")


def createSequence(sequence):
    beats_16th = 0
    while (beats_16th < beats_16th_total):
        user_input = int(input())
        beats_16th = beats_16th + user_input
        beats_16th_left = beats_16th_total - beats_16th
        print(beats_16th_left, "16th notes left to use")

        # when to play sample
        sequence.append(1)
        
        add_zero_for = user_input - 1
    
        # limit for max list length
        # if (beats_16th_left < add_zero_for):
        #     add_zero_for = add_zero_for + beats_16th_total - beats_16th
        #     print(add_zero_for)

        # 16th beats rest
        for j in range(add_zero_for):
            sequence.append(0)
    
    print(beats_16th_total)
    if (beats_16th > beats_16th_total):
        del sequence[(beats_16th_total + beats_16th_left)]

    print(sequence)

createSequence(kick_list, "kick")
createSequence(snare_list, "snare")
createSequence(hihat_list, "hihat")


# sequence * loop_sequence
def playBack(sound_object):
    (sound_object).play() 
    # samplePlay.wait_done()


def playSequence():
    for i in range(beats_16th_total):
        if (kick_list[i] == 1):
            playBack(kick)
            print((i + 1), "Kick")
            time.sleep(beat_16th_duration)

            # play sample
        else:
            time.sleep(beat_16th_duration)
        
        if (snare_list[i] == 1):
            playBack(snare)
            print((i + 1), "Snare")
            time.sleep(beat_16th_duration)

            # play sample
        else:
            time.sleep(beat_16th_duration)
        
        if (hihat_list[i] == 1):
            playBack(hihat)
            print((i + 1), "Hihat")
            time.sleep(beat_16th_duration)

            # play sample
        else:
            time.sleep(beat_16th_duration)

playSequence()

# measure_16th = ["| - - - - | - - - - | - - - - | - - - - |"]

# print((i % 4 + 1), "Bang")