from rich import print
from word import randWord, findWord, compare

def wordle():
    answer = randWord()
    for i in range(6):
        text = input("输入长度为 5 的单词:")
        while len(text) != 5 or findWord(text) is False:
            text = input("输入长度为 5 的单词:")
        print(compare(answer,text))
        if answer == text:
            break
    else:
        print("已经猜了 6 次,没有机会了")
        print("答案是",answer)
        return False
    print("猜对了!")
    return True

if __name__ == "__main__":
    wordle()
