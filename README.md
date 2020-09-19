# Shapeshifting-Geese
The script `find_geese.py` finds positive integers that are the product of some rearrangement of their digits into two or more factors. I call these numbers "shapeshifting geese" numbers. Each of the number's digits must be used once and only once. The first such number is 126, because 21 * 6 = 126. A simple proof that there are infinitely many of these numbers: take any shapeshifting goose number `x`, and append a 0 to the end of it. This 0 digit can be added to the end of one of the factors in the goose factorization of `x`. For example, if `x` = 126 = 21 * 6, then we get that 1260 = 21 * 60 is also a shapeshifting goose number. By induction, there are infinitely many shapeshifting goose numbers.

Run the script `find_geese.py` in Python 2. The first command line argument is the integer at which to start searching for shapeshifting goose numbers. If not provided, starts at 1. The second command line argument is the integer at which to stop searching for goose numbers. If not provided, the script continues searching to infinity. Examples:

Search for all goose numbers from 1 to infinity:  `python2 find_geese.py`

Search for all goose numbers from 1000 to infinity:  `python2 find_geese.py 1000`

Search for all goose numbers from 33000 to 100,001:  `python2 find_geese.py 33000 100001`


## Analysis

Empirically, it seems there are disproportionately more equal product numbers that start with smaller digits like 1 than start with larger digits like 8 or 9. This makes sense when you consider that there are more rearrangements of the digits of an integer `k` that multiply to smaller numbers (with the same number of digits as `k`) than larger numbers (getting larger numbers requires more specific arrangements than smaller numbers).

One question that remains to be answered is whether the fraction of all positive integers that are shapeshifting goose numbers approaches 1.
