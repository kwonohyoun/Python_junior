# 리스트 안에 모든 원소를 더한 합계 출력
datas = ['1', '4', '9']

for idx, d in enumerate(datas):
    datas[idx] = int(d)

print(datas)

# 이를 편하게 실행해주는 내장함수: map()
datas = list(map(int, datas))
print(datas)

datas = list(map(float, datas))
print(datas)

# 원소에 *100을 한 결과값을 리스트에 저장하기
def multiValue(x):
    return x * 100

datas = list(map(multiValue(), datas))
print(datas)

datas = list(map(lambda x: x*100, datas)) # 람다식을 활용하여 간단하게 함수 사용
print(datas)

print((lambda : "반갑습니다.")())