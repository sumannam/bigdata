# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# N 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

def sumMultiples(end_num, num1, num2):
    result = 0
    for n in range(1, end_num):
        if n % num1 == 0 or n % num2 == 0: 
            result += n
    return result

end_num = int(input("자연수의 끝을 입력하시오: "))
n1 = int(input("첫 번째 숫자를 입력하시오: "))
n2 = int(input("두 번째 숫자를 입력하시오: "))

sum = sumMultiples(end_num, n1, n2)
print(sum)