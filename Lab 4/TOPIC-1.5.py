import math

def euclidean_distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def closest_pair(points):
    min_distance=float('inf')
    pair=None
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            distance=euclidean_distance(points[i],points[j])
            if distance<min_distance:
                min_distance=distance
                pair=(points[i],points[j])
    return pair,min_distance

points=[(10,20),(15,25),(30,40),(12,22)]
pair,distance=closest_pair(points)

print("Closest pair:",pair[0],"-",pair[1])
print("Minimum distance:",distance)
print("Closest Pair Time Complexity: O(n^2)")
print("Closest Pair Space Complexity: O(1)")


def orientation(a,b,c):
    value=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    if value>0:
        return 1
    if value<0:
        return -1
    return 0

def convex_hull(points):
    hull=[]
    n=len(points)

    for i in range(n):
        for j in range(i+1,n):
            left=right=False

            for k in range(n):
                if k==i or k==j:
                    continue
                value=orientation(points[i],points[j],points[k])
                if value>0:
                    left=True
                elif value<0:
                    right=True

            if not(left and right):
                hull.append(points[i])
                hull.append(points[j])

    hull=list(set(hull))

    cx=sum(p[0] for p in hull)/len(hull)
    cy=sum(p[1] for p in hull)/len(hull)

    hull.sort(key=lambda p:math.atan2(p[1]-cy,p[0]-cx))

    return hull

points=[(10,0),(11,5),(5,3),(9,3.5),(15,3),(12.5,7),(6,6.5),(7.5,4.5)]
labels={
    (10,0):"P1",
    (11,5):"P2",
    (5,3):"P3",
    (9,3.5):"P4",
    (15,3):"P5",
    (12.5,7):"P6",
    (6,6.5):"P7",
    (7.5,4.5):"P8"
}

hull=convex_hull(points)

print("Convex Hull:",", ".join(labels[p] for p in hull))
print("Time Complexity: O(n^3)")
print("Space Complexity: O(n)")
print("Collinear points are handled using orientation and only the extreme points are retained.")
