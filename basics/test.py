import requests

content = requests.get('http://docs.kubernetes.org.cn/227.html')
print(content.content)