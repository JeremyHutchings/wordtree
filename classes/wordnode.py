from pprint import pprint
from var_dump import var_dump

class WordNode:
    characters = 0

    def __init__(self):
        self.character = None
        self.is_word   = False
        self.children  = {}

        WordNode.characters += 1

    def addWord(self, the_tree, word):

        # If we have something and we are empty and it's not on this level, init ourselves
        first_char = word[:1]
        pass_on    = word[0:0]+word[1:]

        # Is it already at this level?
        if first_char not in the_tree:
            # Nope, then this object can grab it
            the_tree[first_char] = WordNode()
            the_tree[first_char].character = first_char

        #if word == 'ab':
            #exit("it's true")

        # Now we've take the first char off (and maybe assigned it to ourselves, is there any more chars?
        if len(pass_on) > 0:
            # Looks like there are more, so pass them to the class at the index
            #Is there already a child node there ?
            next_level = pass_on[:1]
            if next_level not in the_tree[first_char].children.keys():
                new_node = WordNode()
                the_tree[first_char].children[next_level] = new_node.addWord(self.children, pass_on)
            else:
                the_tree[first_char].addWord(self.children, pass_on)

        else:

            the_tree[first_char].is_word = True

        return the_tree
