data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        
        # if len(data) % 10000 == 0:
        #      print(len(data))
print('檔案讀取完畢，共', len(data), '筆留言')

count = {}
for line in data:
    words = line.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
for word in count:
    if count[word] > 1000000:
        print(word, count[word])
print(len(count))

while True:
    word = input('請問您要查的單字: ')
    if word == 'q':
        break
    elif word in count:
        print(count[word])
    else:
        print('查無此字')
