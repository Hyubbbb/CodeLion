from googletrans import Translator

translator = Translator()


sentence = input("번역할 문장을 입력해주세요 : ")
detination = input("번역하고 싶은 언어를 선택해주세요 : ")

# print(detected.lang)

detected = translator.detect(sentence)
result = translator.translate(sentence,detination) # src는 선택 옵션 (언어감지 기능으로 대체 가능)


print("======출 력 결 과=====")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("====================")