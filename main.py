from classes.wordnode import WordNode
from pprint import pprint
from var_dump import var_dump

content = None

the_tree = {}

#with open('words.txt') as f:
    #content = f.readlines()

#content = [c.strip() for c in content]
## Can't "clean" as we need to keep apostrophes TODO need more of a function approach as we'll have hyphens as well
#content = [c for c in content if c.isalpha()]
#content = [c.lower() for c in content]


content = ['test', 'abc', 'abc', 'tim', 'tim', 'tim', 'tim',
           'tim', 'tim', 'tim', 'tim', 'tim', 'tim', 'tim',
           'tim', 'tim', 'tim', 'tim', 'tim', 'tim', 'tim']


word_count = 0
node_tree  = {}

for word in content:

    word_count += 1
    newOb = WordNode() # Create a new one for each word
    node_tree = newOb.addWord(node_tree, word)

print(f"-------------------------\nOuter: words added {word_count}")

test_word = 'tim'
result = WordNode.isWord(node_tree, test_word)

if (result):
    print(f"Test word = " + str(result.is_word))
    print(f"Count = " + str(result.count))


exit(var_dump(node_tree))
