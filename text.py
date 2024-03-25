numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("Original List:", numbers)

numbers.append(8)
print("After appending 8:", numbers)

numbers.insert(2, 7)
print("After inserting 7 at index 2:", numbers)

numbers.remove(5)
print("After removing the first occurrence of 5:", numbers)

del numbers[4]
print("After deleting element at index 4:", numbers)

print("Element at index 3:", numbers[3])

sliced_list = numbers[2:6]
print("Sliced list from index 2 to 5:", sliced_list)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

print("Length of the list:", len(numbers))

count_of_1 = numbers.count(1)
print("Count of 1 in the list:", count_of_1)

numbers.clear()
print("List after clearing:", numbers)
