
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore#monthly-hot'
headers={
'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('.explore1.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n'+'='*50+'\n')
    file.close()
