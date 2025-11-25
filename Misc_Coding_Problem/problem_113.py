#[MEDIUM] Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

# Follow-up: given a mutable string representation, can you perform this operation in-place?

# [hello, world, here]
def reverse_words(string):
    arr = string.split(" ")
    arr.reverse()
    return " ".join(arr)

word = "hello world here"
print(reverse_words(word))