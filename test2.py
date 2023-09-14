# 평균을 구하는 함수

def f_avg(data):
    ans = sum(data) / len(data)
    return(ans)
    
# 합계를 구하는 함수

def f_sum(data):
    result = 0
    for i in data:
        result += i
    return result

# 오름차순으로 정렬해주는 함수

# 내림차순으로 정렬해주는 함수

def f_desc(data):
    

    for i in range(len(data)):
        max_number = i

        for j in range(len(data)):
            if data[j] > data[max_number]:
                max_number = j

        data[i], data[max_number] = data[max_number], data[i]

f_desc([1, 2, 3, 4])