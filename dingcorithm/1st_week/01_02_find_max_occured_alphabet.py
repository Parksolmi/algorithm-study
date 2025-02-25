# 문제풀이 : 시간복잡도 O(N)
def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char)-ord('a')] += 1

    max_occurrence_alphabet = alphabet_occurrence_array[0]
    for alphabet in alphabet_occurrence_array:
        if max_occurrence_alphabet < alphabet:
            max_occurrence_alphabet = alphabet
    max_index = alphabet_occurrence_array.index(max_occurrence_alphabet)
    return chr(max_index+97)

# 정답1 : 시간복잡도 O(N)
def find_max_occurred_alphabet1(string):
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0

        for char in string:
            if char == alphabet:
                occurrence += 1

        if max_occurrence < occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    return max_alphabet

# 정답2 : 시간복잡도 O(N)
def find_max_occurred_alphabet2(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char)-ord('a')] += 1

    max_occurrence = 0
    max_alphabet = 'a'
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > max_occurrence:
            max_occurrence = alphabet_occurrence_array[index]
            max_alphabet = chr(index+ord('a'))

    return max_alphabet


result = find_max_occurred_alphabet2
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char)-ord('a')] += 1
    return alphabet_occurrence_array


print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("hello my name is dingcodingco"))
print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("we love algorithm"))
print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best youtube"))