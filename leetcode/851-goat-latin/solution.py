class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []

        split = sentence.split()

        for i, word in enumerate(split, 1):
            curWord = []

            if word[0] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                curWord.append(word[1:] + word[0])
            else:
                curWord.append(word)
            
            curWord.append('ma')
            curWord.append('a' * i)
            result.append("".join(curWord))

        return " ".join(result)
        