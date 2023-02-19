# trying tree traverse codes here (BFS/DFS)



def DFS_recursive(visited, graph, curr):
    if curr not in visited:
        print(curr)
        visited.add(curr)
        for neigh in graph[curr]:
            DFS_recursive(visited, graph, neigh)
        
  




#### using chat gpt, to implement bfs abd dfs with iteration, being very similar
def DFS_iterative(graph, start):
    visited = set([start])
    stack = [start]
    
    while stack:
        curr = stack.pop()
        print(curr, "  ", stack)
        for neigh in graph[curr]:
            if neigh not in visited:
                visited.add(neigh)
                stack.append(neigh)



def BFS_iterative(graph, start):
    visited = set([start])
    queue = [start]
    
    while queue:
        curr = queue.pop(0)
        print(curr, "  ", queue)
        for neigh in graph[curr]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)







graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
# visited = set()
# DFS(visited, graph, '5')

BFS_iterative(graph, '5')
print("****************************************")
DFS_iterative(graph, '5')