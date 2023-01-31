data = []
length = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        for  word in line:
            length.append(word)
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完畢，共', len(data), '筆留言')
avg_length = len(length)/len(data)
print(avg_length)
# for word in data[0]:
#     length.append(word.replace(' ', ''))
# print(data[0])
# print(len(length))

    
        