##def box_rep():
##    '''enter a number and acquire a box of 1 to the number'''
##    try:
##        number = int(input("Enter a number: "))
##        for i in range(number):
##            for j in range(number):
##                print('{:3d}'.format(j+1), end='')
##            print()
##    except ValueError:
##        question = input("Continue, y/n? ")
##        if question == 'y':
##            box_rep()
##        elif question == 'n':
##            pass
##        
##    question = input("Continue, y/n? ")
##    if question == 'y':
##        box_rep()
##    elif question == 'n':
##        pass
##
##def box_asc():
##    '''enter a number to generate a box of that number'''
##    try:
##        num = int(input("Enter a number: "))
##        k = num
##        count = 0
##        for i in range(num):
##            for j in range(count, k):
##                print('{:4d}'.format(j+1), end='')
##            k += num
##            count += num
##            print()
##    except ValueError:
##        q = input("Continue, y/n? ")
##        if q == 'y':
##            box_asc()
##        elif q == 'n':
##            pass
##        
##    q = input("Continue, y/n? ")
##    if q == 'y':
##        box_asc()
##    elif q == 'n':
##        pass
##
##def box_number():
##    '''enter a number and acclaim a box of the repeated number'''
##    try:
##        num_1 = int(input("Enter a number: "))
##        for i in range(num_1):
##            for j in range(num_1):
##                print('{:4d}'.format(num_1), end='')
##            print()
##    except ValueError:
##        q1 = input("Continue, y/n? ")
##        if q1 == 'y':
##            box_number()
##        elif q1 == 'n':
##            pass
##        
##    q1 = input("Continue, y/n? ")
##    if q1 == 'y':
##        box_number()
##    elif q1 == 'n':
##        pass

##def tilted_square():
##    try:
##        num = int(input("Enter a number: "))
##        for i in range(num):
##            for j in range(num-i-1):
##                print('  ', end='')
##            for p in range(1):
##                print('*', end='')
##            for k in range(i):
##                print(' ', end='')
##            for x in range(i):
##                print('  ', end='')
##            for y in range(2,i+1):
##                if i < 2:
##                    continue
##                else:
##                    print(' ', end='')
##            for l in range(1):
##                if i == 0:
##                    continue
##                else:
##                    print('*', end='')
##            print()
##        for i_1 in range(num-1):
##            for j_1 in range(i_1+1):
##                print('  ', end='')
##            for k_1 in range(1):
##                print('*', end='')
##            for p_1 in range(num-i_1):
##                if i_1 < num-2:
##                    print(' ', end='')
##                else:
##                    continue
##            for q_1 in range(2,num-i_1):
##                if i_1 < num-3:
##                    print(' ', end='')
##                else:
##                    continue
##            for w_1 in range(2,num-i_1-1):
##                if i_1 < num-3:
##                    print(' ', end='')
##                else:
##                    continue
##            for s_1 in range(3,num-i_1-1):
##                if i_1 <= num-5:
##                    print(' ', end='')
##                else:
##                    continue
##            for t_1 in range(1):
##                if i_1 != num-2:
##                    print('*', end='')
##                else:
##                    continue
##            print()
##    except ValueError:
##        print("Oops, a number wasn't entered.")
##
##    num = input("Try again, y/n? ")
##    if num == 'y':
##        tilted_square()
##    elif num == 'n':
##        pass

##def cool_diamond():
##    try:
##        num = int(input("Enter a number: "))
##        for i in range(num):
##            for j in range(num-i-1):
##                print('  ', end='')
##            for p in range(1):
##                if i == 0 or i == num-1:
##                    print('*', end='')
##                else:
##                    print('/', end='')
##            for k in range(i):
##                print(' ', end='')
##            for x in range(i):
##                print('  ', end='')
##            for y in range(2,i+1):
##                if i < 2:
##                    continue
##                else:
##                    print(' ', end='')
##            for l in range(1):
##                if i == 0:
##                    continue
##                elif i == num-1:
##                    print('*', end='')
##                else:
##                    print('\\', end='')
##            print()
##        for i_1 in range(num-1):
##            for j_1 in range(i_1+1):
##                print('  ', end='')
##            for k_1 in range(1):
##                if i_1 == num-2:
##                    print('*', end='')
##                else:
##                    print('\\', end='')
##            for p_1 in range(num-i_1):
##                if i_1 < num-2:
##                    print(' ', end='')
##                else:
##                    continue
##            for q_1 in range(2,num-i_1):
##                if i_1 < num-3:
##                    print(' ', end='')
##                else:
##                    continue
##            for w_1 in range(2,num-i_1-1):
##                if i_1 < num-3:
##                    print(' ', end='')
##                else:
##                    continue
##            for s_1 in range(3,num-i_1-1):
##                if i_1 <= num-5:
##                    print(' ', end='')
##                else:
##                    continue
##            for t_1 in range(1):
##                if i_1 != num-2:
##                    print('/', end='')
##                else:
##                    continue
##            print()
##    except ValueError:
##        print("Oops, a number wasn't entered.")
##
##    num = input("Try again, y/n? ")
##    if num == 'y':
##        cool_diamond()
##    elif num == 'n':
##        pass    

##def polygon():
##    try:
##        numb = int(input("Enter a number: "))
##        for i in range(numb):
##            for j in range(numb-i):
##                print('  ', end='')
##            for k in range(1):
##                print('*', end='')
##            for l in range(i+1):
##                print('    ', end='')
##            for g in range(1):
##                print('*', end='')
##            print()
##        for i_1 in range(1):
##            print()
##        for i_2 in range(numb):
##            for j_1 in range(i_2+1):
##                print('  ', end='')
##            for k_1 in range(1):
##                print('*', end='')
##            for l_1 in range(numb-i_2):
##                print('    ', end='')
##            for g_1 in range(1):
##                print('*', end='')
##            print()
##    except ValueError:
##        print("A number wasn't entered.")
##
##    numb = input("Try again, y/n? ")
##    if numb == 'y':
##        polygon()
##    elif numb == 'n':
##        pass


##def star():
##    num = int(input("Enter a number: "))
##    for i in range(num):
##        for j in range(i):
##            print('  ', end='')
##        for k in range(i+1):
##            print(k+1, end='')
##        for p in range(num-i-1):
##            print('    ', end='')
##        for q in range(i+1):
##            print(q+1, end='')
##        for l in range(k):
##            print(k-l, end='')
##        for s in range(num-i-1):
##            print('    ', end='')
##        for t in range(i+1):
##            print(k-t+1, end='')
##        print()
##    for i_1 in range(num-1):
##        for j_1 in range(k):
##            print('  ',end='')
##        for k_1 in range(i_1+1):
##            print(' ',end='')
##        for p_1 in range(num-i_1):
##            print(p_1+1, end='')
##        for l_1 in range(i_1):
##            print(num+l_1-k_1+1, end='')
##        for q_1 in range(num-i_1-1):
##            print(q_1+1, end='')
##        for s_1 in range(num-i_1-2,0,-1):
##            print(s_1, end='')
##        for t_1 in range(i_1):
##            print(num-t_1, end='')
##        for y_1 in range(num-i_1,0,-1):
##            print(y_1, end='')
##        print()
##    for i_2 in range(num-1):
##        for j_2 in range(j_1-i_2):
##            print('  ', end='')
##        for p_2 in range(k_1+2):
##            print(' ', end='')
##        for k_2 in range(num-i_2):
##            print(k_2+1, end='')
##        for l_2 in range(i_2+1):
##            print('   ', end='')
##        for s_2 in range(i_2):
##            print('   ', end='')
##        for t_2 in range(num-i_2):
##            print(num-t_2-i_2, end='')
##        print()
    
##    num = input("Try again? y/n ")
##    if num == 'y':
##        star()
##    elif num == 'n':
##        pass

##def crown():
##    num = int(input("Enter a number: "))
##    for i in range(num):
##        for j in range(i):
##            print('  ', end='')
##        for k in range(i+1):
##            print(k+1, end='')
##        for p in range(num-i-1):
##            print('    ', end='')
##        for q in range(i+1):
##            print(q+1, end='')
##        for l in range(k):
##            print(k-l, end='')
##        for s in range(num-i-1):
##            print('    ', end='')
##        for t in range(i+1):
##            print(k-t+1, end='')
##        print()
##    for i_1 in range(num-1):
##        for j_1 in range(k):
##            print('  ',end='')
##        for k_1 in range(i_1+1):
##            print(' ',end='')
##        for p_1 in range(num-i_1):
##            print(p_1+1, end='')
##        for l_1 in range(i_1):
##            print(num+l_1-k_1+1, end='')
##        for q_1 in range(num-i_1-1):
##            print(q_1+1, end='')
##        for s_1 in range(num-i_1-2,0,-1):
##            print(s_1, end='')
##        for t_1 in range(i_1):
##            print(num-t_1, end='')
##        for y_1 in range(num-i_1,0,-1):
##            print(y_1, end='')
##        print()
##
##    num = input("Try again? y/n ")
##    if num == 'y':
##        crown()
##    elif num == 'n':
##        pass






