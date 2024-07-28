#(2) Let A=[‘abc’, ‘xyz’, ‘aba’, 1221’] be a given string, and write a Python
#program that prints the string or strings and their index from the given list,
#ensuring that the first and last characters of the strings to be printed are
#identical.

a = ['abc', 'xyz', 'aba', '1221']

for i, word in enumerate(a):
  if word[0] == word[-1]:
    print("index",i,"element", word)