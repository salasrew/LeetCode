class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        strs = ""

        for i in range(len(words)):
            if len(words[i])>2:
                words[i] = words[i].capitalize()
            else:
                words[i] = words[i].lower()

        for i in words:
            strs = strs + i + " "

        return strs[:-1]
