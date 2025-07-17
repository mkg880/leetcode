class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        in_h, in_m = loginTime.split(':')
        out_h, out_m = logoutTime.split(':')
        in_h, in_m, out_h, out_m = int(in_h), int(in_m), int(out_h), int(out_m)
        if out_h < in_h or (out_h == in_h and out_m < in_m):
            out_h += 24
        mod = in_m % 15
        if mod > 0:
            in_m += 15 - mod
        out_m -= out_m % 15
        if out_m < in_m:
            out_h -= 1
            out_m += 60
        diff = (out_h - in_h) * 60 + (out_m - in_m)
        return max(diff // 15, 0)