text="python is fun and python is fast and python works"
new=text.split()
freq={}
for word in new:
    freq[word]=freq.get(word, 0)+1
max_word=""
max_count=0

for word,count in freq.items():
    if count>max_count:
        max_count=count
        max_word=word
print("Word Freq: ",freq)
print(f"Most frequent word: {max_word} (count: {max_count})")

batch_a = ["python", "sql", "git", "excel", "python"]
batch_b = ["sql", "java", "git", "linux"]

seta=set(batch_a)
setb=set(batch_b)

print("In both batches: " ,seta & setb)
print("Only in batch A", seta - setb)
print("All unique skills: ", seta | setb)