# 평균을 구하는 함수

def f_sum(data):
    result = 0
    for i in data:
        result += i
    return result
    
# 합계를 구하는 함수

def f_avg(data):
    ans = sum(data) / len(data)
    return(ans)


# 오름차순으로 정렬해주는 함수
def f_sort(data):
    data.sort(reverse=False)
    return(data)

(f_sort([1,5,6,4]))
   
# 내림차순으로 정렬해주는 함수
def f_sort(data):
    data.sort(reverse=True)
    return(data)

(f_sort([1,5,6,4]))

print('뭐가 바뀌었는지 맞춰보시오!')