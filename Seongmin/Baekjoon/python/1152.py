string = input("")
if string == " ":  # 예외처리 문장 모두가 공백인 케이스
    print(0)
else:
    words = string.split(" ")  # 공백으로 구분
    while '' in words:  # 문장 양쪽에 공백이 있을 경우
        words.remove('')
print(len(words))



##
##string = input("")
##words = string.split(" ")
##words = [w for w in words if w != ""] # 공백이 아닌 경우에만 words에 넣음 # 리스트 조건제시법사용 (공부 좀 더 할것)
##print(len(words)) 
##
