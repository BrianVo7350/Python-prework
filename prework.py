#Question 1

def hello_user(user_name):
    print(f'hello {user_name}')

hello_user("Brian")

#Question 2

def first_odds(num):
    for i in range(100):
        if i % 2!= 0:
            print(i)

first_odds(0)

#Question 3 

def max_num_in_list(a_list):
    max = -9999
    for i in a_list:
        if i > max:
            max = i

        return max
a_list = [50,30,40,20]

print(max_num_in_list(a_list))


#Question 4

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0): 
        return True
    if (a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2024))


#Question 5

def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        if a_list[i+1] - a_list[i] != 1:
            return False
        return True
print(is_consecutive([1,3,6,9]))
