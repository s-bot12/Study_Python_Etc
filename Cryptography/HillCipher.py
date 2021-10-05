import numpy as np

def is_number(key) : #key 값을 검증
	if(len(key) <= 0) :
		return 0
	for i in key :
		if(type(i) != int) :
			return 0
		elif(i > 25 or i < 0) :
			return 0	
	return 1

def encryption(key, text) : #암호화 알고리즘
	key_index = 0
	for i in range(len(text)) :
		if(ord(text[i].upper()) >= 65 and ord(text[i].upper()) <= 90) :
			text[i] = ord(text[i].upper()) + (ord(key[key_index%len(key)].upper()) - 65) 
			key_index += 1
			while(text[i] > 90) :
				text[i] -= 26
			text[i] = chr(text[i])
	return "".join(text)

def decryption(key, text) : #복호화 알고리즘
	key_index = 0
	for i in range(len(text)) :
		if(ord(text[i].upper())>= 65 and ord(text[i].upper()) <= 90) :
			text[i] = ord(text[i].upper()) - (ord(key[key_index%len(key)].upper()) - 65) 
			key_index += 1
			while(text[i] < 65) :
				text[i] += 26
			text[i] = chr(text[i])
	return "".join(text)



print("====Hill Cipher====\n")


while True :
	print("\n---2x2 Key를 입력해주세요!(26 미만 숫자만 사용 가능)---\n")
	print("예시) 2,1,3,5 입력 시\n\t 2 1 \n\t 3 5 \n")
	try :
		key = list(map(int, input().split(',')))
	except :
		print("숫자 이외의 값은 넣을 수 없습니다! (종료)")
		exit(1)
	if(is_number(key) == 1) :
		break;
			
print("\n---1,2중 선택해주세요! (1-암호화 2-복호화)---\n")
select = int(input())
while(select != 1 and select != 2) :
	print("\n---1또는 2만 입력해주세요! (1-암호화 2-복호화)---\n")
	select = int(input())

print("\n---파일 명을 입력해주세요!(txt 파일)---\n")
title = input()

try:
        open_f = open(title, 'r')
except:
        try:
                open_f = open(title + ".txt", 'r')
        except :
                print("%s 명의 파일이 없습니다! (종료)" % title)
                exit(1)
text = open_f.read()

if(select == 1) :
	text = encryption(key, list(text))

else :
	text = decryption(key, list(text))


#print("\n----------\n" + text + "\n----------\n")
#make_f = open("result.txt", 'w')
#make_f.write(text)
#print("\n---result.txt로 결과 파일이 생성되었습니다!---\n")
#make_f.close()
#open_f.close()


#test_a = np.array([[12,4],[4,19],[12,4],[0,19],[4,8],[6,7],[19,14],[2,11],[14,2],[10,23]])
#test_b = np.array([[7,3],[2,5]])
#result = ((test_a @ test_b) % 26) + 65
#for i in range(len(result)) :
#	print(chr(result[i][0]) + ' ' + chr(result[i][1]))

#print(chr(result[0][1] + 65))
