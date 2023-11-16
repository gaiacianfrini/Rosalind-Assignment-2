
def count_internal_nodes(n):
    if n < 3 or n > 10000:
        raise ValueError
    else:
        return n - 2
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_inod.txt', 'r') as file:
    n = int(file.readline())
result = count_internal_nodes(n)
print(result)
