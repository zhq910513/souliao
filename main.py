import requests
import pprint
from urllib.parse import unquote
pp = pprint.PrettyPrinter(indent=4)


def case_list():
    link = 'https://www.soliao.com/api/app/server' \
           '?data=K383oPYEBrRxoONWwFwioOLB67kK45vgRl15fVpxNUY%252FEOwLVfFhlpG9R5CtUsSW%252FDUlna6vci7C%250ASHXHC%252FhvnZQDI7ToiDp4yoy6QHvCmerM2SxGGdjPPm0CowpWVv4sZ0W6a0uQzcRuLsTvHO8bKU7s%250ANFIUgwU5T%252FtgcErvwZk6kHuylMh1P7ylnUvE9oC9mwfDMQiBneGGWCryRvNohiKO7X6WpByi4dQh%250AEiQ%252Fu7eOSBLE3VMMKz3ZJI3MGs3S7HEZ%252Fl65XJOoT6OL8ShUOOZexv7SufHN6kPpA8NQqOfPjr%252BC%250AhyCcmxhJyU0v%252BEGg6JRlg37iqnZOKnW8ofdbI0EPbGqAm6ibFYdqpcd%252FwxgScmXuB7IZjzQ0tLNk%250AF0T%252FZdm5%252FYa0aUdGFs%252BTiwW7zoF5QEcaEnUQ7DkGSHfTbwFbc9jLJaNnGGv%252BbchYkC1xTQdWvNyT%250AiPiq1Gn4fkPNrS1p1DWXPGG3eE3WjKe21WTPzJQ7c0LCb%252Fyo7fBbZsM1'

    headers = {
        'Cookie': 'Expires=Fri, 03-Mar-2023 03:11:04 GMT; Max-Age=25920000; Path=/;refererCookie=refererCookie;autoCookie="18823450513:1677813064957:d970015f24e42d84207d28ae310591f8b7b36c30"; Version=1',
        'token': 'de52ef10-39b8-4756-af54-38cd1008f997',
        'Host': 'www.soliao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12'
    }

    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


def case_detail():
    link = 'https://www.soliao.com/api/app/server' \
           '?data=RKRkWgMEm5xWrIngH%252B8DL5Mj31c0ptazOxp2d0Xq7jalRoDX9ovO3bD5yslDNsWBaqUFypMdDDcH%250AHFGb0bRThPOp8WYbpLEeO66njDnbWs3ceM15MVpuRG4hHLN2ZjJlIz0XSeAV%252FMH%252BwmdTQbzBgGfA%250Ae0DIs%252BXLKt7keCHehnsP8Wt9EZPoZlIBOD1LK9z64NV7pxGp8sQxmXtiCT4xXPkbeZjQ6YrBBCgk%250AVTwBLplDOasyd5URrnEMTMZHxgFjCP5gEst63S1uTqDrcYy0jkPRMDB%252FnaQeViS%252BvKT36Bev4QmZ%250AdIMTwgAOpCwc%252B6KAh3G5miQ%252FfTU0Oa7VgdujXw%253D%253D'

    headers = {
        'Cookie': 'HttpOnly; Path=/;soliao=5712490CDE89C4BEB4E292D0BE485C8D',
        'token': 'de52ef10-39b8-4756-af54-38cd1008f997',
        'Host': 'www.soliao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12'
    }

    print(unquote(link))
    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


case_detail()