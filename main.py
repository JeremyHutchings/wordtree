from classes.wordnode import WordNode
from pprint import pprint
from var_dump import var_dump

content = None

the_tree = {}

with open('words.txt') as f:
    content = f.readlines()

content = [c.strip() for c in content]
# Can't "clean" as we need to keep apostrophes
content = [c for c in content if c.isalpha()]
content = [c.lower() for c in content]


word_count = 0
node_tree  = {}


for word in ['a', 'abc','adef','ferrr', 'ade']:

    print("node_tree")
    var_dump(node_tree)

    word_count += 1
    print(f"---- Adding word {word}")
    newOb = WordNode() # Create a new one for each word
    node_tree = newOb.addWord(node_tree, word)



print(f"Outer: words added {word_count}")



print("Outside")
print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")
exit(var_dump(node_tree))
