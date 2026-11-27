li1=[1,2,3,4]
set1=set(li1)

print("Unique Numbers: ",set1)
print("Unique Count: ",len(set1))

if len(li1) != len(set1):
    print("Duplicates Found")
else:
    print("All Unique")