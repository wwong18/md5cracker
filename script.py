import hashlib
import itertools
import time

a_z = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
counter = 0;
solved_words = 0;
listOfWords = list()
with open("hashes.txt",'r') as file:
	for line in file:
		line = line.replace("\n", "")
		listOfWords.append(line)
#Start the actual script

while counter < 4:
	start = time.time()
	guesses = itertools.permutations(a_z*counter,counter)
	for guess in list(guesses):
		for word in listOfWords:
			result =  hashlib.md5(''.join(guess))
			if result.hexdigest() == word:
				end = time.time()
				print(''.join(guess))
				print("MD5 Hash: " )
				print(result.hexdigest())
				print(end-start)	
				listOfWords.remove(word)
	counter = counter + 1


file.close()
