import re
file = open("american_tabloid.txt", "r")
sample = file.read()

sentences = re.split("(?<=[.!?]) +", sample)
sentence_count = len(sentences)
total_words = 0
total_letters = 0


for sentence in sentences:
    words = str.split(sentence)
    total_words = total_words + len(words)
    for word in words:
        letters = list(word)
        total_letters = total_letters + len(letters)



avg_sentencelength = (total_words/sentence_count)
avg_wordlength = (total_letters/total_words)

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(total_words))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average Letter Count: " + str(avg_wordlength))
print("Average Sentence Length: " + str(avg_sentencelength))