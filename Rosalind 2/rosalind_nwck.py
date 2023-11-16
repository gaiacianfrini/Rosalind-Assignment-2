from Bio import Phylo
from io import StringIO

with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_nwck.txt', 'r') as file:
   pairs = [i.strip() for i in file.read().strip().split('\n\n')]

distance = []
for i in pairs:
    start, end = i.split('\n')[1].split()
    trees = Phylo.parse(StringIO(i), "newick")
    
    for j in trees:
        if j.find_any(start) and j.find_any(end):
            path = j.trace(start, end)
            if path and path[0].name == start:
                del path[0]
            distance.append(str(len(path)))

print(' '.join(distance))


    