array = [int(x) for x in input("Введите список чисел: ").split()]
while True:
    try:
        element = int(input('Введите число:'))
        assert element in array
    except ValueError:
        print("Число не из списка")
    except AssertionError:
        print("Пожалуйста введите число из списка")
    else:
        break
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    def some(lst, target):
      count = 0
      for array in lst:
       if array < target:
        count += 1
        return count
    def binary_search(array, element, left, right):
      if left > right:
         return False
      middle = (right + left) // 2
      if array[middle] == element:
         return middle
      elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
      else:
        return binary_search(array, element, middle + 1, right)
print(array)
print(binary_search(array, element, 0, len(array)))
