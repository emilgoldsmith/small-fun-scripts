dice_1, dice_2 = map(int, input('Input die such as 3 5: ').split(' '))

def get_ev(dice_1, dice_2, should_print = False):
    min_dice = min(dice_1, dice_2)
    max_dice = max(dice_1, dice_2)

    total_possibilities = 36
    losing_twice_possibilities = (min_dice - 1) * (min_dice - 1) + 2 * (min_dice - 1) * (max_dice - min_dice)
    winning_twice_possibilities = (6 - max_dice + 1) * (6 - max_dice + 1) + 2 * (6 - max_dice + 1) * (max_dice - min_dice)
    tie_possibilities = total_possibilities - (losing_twice_possibilities + winning_twice_possibilities)

    expected_value = float(losing_twice_possibilities * (-2) + winning_twice_possibilities * 2) / 36.0

    one_dice_winning_possibilities = 6 - max_dice + 1
    one_dice_losing_possibilities = 6 - one_dice_winning_possibilities
    one_dice_ev = float(one_dice_winning_possibilities - one_dice_losing_possibilities) / 6.0

    if should_print:
        print('Winning:', winning_twice_possibilities)
        print('Losing:', losing_twice_possibilities)
        print('Tie', tie_possibilities)
        print('Expected value:', expected_value)
        print()
        print('One dice expected value:', one_dice_ev)

    return max(expected_value, one_dice_ev)

get_ev(dice_1, dice_2, should_print=True)

ev_of_3_vs_2 = 0
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            all_dice = [a, b, c]
            sorted_dice = list(reversed(sorted(all_dice)))
            ev_of_3_vs_2 += get_ev(sorted_dice[0], sorted_dice[1])

print('Total EV:', ev_of_3_vs_2)
