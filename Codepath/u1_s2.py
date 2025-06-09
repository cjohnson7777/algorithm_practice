
# 1 - Returns the sentence with word order reversed. If there's only one word, returns it unchanged.
def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

#print("Problem 1: ", reverse_sentence("tubby little cubby all stuffed with fluff"))

def reverse_sentence(sentence):
    word = sentence.split()
    reverse_sentence = ""

    for i in range(len(word) -1, -1, -1):
        reverse_sentence += word[i] + ' '
    
    return reverse_sentence
    
print(reverse_sentence("tubby little cubby all stuffed with fluff"))


# 2 - Returns any number that is neither the min nor the max in nums, or -1 if no such number exists.
def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1
    
    lo, hi = min(nums), max(nums)

    for x in nums:
        if lo < x < hi:
            return x
        
    return -1

print("Problem 2: ", goldilocks_approved([3, 2, 1, 4]))  



# 3 - Removes the minimum element repeatedly and returns the removal order as a new list.
def delete_minimum_elements(hunny_jar_sizes):
    result = []
    jars = hunny_jar_sizes[:]

    while jars:
        m = min(jars)
        result.append(m)
        jars.remove(m)

    return result

print("Problem 3: ", delete_minimum_elements([5, 3, 2, 4, 1]))

# 4 - Returns the sum of the decimal digits of num.
def sum_of_digits(num):
    total = 0
    n = abs(num)

    while n:
        total += n % 10
        n //= 10

    return total

print("Problem 4: ", sum_of_digits(423)) 

# 5 - Starts tigger = 1. 'bouncy' and 'flouncy'  → tigger += 1 'trouncy' and 'pouncy'  → tigger -= 1 Returns final tigger.
def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op in ("bouncy", "flouncy"):
            tigger += 1
        elif op in ("trouncy", "pouncy"):
            tigger -= 1
    return tigger

print("Problem 5: ", final_value_after_operations(["trouncy", "flouncy", "flouncy"]))

# 6 - Returns True if s equals the concatenation of the first letters of each word in order.
def is_acronym(words, s):
    if len(s) != len(words):
        return False
    return all(word[0] == s[i] for i, word in enumerate(words))

print("Problem 6: ", is_acronym(["christopher", "robin", "milne"], "crm"))

# 7 - You can ±1 any element. Returns the minimum total operations to make every element % 3 == 0.
def make_divisible_by_3(nums):
    ops = 0
    for x in nums:
        r = x % 3
        # Either subtract r or add (3 - r), pick the cheaper
        ops += min(r, (3 - r) % 3)
    return ops

print("Problem 7: ", make_divisible_by_3([1, 2, 3, 4])) 

# 8 - Returns items in lst1 not in lst2, followed by items in lst2 not in lst1 (preserving each list’s order).
def exclusive_elemts(lst1, lst2):
    arr = []

    for word in lst1:
        if word not in lst2:
            arr.append(word)

    for word in lst2:
        if word not in lst1:
            arr.append(word)
    
    return arr
    # return [x for x in lst1 if x not in lst2] + \
    #        [x for x in lst2 if x not in lst1]

print("Problem 8: ", exclusive_elemts(
    ["pooh", "roo", "piglet"],
    ["piglet", "eeyore", "owl"]
))

# 9 - Builds a new string by taking letters alternately from word1 and word2; appends any leftover tail at the end.
def merge_alternately(word1, word2):
    res = []
    n1, n2 = len(word1), len(word2)

    for i in range(max(n1, n2)):

        if i < n1:
            res.append(word1[i])

        if i < n2:
            res.append(word2[i])

    return "".join(res)

print("problem 9: ", merge_alternately("wol", "oze")) 
print("problem 9: ", merge_alternately("hfa", "eflump")) 

# 10 - Counts pairs (i,j) where pile1[i] is divisible by (pile2[j] * k).
def good_pairs(pile1, pile2, k):
    count = 0

    for x in pile1:
        for y in pile2:
            if x % (y * k) == 0:
                count += 1

    return count

print("Problem 10: ", good_pairs([1, 3, 4], [1, 3, 4], 1))  
print("Problem 10: ", good_pairs([1, 2, 4, 12], [2, 4], 3))  

# Version 2

# 11
def are_equivalent(word1, word2):
    return "".join(word1) == "".join(word2)

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print("Problem 11: ", are_equivalent(word1, word2))

# 12
def count_evens(lst):
    count = 0

    for word in lst:
        if len(word) % 2 == 0:
            count += 1

    return count

lst = ["na", "nana", "nanana", "batman", "!"]
print("Problem 12", count_evens(lst))

