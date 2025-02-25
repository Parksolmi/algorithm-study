def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]

    for num in array:
        if max_num < num:
            max_num = num
    return 1


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))