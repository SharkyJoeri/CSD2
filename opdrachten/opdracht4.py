import simpleaudio as sa #sa = SimpleAudio
import time


#   setup
BPM                     = 95 
measures                = 4  
beat_16th_duration      = 60 / BPM / 4      # 1/16th measure


#   sound information
kick = {
    'timestamps': [], 
    'instrumentname': "kick", 
    'velocity': 100, # midi velocity
    'duration': 300, # duration to play the sample for
    'sequence': [1, 1, 0, 0,  0, 0, 0, 0,  1, 1, 0, 0,  1, 0, 0, 0],
    'durations': []
}
snare = {
    'timestamps': [], 
    'instrumentname': "snare", 
    'velocity': 100, # midi velocity
    'duration': 300, # duration to play the sample for
    'sequence': [0, 0, 0, 1,  0, 0, 1, 0,  0, 0, 1, 1,  0, 0, 1, 0],
    'durations': []
}
hihat = {
    'timestamps': [], 
    'instrumentname': "hihat", 
    'velocity': 100, # midi velocity
    'duration': 300, # duration to play the sample for
    'sequence': [1, 0, 1, 1,  1, 0, 1, 1,  1, 0, 1, 1,  1, 0, 1, 1],
    'durations': []
}


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
            timestamps.append(i*beat_16th_duration)

    data['timestamps'] = timestamps # writing the list
    print(data['instrumentname'])
    print(data['timestamps'])
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
        if play_seq:
            event = play_seq.pop(0)
        else:
            time_zero = time.time()
            time.sleep(beat_16th_duration)
            play_seq = event_seq.copy()
            event = play_seq.pop(0)
            time_zero = time.time()
    else:
        time.sleep(0.001)






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

