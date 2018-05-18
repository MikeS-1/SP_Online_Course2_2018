
class Generator:

    def sum_of_integers(self, int_list):
        my_sum = 0
        for num in int_list:
            my_sum += num
            yield my_sum

    def doubler(self, start, stop):
        if start < 1:
            start += 1
        cur_value = start
        for num in range(start, stop):
            yield cur_value
            cur_value *= 2

    def sum_series(n,x=0,y=1):
        """return the nth value of fibonacci (x=0,y=1) or lucas (x=2,y=1) series"""
        if x not in (0,2) or y != 1:
            print("function not found for x=" + str(x) + " and y=" + str(y))
        else:
            if n == 0:
                return x
            elif n == 1:
                return y
            else:
                return sum_series(n-2,x,y) + sum_series(n-1,x,y)
    
    def fibonacci(n):
        """return the nth value in the fibonacci series fib(n) = fib(n-2) + fib(n-1)"""
        if n >= 2:
            return sum_series(n)
        else:
            return n

    def prime_numbers(self):
        pass

