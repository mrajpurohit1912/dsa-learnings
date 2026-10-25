from collections import defaultdict,deque

class Graph:
    def __init__(self) -> None:
        self.adj = defaultdict(list)

    def add_edge(self,u,v,directed=False)->None:
        self.adj[u].append(v) 

        if not directed:
            self.adj[v].append(u)
    def bfs(self, start):
            """Breadth-First Search: explores neighbor by neighbor."""
            visited = {start}
            queue = deque([start])
            traversal = []

            while queue:
                node = queue.popleft()
                traversal.append(node)

                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return traversal
    def dfs(self, start):
            """Depth-First Search: explores as deep as possible along each branch."""
            visited = set()
            traversal = []

            def _dfs(node):
                visited.add(node)
                traversal.append(node)
                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        _dfs(neighbor)

            _dfs(start)
            return traversal

if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    print(g.bfs("A"))
    print(g.dfs("A"))
