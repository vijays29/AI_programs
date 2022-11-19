from collections import deque
class Graph:
    def __init__(self, directed):
        self.edges={}
        self.directed = directed
    
    def add_edge(self, node1, node2,_reversed=False):
        try:
            self.edges[node1].add(node2)
        except KeyError:
            self.edges[node1] = set()
            self.edges[node1].add(node2)
        if not self.directed and not _reversed:
            self.add_edge(node2,node1,True)
    
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0],edge[1])

    def neighbours(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []
        
    @staticmethod
    def traceback_path(goal, predecessor):
        current,path = goal,deque()
        while True:
            path.appendleft(current)
            current = predecessor[current]
            if current is None: break
        return path
    
    def bfs(self, start, goal):
        fringe = deque(start)
        visited = {start}
        predecessor = {start: None}
        current = '-'
        print(f"{'Current Node':15} | {'Fringe'}")
        while fringe:
            print(f"{current:15} |", *fringe)
            current = fringe.pop()
            if current == goal:
                path =  Graph.traceback_path(goal,predecessor)
                print(f"Path: {' => '.join(path)}") 
                return path
            for x in self.neighbours(current):
                if x not in visited:
                    fringe.appendleft(x)
                    visited.add(x)
                    predecessor[x] = current

if __name__ == "__main__":
    g = Graph(directed = False)
    g.add_edges([
        ("A","B"),("A","S"),("S","G"),("S","C"),("C","F"),
        ("G","F"),("C","D"),("C","E"),("E","H"),("G","H")
    ])
    start,goal = "A","H"
    g.bfs(start,goal) or print("No paths Found!")
