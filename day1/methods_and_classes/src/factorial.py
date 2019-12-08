
def factorial(value):
   #if type(value) = int:

   try:
        if value < 0:
            return False
        elif value == 0:
            return 1
        else:
            result = 1
            for i in range(1, value + 1):
                result = result*i
            return result;
   except BaseException as err:
       print(err)
       return False

#if __name__ == "__main__":
print(factorial(4.0))


#result=square(2)
#print(result)
