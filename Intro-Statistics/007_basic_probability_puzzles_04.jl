!/usr/bin/env julia

# Task
# B1: contains 4 R, 5 B = 9
# B2: contains 3 R and 7 B = 10

# 1 draw from B1 and 2 from B2
# Find prob. 2 are B and 1 is R

# Cases using NFC
# 1: B B R
# 2: B R B
# 3: R B B

# 1.1: B1B B2B B2R
# 1.2: B2B B1B B2R
# 1.3: B2B B2B B1R

# 2.1: B1B B2R B2B
# 2.2: B2B B1R B2B
# 2.3: B2B B2R B1B

# 3.1: B1R B2B B2B
# 3.2: B2R B1B B2B
# 3.3: B2R B2B B1B

# Case 1
p11 = 5//9 * 7//10 * 3//9
p12 = 7//10 * 5//9 * 3//9
p13 = 7//10 * 6//9 * 4//9
p1 = (p11 + p12 + p13) //3 

# Case 2
p21 = 5//9 * 3//10 
p22 =
p23 =
