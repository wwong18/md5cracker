import hashlib
import itertools
import time

a_z = "1234abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ567890@ "
counter = 0;
solved_words = 0;
listOfWords = list()
with open("hashes.txt",'r') as file:
	for line in file:
		line = line.replace("\n", "")
		listOfWords.append(line)
#Start the actual script

while len(listOfWords) != 0 or counter != 9:
	start = time.time()
	if len(listOfWords) != 0:
		for guess in itertools.permutations(a_z*counter,counter):
			if len(listOfWords) != 0:
				for word in listOfWords:
					result =  hashlib.md5(''.join(guess))
					if result.hexdigest() == word:
						end = time.time()
						print(''.join(guess))
						print("MD5 Hash: " )
						print(result.hexdigest())
						print(end-start)	
						listOfWords.remove(word)
						break;
			else:
				break
		counter = counter + 1
	else:
		break


file.close()
