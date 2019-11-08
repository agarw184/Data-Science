import sys
hw8 =__import__("hw8-1")


if __name__ == '__main__':
    dictionary_final = hw8.getDict(sys.argv[1])
    dictionary_new_final = sorted(dictionary_final.items(), key=lambda x: x[1], reverse=True)
    print (dictionary_new_final[0:10])
