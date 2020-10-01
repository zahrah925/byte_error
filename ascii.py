#!usr/bin/env python3

def summ(ASCII,n):
	return(sum(ASCII))


string = input("Entrez un mot pour convertir en ascii: ")
ASCII = []

for character in string:
	ASCII.append(ord(character))
print("Apres la conversion:", ASCII)

n = len(ASCII)
result = summ(ASCII,n)

print("checksum1 = ", result)
