def findSum(input_array, s):
    n = len(input_array)
    for i in range(0, n):
        for j in range(i + 1, n):
            sum = input_array[i] + input_array[j]
            if (sum == s):
                # print(input_array[i], "*", input_array[j], "=", sum, "<--- true")
                return "true"
            # else:
            #     print(input_array[i], "*", input_array[j], "=", sum, " <--- false")
    return "false"

input_array = [1, 2, 4, 7, 11, 15]
s = 15
print(findSum(input_array, s))
