from pprint import pprint

class WordNode:
    '''Holds a char and bool if this is a word'''
    characters = 0
    children = {}
    character = ''

    def __init__(self, character, is_word=False):
        self.character = character
        self.is_word = is_word
        WordNode.characters += 1

    def displayCharCount(self):
        print(f"Total chars {characters}")

    def addWord(self, word, node_tree):
        for character in word:
            if character in node_tree:
                #print("children")
                pprint(node_tree[character].children)
                #print("------------------")
                node_tree[character].addWord(word[1::], node_tree[character].children)
            else :
                node_tree[character] = WordNode(character, len(word) == 1)

        return node_tree

    def printChildren(self):

        for c in self.children:
            if len(c):
                pprint(c)
                #exit()
                c.printChildren()
            else:
                print(self.character)
