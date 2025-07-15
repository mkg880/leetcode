class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pre = []
        pre_cnt = []
        curr = 0
        cnt = 0
        for i in range(len(boxes)):
            pre.append(curr)
            pre_cnt.append(cnt)
            if boxes[i] == '1':
                curr += i
                cnt += 1
        post = [0] * len(boxes)
        post_cnt = [0] * len(boxes)
        curr = 0
        cnt = 0
        for i in range(len(boxes) - 1, -1, -1):
            post[i] = curr
            post_cnt[i] = cnt
            if boxes[i] == '1':
                curr += i
                cnt += 1
        res = []
        for i, (a, b, c, d) in enumerate(zip(pre, pre_cnt, post, post_cnt)):
            res.append((i * b - a) + (c - i * d))
        return res