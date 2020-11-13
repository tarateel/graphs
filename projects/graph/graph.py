"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        print('GRAPH')

    def add_vertex(self, vertex_id):
        # Add a vertex to the graph.
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # Check for vertices; if there, add a directed edge to the graph.
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        # If not, raise an error
        else:
            raise IndexError('nonexistent vertex')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Print each vertex in breadth-first order beginning from starting_vertex.
        print('bft')
        q = Queue()
        # make a set to track visited
        visited = set()
        # enqueue the start node
        q.enqueue(starting_vertex)
        # while our queue isn't empty
        while q.size() > 0:
            # dequeue from front of line, this is our current node
            current_vertex = q.dequeue()
            # check if we've visited here yet
            if current_vertex not in visited:
                # if not, print and add to visited
                print(current_vertex)
                visited.add(current_vertex)
                # get its neighbors, for each, add to queue
                for neighbor in self.get_neighbors(current_vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex.
        print('dft')
        # make a stack
        s = Stack()
        # make a set to track visited
        visited = set()
        # put the start node into the stack
        s.push(starting_vertex)
        # while the stack isn't empty
        while s.size() > 0:
            # pop off the top of the stack, this is our current node
            current_vertex = s.pop()
            # check if we have visited this node yet
            if current_vertex not in visited:
                # if not, print and add it to our visited set
                print(current_vertex)
                visited.add(current_vertex)
                # and add each of its neighbors to our stack
                for neighbor in self.get_neighbors(current_vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None, s = Stack()):
        # Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion.
        # check for visited, if not there, then
        if visited is None:
            # create set
            visited = set()
            print('dft_recursive')
        # print starting_vertex
        print(starting_vertex)
        # Check for starting_vertex in set
        if starting_vertex not in visited:
            # if not there, add it
            visited.add(starting_vertex)
        # get neighbors and check each to see if already visited
        for neighbor in self.get_neighbors(starting_vertex):
            # if not there,
            if neighbor not in visited:
                # call dft_recursive
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.
        # create empty queue
        print('bfs')
        q = Queue()
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
