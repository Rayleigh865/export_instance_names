import numpy as np
import sys
import re

def main():
	if len(sys.argv) != 2:
		print("フォーマットが違います")
		sys.exit()
	input_word = sys.argv[1].split('-')
	start = int(re.sub("\\D", "", input_word[0]))
	start_moji = re.findall(r'[a-zA-z.]+', input_word[0])
	end = int(re.sub("\\D", "", input_word[1]))
	end_moji = re.findall(r'[a-zA-z.]+', input_word[1])
	for i in range(start,end+1):
		suuji=str(i)
		if i>=0 and i<=9:
			suuji='00'+suuji
		elif i>=10 and i<100:
			suuji='0'+suuji
		print(start_moji[0]+suuji+end_moji[0])  

if __name__ == '__main__':
	main()
