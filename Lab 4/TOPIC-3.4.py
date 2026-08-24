import itertools
import math

def distance(a,b):
    return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)

def tsp(cities):
    start=cities[0]
    shortest_distance=float('inf')
    shortest_path=None
    for perm in itertools.permutations(cities[1:]):
        path=[start]+list(perm)+[start]
        total=0
        for i in range(len(path)-1):
            total+=distance(path[i],path[i+1])
        if total<shortest_distance:
            shortest_distance=total
            shortest_path=path
    return shortest_distance,shortest_path

test_cases=[
    [(1,2),(4,5),(7,1),(3,6)],
    [(2,4),(8,1),(1,7),(6,3),(5,9)]
]

for i,cities in enumerate(test_cases,1):
    shortest_distance,shortest_path=tsp(cities)
    print("Test Case",i,":")
    print("Shortest Distance:",shortest_distance)
    print("Shortest Path:",shortest_path)
    print()
