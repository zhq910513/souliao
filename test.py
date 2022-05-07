from urllib import parse

test = 'RKRkWgMEm5xWrIngH%252B8DL5Mj31c0ptazOxp2d0Xq7jalRoDX9ovO3bD5yslDNsWBaqUFypMdDDcH%250AHFGb0bRThPOp8WYbpLEeO66njDnbWs3ceM15MVpuRG4hHLN2ZjJlIz0XSeAV%252FMH%252BwmdTQbzBgGfA%250Ae0DIs%252BXLKt7keCHehnsP8Wt9EZPoZlIBOD1LK9z64NV7pxGp8sQxmXtiCT4xXPkbeZjQ6YrBBCgk%250AVTwBLplDOasyd5URrnEMTMZHxgFjCP5gEst63S1uTqDrcYy0jkPRMDB%252FnaQeViS%252BvKT36Bev4QmZ%250AdIMTwgAOpCwc%252B6KAh3G5miQ%252FfTU0Oa7VgdujXw%253D%253D'

def text_unquote(text):
    new_text = parse.unquote(text)
    if '%' in text:return text_unquote(new_text)
    else:
        return new_text

print(text_unquote(test))


'frida -U -f io.dcloud.W2Awww.soliao.com -l D:/Projects/souliao/cipher.js --no-pause'

