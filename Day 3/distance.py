WIRE_1 = 1
WIRE_2 = 2

grid = [[ 0 for i in range(1, 100)] for j in range(1, 100)]

def trace_wire_path(route):
    north_south = 0
    east_west = 0
    for span in route.split(','):
        if span[0] == U:
            #traverse up
            #grid[north_south][east_west]
            for i in range(int())