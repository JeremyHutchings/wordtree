from pprint import pprint
from var_dump import var_dump

class WordNode:
    characters = 0

    def __init__(self):
        self.character = None
        self.is_word   = False
        self.count     = 0
        self.children  = {}


        WordNode.characters += 1

    def addWord(self, this_tree, word_list):

        # TODO: check length, type, etc; make it a list,
        word_list = list(word_list)

        # If we have something and we are empty and it's not on this level, init ourselves
        first_char = word_list.pop(0)

        # Is it already at this level?
        if first_char not in this_tree:
            # Nope, then this object can grab it
            this_tree[first_char] = WordNode()
            this_tree[first_char].character = first_char

        # Is this the end of the word (list) passed in ?
        if len(word_list) == 0:
            this_tree[first_char].is_word  = True
            this_tree[first_char].count    += 1
            return this_tree
        else:
            next_char = word_list[0]

        if first_char in this_tree:
            # Pass word list to the node below that matched
            this_tree[first_char].addWord(this_tree[first_char].children, word_list)
        else:
            # Adding the new node
            new_node = WordNode()
            this_tree[first_char].children[next_char] = new_node.addWord(this_tree[first_char].children, word_list)

        return this_tree


    @staticmethod
    def isWord(node_tree, word=''):

        if word:
            word = list(word)

            if len(word) == 1:

                # Word is now one char, we've arrived, but is it a word node?
                if (word[0] in node_tree) and (node_tree[word[0]].is_word):

                    return node_tree[word[0]]

                return False

            if word[0] in node_tree:
                return WordNode.isWord(node_tree[word[0]].children, word[1:])

        return False
