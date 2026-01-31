from collections import deque
def bfs(n,adj,starting_Node):
    visited=[0]*(n+1)
    ans=[]
    queue=deque()
    queue.append(starting_Node)
    visited[starting_Node]=1
    while len(queue)!=0:
        e=queue.pop()
        ans.append(e)
        for node in adj[e]:
            if visited[node]==0:
                queue.append(node)
                visited[node]=1
    return ans

def dfs(node, adj, visited, result):
    visited[node] = 1
    result.append(node)
    for n in adj[node]:
        if visited[n] == 0:
            dfs(n, adj, visited, result)

adj = [[], [2,4], [3,1], [2,4,5], [1,3,5], [4,3]]
n = 5
visited = [0] * (n + 1)
result = []

dfs(2, adj, visited, result)
print(result)
print(bfs(n,adj,2))
