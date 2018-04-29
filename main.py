from classes.wordnode import WordNode
from pprint import pprint
from var_dump import var_dump

content = None

the_tree = {}

with open('words.txt') as f:
    content = f.readlines()

#content = ['Python importing the code could not be easier, but everything gets bogged down when you try to work with it and search for items inside of modify it. In these next few examples I will provide several solutions to working with a word list containing practically every word in the English']


content = [c.strip() for c in content]
# Can't "clean" as we need to keep apostrophes TODO need more of a function approach as we'll have hyphens as well
content = [c for c in content if c.isalpha()]
content = [c.lower() for c in content]

word_count = 0
node_tree  = {}

for word in content:

    word_count += 1
    newOb = WordNode() # Create a new one for each word
    node_tree = newOb.addWord(node_tree, list(word))

print(f"-------------------------\nOuter: words added {word_count}")

print("Finished")
print("len = " + str(len(node_tree)))
#exit(var_dump(node_tree))
