#Question 1
# def hello_name(user_name):
#     print("Hello " + user_name)

# user_name = input("Enter your username: ")
# hello_name(user_name)

#Question 2
# numbers = 0

# while numbers != 100:
#     if numbers % 2 == 1:
#         print(numbers)
#     numbers += 1

#Question 3
# def max_num_in_list(a_list):
#     print(max(a_list))


# a_list = [10, 2, 4, 78, 12]

# max_num_in_list(a_list)

#Question 4
# def is_leap_year(a_year):

#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# year = int(input("Enter a year: "))
# print(is_leap_year(year))

# Question 5
# def is_consecutive(a_list):
#     nums = ""
#     first_num = a_list[0]
#     counter = 0
#     str_list = ""

#     while counter < len(a_list):
#         nums += str(first_num)
#         first_num += 1
#         counter += 1

#     for i in a_list:
#         str_list += str(i)

#     sorted_list = a_list[:]
#     sorted_list.sort()

#     if  sorted_list == a_list:
#         if str_list in nums:
#             return True
#         else:
#             return False
#     else:
#         return False
        


# a_list = [10, 11, 12, 13]
# print(is_consecutive(a_list))