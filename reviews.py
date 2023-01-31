data = []
len_sum = 0
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        len_sum += len(line.split())
        # if len(data) % 10000 == 0:
        #     print(len(data))
print('檔案讀取完畢，共', len(data), '筆留言')
print('留言平均長度為', len_sum/len(data))

new =[]
for d in data:
    if len(d.split())>200:
        new.append(d)
        print(len(d.split()))
print('共有', len(new), '筆留言大於200')



    
        