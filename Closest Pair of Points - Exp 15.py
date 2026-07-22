import math

points = [(1, 2), (4, 5), (7, 8), (3, 1)]

min_distance = float('inf')
closest_pair = ()

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if distance < min_distance:
            min_distance = distance
            closest_pair = (points[i], points[j])

print("Closest Pair:", closest_pair)
print("Distance:", min_distance)
