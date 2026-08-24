import math

def closest_pair(points):
    min_distance=float('inf')
    closest=None

    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x1,y1=points[i]
            x2,y2=points[j]
            distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

            if distance<min_distance:
                min_distance=distance
                closest=(points[i],points[j])

    return closest,min_distance

points=[(1,2),(4,5),(7,8),(3,1)]

pair,distance=closest_pair(points)

print("Closest pair:",pair[0],"-",pair[1])
print("Minimum distance:",distance)
