file = open("AFINN-111.txt","r")
words = file.readlines()

dictionary = {}

for word in words:
	dictionary[word.split('\t')[0]] = int(word.split('\t')[1].split('\n')[0])

	
msg = input("Enter:")
score = 0

for word in msg.split(' '):
	if word.lower() in dictionary:
		score += dictionary[word.lower()]

if score < 0:
	print("sad")
if score > 0:
	print("happy")
if score == 0:
	print("neutral")


input()