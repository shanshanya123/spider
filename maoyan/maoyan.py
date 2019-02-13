import requests
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
 }
    response = requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None
def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)
main()
