from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# create set of unvisited rooms
not_visited = set()

def bft(player):
    q = Queue()
    # make a set to track visited
    visited = set()
    # enqueue starting room and direction
    q.enqueue([('s', player.current_room.id)])

    # while queue is not empty
    while q.size() > 0:
        # dequeue from front (this is current room)
        current_path = q.dequeue()
        # last room from path
        current_room = current_path[-1]

        if player.current_room not in visited:
            visited.add(player.current_room.id)

        # iterate (use get_exits from room.py)
        for direction in world.rooms[current_room[1]].get_exits():
            # check if adjoining room is in not_visited
            if world.rooms[current_room[1]].get_room_in_direction(direction) not in not_visited:
                # if not, add to current path
                current_path.append(
                    (direction, world.rooms[current_room[1]].get_room_in_direction(direction).id))
                return current_path
            # check if adjoining room has been visited and if not:
            if world.rooms[current_room[1]].get_room_in_direction(direction).id not in visited:
                # add to current_path
                new_room = world.rooms[current_room[1]].get_room_in_direction(direction)
                new_path = current_path.copy()
                # add to visited
                new_path.append((direction, new_room.id))
                visited.add(new_room.id)
                q.enqueue(new_path)

def move(current_path):
    # iterate through current_path
    for i in range(1, len(current_path)):
        # add directions
        direction = current_path[i][0]
        # add directions to traversal_path
        player.travel(direction)
        # add to traversal_path
        traversal_path.append(direction)
    # add room to not_visited
    not_visited.add(player.current_room)

while(len(not_visited) != len(room_graph)):
    move(bft(player))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
        
