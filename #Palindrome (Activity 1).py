#Palindrome (Activity 1)

pal = input("Input a word: ")
pals = pal.lower().replace(" ", "")
slap = ""

for i in pals:
    slap = i + slap
if pals == slap:
    print(pal,"is a palindrome!")
else:
    print(pal,"is not a palindrome!")
