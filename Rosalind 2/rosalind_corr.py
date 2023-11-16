from Bio import SeqIO

dataset = []
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_corr.txt', 'r') as file:
    for record in SeqIO.parse(file,'fasta'):
        dataset.append(str(record.seq))
    
def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def error_corrections(reads):
    mutation = []
    original = []
    corrections = []
    reverse={"A": "T", "T": "A", "C": "G", "G": "C"}
    for i in reads:
        rev = "".join([reverse[j] for j in i[::-1]])
        if reads.count(i) + reads.count(rev) >= 2:
            original.append(i)
        else:
            mutation.append(i)

    for wrong in mutation:
        for right in original:
            revc = "".join([reverse[j] for j in right[::-1]])
            if hamming_distance(wrong, right) == 1:
                corrections.append((wrong, right))
                break
            if hamming_distance(wrong, revc) == 1:
                corrections.append((wrong, revc))
                break

    return corrections


corrections = error_corrections(dataset)
for wrong, right in corrections:
    print("{}->{}".format(wrong, right))
        
        
