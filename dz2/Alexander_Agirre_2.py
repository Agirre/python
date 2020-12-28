quantity = int(input("Введите количество элементов: "))
i = 0
c = 0
nums = []
while i < quantity:
    elem = int(input("Введите первый элемент: "))
    nums.append(elem)
    i += 1
for quantity in range(quantity // 2):
    nums[c], nums[c+1] = nums[c+1], nums[c]
    c += 2
print(nums)
