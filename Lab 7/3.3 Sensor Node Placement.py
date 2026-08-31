import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(points):
    if len(points) <= 3:
        min_dist = float('inf')
        pair = None

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    pair = (points[i], points[j])

        return min_dist, pair

    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]

    dl, pair_l = closest_pair(left)
    dr, pair_r = closest_pair(right)

    if dl < dr:
        min_dist = dl
        pair = pair_l
    else:
        min_dist = dr
        pair = pair_r

    mid_x = points[mid][0]
    strip = [p for p in points if abs(p[0] - mid_x) < min_dist]

    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break

            d = distance(strip[i], strip[j])

            if d < min_dist:
                min_dist = d
                pair = (strip[i], strip[j])

    return min_dist, pair


def check_minimum_spacing(nodes, min_safe_distance):
    points = sorted(nodes, key=lambda p: p[0])

    min_dist, pair = closest_pair(points)

    ok = min_dist >= min_safe_distance

    return ok, pair, min_dist


nodes = [(0, 0), (10, 10), (10.5, 10.2), (30, 40), (31, 41)]

ok, pair, min_dist = check_minimum_spacing(
    nodes,
    min_safe_distance=1.0
)

assert ok == False

spaced_nodes = [(0, 0), (10, 10), (20, 20), (30, 30)]

ok2, _, _ = check_minimum_spacing(
    spaced_nodes,
    min_safe_distance=1.0
)

assert ok2 == True

print("Minimum distance:", min_dist)
print("Closest pair:", pair)
print("Spacing requirement satisfied:", ok)
print("All test cases passed!")
