# 문제풀이 : 시간복잡도 O(N)
def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]

    for num in array:
        if max_num < num:
            max_num = num
    return max_num


# 두 번째 방법 : 시간복잡도 O(N^2)
def find_max_num2(array):
    for num in array:
        is_max_num = True
        for compared_num in array:
            if num < compared_num:
                is_max_num = False
        if is_max_num:
            return num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num2([6, 9, 2, 7, 1888]))