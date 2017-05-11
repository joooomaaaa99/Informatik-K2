

liste = [3,2,9,6,235235,235,357135,568,23562,246,5468,246,2635782,2356246,458,1222,4,5,7,83,233,7,34]

def quicksort(liste):
	k = []
	g = []
	if len(liste) > 0:
		pivot = liste[0]
		for j in range(1, len(liste)):
			element = liste[j]
			if element >= pivot:
				g.append(element)
			else:
				k.append(element)
		ksortiert = quicksort(k)
		gsortiert = quicksort(g)
		lsortiert = ksortiert + [pivot] + gsortiert
	else:
		lsortiert = liste
	return(lsortiert)

def insertionsort(liste):
	sorted = []
	sorted.append(liste[0])
	unsorted = liste
	del unsorted[0]
	while len(unsorted)>0:
		element = unsorted[0]
		del unsorted[0]
		for j in range(0, len(sorted)):
			vgl = sorted[j]
			if element <= vgl:
				sorted.insert(j, element)
				break
			elif j == len(sorted)-1:
				sorted.append(element)
	return(sorted)

print(insertionsort(liste))
