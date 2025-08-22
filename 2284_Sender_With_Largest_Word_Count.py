class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        m = {}
        res = [0, '']
        for sender, message in zip(senders, messages):
            words = message.count(' ') + 1
            m[sender] = m.get(sender, 0) + words
            if m[sender] > res[0] or (m[sender] == res[0] and sender > res[1]):
                res = [m[sender], sender]
        return res[1]