def check(text):
    vowel="AEIOUaeiou"
    c=0
    for char in text:
        if char in vowel:
            c+=1
    return c
word=input("Enter anything: ")
print("Total Vowels is: ",check(word))