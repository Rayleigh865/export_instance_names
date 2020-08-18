import sys
import re

def main():
	if len(sys.argv) != 3:
		print("引数の数が合いません")
		sys.exit()

	input_word = sys.argv[1].split('~')
	start = int(re.sub("\\D", "", input_word[0]))
	start_moji = re.findall(r'[a-zA-z.-]+', input_word[0])
	end = int(re.sub("\\D", "", input_word[1]))
	end_moji = re.findall(r'[a-zA-z.-]+', input_word[1])
	
	try:
		output=export(start,start_moji[0],end,end_moji[0])
	except Exception as e:
		print("命名規則がおかしいです")
		sys.exit()

	#表示部分
	if sys.argv[2]=='list':
		[print(i) for i in output]
	elif sys.argv[2]=='comma':
		print(*output,sep=', ')
	else:
		print("第二引数のフォーマットがおかしいです")


def export(start,start_moji,end,end_moji):
	output=[]
	for i in range(start,end+1):
		suuji=str(i)
		if i>=0 and i<=9:
			suuji='00'+suuji
		elif i>=10 and i<100:
			suuji='0'+suuji
		output.append(start_moji+suuji+end_moji)
	return output

if __name__ == '__main__':
	main()
