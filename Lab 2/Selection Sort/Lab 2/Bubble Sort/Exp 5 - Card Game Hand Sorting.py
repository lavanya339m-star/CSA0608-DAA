import random
def bubble_sort_hand(hand):
    hand = hand.copy()
    n = len(hand)
    passes = 0
    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(n - i - 1):
            if hand[j] > hand[j + 1]:
                hand[j], hand[j + 1] = hand[j + 1], hand[j]
                swapped = True
        if not swapped:
            break
    return hand, passes
hand = [2, 4, 6, 8, 9, 11, 13]
hand.append(7)
final_hand, passes_incremental = bubble_sort_hand(hand)
assert final_hand == sorted(hand)
shuffled = hand.copy()
random.shuffle(shuffled)
_, passes_full = bubble_sort_hand(shuffled)
assert passes_incremental <= passes_full
print("Original hand after adding new card:", hand)
print("Sorted hand:", final_hand)
print("Passes for nearly sorted hand:", passes_incremental)
print("Passes for shuffled hand:", passes_full)
print("All test cases passed!")
