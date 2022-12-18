import shutil
for i in range(999,-1,-1):
    shutil.unpack_archive(f'flag_{i}.tar.gz')
with open('flag.txt','r')as f:
    print(f'Solved Challange: {f.read()}')


