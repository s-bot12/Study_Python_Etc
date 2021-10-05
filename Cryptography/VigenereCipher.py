def is_english(key) : #key 값을 검증
	if(len(key) <= 0) :
		return 0
	for i in key :
		if(ord(i.upper()) < 65 or ord(i.upper()) > 90) :
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



print("====Vigenere Cipher====\n")
print("\n---Key를 입력해주세요!(영문자만 사용 가능)---\n")
key = input()
while(is_english(key) == 0) :
	print("\nkey값은 영문자만 입력 가능합니다! 다시 입력해주세요---\n")
	key = input()

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
	text = encryption(list(key), list(text))

else :
	text = decryption(list(key), list(text))


print("\n----------\n" + text + "\n----------\n")
make_f = open("result.txt", 'w')
make_f.write(text)
print("\n---result.txt로 결과 파일이 생성되었습니다!---\n")
make_f.close()
open_f.close()
