from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
"""
traversal_path = []

2nd route
visited =  {}
reverse_path = [] 
o = {"n" : "s", "e": "w", "s":"n", "w": "e" } 

visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) > len(room_graph):
    if player.current_room.id not in visited: 
        visited[player.current_room.id] = player.current_room.get_exits()
        prev = revers_path[-1]
        visited[player.currrent_room.id].remove(prev)
    if len(visited[player.current_room.id]) == 0: 
        prev = reverse_path[-1]
        reverse_path.pop()
        traversal_path.append(prev)
        player.travel(prev)
    else:
        d = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop()
        traversal_path.append(d) 
        reverse_path.append(o[d])
        player.travel(d)

"""
o = { 'n': 's', 's': 'n', 'e': 'w','w': 'e'}

class Path_Taken:

    def rt(self, room, visited=None):

        if visited is None:
            visited = set()
        taken_path = []
        visited.add(room.id)
        for room_exit in room.get_exits():
            next_room = room.get_room_in_direction(room_exit)
            if next_room.id not in visited:
                unvisited = self.rt(next_room, visited)
                if unvisited:
                    current = [room_exit] + \
                                   unvisited + \
                                   [o[room_exit]]
                else:
                    current = [
                        room_exit, 
                        o[room_exit]
                        ]
                taken_path = taken_path + \
                             current
        return taken_path

traversal_path = Path_Taken().rt(player.current_room)

"""
My Plan:
We need to set up a director for the player.
Then loop through all the exits, after that
set it up so that if the player has already visited a room 
to turn around. If the player has not been to this room, 
Then add the new path and update the status to the new one
using recursion. Then return that path and 
fill in the traversal path with the bfs function
"""




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


        