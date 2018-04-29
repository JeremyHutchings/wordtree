from pprint import pprint
from var_dump import var_dump

class WordNode:
    characters = 0

    def __init__(self):
        self.character = None
        self.is_word   = False
        self.children  = {}

        WordNode.characters += 1

    def addWord(self, this_tree, word_list):

        # If we have something and we are empty and it's not on this level, init ourselves
        first_char = word_list.pop(0)

        # Is it already at this level?
        if first_char not in this_tree:
            # Nope, then this object can grab it
            this_tree[first_char] = WordNode()
            this_tree[first_char].character = first_char
        else:
            pass
            # It's there, go down a level

        if len(word_list) == 0:
            this_tree[first_char].is_word = True
            return this_tree
        else:
            next_char = word_list[0]

        if first_char in this_tree:
            this_tree[first_char].addWord(this_tree[first_char].children, word_list)
        else:
            new_node = WordNode()
            this_tree[first_char].children[next_char] = new_node.addWord(this_tree[first_char].children, word_list)

        return this_tree
