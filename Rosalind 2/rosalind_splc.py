from Bio import SeqIO
from Bio.Seq import Seq

fasta_list=[]
for records in SeqIO.parse(r"C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_splc.txt", "fasta"):
    fasta_list.append(records.seq)
    dna = fasta_list[0]
    introns = fasta_list[1:]
    

def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    
    return dna 

def transcribe_and_translate(dna):
    # Transcribe the DNA sequence into mRNA
    mrna_sequence = dna.transcribe()
    
    # Translate the mRNA sequence into a protein
    protein_sequence = mrna_sequence.translate()

    return protein_sequence
   
dna_sequence = remove_introns(dna, introns)  
protein_sequence = transcribe_and_translate(dna_sequence)     

print(protein_sequence)