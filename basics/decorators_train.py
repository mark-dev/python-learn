import time

def type_check(correct_type):
    def check_generator(old_function):
        def new_function(arg):
            if isinstance(arg,correct_type):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check_generator

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])


def timed(method):
    def print_timestamps(*positional,**kvargs):
        before = time.monotonic()
        val  = method(*positional,**kvargs)
        after = time.monotonic()
        print("Method takes {} ".format(str(after-before)))
        return val
    return print_timestamps


@timed
def my_business_logic_func(**kvargs):
    print("business logic func start {}".format(kvargs))
    time.sleep(2)
    print("business logic func end")
    return 'abb'



ss = my_business_logic_func(next='zalupa')
print(ss)