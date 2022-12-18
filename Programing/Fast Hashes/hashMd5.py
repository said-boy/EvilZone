import hashlib
import requests

b = ''
with open('file.txt','r') as f :
    for i in f.readlines():
        j = i.replace('\n','')
        a = hashlib.md5(j.encode("utf-8")).hexdigest()
        b += a
result = hashlib.md5(b.encode("utf-8")).hexdigest()
print(result)
# data = {'action':'generateHasherTask'}
# data2 = {'hash':result,'action':'checkSolution'}
# k = requests.post("https://evilzone.org/challenges/fast_hasher/",params=data)
# k = requests.post("https://evilzone.org/challenges/fast_hasher/",params=data2)
# print(k.text)