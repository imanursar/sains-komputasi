output = []

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        output.append(start)
    visited.add(start)
    for next in sorted(graph[start] - visited):
        if (next not in output):
            output.append(next)
        dfs(graph, next, visited)
    return output

# def dfs_paths(graph, start, goal, path=None):
#     if path is None:
#         path = [start]
#     if start == goal:
#         yield path
#     for next in graph[start] - set(path):
#         yield from dfs_paths(graph, next, goal, path + [next])

# graph = {'A': set(['B', 'C']),
#          'B': set(['D', 'E']),
#          'C': set(['A', 'E']),
#          'D': set(['B', 'E']),
#          'E': set(['B', 'C', 'D', 'F']),
#          'F': set(['D', 'E'])}

# graph = {'A': set(['B', 'C']),
#          'B': set(['D']),
#          'C': set(['D']),
#          'D': set([])}

graph = {'A': set(['B', 'D', 'E']),
         'B': set(['C', 'F']),
         'C': set([]),
         'D': set(['G']),
         'E': set(['G']),
         'F': set([]),
         'G': set(['H']),
         'H': set(['I']),
         'I': set([])}

output = dfs(graph, 'A')
print(output)
# print(list(dfs_paths(graph, 'A', 'I'))) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
