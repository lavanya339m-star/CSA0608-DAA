def assembly_line(entry, exit, line1, line2, transfer1, transfer2):
    n = len(line1)

    time1 = entry[0] + line1[0]
    time2 = entry[1] + line2[0]

    for i in range(1, n):
        new_time1 = min(
            time1 + line1[i],
            time2 + transfer2[i - 1] + line1[i]
        )

        new_time2 = min(
            time2 + line2[i],
            time1 + transfer1[i - 1] + line2[i]
        )

        time1 = new_time1
        time2 = new_time2

    return min(time1 + exit[0], time2 + exit[1])


entry = [6, 7]
exit = [5, 4]

line1 = [2, 4, 3]
line2 = [3, 2, 5]

transfer1 = [1, 2]
transfer2 = [2, 1]

result = assembly_line(
    entry, exit, line1, line2, transfer1, transfer2
)

print("Minimum Production Time =", result)
