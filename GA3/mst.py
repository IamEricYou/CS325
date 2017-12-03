# CS325 - Group Assignment #3 (GA3) 
# Author: Francisco Bolanos, Jaehyung You, Jesus Ortiz
# Date : Tue, November 14, 2017
# Filename : mst.py

import copy
import heapq

def nth_smallest(list,nth_number):
 return (heapq.nsmallest(nth_number, list) or (None,))[-1]

# get number of vertices 
def get_n():
  with open('input.txt') as f:
      number = f.readlines()[0]
  return number

# get number all edges
def get_value(temp_list,n):
  with open('input.txt') as f:
      next(f)
      x = 0
      for line in f:
          for y in range (0,n):
              temp_list[x][y] = int(line.split(',')[y])
          x = x+1

def write_to_output(number):
	with open('output.txt', 'w') as f:
		f.write(str(number[0]) + '\n')
		f.write(str(number[1]) + '\n')
		f.write(str(number[2]))

#refrence 1	  
def merge(a,b):
	merged = [[0 for x in range(0)] for y in range(3)]
	while len(a[1]) !=0 and len(b[1]) !=0:
		if a[1][0] < b[1][0]:
			merged[0].append(a[0][0])
			merged[1].append(a[1][0])
			merged[2].append(a[2][0])
	
			del a[0][0]
			del a[1][0]
			del a[2][0]
		else:
			merged[0].append(b[0][0])
			merged[1].append(b[1][0])
			merged[2].append(b[2][0])
	
			del b[0][0]
			del b[1][0]
			del b[2][0]
	if len(a[1]) == 0:
		merged[0] += b[0]
		merged[1] += b[1]
		merged[2] += b[2]
	else:
		merged[0] += a[0]
		merged[1] += a[1]
		merged[2] += a[2]
	return merged
		
#refrence 1
def mergesort(list):
	if len(list[1]) <= 1:
		return list
	else:
		mid = len(list[1])/2
		L1 = list[0][:mid]
		L2 = list[1][:mid]
 		L3 = list[2][:mid]
		L = [L1,L2,L3]
		if L is None:
			L = [[],[],[]]
		
		R1 = list[0][mid:]
		R2 = list[1][mid:]
 		R3 = list[2][mid:]
		R = [R1,R2,R3]
		if R is None:
			R = [[],[],[]]

		a = mergesort(L)
		b = mergesort(R)
		return merge(a,b)

def min_spanning_tree_test(vert_list_temp, ver, subgrp_temp):
	total = [0 for x in range(3)]
	min_span = []
	min_span2 = [[0 for x in range(0)] for y in range(ver-1)]
	totals = []
	F = 0
	E = 0
	
	if ver < 4:
		total[0] = nth_smallest(vert_list_temp[1],1) + nth_smallest(vert_list_temp[1],2)
		total[1] = nth_smallest(vert_list_temp[1],1) + nth_smallest(vert_list_temp[1],3)
		total[2] = nth_smallest(vert_list_temp[1],2) + nth_smallest(vert_list_temp[1],3)
		return total
		
	while (F < ver-1):
		vertices = vert_list_temp[0][E].split('-')
		ver1 = int(vertices[0])
		ver2 = int(vertices[1])
		if subgrp_temp[ver1] != subgrp_temp[ver2]:
			subgrpchange = subgrp_temp[ver1]
			for vs in range(0,ver):
				if subgrp_temp[vs] == subgrpchange:
					subgrp_temp[vs] = subgrp_temp[ver2]
			total[0] +=vert_list_temp[1][E]
			F+= 1
			min_span.append(E)
		E+=1

	for v in range(0,ver-1):
		F = 0
		E = 0
		temp_total = 0
		for i in range(0,ver):
			subgrp_temp[i] = i
		
		while (F < ver-1):
			vertices = vert_list_temp[0][E].split('-')
			ver1 = int(vertices[0])
			ver2 = int(vertices[1])
			if subgrp_temp[ver1] != subgrp_temp[ver2] and E != min_span[v]:
				subgrpchange = subgrp_temp[ver1]
				for vs in range(0,ver):
					if subgrp_temp[vs] == subgrpchange:
						subgrp_temp[vs] = subgrp_temp[ver2]
				temp_total+= vert_list_temp[1][E]
				F+= 1
				if E not in min_span:
					min_span2[v].append(E)
			E+=1
		totals.append(temp_total)
	total[1] = min(totals)
	index = totals.index(total[1])
	del totals[index]
	
	F = 0
	E = 0
	temp_total = 0
	for i in range(0,ver):
			subgrp_temp[i] = i
	while (F < ver-1):
		vertices = vert_list_temp[0][E].split('-')
		ver1 = int(vertices[0])
		ver2 = int(vertices[1])
		if subgrp_temp[ver1] != subgrp_temp[ver2] and E != min_span[index] and E!= min_span2[index][0]:
			subgrpchange = subgrp_temp[ver1]
			for vs in range(0,ver):
				if subgrp_temp[vs] == subgrpchange:
					subgrp_temp[vs] = subgrp_temp[ver2]
			temp_total+= vert_list_temp[1][E]
			F+= 1
		E+=1
	totals.append(temp_total)
	total[2] = min(totals)
	return total

def main():
	n = get_n()
	temp = [[0 for x in range(int(n))] for y in range(int(n))]
	get_value(temp,int(n))
	vertices_list = [[0 for x in range(0)] for y in range(3)]
	subgroups = []
    
	for i in range(0,int(n)):
		subgroups.append(i)
		for j in range(0,i):
			vertices_list[1].append(temp[j][i])
			vertices_list[2].append('n')
	
	for i in range(0,((int(n)*(int(n)-1))/2)):
		for j in range(0,i):
			if i != j:
				vertices_list[0].append(str(j)+'-'+str(i))
				
	write_to_output(min_spanning_tree_test(mergesort(vertices_list), int(n), subgroups))

main()

