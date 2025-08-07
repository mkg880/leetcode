class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        block = False
        pre_block = ''
        for line in source:
            if not line:
                continue
            slash = line[0] == '/'
            star = line[0] == '*'
            start = 0
            cmt = False
            line_cmt = block
            for i in range(1, len(line)):
                if not block:
                    if line[i] == '*' and slash:
                        block = True
                        cmt = True
                    elif line[i] == '/':
                        cmt = slash
                        line_cmt = cmt
                        slash = True
                    else:
                        slash = False
                    if cmt:
                        if line[i] == '/':
                            s = pre_block + line[start:i-1]
                            if s:
                                res.append(pre_block + line[start:i-1])
                                pre_block = ''
                            break
                        pre_block += line[start:i-1]
                else:
                    if line[i] == '*':
                        star = True
                    else:
                        if line[i] == '/' and star:
                            block = False
                            line_cmt = False
                            cmt = False
                            start = i+1
                            slash = False
                        star = False
            if not block and not line_cmt:
                s = line[start:]
                s = pre_block + s
                pre_block = ''
                if s:
                    res.append(s)
        return res