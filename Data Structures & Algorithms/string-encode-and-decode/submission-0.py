class Solution:
    def encode(self, strs: List[str]) -> str:
        word = ''
        for s in strs:
            word+=s
            word+= 'è'
        #lets put a keysomewhereassumingkey isnt given
        #thechallenge is how we seperate could as a list of numbers as key
        return word

    def decode(self, s: str) -> List[str]:
        words = []
        word = ''
        #print(s)

        for i in s:
            if i != 'è':
                word += i
            if i == 'è':
                words.append(word)
                word = ''


        return words