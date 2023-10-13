sequence = [1, 0, 0, 0, 1, 1, 0, 1]
timestamps = []
# if 1 add timestamp

# for i in (lengte sequence)
    # timestamp [i]
    # if 1 add timestamp for [i]
    # if 0 go next

# print(sequence)

# for i in range(len(sequence)):
#     if (sequence[i] == 1):
#         timestamps.append(i)
    
# print(timestamps)

default_val = '120'
inp = input("Enter a new BPM or press enter for default of '"+default_val+"'")
if not inp:
    inp = default_val
print(inp)
BPM = inp