input = "abadabac"

# 시간복잡도 : O(N)
def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    occurrence_array = find_alphabet_occurrence_array(string)

    #1개만 나오는 알파벳 구하기
    not_repeating_char_array = []
    for index in range(len(occurrence_array)):
        if occurrence_array[index] == 1:
            not_repeating_char_array.append(chr(index+ord('a')))

    #먼저 나오는 알파벳 구하기
    for char in string:
        if char in not_repeating_char_array:
            return char

    return "_"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        alphabet_occurrence_array[ord(char) - ord('a')] += 1
    return alphabet_occurrence_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
