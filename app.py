import urllib.request
webUrl = urllib.request.urlopen('https://5f07a8fa6a8b4.htmlsave.net/')
print("result code: " + str(webUrl.getcode()))
data = webUrl.read()
print(data)
