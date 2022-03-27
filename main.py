from rich import print
from word import randWord, findWord, compare


anwser = randWord()
print(anwser)
# 记次用的
Count = 0
# 输入六次
for i in range(6):
    userInput = input("请输入单词:")
    # 检测长度
    if len(userInput) != 5 or findWord(userInput) is False:
        print("请您输入5个字母的英语单词")
    else:
        print(compare(anwser, userInput))
print("垃圾，这都猜不出来，这说明什么，这说明你就是个大混子")
