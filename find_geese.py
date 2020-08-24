#!/usr/bin/env python2
from itertools import permutations
import csv
import time

# tests all integers up to this integer
test_until = 10000

def nPk(n, k):
    numerator = 1.0

    for i in range(1,n+1):
        numerator *= i

    denominator = 1.0
    for i in range(1, n-k+1):
        denominator *= i
    
    return int(numerator/denominator)


def generate_combos_all(digits): # alternative way of getting combos

    groups = 0 # Start with 0 groups and increment

    group_sizes = []
    arrangements = []

    arrangements.append(list(int(d) for d in num_str))

    number_of_digits = len(digits)

    while groups*2 <= number_of_digits:
        group_sizes.clear()

        for f in range(groups):
            group_sizes.append([])

        
        groups += 1

    return arrangements


def partitions(s):
    if s:
        for i in range(1, len(s) + 1):
            for p in partitions(s[i:]):
                yield [s[:i]] + p
    else:
        yield []
        
        
# takes a list of lists of number combinations, multiplies them, checks for a match and prints match
def mult_combos(number, combos):
    global numbers_found_list
    global numbers_found_dict

    l = len(combos)

    good_arrangements = set() # set of frozensets
    already_found = False

    for arrangement in combos:
        already_found = False
        
        product = 1
        for num in arrangement:
            product *= num

        l_dict = {}
        for num in arrangement:
            if num in l_dict:
                l_dict[num] += 1
            else:
                l_dict[num] = 1

        immutable = frozenset(l_dict.items())

        already_found = immutable in good_arrangements

        if product == number and not already_found:
            numbers_found_list.append(number)

            if number in numbers_found_dict:
                numbers_found_dict[number] += 1
            else:
                numbers_found_dict[number] = 1

            good_arrangements.add(immutable)

            print "\n"*0
            print str(number)," satisfies the condition!!!!" 
            print "Arrangement:", arrangement

developing = False
def p_dev(*args):
    if developing:
        final = ''
        for arg in args:
            final += str(arg)
        print final



digits = []
num_str = ''

numbers_found_list = []
numbers_found_dict = {}

start_time = time.time()



for i in range(100, test_until): # numbers to be tested
    
    if i % 1000 == 0:
        print "\n-- "+str(i)+" --"
    num_str = str(i)    
    perms = []

    for p in permutations(num_str):
        combined_num = ''.join(p)
        if not(int(combined_num) == int(num_str)):
            perms.append(combined_num)

    perms = list(set(perms))
 
    every_way = []

    for order in perms:
        every_way.extend(list(partitions(order)))

    for h, p in enumerate(every_way): # convert to ints
        for j, k in enumerate(p):
            every_way[h][j] = int(k)


    mult_combos(i, every_way)

end_time = time.time()

elapsed_time = end_time - start_time

print "\n"*3+"-"*10+"\n"+"Elapsed Time:",str(elapsed_time)

with open('Equal Product Numbers.csv', 'wb') as csvfile:
    numwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for number in numbers_found_dict:
        numwriter.writerow([number, numbers_found_dict[number]])


print "\nnumber of numbers found:", len(numbers_found_list)
print numbers_found_list
print "\n"*2



