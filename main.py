from classes.wordnode import WordNode
from pprint import pprint
from var_dump import var_dump

content    = None
word_count = 0
node_tree  = {}

with open('big.txt') as f:
    content = f.readlines()
    content = [c.strip() for c in content]
    #filter(None, content)

    for line in content:
        if len(line):
            for word in line.split():

                word_count += 1
                newOb = WordNode()
                node_tree = newOb.addWord(node_tree, WordNode.cleanString(word))

print(f"-------------------------\nOuter: words added {word_count}")

test_word = "distinctly"
result = WordNode.isWord(node_tree, WordNode.cleanString(test_word))

var_dump(result)

#exit(var_dump(node_tree))
