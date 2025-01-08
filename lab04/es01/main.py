import string

class CustomStr(str):

    def is_palindrome(self):
        s = ''.join(c for c in self.lower() if c not in string.whitespace and c not in string.punctuation)
        return s == s[::-1]

