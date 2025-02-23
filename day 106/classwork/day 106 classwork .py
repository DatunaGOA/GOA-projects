# Initialize a set: flush = set()

# A set is used because it automatically removes duplicates.
# Loop through each card: for i in cards:

# Iterates over each card in the list cards.
# Add the suit to the set: flush.add(i[-1])

# i[-1] gets the last character of the card string, which represents the suit (e.g., 'H' for hearts).
# Check if all suits are the same: return len(flush) == 1

# If the set flush has only one unique suit, it means all cards are of the same suit.


def Flush(cards):
    flush = set()
    for i in cards:
        flush.add(i[-1])
    return len(flush) == 1
