comment = input("문자열을 입력하세요. :")
i = 0
c = ""
length = len(comment) - 1

while length > -1:
    c += comment[length]
    length -= 1



print(c)
