import numpy as np

def make_inverse(list) : #mod 26에 대한 역행렬 만드는 함수
	result = []
	inverse = (list[0] * list[3]) - (list[1] * list[2])
	if(inverse < 0) :
		inverse = inverse % 26  
	for i in range(1,26) :
		if (inverse * i) % 26 == 1 :
			inverse = i
			break
	list[0], list[3] = list[3], list[0]
	list[1] = 26 - list[1]
	list[2] = 26 - list[2]
	for i in range(len(list)) :
		list[i] = (inverse * list[i]) % 26
	return list
	
def list_chunk(list, n) : #n개씩 하위 리스트로 분할
	return [list[i:i+n] for i in range(0, len(list), n)]

def is_key(key) : #예외처리 및 gcd 기반 key 값을 검증
	if(len(key) != 4) :
		return 0
	for i in key :
		if(type(i) != int) :
			return 0

	inverse = (key[0] * key[3]) - (key[1] * key[2])

	if(inverse < 0) :
		inverse = inverse % 26  
	for i in range(1,26) :
		if (inverse * i) % 26 == 1 :
			return 1
	return 0

def encryption(key, text) : #암호화 알고리즘
	text_array = []
	result = []
	index = 0 #text에서 알파벳만 바꿔주는 index
	switch = 0 #마지막 text에 x를 추가했는지 구분
	
	for i in range(len(text)) :
		if(ord(text[i].upper()) >= 65 and ord(text[i].upper()) <= 90) :
			text_array.append(ord(text[i].upper()) - 65)

	if len(text_array) % 2 == 1 : #text가 홀수이면 x 하나를 넣어줌
		text_array.append(23)
		switch = 1 

	text_array = np.array(list_chunk(text_array, 2))
	key_array = np.array(list_chunk(key, 2))

	text_array = ((text_array @ key_array) % 26) + 65 #2차원 배열 곱(내적)

	for i in range(len(text_array)) :
		result.append(chr(text_array[i][0]))
		result.append(chr(text_array[i][1]))
		
	for i in range(len(text)) :
		if(ord(text[i].upper()) >= 65 and ord(text[i].upper()) <= 90) :
			text[i] = result[index]
			index += 1

	if switch == 1 :
		text.append(result[index])
		
	return ''.join(text)

def decryption(key, text) : #복호화 알고리즘
	text_array = [];
	result = [];
	index = 0
	
	for i in range(len(text)) :
		if(ord(text[i].upper()) >= 65 and ord(text[i].upper()) <= 90) :
			text_array.append(ord(text[i].upper()) - 65)

	text_array = np.array(list_chunk(text_array, 2))	
	key_array = make_inverse(key)
	key_array = np.array(list_chunk(key, 2))

	text_array = ((text_array @ key_array) % 26) + 65 #2차원 배열 곱(내적)

	for i in range(len(text_array)) :
		result.append(chr(text_array[i][0]))
		result.append(chr(text_array[i][1]))

	for i in range(len(text)) :
		if(ord(text[i].upper()) >= 65 and ord(text[i].upper()) <= 90) :
			text[i] = result[index]
			index += 1

	return ''.join(text)



print("====Hill Cipher====\n")

while True :
	print("\n---2x2 Key를 입력해주세요! GCD(ad-bc, 26) = 1을 만족해야함---\n")
	print("예시) 5,8,17,3 입력 시\n\t 5  8 \n\t 17 3 \n")
	try :
		key = list(map(int, input().split(',')))
	except :
		print("숫자 이외의 값은 넣을 수 없습니다! (종료)")
		exit(1)
	if(is_key(key) == 1) :
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

print("\n----------\n" + text + "\n----------\n")
make_f = open("result.txt", 'w')
make_f.write(text)
print("\n---result.txt로 결과 파일이 생성되었습니다!---\n")
make_f.close()
open_f.close()

