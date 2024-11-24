
# *Change Every Letter to the Next Letter
# *Write a function that changes every letter to the next letter:

#? "a" becomes "b"
# ?"b" becomes "c"
# ?"d" becomes "e"
# ?and so on ...
# !Examples
# ?move("hello") ➞ "ifmmp"

# ?move("bye") ➞ "czf"

# ?move("welcome") ➞ "xfmdpnf"
# !Notes
# !There will be no z's in the tests.



# def move(word):
#     #ap=
#     alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     tito=list( word)
#     mylist = []
#     for x in tito:
#         if x in alp:
#            mylist.append(alp.index(x)+1)
#     return mylist
# print(move("word"))

# print(chr(23))

def move(string):
    char_list = [char for char in string]
    my= [ord(x)+1 for x in char_list]
    yy = [chr(y) for y in my]
    return "".join(yy)
print(move("tito"))
print(move("hello"))


#print(ord("a"))

def move(string):
    # Convert each character to ASCII, add 1, and convert back to a character
    shifted_chars = [chr(ord(char) + 1) for char in string]
    # Join the characters into a single string
    return "".join(shifted_chars)

# Examples
print(move("hello"))   # Output: "ifmmp"
print(move("bye"))     # Output: "czf"
print(move("welcome")) # Output: "xfmdpnf"
