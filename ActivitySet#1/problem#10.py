counts = dict()
file_handling = open("mbox-short.txt")

for line in file_handling:

    if line.startswith("From"):
        words = line.split()

        if len(words) > 6:
            counts[words[1]] = counts.get(words[1], 0) + 1

big_count = None
big_word = None

for word, count in counts.items():
    
    if big_count is None or count > big_count:
        big_count = count
        big_word = word
        
print(big_word, big_count)
