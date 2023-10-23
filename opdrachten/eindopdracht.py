import simpleaudio as sa #sa = SimpleAudio
import time 
import random
from midiutil import MIDIFile


#   sound information
kick = {
    'timestamps': [], 
    'instrumentname': "kick", 
    'velocity': 100, # midi velocity
    'sequence': [],
    'durations': [],
    'midi_note_pitch': 36
}
snare = {
    'timestamps': [], 
    'instrumentname': "snare", 
    'velocity': 100, # midi velocity
    'sequence': [],
    'durations': [],
    'midi_note_pitch': 38
}
hihat = {
    'timestamps': [], 
    'instrumentname': "hihat", 
    'velocity': 100, # midi velocity
    'sequence': [],
    'durations': [],
    'midi_note_pitch': 42
}


#   setup
BPM                     = 120
measures                = 4  
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
            BPM = inp 
        except ValueError:
            print("Please enter a valid integer")
            continue
        print("BPM of", inp, "set")
        print()
        break
       

beat_16th_duration      = 60 / BPM / 4      # 1/16th measure

#   asking for time signature
def get_multiplier_from_time_signature():
    while True:
        time_signature = input("Enter a time signature in a (x/y) format: ")
        
        if time_signature == "":
            print("Default time signature of 4/4 set")
            return 4

        # split the input string using the '/' character
        parts = time_signature.split('/')

        # check if the input is in the correct format
        if len(parts) != 2:
            print("Invalid time signature format. Please use 'x/y' format.")
            continue
        
        # try to extract the first number and convert it to an integer
        try:
            multiplier = int(parts[0])
        except ValueError:
            print("Invalid amount of beats per measure. Please provide a valid integer.")
            continue
        
        print("Time signature of", time_signature, "set")
        return multiplier

#   get time signature and multiply by 4 for the amount of 16th notes
multiplier = get_multiplier_from_time_signature()
beat_16th_amount = multiplier * 4


#   asking for the amount of measures
while True: 
    # ask for input
    measures = input("Enter the amount of measures the sequence should consist of: ")

    # if not input default value
    if not measures:
        measures = 1
        print("Default sequence length of", measures, "measures set")
        break

    # else ask for integer, if not an integer repeat till it is
    else:
        try:
            measures = int(measures)
        except ValueError:
            print("Please enter a valid integer")
            continue
        print("Sequence length of", beat_16th_amount*measures, "set")
        break


#   amount of 16th notes times measures to get total sequence length
sequence_len = beat_16th_amount * measures


#   get polyrhythmic values
def get_polyrhythmic_values():
    while True:
        polyrhythm = input("Enter the polyrhythm values for the kick, snare and hihat in (k:s:h) format: ")
        
        if polyrhythm == "":
            print("Default values of 3:5:2 set")
            pr_k = 3
            pr_s = 5
            pr_h = 2
            return pr_k, pr_s, pr_h

        # split the input string using the ':' character
        parts = polyrhythm.split(':')

        # check if the input is in the correct format
        if len(parts) != 3:
            print("Invalid format. Please use (k:s:h).")
            continue
        
        # extract the number corresponding to the right sample and convert it to an integer
        try:
            pr_k = int(parts[0])
            pr_s = int(parts[1])
            pr_h = int(parts[2])
            return pr_k, pr_s, pr_h
        except ValueError:
            print("Invalid amount of beats per measure. Please provide a valid integer.")
            continue
        

#   paste values onto
pr_kick, pr_snare, pr_hihat = get_polyrhythmic_values()

#   print values
print(f"Kick: {pr_kick}, Snare: {pr_snare}, Hihat: {pr_hihat}")

  
#   create a list with lenght sequence_len that contains only zeros
def random_seq(data,  sequence_len):
    seq = [0]*sequence_len
    
    # append values for chosen polyrhythm value
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
            timestamps.append(i*beat_16th_duration)

    data['timestamps'] = timestamps # writing the list
    # print(data['instrumentname'])
    # print(data['timestamps'])
    return data 


#   midi setup
track       = 0
channel     = 9  # aka channel 10 drums
moment      = 0
tempo       = BPM
duration    = beat_16th_duration # why 8?? no idea but its works after trial and error
velocity    = 100

beat = MIDIFile(1)
beat.addTrackName(track, moment, "Generated Beat")
beat.addTempo(track, moment, tempo)


#   creating midi file
def create_midi_file():
    # writing data onto midi file
    def add_onto_midifile(data):
        moment = 0

        for hits in data['sequence']:
            if hits == 1:
                beat.addNote(track, channel, data['midi_note_pitch'], moment, duration, data['velocity'])
            moment = moment + 0.25

    # writing data onto
    add_onto_midifile(kick)
    add_onto_midifile(snare)
    add_onto_midifile(hihat)

    # actually create the file
    print("Midi File Created")
    with open("beat.mid", "wb") as output_file:
        beat.writeFile(output_file)


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


#   sort list
event_seq.sort(key=get_ts) 


#   setting up time 
time_zero = time.time()
play_seq = event_seq.copy()
event = play_seq.pop(0)

print("Press CTRL+C to interupt loop")


#   playback loop
while True:
    try:
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

    except KeyboardInterrupt:
        user_input = input("  Do you want to save the MIDI file (y/n)? ").strip().lower()
        if user_input == 'y':
            create_midi_file()
            break  # Exit the program
        elif user_input == 'n':
            print("New sequence generated")
            # Regenerate the random sequence
            kick['sequence'] = random_seq(pr_kick, sequence_len)
            snare['sequence'] = random_seq(pr_snare, sequence_len)
            hihat['sequence'] = random_seq(pr_hihat, sequence_len)

            #   convert binary sequence to timestamps
            convert_sequence_to_timestamps(kick)
            convert_sequence_to_timestamps(snare)
            convert_sequence_to_timestamps(hihat)


            #   create one big list of dictionaries for playback
            event_seq = []
            event_seq += create_events(kick['timestamps'], 'kick')
            event_seq += create_events(snare['timestamps'], 'snare')
            event_seq += create_events(hihat['timestamps'], 'hihat')


            #   sort list
            event_seq.sort(key=get_ts) 


            # Reset time_zero
            time_zero = time.time()
            play_seq = event_seq.copy()
            event = play_seq.pop(0)
        else:
            print("Invalid input. Code shutting down")
            break
