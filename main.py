import requests
import pprint
from urllib.parse import unquote
pp = pprint.PrettyPrinter(indent=4)


def case_list():
    # link = 'https://www.soliao.com/api/app/server' \
    #        '?data=K383oPYEBrRxoONWwFwioOLB67kK45vgRl15fVpxNUY%252FEOwLVfFhlpG9R5CtUsSW%252FDUlna6vci7C%250ASHXHC%252FhvnZQDI7ToiDp4yoy6QHvCmerM2SxGGdjPPm0CowpWVv4sZ0W6a0uQzcRuLsTvHO8bKU7s%250ANFIUgwU5T%252FtgcErvwZk6kHuylMh1P7ylnUvE9oC9mwfDMQiBneGGWCryRvNohiKO7X6WpByi4dQh%250AEiQ%252Fu7eOSBLE3VMMKz3ZJI3MGs3S7HEZ%252Fl65XJOoT6OL8ShUOOZexv7SufHN6kPpA8NQqOfPjr%252BC%250AhyCcmxhJyU0v%252BEGg6JRlg37iqnZOKnW8ofdbI0EPbGqAm6ibFYdqpcd%252FwxgScmXuB7IZjzQ0tLNk%250AF0T%252FZdm5%252FYa0aUdGFs%252BTiwW7zoF5QEcaEnUQ7DkGSHfTbwFbc9jLJaNnGGv%252BbchYkC1xTQdWvNyT%250AiPiq1Gn4fkPNrS1p1DWXPGG3eE3WjKe21WTPzJQ7c0LCb%252Fyo7fBbZsM1'
    link = 'https://www.soliao.com/api/app/server' \
           '?data=SuT%252BS1tk0tOloc3CsPdg80oEWyAyDRE1fzlOH3htfID8R2b2DnKYRhiCr9ZcyjgbC1jwp4tHkIW9%250Ax7yWTc4yLaibFJ0TFNud0oWa6rbTk%252FSCGEkSqQ7rywwl3zVKiOnOGjg7Ns4f6lA%252BdWbT%252BHc1IFCa%250AJvfjysEMLrmzDZYONGVakt1Esvc2ta8YuQFD1VLggGRhIrT6pU%252BrDVUluPhL4eBtHEFEIqujNYli%250AkhVMzpGQ9yoU71yzY6TvJArEjBQ6NvxGdvvJcefTLd9S9dfulxLKwrZwRex3InsG7dTzLmgUZgNY%250AaSOisnA9NKG0HaON1mmej%252FAF5kRm85gyp0xd2FHK9eUr%252F2uRO%252FbDW%252B6qUsv4JRKCzGyQON5llvvG%250A7Lg%252FBm8h5j4a22nz5eZejsAzbUzyT2Rk9g6t1RerSWFEFsOemCjpJD0SIBkcK6tI2MXh3cgoZM5k%250ASBVQ%252BTDFOwSz5ApSJXMazne3mAwThSLxAG6gXT3DkI%252B%252FaT4Q5HLs4I20'
    headers = {
        # 'Cookie': 'Expires=Fri, 03-Mar-2023 03:11:04 GMT; Max-Age=25920000; Path=/;refererCookie=refererCookie;autoCookie="18823450513:1677813064957:d970015f24e42d84207d28ae310591f8b7b36c30"; Version=1',
        # 'token': 'de52ef10-39b8-4756-af54-38cd1008f997',
        # 'Cookie': 'HttpOnly; Path=/;soliao=487603685A396609ACF8D8E9E4AEB730',
        # 'token': '795d7759-0c9c-4b54-8638-1b8d28731d38',
        'Host': 'www.soliao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12'
    }

    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


def case_detail():
    # link = 'https://www.soliao.com/api/app/server' \
    #        '?data=RKRkWgMEm5xWrIngH%252B8DL5Mj31c0ptazOxp2d0Xq7jalRoDX9ovO3bD5yslDNsWBaqUFypMdDDcH%250AHFGb0bRThPOp8WYbpLEeO66njDnbWs3ceM15MVpuRG4hHLN2ZjJlIz0XSeAV%252FMH%252BwmdTQbzBgGfA%250Ae0DIs%252BXLKt7keCHehnsP8Wt9EZPoZlIBOD1LK9z64NV7pxGp8sQxmXtiCT4xXPkbeZjQ6YrBBCgk%250AVTwBLplDOasyd5URrnEMTMZHxgFjCP5gEst63S1uTqDrcYy0jkPRMDB%252FnaQeViS%252BvKT36Bev4QmZ%250AdIMTwgAOpCwc%252B6KAh3G5miQ%252FfTU0Oa7VgdujXw%253D%253D'
    link = 'https://www.soliao.com/api/app/server' \
           '?data=R1k9heGYIpLvN2usQYtwH4WjTV8Oi4zmaPgR%252FlLnI00gwNVXvIrB6Cs8nZVXAqXN6i3IV3T6OMEH%250Ah78Ad2Kwi5vVDfXSiK8lHXNTU%252FFz50ZQMoRohK9koUnKIvR7JfuUhoRNDqvU69sSE2QX1xPI3ui5%250ApYcrimZPizN1reU1Ad9D%252FV1nym6MumI5yaShWJ3eZDQeRRbLyVZoKd93cv2I7uF2IpPc1v%252BTdkE8%250A%252FsgCsqp0GmW5gKODkLM%252BQrGcC6HzPMvT7xadVWrDNND1w3sU2XOHCK9Z6s6Mbg3pZ7zxVDjAk458%250AuI2FY2gi46CIEsH2Qor7KG4N2WLy9Y9E1zdi1A%253D%253D'
    headers = {
        # 'Cookie': 'HttpOnly; Path=/;soliao=487603685A396609ACF8D8E9E4AEB730',
        # 'token': '795d7759-0c9c-4b54-8638-1b8d28731d38',
        'Host': 'www.soliao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12'
    }

    print(unquote(link))
    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


if __name__ == '__main__':
    case_detail()
