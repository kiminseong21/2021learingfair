
# 개인정보 보호 지침 출력 장면

print( " 지금부터 우리 함께 개인정보 보호방법 알아봐요!! " )


loopCut = 12

for i in range(loopCut):
    for j in range(loopCut-i-1):
        print(' ' ,end='')

    for k in range((i+1)*2-1):
        print('*' ,end='')

    print()



print( " 1. 개인정보처리방침 및 이용약관 꼼꼼히 살피기 " )


print( " 2. 타인이 유추하기 어려운 안전한 비밀번호 사용 ")


print( " 3. 비밀번호는 주기적으로 변경하기 ")


print( " 4. 본인확인은 주민번호 대체수단 사용 ")


print( " 5. 명의도용확인 서비스 이용하여 가입정보 확인 ")


print( " 6. 개인정보는 친구에게도 알려주지 않기 ")


print( " 7. P2P 공유폴더에 개인정보 저장하지 않기 ")


print( " 8. 금융거래는 pc방에서 이용하지 않기 ")


print( " 9 . 출처가 불명확한 자료는 다운로드 금지 ")


print( "10. 개인정보 침해신고 정극 활용하기 ")





# 해킹장면

password = '1'
count = 1

while count <= 5:
    inputPw = input('암호를 입력해라.')

    if inputPw != password:
        if count == 5:
            print(' 횟수를 초과했다. 너의 모든 정보는 해킹된다.~~~~')
            break
        print(' 틀렸다. 다시 입력해라.')
        count = count + 1

    elif inputPw == password:
        print(' 정답이다. 하지만, 나는 원래부터 너의 모든 정보를 해킹 할 생각이었다. ~~~~~.')
        break
    print()

   
    
for num in range(1, 500):
    if num <= 499:
        if num % 3 ==0:
            print(num, ' Microsoft Windows Copyright <c> 2009 Microsift orporation All C:/users ' , end= '')
        else:
            print(num, end=' C:/Users/ wikiHow/title hack03.')
