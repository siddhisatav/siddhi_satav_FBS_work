mount = int(input("Enter the amount: "))

# List of available notes
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Dictionary to store number of each note
note_count = {}

# Loop through each note
for note in notes:
    if amount >= note:
        note_count[note] = amount // note   # number of notes of this denomination
        amount = amount % note              # remaining amount

# Output result
print("Minimum number of notes required:")
for note, count in note_count.items():
    print(f"{note} : {count}")