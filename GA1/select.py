# CS325 - Group Assignment #1
# Author: Francisco Bolanos, Jaehyung You
# Date : Tue, October 10, 2017
# Filename : select.py

import os
import struct

def get_m():
    with open('input.txt','rt') as f1:
        for line in f1:
            x = line.split(',')[0]
    return x

def get_n():
    with open('input.txt','rt') as f2:
        for line in f2:
            y = line.split(',')[1]
    return y

def get_k():
    with open('input.txt','rt') as f3:
        for line in f3:
            z = line.split(',')[2]
    return z
	
def write_to_output(number):
	with open('output.txt', 'w') as f4:
		f4.write(str(number))

#it will give you an element to the specific index.
def getnum(index, filename):
    f = open(filename,'r')
    f.seek(4*index)
    return struct.unpack('>I',f.read(4))[0]
	
#binary search. it will return the index of the element.
def binary_search(sizeArray, filename, number):
	while sizeArray[1] > sizeArray[0]:
		middle = (sizeArray[1] + sizeArray[0])/2
		numberAtIndex = getnum(middle, filename)
		
		if numberAtIndex == number:
			return middle
		if numberAtIndex == getnum(sizeArray[1], filename):
			return sizeArray[1]
		
		if (sizeArray[1] - sizeArray[0]) == 1:
			if number > getnum(sizeArray[1], filename):
				return sizeArray[1]
			if numberAtIndex < number:
				return sizeArray[0]
			return sizeArray[0]-1
		
		elif numberAtIndex < number:
			sizeArray[0] = middle
		elif numberAtIndex > number:
			sizeArray[1] = middle
	
	if getnum(sizeArray[0], filename) <= number :
		return sizeArray[0]
	else:
		return -1
			
#find the longest array so that we can find the middle number.
def LongestArray(sizes,m):
	longArray = 0
	for i in range(0,m):
		temp = sizes[i]
		if temp > sizes[longArray]:
			longArray = i
	return longArray
	
			
def main():
	m = int(get_m())
	n = int(get_n())
	k = int(get_k())-1
	
	#create and truncate array to size K
	ArraySize=[]
	SizesofArrays= []
	
	if k <= n-1:
		for i in range(0,m):		
			ArraySize.append([0,k])
			SizesofArrays.append(k+1)
	else:
		for i in range(0,m):		
			ArraySize.append([0,n-1])
			SizesofArrays.append(n)

    #if all the size of arrays is 1 or 0, x == false. Otherwise keep looping.
	x = True
	while (x == True):
		#find largest size array
		indexLongArray = LongestArray(SizesofArrays,m)
		
		# pick middle element of longest array
		middleIndex = (ArraySize[indexLongArray][0] + ArraySize[indexLongArray][1]) / 2
		middNum = getnum(middleIndex, str(indexLongArray+1)+'.dat')
		
		BSearchIndex = []
		sumIndex = 0
		for i in range(0,m):
			if -1 not in ArraySize[i]:
				temp = [ArraySize[i][0], ArraySize[i][1]]
				index = binary_search(ArraySize[i], str(i+1)+'.dat', middNum)
				BSearchIndex.append(index)
				ArraySize[i] = [temp[0], temp[1]]
				if index >= ArraySize[i][0]:
					sumIndex += (index - ArraySize[i][0]) + 1

		if k < sumIndex:
			empty = 0
			for i in range(0,m):
				p = i - empty
				if SizesofArrays[i] == 0:
					empty+=1
				else:
					if BSearchIndex[p] < ArraySize[i][0]:
						ArraySize[i][0] = ArraySize[i][1] = -1
						SizesofArrays[i] = 0
					else:
						ArraySize[i][1] = BSearchIndex[p]
						SizesofArrays[i] = ArraySize[i][1] - ArraySize[i][0] + 1
		else:
			k = k - sumIndex
			empty = 0
			for i in range(0,m):
				p = i - empty
				if SizesofArrays[i] == 0:
					empty+=1
				else:
					if BSearchIndex[p] != -1:
						if BSearchIndex[p]+1 > ArraySize[i][1]:
							ArraySize[i][0] = ArraySize[i][1] = -1
							SizesofArrays[i] = 0
						else:
							ArraySize[i][0] = BSearchIndex[p]+1
							SizesofArrays[i] = ArraySize[i][1] - ArraySize[i][0]+1
		
		x = False
		for i in SizesofArrays:
			if i > 1:
				x = True

	finalArray = []
	for i in range(0,m):
		if SizesofArrays[i] != 0:
			finalArray.append(getnum(ArraySize[i][0], str(i+1)+'.dat'))
	
	finalArray.sort()
	write_to_output(finalArray[k])
		
		
	
			
main()
