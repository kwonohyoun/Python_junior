# 1~10 => 데이터
nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    print(n, end='_' if n != 5 else '\n')
print("END")

for num in range(1,6):
    print('*' * num)
for num in range(6,0,-1):
    print('*' * num)