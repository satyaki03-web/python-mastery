dict={"Amit":78,"Riya":92,"Neha":64}
tot=0
for score in dict.values():
    tot+=score
avg=tot/len(dict)

print(f"The average is :{avg:.2f}")

name=input("Enter a name: ").strip().lower()

if name in dict:
    print(f"{name}'s marks is {dict[name]}")
else:
    print("Not Found")