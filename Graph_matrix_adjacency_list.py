# Array of Edges (Directed) [Start, End]

a = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
n = len(a) - 1
print(a,n)

# Convert Array of Edges -> Adjacency Matrix

m = []
for i in range(n):
    m.append( [0] * n )

print (m)

for u, v in a:
    m[u][v] = 1

  # Uncomment the following line if the graph is undirected
  # M[v][u] = 1


  # Convert Array of Edges -> Adjacency List

from collections import defaultdict
d = defaultdict(list)
for u,v in a:
    d[u].append(v)

  # Uncomment the following line if the graph is undirected
  # D[v].append(u)

# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges

def dfs_recursive(node):
    
    seen = set()
    print(node)

    for nei_node in d[node]:
        if nei_node not in seen:
            seen.add(nei_node)
        dfs_recursive(nei_node)

# Iterative DFS with Stack - O(V + E)

start = 0
seen = set()
seen.add(start)
stack = [start]

while stack:
    node = stack.pop()
    for nei_node in d[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)


# BFS (Queue) - O(V + E)

from collections import deque
start = 0
seen  = set()
q = deque()
q.append(start)

while q:
    for nei_node in d[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)
        


if __name__ == '__main__':
    dfs_recursive(0)

