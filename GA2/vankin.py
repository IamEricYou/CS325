# CS325 - Group Assignment #2 (GA2) 
# Author: Francisco Bolanos, Jaehyung You
# Date : Tue, October 24, 2017
# Filename : vankin.py

import time
#get n to get the size of the matrix
def get_n():
    with open('input.txt') as f:
        number = f.readlines()[0]
    return number

#Fill the matrix with the numbers from the input.txt
def get_value(temp_list,n):
    with open('input.txt') as f:
        next(f)
        x = 0
        for line in f:
            for y in range (0,n):
                temp_list[x][y] = int(line.split(',')[y])
            x = x+1

#write the output value into the output.txt 
def write_to_output(number):
	with open('output.txt', 'w') as f:
		f.write(str(number))

#return higher value
def find_max(x,y):
	if(x >= y):
		return x
	else:
		return y


#main algorithm function. 
def VM(Array,n): 
	MaxScore=0
	num = n-1
	for y in range(num,-1,-1):
		for x in range(num,-1,-1):
			if x+1 == n:
				if y+1 == n:
					Array[x][y] = Array[x][y]
				else:
					Array[x][y] = Array[x][y] + find_max(0,Array[x][y+1])
			elif y+1 == n:
				Array[x][y] = Array[x][y] + find_max(Array[x+1][y],0)
			else:
				Array[x][y] = Array[x][y] + find_max(Array[x+1][y],Array[x][y+1])
			MaxScore = find_max(MaxScore, Array[x][y])
	return MaxScore

def main():
    #n = 1000 is WORKING!
	n = get_n() #please use int(n) when pass this n as a parameter
	temp_list = [[0 for x in range(int(n))] for y in range(int(n))]
	get_value(temp_list,int(n))
	write_to_output(VM(temp_list,int(n))) #since the matrix has been changed, VM functions won't print output same after this call.
	#print VM(temp_list,int(n))

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
