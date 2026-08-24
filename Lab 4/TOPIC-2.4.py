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

    import math
    hull.sort(key=lambda p:math.atan2(p[1]-cy,p[0]-cx))

    return hull

points=[(2,2),(4,1),(6,3),(5,5),(3,6),(1,4)]
hull=convex_hull(points)

print("Convex Hull Points:")
print(", ".join(map(str,hull)))
