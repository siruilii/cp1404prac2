import random
QUICK_PICKS = 5
MIN_NUM = 1
MAX_NUM = 45
NUMBER_PICK = 6

for _ in range(QUICK_PICKS):
    quick_pick = []
    while len(quick_pick) < NUMBER_PICK:
        new_num = random.randint(MIN_NUM, MAX_NUM)
        if new_num not in quick_pick:
            quick_pick.append(new_num)

    sorted_quick_pick = sorted(quick_pick)
    print(" ".join(f"{num:2}" for num in sorted_quick_pick))