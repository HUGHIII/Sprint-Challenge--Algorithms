#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) linear = the amount of times the loop runs increases linearly with the value of 'n'

b)linearithmic O(n\*log n) = the for loop increases at a linear rate, based on n. inside the for loop is a O(log(n)) while loop based on j < n and j doubles itself each time

c)O(n) linear = recursions are dependent merely on n

## Exercise II

i would set bottom floor, top floor, and middle to variable
bottom = 0
top = n or len(n)
middle = bottom + top //2

drop the egg from the middle floor, if it breaks i would halve the floors again making the new top one floor down from old middle then add bottom // 2. if it didn't break i would do the same in the opposite direction, make the new bottom the middle + 1 and repeat until f was found.

this would be a logarithmic run time because the possible floors would be halved each time.
