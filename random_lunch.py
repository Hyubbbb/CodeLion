import random
import time

# for x in range(30):
#     print(random.choice(["된장찌개","제육볶음", "치킨", "떡볶이", "라면"]))

while True:
    break
    print(random.choice(["된장찌개","제육볶음", "치킨", "떡볶이", "라면"]))
    # break
    time.sleep(1)


# lunch <= "떡볶이" 퇴화 !!


## dictionary
information = {'취미': '기타치기', '고향':'광명', '좋아하는 음식':'햄버거'}
print(information)
print(information.get("취미"))

imformation2 = {'특기':"피아노", '사는 곳':"서울"}
print(imformation2.get('특기'))
print(imformation2.get('사는 곳'))

information["특기"] = "피아노"
print(len(information))
information.clear()
print(information)


## list
foods = ['된장찌개', '피자', '제육볶음']
print(foods[1])
# print(foods[3])
foods.append("김밥")
del foods[1] # 이름이 아니라 인덱스로 적는구나 (<-> 딕셔너리)

print(foods)

## set
foods = ['된장찌개', '피자', '제육볶음','된장찌개']
foods_set = set(foods)
print(foods)
print(foods_set)

menu1 = set(['된장찌개', '피자', '제육볶음'])
menu2 = set(['된장찌개', '떡국', '김밥'])
menu3 = menu1 | menu2 # 합집합
menu3 = menu1 & menu2 # 교집합
menu3 = menu1 - menu2 # 차집합
print(menu3)


## 만약에

food = random.choice(["된장찌개", "피자", "제육볶음"])

if (food=="제육볶음"):
    print("곱빼기 주세요")
else:
    print("그냥 주세요")
print("end")