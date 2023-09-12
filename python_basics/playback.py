print("How long should the sequence be?")
numPlaybackTimes = int(input())

beat = []

print("Enter the lengths of the individuel notes one by one")
for i in range(numPlaybackTimes):
    beat.append(int(input()))

print("Your sequence has been generated")
print(beat)

print("Enter the BPM at which it should be played back")
BPM = int(input())

print("BPM of", BPM, "confirmed")

