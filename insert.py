numbers = [1,2,3,45,2,68]
numbers.sort()# sort the numbers in ascending order 
numbers.reverse()# to get it in decending order 
print(numbers) 

number2 = numbers.copy # copy the list of the numbers 







print(numbers.index(2))







# Output: 1
print(45 in numbers) # True check and give boolean value 
numbers.insert(3,78) #insert 78 at index 3
print(numbers)
numbers.remove(68)
print(numbers) 
numbers.count(2)# count the number of 2 in the list
numbers.clear() # clear the list
# numbers.pop() # pop the last element





num = [ 1,2,2, 67, 2,5,7,9,9,3]
for duplicate in num:
    if num.count (duplicate) > 1:
        num.remove(duplicate)
        num.sort()
        print(num) # [1, 5, 7, 9, 3]