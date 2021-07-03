'''
while condtion
    block of code executed till condition is true
    condition modifier
'''

# add numbers from 1 to 10
count = 0
total = 0
while count < 10:
    count = count + 1
    if count == 5:
        continue # Skipping an ietration
    total = total + count
    '''
    if count == 5:
        print("Breaking loop here")
        break
    '''
    print("Counter " , count)

print("Total", total)