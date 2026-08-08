def distribute_prizes(participants):
    participants = participants.copy()
    ranking = []
    n = len(participants)

    for i in range(n):
        max_index = i

        # Find the participant with the highest score
        for j in range(i + 1, n):
            if participants[j][1] > participants[max_index][1]:
                max_index = j

        # Swap the highest scorer into the current position
        participants[i], participants[max_index] = participants[max_index], participants[i]

        # Add the ranked participant to the output
        ranking.append(participants[i])
        print("Rank", i + 1, ":", participants[i][0])

    return ranking


# Test Case
ranking = distribute_prizes([
    ('Asha', 88),
    ('Ravi', 95),
    ('Meera', 79),
    ('Dev', 95)
])

scores_only = [p[1] for p in ranking]

assert scores_only == sorted(scores_only, reverse=True)
assert ranking[0][1] == 95

print("All test cases passed!")
