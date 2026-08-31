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


entry = [10, 12]
exit = [18, 7]

line1 = [4, 5, 3, 2]
line2 = [2, 10, 1, 4]

transfer1 = [7, 4, 5]
transfer2 = [9, 2, 8]

result = assembly_line(
    entry,
    exit,
    line1,
    line2,
    transfer1,
    transfer2
)

print("Minimum Production Time =", result)
