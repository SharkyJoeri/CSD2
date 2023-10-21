import simpleaudio as sa #sa = SimpleAudio
import time 
import random


#   sound information
kick = {
    'timestamps': [], 
    'instrumentname': "kick", 
    'velocity': 100, # midi velocity
    'sequence': [],
    'durations': []
}
snare = {
    'timestamps': [], 
    'instrumentname': "snare", 
    'velocity': 100, # midi velocity
    'sequence': [],
    'durations': []
}
hihat = {
    'timestamps': [], 
    'instrumentname': "hihat", 
    'velocity': 100, # midi velocity
    'sequence': [],
    'durations': []
}

pr_kick = 0
pr_snare = 0
pr_hihat = 0

#   setup
BPM                     = 120
measures                = 4  
beat_16th_duration      = 60 / BPM / 4      # 1/16th measure
beat_16th_amount        = 0
sequence_len            = 16  


#   setting BPM
while True:
    # ask for input
    inp = input("Enter a new BPM: ")

    # if no input, default value
    if not inp:
        inp = BPM
        print("Default BPM of", inp, "set")
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


#   asking for time signature
def get_multiplier_from_time_signature():
    while True:
        time_signature = input("Enter a time signature in a (x/y) format: ")
        
        if time_signature == "":
            return 4

        # split the input string using the '/' character
        parts = time_signature.split('/')

        if len(parts) != 2:
            print("Invalid time signature format. Please use 'x/y' format.")
            continue
        
        # try to extract the first number and convert it to an integer
        try:
            multiplier = int(parts[0])
        except ValueError:
            print("Invalid amount of beats per measure. Please provide a valid integer.")
            continue
        
        return multiplier


# Call the function to get the multiplier
multiplier = get_multiplier_from_time_signature()
beat_16th_amount = multiplier * 4

while True: 
    measures = input("Enter the amount of measures the sequence should consist of: ")

    if not measures:
        measures = 1
        print("Default sequence length of", measures, "measures set")
        break

    else:
        try:
            measures = int(measures)
        except ValueError:
            print("Please enter a valid integer")
            continue
        print("Sequence length of", measures, "set")
        break


sequence_len = beat_16th_amount * measures

# def polyrhythms():
#     kick = 3
#     snare = 5
#     hihat = 2

#     def get_input(prompt, default_value):
#         while True:
#             try:
#                 user_input = input(prompt)
#                 if user_input == "":
#                     return default_value
#                 value = int(user_input)
#                 if 0 < value < beat_16th_amount:
#                     return value
#                 else:
#                     print("Input must be an integer between 1 and", beat_16th_duration,".")
#             except ValueError:
#                 print("Invalid input. Please enter an integer.")

#     kick = get_input(f"Enter a value for kick (default {kick}): ", kick)
#     snare = get_input(f"Enter a value for snare (default {snare}): ", snare)
#     hihat = get_input(f"Enter a value for hihat (default {hihat}): ", hihat)

#     print(f"kick = {kick}, snare = {snare}, hihat = {hihat}")



# if __name__ == "__main__":
#     polyrhythms()


# #   setting BPM
# def polyrythms(sample):
#     while True:
#         # ask for input
#         inp = input("Enter a polyrythm value for the", sample, ": ")
      
#         # if no input, default value
#         if not inp:
#             pr_kick = 3
#             print("Default polyrythm value of", inp, "set for", sample)
        
#         if not snare:
#             pr_kick = 3
#             print("Default polyrythm value of", inp, "set")

#         if not kick:
#             pr_kick = 3
#             print("Default polyrythm value of", inp, "set")
#             break
            
        
#         # else ask for integer, if not an integer repeat till it is
#         else:
#             try:
#                 inp = int(inp)
#             except ValueError:
#                 print("Please enter a valid integer")
#                 continue
#             print("BPM of", inp, "set")
#             break
#     return polyrythm

# pr_kick = polyrythms(kick)
# pr_snare = polyrythms(snare)
# pr_hihat = polyrythms(hihat)


    
# firstly we make a list with lenght sequence_len that contains only zeros
def random_seq(data,  sequence_len):
    seq = [0]*sequence_len
    
    for i in range(0, sequence_len, data):
        seq[i -1 + random.choice([1, -1])] = 1

    return seq


kick['sequence'] = random_seq(pr_kick, sequence_len)

snare['sequence'] = random_seq(pr_snare,sequence_len)
    
hihat['sequence'] = random_seq(pr_hihat,sequence_len)


#   function for adding information onto timestamps
def create_events(ts_seq, sample_id):
    events = []
    for ts in ts_seq:
        events.append({'ts': ts, 'sample_id': sample_id})
    return events

def get_ts(event):
    return event['ts']


#   convering the timestamps to note durations in seconds
def convert_sequence_to_timestamps(data): 
    timestamps = [] # temporary list for converted timestamps

    for i in range(len(data['sequence'])): # converting 1/0 > timestamps
        if data['sequence'][i] == 1:
            # if (i%1 == 0):
            #     print()
            #     beat_16th_duration + groove_delay
            #     print(beat_16th_duration)
            # else:
            #     beat_16th_duration - groove_delay
            #     print(beat_16th_duration)
            timestamps.append(i*beat_16th_duration)

    data['timestamps'] = timestamps # writing the list
    # print(data['instrumentname'])
    # print(data['timestamps'])
    return data 


#   load audio files, defining location of
samples = {}
samples['kick'] = sa.WaveObject.from_wave_file("kick.wav")
samples['snare'] = sa.WaveObject.from_wave_file("snare.wav")
samples['hihat'] = sa.WaveObject.from_wave_file("hihat.wav")


#   convert binary sequence to timestamps
convert_sequence_to_timestamps(kick)
convert_sequence_to_timestamps(snare)
convert_sequence_to_timestamps(hihat)


#   create one big list of dictionaries for playback
event_seq = []
event_seq += create_events(kick['timestamps'], 'kick')
event_seq += create_events(snare['timestamps'], 'snare')
event_seq += create_events(hihat['timestamps'], 'hihat')

event_seq.sort(key=get_ts) # sort list


#   setting up time 
time_zero = time.time()
play_seq = event_seq.copy()
event = play_seq.pop(0)
num_playback_times = 4


#   playback loop
while num_playback_times:
    now = time.time() - time_zero

    if(now > event['ts']):
        sample_id = event['sample_id']
        samples[sample_id].play()
        # print(play_seq)
        if   play_seq:
            event = play_seq.pop(0)

        else:
            time_zero = time.time()
            time.sleep(beat_16th_duration)
            play_seq = event_seq.copy()
            event = play_seq.pop(0)
            time_zero = time.time()
    else:
        time.sleep(0.001)


"""-

time signature > 4/4, 5/4, 7/8   x/y

3/4     1 uh me     2 nu me     3 nu me     4 ne me
4/4     1   uh      2   uh      3   uh      4   uh
5/4     1   uh      2   uh      3   uh      4   uh    

if 8 note duration / 2


x = amount of 16th notes per beat (x * y for total 16th notes)
y = amount of beats


how many measures to input? is amount of 16th notes in time signature times amount of measures




how long sequence? > 16

ask polyrythm all samples
- 3 kick
- 5 snare
- 2 hihat

generate sequence

>> velocity (amplitude samples)


beat_16th_



- - - - - - - - % 
x . . x . . x . . x . . x . .





"""


# def random_seq(data):
#     sequence = []
#     for i in sequence_len:
#         sequence.append(1)
    
#         add_zero_for = user_input - 1

#         # 16th beats rest
#         for j in range(add_zero_for):
#             sequence.append(0)


# 4/4 slices 4 > 1 1 0 1 > add zero inbetween > 1 0 1 0 0 0 1 0 > sequencer > x3 for every sample
# 5/4 slices 5



# def convert_timestamps_to_durations(data):
#     durations = []

#     beat_16th_durations = 60 / BPM / 4

#     for timestamp in range(len(data['sequence'])):
#         durations.append(timestamp * beat_16th_duration)

#     data['durations'] = durations
#     print(data['durations'])
#     return data



# print(beat_16th_duration)

# # define start position
# startTime = time.time()

# while True:
#     currentTime = time.time()
    
#     if(currentTime == beat_16th_duration):
#         print(currentTime)

#         # if timestamps:
#         #     timestamp = timestamps.pop(0)
#         # else:
#         #     break
    
#     else:
#         time.sleep(0.001)

# time.sleep(1) # end buffer for last note 

