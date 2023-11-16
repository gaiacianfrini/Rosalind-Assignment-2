from Bio import Phylo
from io import StringIO

with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_nkew.txt', 'r') as file:
   pairs = [i.strip() for i in file.read().strip().split('\n\n')]
   
   distance = []
for i in pairs:
    start, end = i.split('\n')[1].split()
    weight = Phylo.parse(StringIO(i), "newick")
    print(weight)