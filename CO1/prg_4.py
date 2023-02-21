#Count the occurrences of each word in a line of text.
linetext = "this is a sample of text"
word= dict()
txt =linetext.split(" ")
for t in txt:
    if t in word:
        word[t] += 1
    else:
        word[t] = 1
print(word)