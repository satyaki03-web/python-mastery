str=input("Enter a string: ")
clean=str.lower().replace(" ","")
rev=""
for char in clean:
    rev=char+rev
if rev==clean:
    print("Palindrome String")
else:
    print("Not Palindrome String")

vowel=0
cons=0
for ch in clean:
    if ch.isalpha():
        if ch in 'aeiou':
            vowel+=1
        else:
            cons+=1
print("Vowel: ",vowel)
print("Consonent: ",cons)