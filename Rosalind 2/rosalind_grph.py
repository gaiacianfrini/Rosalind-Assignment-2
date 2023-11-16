from Bio import SeqIO
from Bio.Seq import Seq
import itertools

fasta_list=[]
#for records in SeqIO.parse(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_grph.txt", "fasta"):
    #fasta_list.append(records.seq)
    
sequences_records = list(SeqIO.parse(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_grph.txt", "fasta"))
dna = {record.id: str(record.seq) for record in sequences_records}    
#print(dna)


def overlap_seq(s1,s2,k):
    return s1[-k:] == s2[:k]


def create_adjacency_list(dna, k=3):
    adjacency_list = {}
    for id1, s1 in dna.items():
        for id2, s2 in dna.items():
            if id1 != id2 and overlap_seq(s1, s2, k):
                    # Add an edge in the adjacency list
                    if id1 not in adjacency_list:
                        adjacency_list[id1] = []
                    adjacency_list[id1].append(id2)

    return adjacency_list

adjacency_list = create_adjacency_list(dna, k=3)
for node, neighbors in adjacency_list.items():
    for neighbor in neighbors:
        print(f"{node} {neighbor}")

   

    