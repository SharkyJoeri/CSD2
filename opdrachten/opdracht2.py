import simpleaudio
import time

filename = "kick.wav"
sound_object = simpleaudio.WaveObject.from_wave_file(filename)

beat = []

#Defining variables
print("How long should the sequence be?")
numPlaybackTimes = int(input())

print("Enter the lengths of the individuel notes one by one, 1 equals a quarter note")
for i in range(numPlaybackTimes):
    beat.append(float(input()))

print("Your sequence has been generated")
print(beat)

print("Enter the BPM at which it should be played back")
BPM = int(input())

print("BPM of", BPM, "confirmed")   


#Playing sound
def playback():
    play_object = sound_object.play()
    # play_object.wait_done()

#to get a quarter note as a baseline multiple
step = (60/BPM)

for n in beat: # range(beat.length)
    playback()
    time.sleep(n * step)
    print(n * step)



