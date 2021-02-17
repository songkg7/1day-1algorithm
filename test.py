numbers = [1, 2, 3, 4, 5, 5]

# def solution(numbers):

#     for i in numbers:
#         for j in numbers[i:]: # i 부터 끝까지
#             print(j)

# print(solution(numbers))

print(max(numbers))
print(min(numbers))
numbers.remove(max(numbers))

print(numbers)