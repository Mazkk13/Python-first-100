
##def num_triangle():
##    num = int(input("Enter a number indicating the size of your triangle: "))
##    try:
##        for i in range(1,num+1):
##            for j in range(i):
##                print(j+1, end='')
##            print()
##    except ValueError:
##        print("A number wasn't entered")
##    
##    num = input("Do you want to enter another number?Enter y/n or quit to end: ")
##    if num == 'y':
##        num_triangle()
##    elif num == 'n':
##        pass
##    while num == 'quit':
##        break
##    
##def rev_num_triangle():
##    num_1 = int(input("Enter a number indicating the size of your triangle: "))
##    try:
##        for i in range(1,num_1+1):
##            for j in range(num_1+1-i,1,-1):
##                print(' ', end='')
##            for k in range(1,i+1):
##                print(k, end=' ')
##            print()
##    except ValueError:
##        print("A number wasn't entered")
##    
##    num_1 = input("Do you want to enter another number?Enter y/n or quit to end: ")
##    if num_1 == 'y':
##        rev_num_triangle()
##    elif num_1 == 'n':
##        pass
##    while num_1 == 'quit':
##        break
##
##def times_table():
##    x = int(input("Enter a number: "))
##    try:
##        for i in range(x+1):
##            for j in range(x+1):
##                print('%3s' %(i*j), end=' ')
##            print()
##    except ValueError:
##        print("Oops you didn't enter a number")
##        
##    x = input("Do you want to try another number? Enter y/n or quit to end: ")
##    if x == 'y':
##        times_table()
##    elif x == 'n':
##        pass
##    while x == 'quit':
##        break

##def num_diamond():
##    q = int(input("Enter a number indicating the size of your box: "))
##    try:
##        for i in range(1,q+1):
##            for x in range(q+1-i,1,-1):
##                print(' ', end='')
##            for y in range(1,i+1):
##                print(y, end='')
##            for h in range(1,y):
##                print(y-h, end='')
##            print()
##        for f in range(1,q+1):
##            for j in range(f):
##                print(' ', end='')
##            for k in range(q-f):
##                print(k+1, end='')
##            for p in range(1,k+1):
##                print(q-f-p, end='')
##            print()
##    except ValueError:
##        print("A number wasn't entered")
##
##    q = input("Do you want to try another number? Enter y/n or quit to end: ")
##    if q == 'y':
##        num_diamond()
##    elif q == 'n':
##        pass
##    while q == 'quit':
##        break

##def leap_year(y):
##    ''' enter a year to check if its a leap year'''
##    if y % 4 == 0:
##        if y % 100 == 0:
##            if y % 400 == 0:
##                print(str(y), "is a leap year")
##            else:
##                print(str(y), "isn't a leap year")
##        else:
##            print(str(y), "is a leap year")
##    else:
##        print(str(y), "isn't a leap year")


##def bottom(n):
##    '''enter a number as the grid size'''
##    x = '+ '
##    y = '- '*n
##    print((x+y)*2 + x)
##
##def middle(num):
##    '''enter a number as the grid size'''
##    x = '|'
##    y = '  '*num + ' '
##    for i in range(num):
##        print((x+y)*3)
##    
##def top(numb):
##    '''enter a number as the grid size'''
##    bottom(numb)
##    middle(numb)
##    
##def box(number):        
##    '''enter a number as the grid size'''
##    top(number)
##    top(number)
##    bottom(number)

##def is_prime(n):
##    '''return True or False if a number is prime'''
##    for i in range(2,n):
##        return n%i != 0
##            
##
##def nth_prime(num):
##    '''returns the running sum nth prime numbers until number entered'''
##    y = 3
##    prime = 2
##    if num == 1:
##        return 2
##    while prime < num:
##        y += 2
##        if is_prime(y):
##            prime += 1
##    return y
##
##def nth_prime_list(num):
##    '''returns the running sum nth prime numbers until number entered'''
##    y = 3
##    d = [3]
##    prime = 2
##    if num == 1:
##        return 2
##    while prime < num:
##        y += 2
##        d.append(y)
##        if is_prime(y):
##            prime += 1
##    print(d)

##s, n, d = 6, 9, 20
##
##def nuggets(y):
##    global x
##    x = dict()
##    for i in range(10):
##        for j in range(10):
##            for k in range(10):
##                tot = k*s + j*n + i*d
##                x[tot] = [k,j,i]
##                if y == tot:
##                    break
##            if y == tot:
##                break
##        if y == tot:
##            break
##    print(y, x[y])
##
##nugget(201)

##def adder(arg):
##    '''enter a number and all numbers until that number will be subtotaled.'''
##    if arg == 0:
##        return arg
##    else:
##        return arg + adder(arg-1)
##
##print(adder(4))

##question = True
##names = []
##while question:
##    query = input('Enter your name to add it to the list, del to delete or quit to end: ')
##    if query == 'del':
##        question_2 = input("which name do you wish to delete? ")
##        y = names.index(question_2)
##        names.pop(y)
##        print(names)
##    elif query == 'quit':
##        question = False
##    else:
##        names.append(query)
##        print(names)

##window = True
##while window:
##    comment = input("Enter an adjective about yourself: ")
##    question = input("What is your name? ")
##    print("{} is {}".format(question,comment))
##    question_2 = input("quit or continue ")
##    if question_2 == 'quit':
##        window = False
##    elif question_2 == 'continue':
##        continue

##import sys
##
##if len(sys.argv) > 1:
##    print('hello {}'.format(sys.argv[1]))
##else:
##    print('hello world')

##def num_pyramid(num):
##    for i in range(num+1):
##        for j in range(num+1-i):
##            print(' ',end='')
##        for k in range(i+1):
##            print(k, end='')
##        for l in range(k):
##            print(k-l-1, end='')
##        print()

##names = {'john':1,'mark':2,'jacob':3}
##names_1 = names.items()
##        
##for k,v in names_1:
##    print(k, ':', v)

##def adding(x,y=5):
##    'enter two numbers to add'
##    return x + y
##
##print(adding(5))

##file = '''jack and jill went on a ride. The ride was apocalyptic because jack and
##          jill hated it. They detested it. They loathed it. They absolutely reeked
##          vengeance against it. It was the bane of their existence. So cruel and so
##          malicious and so distasteful and so horrible, absolutely gruelling, problematic
##          and jack and jill just were so angry, horrified, terrified, disaligned from
##          such a putrid experience of a disparaging trip.'''
##                        
##story = file.split()
##
##words = {}
##for i in story:
##    if i in words:
##        words[i] += 1
##    else:
##        words[i] = 1
##
##del story
##
##def last(x):
##    return x[-1]
##
##words = words.items()
##
##sort_words = sorted(words,key=last,reverse=True)
##
##for i in sort_words:
##    print(i[0], ':', i[1])

##def max(*numbers):
##    count = 0
##    for arg in numbers:
##        if arg > count:
##            count = arg
##        elif arg < 0 and count == 0:
##            count = arg
##        else:
##            continue      
##    return count

##def min(*numbers):
##    count = 0
##    for arg in numbers:
##        if arg < count:
##            count = arg
##        else:
##            continue      
##    return count
##
##print(min(-1,-10,-3,6,-8,7))

##names = ['mark','kyle','anthony']
##
##numbers = [20,35,73]
##
##names_2 = []
##count = 0
##for i in names:
##    names_2.append((i,numbers[count]))
##    count += 1
##
##print(names_2)

##names = ['mark','kyle']
##
##numbers = [20,35,73]
##
##names_2 = list(zip(names,numbers))
##
##print(names_2)

##names = ['kylie','hopkins','juliet']
##
##count = 0
##enumerate = []
##for i in names:
##    enumerate.append((count,i))
##    count += 1
##
##print(enumerate)
        
##names = ['kylie','hopkins','juliet']
##
##names_enum = list(enumerate(names))
##
##print(names_enum)

##def absolute(x):
##    '''makes negative numbers positive and leaves positive numbers as they are'''
##    if x < 0:
##        return (0-x)
##    else:
##        return x
##
##print(absolute(-9))
##print(absolute(10))

##print(abs(-9))
##print(abs(10))

##question = input('Enter a calculation: ')
##print(question)

##question = eval(input('Enter a calculation: '))
##print(question)

##story = '''jack hit jill, they had a ball, they loved it,
##                                     they hated it, it was fun, maybe it wasn't,
##                                     maybe it was, who knows?'''
##                                     
##count = 0
##
##for i in story:
##    if i == 't':
##        count += 1
##        
##print(count)

##story = '''jack hit jill, they had a ball, they loved it,
##                                     they hated it, it was fun, maybe it wasn't,
##                                     maybe it was, who knows?'''
##
##print(story.count('t'))

##story = '''jack hit jill, they had a ball, they loved it,
##         they hated it, it was fun, maybe it wasn't,
##         maybe it was, who knows?'''
##
##story = story.split()
##
##count = 0
##for i in story:
##    if i == 'they':
##        count += 1
##
##print(count)

##import string
##
##alphabets = string.ascii_letters
##
##lower_case = string.ascii_lowercase
##
##upper_case = string.ascii_uppercase
##
##print(alphabets)
##print(lower_case)
##print(upper_case)

##import string
##
##alphabets = string.ascii_lowercase
##
##numbers  = range(1,27)
##
##alphabets_num = dict(zip(alphabets,numbers))
##
##print(alphabets_num)

##name = 'jack'
##
##for i in name:
##    print(ord(i))

##import string
##
##letters = string.ascii_lowercase
##
##numbers = range(1,27)
##
##alpha_nums = dict(zip(letters,numbers))
##
##count = 0
##
##word = str(input('Enter a word: '))
##
##for i in word:
##    count += alpha_nums[i]
##
##print(count)

##import string
##
##letters = string.ascii_lowercase
##
##numbers = range(1,27)
##
##alpha_nums = dict(zip(letters,numbers))
##
##count = sum([alpha_nums[i] for i in input('Enter a word: ')])
##
##print(count)

##def num_triangle(x):
##    '''enter a number representing your number triangle's size'''
##    for i in range(x):
##        for j in range(x-i-1):
##            print('   ', end='')
##        for k in range(i+1):
##            print('{:3d}'.format(k+1), end='')
##        print()

##done = True
##while done:
##    question = input('Enter a word to receive letter sums. Press quit to end. ')
##    if question == 'quit':
##        done = False
##    count = 0
##    for i in question:
##        count += ord(i) - 96
##    print(count)

##done = True
##while done:
##    question = input('Enter a word to receive letter sums. Press quit to end. ')
##    if question == 'quit':
##        done = False
##    count = sum([ ord(i) - 96 for i in question])
##    print(count)

##x = [1,4,5,67,89]
##
##count = 0
##for i in x:
##    count += i
##
##print(count)

##x = [1,4,5,67,89]       
##print(sum(x))

##def lowest_denominator(x,y):
##    '''enter two numbers and the highest will divide the lowest'''
##    if x > y:
##        return x/y
##    else:
##        return y/x
##
##print(lowest_denominator(5,6))

##def lowest_denominator(x,y):
##     'enter two numbers and the highest will divide the lowest'
##     return max(x,y) / min(x,y)
##
##print(lowest_denominator(18,3))
##print(lowest_denominator(8,4))
##print(lowest_denominator(5,6))

##numbers = list(range(1,10))
##print(numbers)

##name = 'john'
##for i in range(len(name)):
##    print(i)

##numbers = list(range(1,11))
##for i in range(len(numbers)):
##    print(i)

##def lcd(x,y):
##    'enter two numbers to find the lowest common denominator'
##    for i in range(2,min(x,y)+1):
##        if max(x,y)%i == 0 and min(x,y)%i == 0:
##            print(i)
##            break
##
##lcd(18,3)
##lcd(24,8)

##name = 'john'
##print(name[3])

##names, numbers = ['john','mark','jack'],[1,2,4]
##
##print(names)
##print(numbers)

##names = [1,2,4], ['john','mark','jack']
##print(names)

##x = 'abcdefghij'
##y = ''
##for i in x:
##    if len(y) < 4:
##        y += i
##    else:
##        break
##    print(y)

##names = 'jackfredjacksamsamdadfreddad'
##count = 0
##for i in range(len(names)):
##    if names[i:i+4] == 'fred':
##        count += 1
##print(count)

##names = 'jackjilljackgillgillianfredfrederickderekisabella'
##print(names.find('jack',1))

##names = 'jackjilljackgillgillianfredfrederickderekisabella'
##print(names[names.find('jack',1)])

##names = 'jackjilljackgillgillianfredfrederickderekisabella'
##place,count = 0,0
##while names.find('jack',place) >= 0:
##    place = names.find('jack', place) + 1
##    count += 1
##print(count)

##def sub_string(word,string):
##    '''enter a sub-string word and the string which you want to count the
##    sub-string from'''
##    count, place = 0,0
##    while string.find(word,place) >= 0:
##        place = string.find(word,place) + 1
##        count += 1
##    print('{} is repeated {} times in {}'.format(word,count,string))
##
##sub_string('jack','jackjilljackgillgillianfredfrederickderekisabella')
##sub_string('fred','jackjilljackgillgillianfredfrederickderekisabella')
##sub_string('jill','jackjilljackgillgillianfredfrederickderekisabella')
##sub_string('gillian','jackjilljackgillgillianfredfrederickderekisabella')

##def sub_string(word,string):
##    '''enter a sub-string word and the string which you want to count the
##    sub-string from'''
##    count, place = 0,0
##    while string.find(word,place) >= 0:
##        place = string.find(word,place) + 1
##        count += 1
##    print('{} is repeated {} times'.format(word,count))
##
##story = '''jack and jill went on a ride. The ride was apocalyptic because jack and
##      jill hated it. They detested it. They loathed it. They absolutely reeked
##      vengeance against it. It was the bane of their existence. So cruel and so
##      malicious and so distasteful and so horrible, absolutely gruelling, problematic
##      and jack and jill just were so angry, horrified, terrified, disaligned from
##      such a putrid experience of a disparaging trip.'''
##
##sub_string('They', story)
##sub_string('jack', story)
##sub_string('and', story)
##sub_string('jill', story)

##names = 'jackjilljackgillgillianfredfrederickderekisabella'
##print(names.count('jack'))
##print(names.count('jill'))
##print(names.count('isabella'))
##print(names.count('gill'))

##names = 'bobobmamamjackjilljohnjosephjack'
##print(names.count('bob'))

##def square(number):
##    '''enter a number and acquire its square'''
##    return number**2
##
##print(square(3))
##print(square(4))
##print(square(5))

##def pow(number,power=2):
##    '''enter a number and a power to return the number to that power. Powers will
##    be defaulted to 2.'''
##    return number**power
##
##print(pow(3))
##print(pow(4,3))
##print(pow(5,4))

##def pow(*numbers):
##    '''enter a number to return the number to that power. Powers will be defaulted to
##    2.'''
##    count = 0
##    new = 1
##    for i in numbers:
##        if count < len(numbers):
##            new *= i
##            count += 1
##    return new
##        
##print(pow(5,5,5,5))
##print(pow(4,4,4))
##print(pow(3,3,3))

##def root(number):
##    '''enter a number to find its square root'''
##    return number**(1/2)
##
##print(root(4))
##print(root(25))
##print(root(9))
##print(root(65))

##def root(number, root=2):
##    '''enter a number to find its square root'''
##    return int(number**(1/root))
##            
##print(root(4))
##print(root(64,3))
##print(root(81))
##print(root(729,3))

##def root(*numbers):
##    count = 0
##    start = 1
##    for i in numbers:
##        if count <= len(numbers):
##            start *= i
##            count += 1
##    return start
##
##print(root(64,1/2,1/2,1/2,1/2,1/2))
##print(root(16,1/2,1/2,1/2))

##def divisor(num_1, num_2):
##  '''enter two numbers to check whether the second is a multiple of the first'''
##  return num_1%num_2 == 0
##
##print(divisor(12,4))
##print(divisor(14,7))
##print(divisor(9,2))

##def factor(number):
##    '''returns all factors of our number'''
##    d = list()
##    for i in range(2,number+1):
##        if number%i == 0:
##            d.append(i)
##    return d
##
##print(factor(27))
##print(factor(4))
##print(factor(30))

##def factor(number):
##    '''returns all factors of our number'''
##    d = [i for i in range(2,number+1) if number%i == 0]
##    return d
##
##print(factor(27))
##print(factor(4))
##print(factor(30))

##def factor(number):
##    '''returns all factors of our number'''
##    d = [i for i in range(number+1,0,-1) if number%i == 0]
##    return d
##
##def gcd(x,y):
##    '''enter 2 numbers and find there greatest common divisor'''
##    for i in factor(max(x,y)):
##        if i in factor(min(x,y)):
##            print('{} is the greatest common divisor of {} and {}'.format(i,max(x,y),min(x,y)))
##            break
##                         
##print(factor(30))
##print(factor(4))
##gcd(30,4)

##def factor(number):
##    '''returns all factors of our number'''
##    d = [i for i in range(number+1,1,-1) if number%i == 0]
##    return d
##
##def gcd(x,y):
##    '''enter 2 numbers and find there greatest common divisor'''
##    l = [print('{} is the greatest common divisor of {} and {}'.format(i,max(x,y),min(x,y))) for i in factor(max(x,y)) if i in factor(min(x,y))]
##    return l
##
##print(factor(30))
##print(factor(4))
##gcd(30,4)

##def gcd(x,y):
##    '''enter 2 numbers and find their greatest common divisor'''
##    common = min(x,y)
##    while x%common != 0 or y%common != 0:
##        common -= 1
##    return common
##
##print(gcd(30,4))
##print(gcd(15,20))

##def multiply(x,y):
##    'multiplies 2 values together'
##    return round(x*y,2)
##
##print(multiply(14.70,15.60))
##print(multiply(15.66,17.31))

        
