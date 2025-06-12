import requests

# r = requests.get('https://imgs.xkcd.com/comics/olympic_sports.png')
# print(r)  
# print(dir(r))
# print(r.content)

# with open ('comic.png','wb') as f:
#     f.write(r.content)
# print(r.ok)
# print(r.headers)

#GET REQUEST
# payload = {'page':2,'count':25}
# r = requests.get('https://httpbin.org/get',params=payload)
# print(r.text)
# print(r.status_code)

#POST REQUEST
# payload = {'username' : 'corey', 'password' : 'testing'}
# r = requests.post('https://httpbin.org/post',data=payload)
#  print(r.text)
# print(r.json())

#AUTHENTICATION REQUESTS
r = requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('corey','testing'),timeout=20)
print(r.text)