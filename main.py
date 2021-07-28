#getting the number
number = int(input('whats the number? '))

#variables
numbers_to_input_number = []
numbers = []
can_be = []
num1 = 1
num2 = None
num3 = -1
is_prime = None

#main program
class prime_number():
        while num1 < number:
                numbers_to_input_number.append(num1)
                num1 += 1
        for num in numbers_to_input_number:
                num2 = number / num
                numbers.append(num2)
        for num in numbers:
                for string in str(num):
                        num3 += 1
                num = str(num)
                try:
                        if num[num3] == '0':
                                can_be.append(num)
                except:
                        pass
                num3 = -1
        
#running the program
prime_number()

#one more thing
def check():
        if len(can_be) > 1:
                print('this number is not a prime number')
        else:
                print('this number is a prime number')

check()

#quiting the code
quit()