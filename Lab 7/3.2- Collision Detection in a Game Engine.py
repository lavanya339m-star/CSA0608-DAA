import math

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def brute_force(points):
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
        return brute_force(points)

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

def detect_potential_collision(sprites,threshold):
    if len(sprites)<2:
        return None,float('inf')

    points=sorted(sprites,key=lambda p:p[0])
    pair,min_dist=closest_pair(points)

    if min_dist<=threshold:
        return pair,min_dist

    return None,min_dist

sprites=[(0,0),(1,1),(50,50),(100,100),(1.2,0.9)]

pair,min_dist=detect_potential_collision(sprites,threshold=2.0)

assert pair is not None and min_dist<=2.0

far_sprites=[(0,0),(100,100),(200,200)]

pair2,min_dist2=detect_potential_collision(far_sprites,threshold=1.0)

assert pair2 is None

print("All test cases passed!")
