import unittest

def counting_sort(arr, max_value):
    count_array = [0] * (max_value + 1)

    for num in arr:
        count_array[num] += 1

    sorted_list = []
    for value in range(len(count_array)):
        sorted_list.extend([value] * count_array[value])

    return sorted_list

def max_hamsters(S, C, hamsters):
    def is_enough(count):
        food_needs = []

        for i in range(C):
            treba_food = hamsters[i][0] + hamsters[i][1] * (count - 1)
            food_needs.append(treba_food)

        if len(food_needs) < count:
            return False

        sorted_food_needs = counting_sort(food_needs, max(food_needs))
        treba_food = sum(sorted_food_needs[:count])
        return treba_food <= S

    left = 0
    right = C
    while left < right:
        mid = (left + right + 1) // 2
        if is_enough(mid):
            left = mid
        else:
            right = mid - 1
    return left

print(max_hamsters(7, 3, [[1, 2], [2, 2], [3, 1]]))  #2


