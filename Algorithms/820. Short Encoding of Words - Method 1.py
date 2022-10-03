# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.


class TNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TNode()
        for word in words:
            self.to_trie(root, word)
        return self.dfs(root, 1)
        
    def to_trie(self, root: TNode, word: str) -> TNode:
        node = root
        for i in word[::-1]:
            if i not in node.children:
                node.children[i] = TNode()
            node = node.children[i]
        node.is_end = True
        return root
    
    def dfs(self, node: TNode, count: int) -> int:
        if node.children:
            return sum(self.dfs(i, count+1) for i in node.children.values())
        else:
            return count
