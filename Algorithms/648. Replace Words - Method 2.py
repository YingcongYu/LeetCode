# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. 
# For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. 
# If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.


class TNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = self.dict_to_trie(dictionary)
        output = []
        for i in sentence.split():
            output.append(self.search_trie(trie, i))
        return ' '.join(output)
        
    def dict_to_trie(self, dictionary: List[str]) -> TNode:
        root = TNode()
        for word in dictionary:
            node = root
            for i in word:
                if i not in node.children:
                    node.children[i] = TNode()
                node = node.children[i]
            node.is_end = True
        return root
    
    def search_trie(self, root: TNode, word: str) -> str:
        node = root
        output = ''
        for i in word:
            if i not in node.children or node.is_end:
                break
            output += i
            node = node.children[i]
        if node.is_end:
            return output
        else:
            return word
