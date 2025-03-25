from hog import *
dice = make_test_dice(4, 2, 5, 1)
averaged_dice = make_averaged(roll_dice, 40)
averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's