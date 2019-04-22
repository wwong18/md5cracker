import hashlib
import itertools
import time

a_z = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = 0;
solved_words = 0;
listOfWords = list()
with open("hashes.txt",'r') as file:
	for line in file:
		listOfWords.append(line)
#Start the actual script

while solved_words != len(listOfWords):
	start = time.time()
	guesses = itertools.permutations(a_z,counter)
	for guess in list(guesses):
		print(''.join(guess))
		result =  hashlib.md5(''.join(guess))
		for word in listOfWords:
			if result.hexdigest() == word:
				end = time.time()
				listOfWords.remove(word)
				print(''.join(guess))
				print("MD5 Hash: " )
				print(result.hexdigest())
				print(end-start)	
	counter = counter + 1


file.close()
