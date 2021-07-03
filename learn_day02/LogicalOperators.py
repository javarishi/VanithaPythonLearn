# combines multiple logical expression
# Logical = generates boolean results

S1 = True
S2 = False
S3 = True
'''
Truth Table
and --> result = S1 and S2 and S3
S1  S2  S1 and S2
T   T   T
T   F   F
F   T   F
F   F   F
'''
print("True and False" , S1 and S2)
print("True and True" , S1 and S3)
'''
Truth Table
or --> result = S1 or S2 or S3
S1  S2  S1 or S2
T   T   T
T   F   T
F   T   T
F   F   F
'''
print("True or False" , S1 or S2)
print("True or True" , S1 or S3)

# Negation - not statement

print(not True)
print(not False)