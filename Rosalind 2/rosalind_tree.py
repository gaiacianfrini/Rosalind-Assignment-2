
with open(r'C:\Users\ACER\OneDrive\Desktop\VISUAL STUDIO\Rosalind 2\rosalind_tree.txt', 'r') as file:
    n = int(file.readline().strip())
    edges = []
    for line in file:
            raw_edge = line.split(' ')
            edge = [node.strip() for node in raw_edge]
            edges.append(edge)

def min_edges_to_make_tree(n, adjacency_list):
    num_edges = sum(len(neighbors) for neighbors in adjacency_list) // 2
    min_edges_needed = n - 1 - num_edges

    return min_edges_needed
result = min_edges_to_make_tree(n, edges)

print(result)
