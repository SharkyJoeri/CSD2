import simpleaudio

filename = "klaxon.wav"
sound_object = simpleaudio.WaveObject.from_wave_file(filename)

def soundplay():
    print("Playing sound", i + 1)
    play_object = sound_object.play()
    play_object.wait_done()

print("How many times do you want the sound to play?")
n = int(input())

for i in range(n): 
    soundplay()

print("Script done")
    
    