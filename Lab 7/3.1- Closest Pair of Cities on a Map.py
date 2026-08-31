import math
import random

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def brute_force_closest(points):
    min_dist=float('inf')
    pair=None
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            d=distance(points[i],points[j])
            if d<min_dist:
                min_dist=d
                pair=(points[i],points[j])
    return pair,min_dist

def closest_pair(points):
    n=len(points)
    if n<=3:
        return brute_force_closest(points)

    mid=n//2
    left=points[:mid]
    right=points[mid:]

    pair1,d1=closest_pair(left)
    pair2,d2=closest_pair(right)

    if d1<d2:
        best_pair,best_dist=pair1,d1
    else:
        best_pair,best_dist=pair2,d2

    mid_x=points[mid][0]
    strip=[p for p in points if abs(p[0]-mid_x)<best_dist]
    strip.sort(key=lambda p:p[1])

    for i in range(len(strip)):
        j=i+1
        while j<len(strip) and strip[j][1]-strip[i][1]<best_dist:
            d=distance(strip[i],strip[j])
            if d<best_dist:
                best_dist=d
                best_pair=(strip[i],strip[j])
            j+=1

    return best_pair,best_dist

def closest_pair_of_points(points):
    points=sorted(points,key=lambda p:p[0])
    return closest_pair(points)

pts=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]

pair,d=closest_pair_of_points(pts)
brute_pair,brute_d=brute_force_closest(pts)

assert abs(d-brute_d)<1e-9

random.seed(0)

random_pts=[(random.uniform(0,100),random.uniform(0,100)) for _ in range(50)]

_,d2=closest_pair_of_points(random_pts)
_,brute_d2=brute_force_closest(random_pts)

assert abs(d2-brute_d2)<1e-9

print("All test cases passed!")
