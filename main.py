from classes.wordnode import WordNode
from pprint import pprint

fname = 'words.txt'
content = None

with open(fname) as f:
    content = f.readlines()


content = [c.strip() for c in content]

## Can't "clean" as we need to keep apostrophes
content = [c for c in content if c.isalpha()]
content = [c.lower() for c in content]


node_tree = {}

for word in content:

    node_tree = WordNode.addWord(None, word, node_tree)

    for char, node in node_tree.items():
        node.printChildren()



print("Outside")
print(WordNode.displayCharCount)
print(len(node_tree))
