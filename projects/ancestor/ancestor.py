# initialize Queue
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_vertex):
    # create dict parents
    parents = {}
    # relationship = edge
    for relationship in ancestors:
        # parent: child
        parent = relationship[0]
        child = relationship[1]
        if child not in parents:
            parents[child] = set()
        parents[child].add(parent)

    earliest_ancestor = -1
    # bfs
    # create empty queue
    q = Queue()
    # enqueue the PATH TO the starting vertex
    q.enqueue(starting_vertex)
    while q.size() > 0:
        current_vertex = q.dequeue()
        if current_vertex in parents:
            earliest_ancestor = None
            for parent in parents[current_vertex]:
                if (earliest_ancestor is None) or (parent < earliest_ancestor):
                    earliest_ancestor = parent
                q.enqueue(parent)
            if earliest_ancestor is not None:
                earliest_ancestor = earliest_ancestor

    return earliest_ancestor

'''
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.
'''
