#!usr/bin/env python3

def pair(arr):
	countn = 0
	results = []
	
	for i in arr:
		countn = 0
		
		#count for number of 1 present in the byte
		for j in i:
			if '1' in j:
				countn = countn + 1
		#if the number of 1 is even then add 0 in the beginning
		if countn%2==0:
			results.append("0" + i)
		else:
			results.append("1" + i)
	return results

num = int(input("Entrez un chiffre: "))
byte = "{0:b}".format(num)
print("Le chiffre en binaire:", byte)

byte_arr = [byte]
print("---Bit de parite pair---")
print(pair(byte_arr))
