data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

total = 0
for d in data:
	num = len(d)
	total += num
print('平均留言長度為', total/len(data), '字。')
