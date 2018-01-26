class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.value = ""

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word or self.search(word):
            pass
        else:
            curr_trie = self
            i = 1
            curr_alpha = word[:i]

            while curr_alpha in curr_trie.children:
                curr_trie = curr_trie.children[curr_alpha]
                i = i + 1
                curr_alpha = word[:i]
            
            while i < len(word):
                new_trie = Trie()
                curr_trie.children[curr_alpha] = new_trie
                curr_trie = new_trie
                i = i + 1
                curr_alpha = word[:i]

            new_trie = Trie()
            new_trie.value = word
            curr_trie.children[curr_alpha] = new_trie


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        curr_trie = self
        i = 1
        curr_alpha = word[:i]

        while curr_alpha in curr_trie.children:
            curr_trie = curr_trie.children[curr_alpha]
            i = i + 1
            curr_alpha = word[:i]

        if word == curr_trie.value:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return False
        curr_trie = self
        i = 1
        curr_alpha = prefix[:i]

        while curr_alpha in curr_trie.children and i < len(prefix) + 1:
            curr_trie = curr_trie.children[curr_alpha]
            i = i + 1
            curr_alpha = prefix[:i]

        if i == len(prefix) + 1:
            return True
        else:
            return False



# Your Trie object will be instantiated and called as such:
obj = Trie()
prefix = "ab"
obj.insert(prefix)
param_2 = obj.search("ab")
param_3 = obj.startsWith("a")
print(param_2)
print(param_3)