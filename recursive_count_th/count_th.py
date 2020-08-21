'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# need to go over each two characters starting from the beginning moving left to right
# if they match 'th' remove them and continue checking the characters while adding 1 to a count
# if they do not match remove one character from the left




def count_th(word):
    # set base case = once chopped the string down to less than 2 characters return 0
    if len(word) < 2:
        return 0 
    else:
        # if first two letters = 'th' return recursive call removing the 'th' characters and return int +1
        if word[:2] == 'th':
            return 1 + count_th(word[2:])
        else:
            # if the characters do not = 'th' then return recursive call removing first character from the left
            return count_th(word[1:])


count_th('this thicket thickens throughout the thoroughfare')