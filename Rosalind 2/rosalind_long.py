from Bio import SeqIO

with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_long.txt', 'r') as file:
    dna_strings = []
    
    for record  in SeqIO.parse(file,'fasta'):
            dna_strings.append(str(record.seq))
            length = len(str(record.seq))


def find_shortest_superstring(dna_strings):  # Seq[String] => Map[String, String]
    for i in range(len(dna_strings)):
        for s1 in dna_strings:
            for s2 in dna_strings:
              if s1 != s2:
                for j in range(len(s1)):
                    if s1[:j] == s2[-j:] and j >= int(length//2)-1:
                        dna_strings.append(s2+s1[j:])
                        if s1 in dna_strings:
                            dna_strings.remove(s1)
                        if s2 in dna_strings:
                            dna_strings.remove(s2)
#print(dna_strings)
 
  
result = ''.join(find_shortest_superstring(dna_strings))
print(result)
                
    
