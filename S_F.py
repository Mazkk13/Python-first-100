def episode(x):
    '''x marks the episode of the channel, e.g. if 1 is pressed,
    the user will learn about the contents of ep.1. If more is pressed in a second prompt you can loop through all ep's '''
    window = True
    while window:
        if x == 1:
            print('''
                     This episode is about strings. In python strings are typically lines of text, or words
                     example: assigning a string value to a variable y.
                     
                     y = 'name'
                     print(y)
                     
                     In this example, y is assigned the value 'name' and to show y on the screen,
                     the print("value") function does the job.
                     To check if 'name' is a string, the type() function plays this role. Simply wrap
                     y with the string function type() to check whether y is a string e.g. type(y)''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(str)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 2:
            print('''
                     This episode is about integers. In python, an integer is not a string, but a number

                     y = 5
                     print(y)
                     
                     In this example, y is no longer a string but an integer. Distinguishing between a string
                     and an integer can be quite an ordeal. However, a key difference is that a string is normally
                     placed between two embedded clauses, like in the example of 'name'.
                     Note that if there isn't any embedded clauses around the assigned variable, and if the variable isn't
                     an integer value, python will recognize it.
                     Conversely, an integer can be a string, if it is placed in between double apostrophes such as "1".
                     This is not a integer but a string because of the additive clauses. To change an integer to a string,
                     wrap the integer variable with the function str() such that python changes the integer into a string value.
                     The reverse is achieved by wrapping a string integer with the int(), changing the string integer into an integer value.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(int)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 3:
            print('''
                     This episode is about floats. In python, a float is like an integer with additional decimals

                     example: assigning a float to variable y
                              y = 5
                              z = float(y)
                              print(z)
                     
                     For this instance, I have assigned an integer value 5 into y, then changed the integer into
                     a float (or a rational number) using the built-in float() function. This value is reassigned to the
                     variable z and to show z on the screen, I used the print() function.
                     Floats and integers are very alike, but floats are more suitable for real world applications
                     like calculating or printing monetary/ currency values which (procedurally fixed at 2 decimal places).
                     For example, 23.56 is a float, but it isn't an integer. So it is recommended to use a float in this scenario''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(float)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = input("Enter another episode you wish to learn about: ")
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 4:
            print('''
                     To create your own functions in python, the keyword def is used followed by colons.
                     e.g. creating a simple addition function:

                     def add(x,y):
                        return x+y
                     print(add(2,3))
                     answer will be 5.
                    
                     When writing a function in Python, the keyword return is used to create a new variable
                     which takes in several inputs and produces a new variable. Note that return, unlike print,
                     doesn't show your result to the screen. Don't be discouraged because this doesn't neccessarily
                     mean that your function is not working, only that the return keyword hasn't printed it onto the screen.
                     If you require a result on the screen, you could try and attach a print statement into your function like follows:

                     def add(x,y):
                        print(x+y)
                        
                     However, don't always be tempted to embed a print into your function because print does not create a new
                     variable, it only shows the result obtained onto your screen. The best practice to follow would be
                     creating a new variable through the return keyword in your function and then printing afterward using the print option.
                     Functions can also take in no variables or default variables accordingly.
                     example:-
                    
                     x = 2
                     y = 3
                     def add():
                        return x + y
                     print(add())

                     In this example, the variables x and y were pre-assigned the values 2 and 3, so the function
                     didn't require extra information to add them together. Assigning default values to a function can be
                     accomplished as follows:
                    
                     def add(x=1,y):
                        return x + y
                     print(add(y))

                     Here the parameter x is defaulted as 1, so entering only the parameter y into the function
                     will not cause an error of too few arguments because x is defaulted as 1. This doesn't mean that
                     x cannot be altered, only that it is fixed at 1 if the user decides to enter only one argument where
                     the function calls for 2. Note that Python raises an error if there is too few arguments entered, when
                     a function calls for more. Therefore, it is good practice create default arguments to increase usability
                     of a function.

                     Remember that python has also created a library of built-in functions, meaning that simple arithmetic
                     like multiplication, addition, subtraction, etc. has been accounted for in python's string or integer libraries.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 5:
            print('''
                     THE FOR LOOP IN PYTHON
                     the 'for' loop is used in python when you have a string or a list of numbers, and you want to
                     transform each of the numbers (or letters if you enter a string) in a specified manner for loops
                     are mostly used in lists of objects, whereby python either stores a list of names or numbers
                     into the list as independent objects. Each of these items in your list is known to python as
                     iterables, where the for loop works it's magic. To find out more about lists a supplemental
                     episode is at your command.

                     Now for examples of where one can identify with a for loop.

                     example:-
                     for x in 'letter':
                         print(x)

                     In this example, python will iterate/go-through each letter in the word 'letter', printing
                     each letter once on a separate line. If you want it so that python prints the word 'letter'
                     you can either/or:
                             1)
                             x = 'letter'
                             print(x)
                             2)
                             for x in 'letter':
                                 print(x, end='')
                                 
                    Through these specific examples, I have utilized the print function to print each letter
                    of the word letter ending without spaces on the same line. If unspecified, the print function
                    is defaulted to print each letter in the word 'letter' on a separate line. Depending on your preference
                    the for loop can be used to generate a vertical alignment of your string, whereas
                    the print statement simply prints your string on a single line.

                    The primary purpose of the for loops is also interspersed with the range function.
                    What the range function does is that it generates numbers within a range to which the user specifies.
                    It is important to note that the range function always starts at 0 and is defaulted to increment
                    by 1 until it reaches the penultimate number inputted.

                    example:
                        print(range(5))

                    This will print the number starting from 0 up till 5, increasing by 1 each time.
                    the ouput should be 01234, excluding the last number. Should you want to change the increments
                    and start from another value, you can enter:

                    example:
                        print(range(1,5,2))

                    Now you are printing all the numbers between 1 and 4 (excluding the last remember!) but
                    each number will be incremented by 2 instead of 1. So you should acquire as an output
                    13.

                    Blending the for loop and the range function opens up a host of posibility, below are some examples:

                    example 1) for i in range(5):
                                    print(i)

                    output: 0
                            1
                            2
                            3
                            4

                    example 2) for i in range(1,5,2):
                                    print(i)

                    output: 1
                            3

                    mixing simple arithmetic with the range:

                    example 3) for i in range(5):
                                    print(i+1)

                    output:1
                           2
                           3
                           4
                           5
                    ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(help)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 6:
            print('''
                     SLICING STRINGS
                     In python you can slice through strings by utilizing something known as indexes
                     Indexing simply means to select a specific letter in a word or a word in a sentence (if more than one word is supplied).
                     Python understands letters in a word each with their own independent indexes.
                     the first letter of a string word is indexed with 0 and each consecutive
                     letter of the word is indexed with a number incremented by 1. This will make more sense through some examples:

                     example:-
                            x = 'letter'
                            print(x[0])

                     output: l

                     In this instance, because the string is a single word, python treats each letter of the word with
                     its own index. The index of the first letter of the word 'letter' is 0 and depending on which letter you
                     want to print, simply enter the specified index value.

                     example:-
                            x = 'letter'
                            print(x[1])

                     output: e

                     Specifying index 1, determines the second position of the string, which is
                     the second letter of the word 'letter'. The formatting of indexing is somewhat like a list
                     in that indexing a specific letter in a word or a word in a sentence involves
                     entering the stored variable followed by square brackets wrapping the index number.
                     You can also mix the for loop with string slicing as follows:

                     example:-
                            x = 'letters and words'
                            for i in x:
                                print(x[i])

                     output: l
                             e
                             t
                             t
                             e
                             r
                             s

                             a
                             n
                             d

                             w
                             o
                             r
                             d
                             s

                     In this example I have decomposed a sentence into words and used string slicing to
                     print individual letters of the words in the sentence. Indexing also has other rules.
                     If you want to index starting from a value up til a value (excluding the last like range)
                     you would implement string indexing using colons.

                     example 1)
                             x = 'letters'
                             print(x[:], end='')
                     output: letters
                     example 2)
                             x = 'letters'
                             print(x[1:], end='')
                     output: etters
                     example 3)
                             x = 'letters'
                             print(x[:6],end='')
                     output: letter

                    In these few examples I have provided you with some of the many powerful functions that string slicing
                    can accomplish.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 7:
            print('''
                     This episode is about adding strings
                     In python, two separate strings/ string variables can be added together through several ways
                     A method known as string concatenation is python's default method of piecing together
                     two separate strings into a single word, or phrase without spaces. This is useful when, for example,
                     you want to combine multiple letters together to create a word (or combining many words together to create
                     a longer word. Below are some examples of what can be achieved through string concatenation.

                     example 1) x = 'jo'
                                y = 'hn'
                                print(x+y)
                     output: 'john'

                     In this example, I have saved two separate phrases, 'jo' and 'hn' to create the name
                     'john' through string concatenation. Note that python cannot concatenate strings and integers
                     together.

                     example 2) x = 'jo'
                               y = 5
                               print(x+y)
                     output: error

                     In this instance, I attempted to concatenate the string 'jo' with 5, so python throws
                     back an error. A better method would be to concatenate the string 'jo' with the string
                     '5', to which python understands as simple string concatenation.

                     example 3) x = 'jo'
                               y = '5'
                     output: jo5

                     Now you have seen how string concatenation works, remember to always check the type
                     of your variable to make sure they are of the same str() kind, otherwise python
                     doesn't understand what you're implying''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 8:
            print('''
                     LISTS AND STRING APPEND AND EXTEND METHODS
                     Sometimes in python we prefer to save multiple strings or integers into their own groups
                     of objects. This group of multiple strings and/or integers is known as a list. The
                     strings/integers which occupy these lists are called 'iterables'. Like strings, lists also have
                     their own built-in methods. To check for string or list methods, python has within it created a
                     function known as dir() short for directory, showing all the available built-methods for the
                     string or the list at hand. This function is so powerful that it can also be applied to modules
                     or different classes of objects. More information on dir() can be found in a separate episode.

                     In this episode, the focus will be on the list extend and append methods. It is quite difficult
                     to differentiate between these list methods but the key principle to understand is that list
                     extend saves any new iterables as separate objects to the end of the list, whereas list append
                     adds all the separate iterables as one iterable to the end of an existing list. This will make more
                     sense through example and practice.

                     example 1) x = ['john', 'sam', 'jack']
                               print(x)
                     output: ['john', 'sam', 'jack']

                     This is a basic list example. Inside the list I have created string objects 'john', 'sam' and
                     'jack'. A list is typically created in this format, with string/integer iterables as independent
                     values separated with commas. All the iterables comprise of one list which was stored as x. Printing
                     x shows to the screen the list containing all the independent string name variables.

                     example 2) x = [1,2,3]
                               print(x)
                     output:[1,2,3]

                     This is a similar example, but with integer iterables instead of strings.

                     Now that I have outlined the characteristics of lists, it is time to discuss list append and extend
                     methods. In python, methods define the applications of the specific class of variable in use. All classes of variables
                     have their own methods. The basic classes of variables are the string, list and dictionary- more information in the
                     dictionary class can be located in a separate episode. Two of the methods of the list class are the extend and append.

                     To invoke these methods, simply save a list as another variable as I demonstrated in the previous string and integer
                     list examples. Then type x.append() or x.extend() to command python of what needs to be done to the list. Now to
                     provide concrete examples to really demonstrate the subtle difference between list append and extend.

                     example 3) x = [1,2,3]
                               y = ['john','sam','jack']
                               x.append(y)
                               print(x)
                     output: [1,2,3,('john','sam','jack')]

                     example 4) x = [1,2,3]
                               y = ['john','sam','jack']
                               x.extend(y)
                               print(x)
                     output: [1,2,3,'john','sam','jack']

                     In the first example, the list append extends the pre-existing list x with a tuple of all the iterables of list y.
                     As for the list extend, each iterable of list y is added to pre-existing list x as independent iterables. This is the
                     key difference between list extend and append. We will discuss tuples more in another video.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = list()
                q_4 = input("List append or extend? ")
                if q_4 == 'append':
                    help(x.append)
                elif q_4 == 'extend':
                    help(x.extend)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 9:
            print('''
                     THE SHELL AND CREATING FUNCTIONS ON THE SHELL
                     While it takes some familiarization, the python shell can be used for creating functions, loading and saving variables and printing. The shell can essentially do everything the script
                     can with one key difference that is, the shell immediately runs your script as your typing it, whereas an extra 'run module'
                     step in the 'run' icon in the script is neccessary to actually test whether your functions are working. Depending on your
                     goals, the shell is recommended for checking and debugging smaller pieces of code, but a script is a better tool for
                     creating detailed and multi-functional pieces of code.
                     It is recommended to simultaneously use the shell and Python script window side by side to run smaller pieces of code
                     in your shell and to test-run your script in the shell to check if its working.
                     Creating functions with the shell can be achieved in two ways:

                     1) you can copy and paste a function from your python script onto the shell to test it.
                     2) run your module and the result will be printed to your screen on the shell.

                     example 1) >>> def sub(x,y):
                                        return x-y
                               >>>print(sub(4,3))
                               >>>1

                     example 2) def sub(x,y):
                                    return x-y

                               print(sub(4,3))

                     In the first example, I defined my subtraction function aliased as sub. It has two arguments which are the numbers
                     the user is required to input to subtract one from the other. The return key creates a new variable, but to print to
                     the screen I used the print function embedding my function to obtain 1 as a result. The first example demonstrates
                     how you can use the python shell directly for creating functions and testing them. In the second example, an additional
                     step is required (run module) to print the desired ouput to your screen via the shell. In this scenario, the shell
                     command was better fitted, but for longer, more complicated functionality, the python script is highly recommended, using the
                     python shell simultaneously to test whether sub-segments of the longer python script code is functional.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
                episode(x)
        if x == 10:
            print('''
                     FOR LOOP WITH LISTS
                     One of the reasons to why the for loop is so handy is how its implemented with lists
                     Adopting a for loop with a list enables you to iterate (in other words, test each iterable of the list independently)
                     and apply specific functions to each iterable of the list. This can only be understood through solid examples.

                     example 1) x = ['john', 'sam', 'jack']
                               for i in x:
                                   print(i)
                     output: john
                             sam
                             jack

                     example 2) x = [1,2,3]
                               for i in x:
                                   print(i)
                     output:1
                            2
                            3

                     In both case, I created a list of object strings and integers, then applying the for loop, python associates the i
                     in the for loop with each string or integer in the specified list. After identifying the iterables of the list,
                     commanding python to print each iterable, is identical to printing one item off the list, then looping through, printing
                     the next object and the next (until all iterables of the list are printed onto the screen). For more intricate python,
                     the following examples utilize lists and string concatenate, split.

                     example 3) x = ['john', 'sam', 'jack']
                                for i in x:
                                    print(i + '1')
                     output: john1
                             sam1
                             jack1

                     example 4) x = ['john', 'sam', 'jack']
                                for i in x:
                                    print(i+i)
                     output:johnjohn
                            samsam
                            jackjack

                     example 5) x = ['john', 'sam', 'jack']
                                y = [1,2,3]
                                for i in y:
                                    print(x[i] + 'i')
                     output:john1
                            sam2
                            jack3

                     example 6) x = ['john', 'sam', 'jack']
                                y = [0,1,2]
                                for i in y:
                                    print(x[i:])
                     output:(john,sam,jack)
                            (sam,jack)
                            (jack)

                     The first example explores how one could make a alphanumeric phrases print to the screen with a simple
                     for loop and printing each iterable (the names) with the string integer 1. A second example is used to
                     show how string concatenation can be blended with the for loop in lists. Printing each iterable of the list
                     with itself is identical to concatenating each string object of the list with itself. The outcome is quite
                     beautiful in that each name in the list is printed twice, then concatenated with its duplicate and python
                     loops through each name of the list this way. If you wanted to concatenate string integers with string names,
                     the third example makes light of this scenario, combining string indexing of a list of names with a separate
                     list of numbers (there is a separate video on string indexing if you're unfamiliar) to print the first name in the
                     first list with the first number of a separate list. Note that python will print an error if the length of the
                     first list is smaller than that of the second (as python loops through the last number of the second list, it
                     cannot locate the index that is associated with the last string of the first).In the last example I have used
                     string slicing and two lists to produce a pattern of descending iterables of names onto the screen.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 11:
            print('''
                     NESTED FOR LOOP AND LISTS
                     If you want python to loop through two or more lists and combine iterables from both lists the
                     nested for loop is utilitarian. The nested for loop, like the regular for loop for applying
                     commands to individual iterables in a list, is used to manipulate and command more than one
                     list at a time. An example will make this clear.

                     example 1) x = ['john', 'sam', 'jack']
                                y =[1,2,3]
                                for i in x:
                                    for j in y:
                                        print(i + 'j')
                     outcome: john1
                              john2
                              john3
                              sam1
                              sam2
                              sam3
                              jack1
                              jack2
                              jack3

                     In this example, you identify how python treats lists of lists or nested lists. The first for loop iterates through each
                     name of the first list, then adding a second for loop, python focuses on each number of the second list. Note that python
                     focuses on iterating through each element of the innermost list(the most indented list) and then it iterates through
                     a list with one less indent. Therefore, python searches for the first element of the first list, it stops at this element,
                     finds the first element of the second list, and concatenates it with the first element of the first list. It does this until
                     it iterates through all elements of the second list concatenated with the first element of the first list. After this is done,
                     the process is repeated for remaining elements of the first list until fully completed. Another example of string
                     concatenation and the for loop with lists is demonstrated below.

                     example 2) x = ['john', 'sam', 'jack']
                                y = [0,1,2]
                                for i in x:
                                    for j in y:
                                        print(x[j] + i)
                     output:johnjohn
                            samjohn
                            jackjohn
                            johnsam
                            samsam
                            jacksam
                            johnjack
                            samjack
                            jackjack

                     For this example, I have utilized the string index and concatenation to print all outcomes of individual names of
                     the first list with each other. Take time to understand the logic, copy it you must, but try and replicate.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = list()
                help(x)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 12:
            print('''
                     USING ONE PYTHON FUNCTION TO BUILD ANOTHER
                     Another application of functions is that they can be implemented within another function to create a more
                     powerful command
                     Once created, a function is stored in your computer. If inputted correctly, your function reacts like any built-in
                     python function and will be treated by your shell in the same way. Using this idea, you can create a separate function
                     that perhaps adds more functionality to your first without needing to type in your first function. Simply invoke your
                     first function in your second and you will save time and space in your script.

                     example 1) def add(x,y):
                                     return x+y

                                def mul(x,y):
                                    m = add(x,y)
                                    return m*y

                                print(mul(2,3))
                     output: 15

                     In this demonstration, I embedded the pre-defined add function to mutiply the additive of two numbers with the second number
                     (in this case defined as y). The addition of 2+3 equals 5 and 5 mutiplied with 3 is 15, which is the desired ouput.

                     example 2) def div(x,y):
                                    return x/y

                                def add(x,y):
                                    a = div(x,y)
                                    return a+x

                                print(add(15,5))
                     output:18

                     This example sheds light on how you can use arithmetic functions and combine them with one another. The first function
                     absorbs two inputs and divides the first by the second, 15 divided with 5 is 3. Using this value, I add 3 with the first
                     argument of the function which equals 18.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 13:
            print('''
                     TRUE AND FALSE STATEMENTS
                     This episode is about boolean statements which is defaulted into Python as TRUE and FALSE.
                     A boolean statetement like TRUE or FALSE is the defaulted output when a simple condition is
                     tried in the shell. There is no better explanation of boolean statements but pure demonstration:

                     example 1) >>> 5 > 4
                                >>>TRUE

                     example 2) >>> 5 < 4
                                >>>FALSE

                     example 3) >>> 5 != 4
                                >>>TRUE

                     As shown, boolean statements are logical statements within python's memory that check whether a certain condition is
                     met or unmet by python's standards. You can also use boolean statements to print certain values using the simple
                     conditions.

                     example 4) >>> if 5 > 4:
                                    print('YES')
                               >>>'YES'

                     In this example, I am checking whether the integer 5 is greater than 4, python knows to check this against
                     TRUE or FALSE statements. In this case, it is TRUE, so the condition is met and the string 'YES' will be printed
                     to the screen. Now you understand how the if statement works (if a condition is TRUE proceed with a command and if it
                     its FALSE don't). This is the basis of conditional statements and a pre-requisite for much more to come.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                q_4 = input("Do you want help with the True or False statement? ")
                if q_4 == 'True':
                    help(True)
                elif q_4 == 'False':
                    help(False)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 14:
            print('''
                     IF AND ELSE STATEMENTS
                     In python, the 'if' and 'else' statements are python's method of checking whether a condition is met, in
                     which case python defaults the outcome to TRUE and proceeds with whatever command you want done if a
                     certain condition is met. The else statement is a way you can obtain a value, say if your condition
                     is met, any other value apart from the condition will be under the else statement, and whatever command
                     you want to occur if the command for the 'if' statement is not met.
                     This idea is highlighted further using several examples.

                     example 1) x = 'name'
                                if x == 'name':
                                    print(x)
                     output: 'name'

                     example 2) x = 'man'
                                if x == 'name':
                                    print(x)
                                else:
                                    print('not found')
                     output: 'not found'

                     In the first example, the variable x stored the string 'name'. The 'if' statement defaulted as TRUE because variable
                     x was identical to 'name'. As this condition was met, 'name' was printed to the screen because python understood the
                     equivalence. In the second example, the variable x was stored as 'man', but the 'if' statement checks whether variable
                     x is identical to 'name'. In this instance, x does not store the value 'name' so the default boolean is FALSE because the
                     condition isn't met. Because an 'else' statement was provided and x is not identical to string 'name' the string
                     value 'not found' is printed to the screen, which is the reverse logic of the 'if' statement. The only condition opposite
                     of TRUE in this case is FALSE. The examples below shed light on more intricate logic apart from the boolean TRUE or
                     FALSE statements.

                     example 3) y = 5
                               if y != 6:
                                   print(y)
                               else:
                                   print('6')
                     output: 5

                     example 4) y = 6
                               if y == 12/2:
                                    print(y)
                                else:
                                    print('12')
                     output: 6

                     In these cases, a more intricate condition is checked. The first stores 5 under y. An 'if' statement compares whether
                     5 is not equal to 6, which is TRUE, so python prints y to the screen following the print(y) command supplied to the
                     computer if the condition was met. If y was 6 instead, the string 6 would print to the screen because the only number
                     which is not unequal to 6 is 6 itself. The second example makes use of the divide key '/' and checks whether stored value
                     of y is equal to 12/2. This returns a TRUE because 12 divided by 2 is 6 which is identical to the condition for the 'if'
                     statement. If y stored a separate value, say 4, 4 isn't equal to 6, so this returns a FALSE, but an 'else' statement was
                     provided to command any values of y that aren't equal to 6 to print the string '12'. Therefore the shell would print
                     '12' if any value other than 6 was the stored value of y.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 15 or x == 16:
            print('''
                    NESTED IF AND ELSE STATEMENTS
                    Suppose you want to have two statements or more to be met before proceeding to execute a command, this is resolved
                    using nested if and else statements, which check if a first condition is met, to proceed to the second and if a second
                    condition is not met but the first is, whether to execute the command or not
                    The easiest way to clarify any uncertainties is to demonstrate what is really meant by a nested if and else statement.

                    example 1) x = 'man'
                               if x == 'man':
                                   if x != 'man':
                                       print('no')
                                   else:
                                       print(x)
                    output: 'man'

                    example 2) x = 'man'
                               if x != 'man':
                                   if x == 'tan'
                                       print('tan')
                                   else:
                                       print(x)
                    output: 'man'

                    These are some delibarately confusing but testing examples of nested if and else statements. The first example shows
                    how you can create a nested if and else statement if an initial condition is met. The string 'man' is stored as x, an
                    if statement checks whether the string of x is equivalent to 'man'. This condition is TRUE, but another condition needs
                    to be compared to with the statement before the command is executed. x is equivalent to 'man' but the embedded if
                    statement compares whether x is not equivalent to 'man'. As the second condition isn't met but an initial condition is
                    met, the embedded else statement prints anything opposite of the embedded if statement. An embedded if statement isnt met,
                    so the else statement command is executed and 'man' is printed. The second example sheds light on emdedded if statements
                    and an else statement. First it compares whether the stored string of x is not equivalent to man. Since x is equivalent
                    to 'man', the first if condition is unmet and x is printed to the screen under the else line of command. If x stored value
                    'tan' instead, the string 'tan' would print to the screen, because 'tan' is not equivalent to 'man', meeting the first condition
                    of if statement. The second 'if' statement is occupied because tan is equivalent to tan, so tan is printed on the screen as
                    expected.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 17:
            print('''
                     THE ELIF STATEMENT
                     The elif statement is used in python when the conditions for an if statement are unmet, but instead of following
                     the path of an else statement, which executes a command for any other instance apart from the condition of the if
                     statement, the elif creates another condition within the path to check whether the value meets another condition
                     apart from the if statement
                     This idea will make more sense with examples.

                     example 1) x = 'name'
                                 if x == 'man':
                                     print(x)
                                 elif x == 'name':
                                     print('name')
                     output: 'name'

                     example 2) x = 'john'
                                 if x != 'man':
                                     print(x)
                                 elif x == 'george':
                                     print('john')
                     output: 'john'

                     example 3) x = 'john'
                                 if x == 'man':
                                     print(x)
                                 elif x == 'ban':
                                     print('ban')
                     output: None

                     example 4) x = 'john'
                                if x == 'man':
                                    print(x)
                                elif x == 'ban':
                                    print('ban')
                                else:
                                    print('yea')
                     output: 'yea'

                     In the first example, the if statement is unmet because x is not equivalent to 'man'. The second condition under
                     the elif statement is met, so 'name' is printed as requested. In the second example, the condition of the first if
                     statement is satisfied so the string 'john' is printed. If the condition under the elif statement was for x to be
                     equivalent to string 'john', this would be a dilemma because the stored value of x is not equivalent to 'man', meeting
                     the first if condition, but also meeting the second elif condition as x would be equivalent to 'john'. In this scenario
                     it is important to understand the chronology of python's logic. Since the first if statement is met immediately, python
                     would print string 'john' and completely ignore the elif statement because the initial if condition was already met. If
                     this happens for you, it is always important to remember the chronology of how python responds to conditional statements.
                     The third example expresses one of the key issues with the elif statement. If neither the initial if nor the consecutive
                     elif statement conditions are fulfilled, python doesn't know how to respond so nothing is printed to the screen. Unlike, the
                     else statement, when an if statement is unfulfilled and conditions aren't met for the elif, the elif doesn't respond with
                     whatever outcomes leftover from the if, but the leftover's must fulfill a certain criteria. That is why a last example is provided
                     to highlight this case and to print something to the screen when the conditions for both an if and elif statement are not met.
                     In the last example, 'yea' is printed because x is not equivalent to man nor is it equivalent to 'ban' so the only leftover
                     condition is else, which executes a print('yea') statement if neither of the other conditions are done.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 18:
            print('''
                     MODULO AND ITS FUNCTIONALITY
                     the modulo symbol also known as % is an arithmetic operator unlike the rest, dividing two numbers
                     with each other and printing the remainder of two numbers. If the remainder is none when two numbers are
                     mutiples of each other, the modulo will output a zero because the remainder is null
                     It is best to demonstrate this knowledge through example.

                     example 1) 12%6
                     output: 0

                     example 2) 12%5
                     output: 2

                     example 3) 12%9
                     output: 3

                     The examples are self-explanatory. If still no understood,
                     the remainder of 12 divided by 6 is 0 because 12 is divisible by 6, 12 is not divisible by 5 leaving a remainder of
                     2 behind, so the output is 2, 12 is not divisible by 9 with remainder 3, the ouput is 3.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 19:
            print('''
                     LIST SORT METHOD
                     The list sort method is a built-in list method which organizes a list following a specific condition known
                     as the key.Normally, the key is defaulted to a value of None, meaning that if no key argument is inputted
                     into the function method a too few argument error will not occur. More about basic functions can be sourced
                     in another video. The list sort method also takes in a reverse argument which is defaulted to False.
                     Setting this argument to through sorts the iterables in ascending order. Sorting iterables in a list that
                     meet a certain 'key' criteria is vital to recognize patterns that weren't previously discernible in the
                     pattern of objects in the list.

                     example 1) x = ['mas','zax','fac']
                                x.sort()
                                x
                     output: ['fac', 'mas', 'zax']

                     example 2) x = [1,2,3]
                                x.sort(reverse=True)
                                x
                     output: [3,2,1]

                     example 3) def x():
                                   return x[:-1]
                                y = [1,2,3]
                                y.sort(key=x)
                     output: [3,2,1]

                     These three examples explore the main arguments within the list sort method descriptor. The first example highlights
                     how the sort method organizes strings in ascending order according to their individual ascii values. The iterables of list
                     x in the first example are string values. With x.sort(), no additional arguments are inserted, so the key takes default value
                     None and reverse is defaulted as False. Ascii enumeration is case insensitive and capital letters are enumerated with lower
                     values compared to small letters. This example deals with small letters each of which are enumerated with values 141 to 172.
                     Since letter f is enumerated with a smaller ascii value compared to m and z, the sort method organizes the list starting with
                     the smallest ascii value of the first letter of each member in the list (f comes before m and m before z). Sorting in ascending order
                     the list printed is as shown. In the second example, I have utilized the reverse argument of the sort method. Switching to True
                     reverses from ascending to descending order starting from the largest till the smallest value. The third and last example clarifies
                     how the key argument is implemented in the sort method. You must first create a definition for which will become the key condition
                     that the list must fulfill. In this scenario, the key is the last iterable until the first, so the list 1,2,3 is flipped to 3,2,1
                     where the last digit of the previous list is sorted into the first position of the new list.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = list()
                q_4 = input('Extra help is available for list sort method: ')
                if q_4 == 'sort':
                    help(x.sort)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 20:
            print('''
                     STRING CAPITALIZE AND LOWER
                     Within the string class, you can also change the case of the string to upper or
                     lower case using the str.capitalize() or str.lower() built-in string method
                     Examples are shown below:

                     example 1) x = 'name'
                                x.capitalize()
                     output: 'Name'

                     example 2) x = 'NAME'
                                x.lower()
                     output: 'name'

                     As demonstrated above, string capitalize changes the first letter of the string variable
                     from lower to an uppercase. String lower method changes all the letters of the variable
                     from upper to lower cases''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                q_4 = input("Is help needed for capitalize or lower methods? ")
                if q_4 == 'capitalize':
                    help(x.capitalize)
                elif q_4 == 'lower':
                    help(x.lower)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 21:
            print('''
                      ARGS
                      In python multiple arguments can be supplied to a function known as *args by default.
                      Examples include:

                      example 1) def pr(*args):
                                      for arg in args:
                                          print(arg)
                                pr(1,2,3,4,5)
                      output:1
                             2
                             3
                             4
                             5

                      The asterisk tells the function that more that one argument can be supplied. If so, the function
                      iterates through the list of all arguments and prints one and transfers to the next, prints it etc.
                      This is useful when you want to create a function that takes in more than a single argument.
                      A more advanced function which utilizes this idea is below

                      example 2) def add(*args):
                                          first = 0
                                          for arg in args:
                                              first += arg
                                              print(first)
                                  add(1,2,3)
                      output:1
                             3
                             6

                      In this example I assign value 0 to the variable first. Iterating through the list of all arguments
                      the value assigned to first is incremented by the next iterable each time and printed.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 22:
            print('''
                     IS EVEN FUNCTION
                     The aim of this episode is to create a function that checks whether a specific number
                     is even or odd. If the number is odd, 'odd' should be printed, otherwise 'even'. A bonus
                     challenge would be to use a mutiple argument assignment to check whether multiple numbers
                     are even or odd using the splat *args in the argument section of the function''')
            query = ("Do you want to solve the problem yourself or not? Enter yes or no: ")
            if query == 'yes':
                print('''Congratulations on solving your first problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''Solution:
                         def is_even(num):
                             if num%2 == 0:
                                 print("even")
                             else:
                                 print("odd")
                        BONUS:
                             def is_even(*nums):
                                 for num in nums:
                                     if num%2 == 0:
                                         print("even")
                                     else:
                                         print("odd")''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 23:
            print('''
                     THE WHILE LOOP
                     In python, the 'while' keyword is similar to that of the 'if' statement, but instead of
                     a single application, when a condition is met, the command would be continuously executed
                     till the point the condition is exhausted or unmet. This is a key difference to the
                     'if' statement, which executes a command single-handedly if and when a condition is met,
                     but only for the first instance of when a condition is met. This will become apparent
                     through examples.The while statement is most effective when looping through numbers in a range or
                     a list because it compares all numbers within a given range (or iterables in a list) and if the
                     a condition is fulfilled, the number will be eligible for executing a command, then the next number
                     will be tried and compared to the same condition. If consecutive values all meet the required
                     condition, they will all be stored and printed as candidates for the executable. Contrastingly,
                     the the if statement only checks for the first instance when a value or iterable meets the
                     condition and applies a command to the first instance. It neglects further values in a list that
                     fulfill the same condition, so it's not an ideal conditional statement for such cases.

                     example 1) n = 5
                                while n <= 10:
                                    n += 1
                                    print(n)
                     output: 6
                             7
                             8
                             9
                             10
                             11

                     example 2) n = 0
                                while n >= 0:
                                    n += 1
                                    print(n)
                     output:1
                            2
                            3
                            4
                            5
                            6
                            ...

                     example 3) n = 5
                                if n <= 10:
                                    n += 1
                                    print(n)
                     output:6

                     example 4) n = 0
                                x = ['john', 'max', 'poe']
                                while n <= 2:
                                    print(x[n])
                                    n += 1
                     output: john
                             max
                             poe
                               

                     The four examples above demonstrate the utility of the while statement in iterating through values
                     that meet a certain condition and for iterables in a list until a condition is exhausted. The
                     first example dictates the condition that the stored value of variable n should be less than or
                     equal to the number 10, after which, the condition is umnet and the cycle is broken. As n starts
                     at 5, this integer satisfies the condition, n is stored as 5, incremented by 1 to 6, then printed
                     to the screen. 6 is also less than 10, so it fulfills the condition like 5, it is incremented to 7
                     and printed. The same judgement is applied to all values until 10, but because the inequality states
                     values less than or equal to 10, this value is stored and incremented to 11, where the condition is
                     finally unmet as 11 is greater than 10 so the loop breaks. The second example is a what is known
                     as an infinite loop because, value n is stored as 0 for starters, the condition asks for values
                     greater than or equal to zero. Starting at zero means that every value after zero fulfills the
                     condition. But after each value, the next is incremented by 1, so every value from 1 to infinity
                     is printed to the screen. It is not advised to practice such a use of the while loop because
                     the outcome is extensive and will continue endlessly until interrupted. It is recommended to use
                     the for loop in a range or supply a stopping point like the first example to really absorb the
                     values printed to the screen. A third example expresses why the 'if' statement is not an ideal
                     conditional statement for values in lists or ranges because the first value of n satisfies the
                     condition, it is incremented to 6, but then the cycle is broken and 6 is the only value printed to
                     the screen. However, there are 5 numbers less than or equal to 10, so the while loop is more
                     suited for such an example. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 24:
            print('''
                     IN AND NOT IN STATEMENTS
                     Finding iterables than are elements or not elements of a list can be achieved
                     using the keywords 'in' and 'not in'. Often the keyword's in and not in are perceived in
                     the for loop to focus the program to only members or participating string/ integers where
                     a commmand or a print statement will occur. This is visible through example.

                     example 1) for i in range(1,5):
                                    print(i)
                     output: 1
                             2
                             3
                             4

                     example 2) x = [0,2,4]
                                for i in range(5):
                                    for i not in x:
                                        print(i)
                     output:1
                            3

                     example 3) for i in range(10):
                                     if i%2 == 0:
                                         print(n)
            
                     output:2
                            4
                            6
                            8

                     In these few examples, the applications of the in and not in statements are exhibited.
                     The first example stores each iterable i within a range of numbers (starting from 1 to 4),
                     and prints all the values. The in statement can be thought of as the condition which
                     focuses python's attention to only numbers within a certain range that need to be printed
                     to the screen. It is similar to a filter. For mathematicians, the in and not in
                     statements can be thought of as all the elements in or outside a set. The range is the set
                     and the in is the elements of the set. The second example is more sophisticated in that it
                     uses the range function to list all numbers within a set. A supplementary condition is then
                     supplied such that for all members of the set (range), members that are not elements of the
                     subset (list x) should be printed. It is noticeable that members not belonging to subset x are odd numbers between 0 and 4 because all members of x are even
                     numbers in the range (or the original set). So there are two conditions in this example:
                     elements that belong to the set that don't belong to a subset of the original set are printed
                     and the rest of the elements are neglected. This leaves numbers 1 and 3 which are the only
                     odd numbers between 0 and 4. A third example showcases the reverse effect using a wider
                     range of numbers from 0 to 9. Numbers that are divisible by 2 meet the conditions as
                     participating elements of a subset of original set (range 10). The only numbers divisible by 2
                     are even, so the third example is a more abstract filter of all even natural numbers between 0
                     and 9.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 25:
            print('''
                     KEYWORDS
                     Keywords in python are certain reserved words that python really understands and take
                     highest priority in the chronology of python's command.
                     Some of python's keywords have been introduced already and you have most probably been
                     using them without truly understanding their importance.
                     Keywords like in, not in, def, return, as, is , from, import are words that python really
                     understands and executes primarily before paying attention to the rest of the conditions
                     supplied in a line of code. The keywords in, not in, def have been touched upon
                     which focuses python's attention to members that belong or not belong to a set of
                     values, or defining a new function which takes in arguments and returns/ creates a new
                     variable which can be printed to the screen. The keywords as, is, from and import
                     will be touched in a later episode, but essentially they act as separate filters when
                     selecting what methods from an external package you wish to implement into your code and
                     aliasing these methods with shorthand notation to avoid mispelling errors in your code. More
                     will be discussed on these keywords later.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 26:
            print('''
                      INCREMENTING AND DECREMENTING VALUES
                      You may have or have not realized the notation += in some of the earlier code
                      examples. This notation is a direct reference to value incrementation and decrementation.
                      In other words, when a condition is met, a previous value is incremented or decremented,
                      assigning a new stored value to the old value and if the new value fulfills the same condition,
                      it is incremented twice and stored as the newest value to be checked against the same condition.
                      This method is valuable in simple arithmetic operations and in the for or while loops to continuosly
                      check all numbers without reassigning values to multiple variables.
                      This is made clear through rigorous examples.

                      example 1) x = 1
                                 if x == 1:
                                     x = x + 1
                                     print(x)
                      output: 2

                      example 2) x = 0
                                 while x < 10:
                                     x = x + 1
                                     print(x)
                      output:1
                             2
                             3
                             4
                             5
                             6
                             7
                             8
                             9
                             10

                      example 3) x = [2,4,6,8,10]
                                 for i in x:
                                     i = i/2
                                     print(i)
                      output:1
                             2
                             3
                             4
                             5

                      example 4) x = [2,4,6,8,10]
                                 for i in x:
                                     i = i*2
                                     print(i)
                      output:4
                             8
                             12
                             16
                             20

                      In these four examples, the incrementation and decrementation is implemented to
                      execute commands the iterables of lists or to augment stored values of variables
                      in the script without assigning new variables to new values and adding more space
                      where it can be saved. The first example checks is the stored value of variable x is
                      equivalent to 1. It is True, so the condition is met and the stored value of x, which
                      is previously 1, is incremented or added by 1. The new stored value is 2. With your
                      knowledge of the if statement, only the first instance of a condition is printed and
                      afterward the loop is broken. So the final output is 2, incrementing the stored value of
                      variable x by 1. The second example utilizes the while loop, checking all natural
                      numbers from 0 to 10 and if they're 10, the assigned value to variable x is incremented by 1 and stored to x as the new incremented value. Starting
                      at value zero, this number meets the condition such that it is less than 10. It is incremented
                      by 1 so x is now 1 and printed to the screen. The number 1 is also less than 10, so it is incremented
                      by 1 and printed to the screen. This process is continued until 10. A strict inequality is
                      applied in this case, so 10 doesn't satisfy the condition and the loop breaks at 10. As a result,
                      all values from 1 to 10 are printed to the screen. The third and last example
                      express other arithmetic operations that can be used in string increment or decrementation. For
                      instance, the third example shows how a for loop checking iterables in a list and dividing them
                      by 2 and printing them to screen. The last example is similar but using multiplication instead of
                      division to members of a list. Multiples of 2 were chosen to produce whole value results, but
                      decimals or floating point numbers are created if different values were assigned to the list.
                      A simplified manner of incrementing/ decrementing values in a list is using shorthand notation +=,
                      -=, /=, != . This notation achieves the exact result without needing to repeat the variable twice
                      in a line.

                      example 5) x = 1
                                 x += 1
                                 print(x)
                      output: 2

                      example 6) x = 1
                                 if x != 2:
                                     print(x)
                      output:1

                      The last example checks whether the value assigned to x is not equal to 2. This is True
                      so the condition is met and x is printed to the screen.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 27:
            print('''
                     INCREMENT STRINGS
                     Like integer values string values can also be incremented using a similar logic
                     to that of integer incrementation.
                     Simple examples of string incrementation are listed below:

                     example 1) l = 'letter'
                                x = ''
                                b = 'bell'
                                for i in b:
                                    for i not in l:
                                        x += i
                                print(x, end = '')
                     output: be

                     example 2) vowels = 'aeiou'
                                name = ''
                                n = 'marcus'
                                for i in n:
                                    for i not in vowels:
                                        name += i
                                print(name, end='')
                     output: mrcs

                     It can be observed that string incrementation is very similar to the method employed
                     with integers. A key difference is a variable assigned with an empty string needs to
                     be created and for each letter/iterable in a word that doesn't belong to another string
                     of letters, the letter is concatenated to the empty string variable until all letters
                     that don't belong to a set of another string are exhausted and the empty string stores
                     all concatenated letter which form a word. This is a good way of filtering out all the
                     vowels in a word to locate consonants as displyed in the second example.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(str)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 28:
            print('''
                     NUMBER TRIANGLE
                     This episode absorbs all that was discussed so far into forming a pattern of
                     numbers onto the screen in the shape of a triangle. A hint to the solution of this
                     problem is to think about the format of the numbers and the conditioning to apply
                     to the numbers to print them to the screen following such a format''')
            query = input('''If you wish to solve the problem independently, the shape in question is
                            provided below.
                            
                            1   
                            12
                            123
                            1234
                            12345

                            1 
                            1 2 
                            1 2 3 
                            1 2 3 4 
                            1 2 3 4 5 
                            
                            Enter yes or no to choose your option''')
            if query == 'yes':
                if query == 'yes':
                    print('''Congratulations on solving your this problem! Your well on your way to becoming
                             a programmer''')
                    question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                    if question == "help":
                        help()
                        q_2 = input("Do you wish to learn more, enter yes or no: ")
                        if q_2 == 'yes':
                            x = int(input("Enter another episode you wish to learn about: "))
                        else:
                            break
                    if question == "quit":
                        window = False
                    if question == "more":
                        x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         The solution will be broken down into several steps:

                         Solution:

                         As we expect to automate the number triangle for any input, it is
                         advised to define a function that takes in a number input and
                         creates a number triangle with the largest value equivalent to the
                         number entered. The number triangle above is created by entering
                         5 into the function.

                         def num_triangle(num):
                             'enter a number to indicate the size of the triangle'

                         A docstring is added to the function informing users of what to insert
                         into the function.

                         def num_triangle(num):
                             'enter a number to indicate the size of the triangle'
                             for i in range(1,num+1):
                                 print('*')

                         num_triangle(5)

                         output: *
                                 *
                                 *
                                 *
                                 *

                        The first step is to examine the shape of the triangle we are trying
                        to produce. When the user enters a number into the function, the
                        number is used as the range of the function. As the range function
                        starts at zero by default, a starting point argument is required to
                        train the range to begin at 1 and end at number specified by the user
                        excluding itself. To resolve this problem and to print all the
                        numbers up to the user's number including the number, an extra 1 must
                        be added to the range. As the focus is the string format, I started by
                        printing * to the screen and observing the result. The required triangular
                        format is still invisible. The problem remains that python prints
                        * as the placholder for numbers up to and including the number entered into
                        the function, printing the value and separating each number separated
                        by a new line. 5 numbers are printed to the screen which is the required
                        levels of the number triangle.

                        def num_triangle(num):
                             'enter a number to indicate the size of the triangle'
                             for i in range(1,num+1):
                                 print('*', end='')

                         num_triangle(5)

                         output: *****

                         It can be observed that the placeholder of values 1 to 5 in the range provided
                         is printed to the screen in a line. Changing the end argument in the print function
                         to '' tells python that we want to print each number in the range provided separated
                         without spaces. We know how to create the levels and how to print numbers on a line,
                         now we try and create the required shape.
                         
                         def num_triangle(num):
                             'enter a number to indicate the size of the triangle'
                             for i in range(1,num+1):
                                 for j in range i:
                                     print('*', end='')

                         num_triangle(5)

                         output: ***************

                         The nested loop is required because using a single loop only generates
                         a number of values entered into the function. For a number triangle of 5
                         we expect an ascending pattern of values with 15 numbers altogether.
                         Using a nested for loop with j values in the range of values provided
                         to the first for loop will print the right amount of numbers to the screen
                         aliased by the placeholder *. This is still the wrong format so an extra step
                         is remains.

                         def num_triangle(num):
                             'enter a number to indicate the size of the triangle'
                             for i in range(1,num+1):
                                 for j in range i:
                                     print('*', end='')
                                 print()

                         num_triangle(5)

                         output:*
                                **
                                ***
                                ****
                                *****

                         This is the required triangular format. In printing such a format, it was
                         required to add an extra print statement outside the nested loop which meant
                         that values up to and excluding the value in the first range function were
                         printed, then the nested loop is exhausted for the all values in the range of
                         the first value of the first for loop. After this point, the initial for loop
                         is tried and a print empty string is understood by python to print a new line
                         after exhausting all possibilities of the embedded for loop. The first iterable
                         of the initial for loop is 1 so the only number in the embedded loop which is less
                         than 1 is zero. This value becomes is printed with placeholder *. The embedded for
                         loop has exhausted all its possibility as zero is the only number in the range function
                         for which is less than 1 excluding 1. The embedded for loop is broken and the next
                         value is printed to a new line through the print empty string one level above the embedded
                         for loop. This process is continued until all values in the range entered by the user.
                         The string format is correct, so now we can add values.

                         def num_triangle(num):
                             'enter a number to indicate the size of the triangle'
                             for i in range(1,num+1):
                                 for j in range i:
                                     print('j+1', end='')
                                 print()

                         num_triangle(5)

                         output:1   
                                12
                                123
                                1234
                                12345

                        We have obtained the desired result. The process is also automated because
                        we have defined a function which takes in any input and produces a number
                        triangle to the size of the input. This will work with larger values of
                        num_triangle like 6,7,8,9 and 10. Note that printing j itself will produce
                        values starting at zero up till a number before the number entered. This is
                        incorrect practice so incrementing by an extra 1 resolves this problem as we
                        begin at 1 instead of zero and every consecutive number is increased by 1
                        satisfying that we start at a number before the last increased by 1 which is
                        equivalent to the number itself. To format the shape with more spacing add a
                        space to the embedded print statement.

                        def num_triangle(num):
                             'enter a number to indicate the size of the triangle'
                             for i in range(1,num+1):
                                 for j in range i:
                                     print('j+1', end=' ')
                                 print()

                         num_triangle(5)

                         output:1 
                                1 2 
                                1 2 3 
                                1 2 3 4 
                                1 2 3 4 5
                        ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 29:
            print('''
                     PRINT FUNCTION
                     The print function is essential in python as it prints results to your screen
                     which checks whether your function or lines of code are correct. The print function
                     takes in 5 arguments, but 3 are essential to understand. If you've entered any previous
                     episode you will understand the value argument prints whatever string or integer you want
                     to your screen. The end argument is defaulted at new line which is the typical format
                     when iterating through lists and printing values that fulfill a certain criteria to a new
                     line. The sep argument is shorthand for separation. This argument is defaulted at a space
                     which is the way words are separated by spaces. Changing the sep argument is important
                     when separating values by different characters or delimiters. These include commmas or
                     exclamation points in a sentence or a string of text. If you don't want any one of these
                     elements simply input a new sep variable into the print function''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(print)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    q_3 = input("Enter another episode you wish to learn about: ")
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 31:
            print('''
                     STRING SPLIT METHODS
                     There are several methods which enable us to split a string. One is to turn a string sentence
                     into a list of string words as iterables of the list. String slicing can also be achieved by
                     using the str.find() method and isolating the index of a particular phrase or string in a
                     string sentence. Using the str.find() to source the index value and then assigning this string
                     index value to another variable - say x - let's us isolate a particular letter in a word or word
                     in a sentence by using the new variable as the index to locate the particular letter you are in
                     search of.
                     The examples below should resolve any uncertainties.

                     example 1) name = 'ian'
                                x = name.find('i')
                                name[x]
                     output: 'i'

                     example 2) sen = 'This is awesome'
                                x = sen.find('T')
                                y = sen.find('e')
                                sen[x:y]
                     output: 'This is aw'

                     example 3) sen = 'This is awesome'
                                sen.split()
                     output: ['This', 'is', 'awesome']

                     example 4) sen = 'This is awesome'
                                line = sen.split()
                                for i in line:
                                    print(i)
                     output: This
                             is
                             awesome

                     example 5) sen = 'This, is awesome'
                                line = sen.split(',')
                                for i in line:
                                    print(i)
                     output: This
                             is awesome

                     The first example displays the use of the string find method in isolating a particular
                     index of a string. The name variable saves a string value 'ian'. As the class of variable
                     'ian' is a string (to confirm this you can also apply the built-in type() function which
                     checks the class of a variable), name.find() takes in 2 optional arguments the string start and
                     end. The first argument of the str.find() method is the most vital, but you musn't forget
                     that str.find() takes in string arguments and returns the index of the string specified through
                     the primary argument. The first example sheds light on this idea. Using the string find method,
                     I have isolated a search on the string name 'ian' to the letter 'i'. The string find method
                     returns the index value of sub-string i in the name 'ian'. Then using the string indexing method,
                     to print the value 'i' to the screen, the string find value is used as an index of the original
                     string, so 'i' is printed to the screen. The second example features a way in which string
                     finds can be useful in isolating very particular sub-string values within a search range.
                     Short for sentence, the variable 'sen' stores the string sentence 'This is awesome'. Then
                     using the string find method, the index of uppercase 'T' and the letter 'e' are stored as
                     separate variables. Applying string indexing with the stored values of letter 'T' and 'e'
                     print to the screen 'This is aw'. The string find method isolates the whole phrase up till
                     and not including the first 'e' in the sentence. A third example expresses how string slicing
                     is achievable using lists. The string.split() method cuts a string sentence by whatever
                     delimiter is provided. In this example, without adding an optional delimiter argument, python
                     understands that we want to cut the sentence by its spaces, so a list of word iterables is
                     created. The sentence 'This is awesome' is therefore split into three iterables 'This', 'is'
                     and 'awesome'. To isolate a specific word in the list, you could apply the for loop and apply
                     commands to each individual word in the sentence. For advance filtering, you could apply to
                     string splits and loop through to isolate singular letters of words of the sentence. The last
                     example shows you string splitting using the comma as a delimiter. The output is different
                     because one comma splits the phrase 'This, is awesome' so the list is made of two iterables
                     'This' and 'is awesome'. Printing the iterables to screen separated by a new line produces the
                     output above.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                q_4 = input('Where is help needed, split or find? ')
                if q_4 == 'split':
                    help(x.split)
                elif q_4 == 'find':
                    help(x.find)
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 32:
            print('''
                     LIST COMPREHENSION
                     There are many tips and tricks which can both save space and execute code at a faster
                     rate in python. The phrase 'pythonic' has been coined to execute python commands in the
                     most aesthetic and efficient manner. One of this tips is understanding list
                     comprehension.
                     List comprehension is an efficient way of appending to a list with a for loop in a single
                     line. Extensive practice and examples will highlight this.

                     example 1) x = ['john', 'jack', 'magenta']
                                y = []
                                for i in x:
                                    y.append(i)
                                print(y)

                     example 2) x = ['john', 'jack', 'magenta']
                                y = [i for i in x]
                                print(y)

                     The two examples above show two versions of code that achieve the same result, one of which
                     uses list comprehension and the other, the for loop and list append method. The idea of list
                     comprehension is to always start at the back and think through forward. You want to make a list
                     involving the iterables of list x and appending them to y using a for loop. So the first step
                     is to create an empty list like follows:

                     y = []

                     You want append to the list using values in a for loop, so you add a for loop within the empty
                     list, which python understands as commanding the empty list to do something with a for loop, but
                     that something hasn't been specified yet. At this stage you enter:

                     y = [for i in x]

                     This tells python you want to iterate through previous list x and do something to list y using the
                     for loop. To append to list y using iterables from list x in the for loop you simply write:

                     y = [i for i in x]

                     The last step tells python what you want to achieve or command list y to do. Since you want to
                     add a new iterable from x to y, the i in front of 'for i in x' tells python to add that i in x
                     to empty list y until all i's in x are found. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(list)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 33 or x == 34:
            print('''STRING PALINDROME: LETTERS BACKWARDS TO FORWARD AND VICE VERSA''')
            query = input("If you wish to solve this problem individually enter yes, otherwise enter no: ")
            if query == 'yes':
                if query == 'yes':
                    print('''Congratulations on solving your this problem! Your well on your way to becoming
                             a programmer''')
                    question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                    if question == "help":
                        help()
                        q_2 = input("Do you wish to learn more, enter yes or no: ")
                        if q_2 == 'yes':
                            x = int(input("Enter another episode you wish to learn about: "))
                        else:
                            break
                    if question == "quit":
                        window = False
                    if question == "more":
                        x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         The solution to this problem will be broken down into a series of logical and
                         intuitive steps.

                         The first step is to understand exactly what we're aiming to achieve. The idea is,
                         a string variable should be entered and the user should be able to acquire
                         True if a word is the same backwards as forwards or False if this is not True.

                         The first test is to enter a string a find a method of reversing the letters in the
                         word backwards. Eventually a function needs to be defined, but for primary purposes
                         we need to find a method to which reverses the letters in a word backward.

                         >>> name = 'john'
                         >>> name[:-1]
                         >>> 'joh'

                         >>> sen = 'john is dope'
                         >>> sen[:-2]
                         >>> 'john is do'

                         >>> sen = 'john is dope'
                         >>> sen[:10]
                         >>> 'john is do'

                         In order to understand how to order a string backwards, it is vital to truly
                         register the power and applications of string indexing with negative and positive
                         numbers. In the first scenario, name stores value 'john' and the negative string
                         index reads the string from the first to the last index, excluding the last
                         index, which in example 1 is string 'n'. The output is 'joh' because the last
                         'n' is excluded in the search. The way to think about negative string indexing is
                         to reverse the way you think of positive string indexing. In the first example, where
                         name is assigned value 'john', the letters 'j', 'o', 'h' and 'n' and assigned index
                         values starting at zero in chronological order; 'j' is assigned index zero, o is
                         assigned index 1, h is assigned index 2 and n is assigned index 3. Reversing this idea,
                         negative string indexing starts from the last letter of the string forward; 'n' is
                         string index '-1', h is string index -2 and so forth. In other words, the same output
                         in the first example can be acquired by indexing through all the strings up till index
                         three which is value 'n' where the cycle ends. More substantive examples are evident through
                         examples 3 and 4 which practically achieve the same result in two ways. Now that you
                         have a better idea of string indexing, it is time to dive into double string indexes.

                         >>> name = 'john'
                         >>> name[::-1]
                         >>> 'nhoj'

                         >>> sen = 'john is dope'
                         >>> sen[::-2]
                         >>> 'eo ino'

                         >>> sen = 'john is dope'
                         >>> sen[::-1]
                         >>> 'epod si nhoj'

                         The last index is known to python as the stride. The stride tells python how many
                         steps to take before reading the next index in a string. A stride of 1 meaning [::1]
                         tells python to interpret all the letters in the string because the first ':' index
                         between the square brackets defines the range to read the letters or word in the
                         string word/sentence.

                         >>> name = 'john'
                         >>> name[2:3]
                         >>> 'h'

                         >>> name = 'john'
                         >>> name[0:2]
                         >>> 'jo'
 
                         >>> name = 'john'
                         >>> name[:]
                         >>> 'john'

                         In these examples, it is made apparent that specifying the range of string indexes
                         slices the word or letter at the right interval to acquire a sub-string of the original
                         word. When no string index range is applied, python understands this as printing the
                         index value of the first and last non-spaces of the word or sentence stored as the
                         variable. In the last example, there isn't a space before letter 'j' so python starts
                         indexing from this string until the last non-space which is after the letter 'n'. The bauty
                         of string indexing is the last point is not indexed, so the penultimate letter before
                         the last non-space is the letter 'n'. This prints out the entire string when no boundarues
                         are specified.

                         [::1] tells python to index and read through all the characters of the string specified
                         with a stride of 1, meaning after every letter in the word, read the next and the next
                         until the whole string is read and indexed and printed to the screen. If the stride is
                         set to 2, it tells python that after the first letter in the string, skip 2 and index
                         every second letter.

                         >>> name = 'john'
                         >>> name[::2]
                         >>> 'jh'
 
                         >>> name = 'john'
                         >>> name[::3]
                         >>> 'jn'

                         In these last examples it is clear how stride works. Negative strides work congruently
                         in the reverse manner. When stride is 1, python indexes and reads every letter in the
                         string. As you know already, negative string indexing starts from the last letter in the
                         string to the first. So a stride of negative 1 reads the last letter of the string first
                         and then the next etc. This is exactly what we expect as a palindromic word. Now we have
                         the tools to create a palindrome we can define a function that tests it.

                         >>> name = 'john'
                         >>> name == name[::-1]
                         >>> False

                         >>> name = 'dad'
                         >>> name == name[::-1]
                         >>> True

                         Note that python returns booleans when a condition is posed. The first
                         example shows the word 'john' is not palindromic, but 'dad' is. All we have to do
                         is create a function that returns True or False if a word or phrase is a palindrome.

                         def palin(string)
                         'enter a string to test whether it is a palindrome (same backwards as forward)'
                         string.lower()
                         if string == string[::-1]:
                             print('True')
                         else:
                             print('False')

                         palin('Bob')
                         palin('michael')
                         palin('dad')

                         output: True
                         output: False
                         output: True

                         It is important to take note of the string.lower() method thrown into the function
                         which guarantees that palindromes which start with uppercase letters will be considered.''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 35 or x == 36:
            print('''
                     PRIME NUMBERS
                     The aim of this episode is to find a way to print to the screen True if
                     a number is prime and False if a number isn't. The words True and False are
                     not important, words like yes or no or correct and incorrect can also be used
                     to inform us of prime numbers and numbers that aren't prime''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                          The solution to this problem will be broken down into mutiple steps.

                          As we are expected to take in a number and check against a condition,
                          a function must be defined. This function should take in one argument, that
                          being the number which the user wishes to check against two criteria: prime
                          or not prime.

                          def is_prime(num):
                              'enter a number to check if its prime or not prime'

                          Having defined out function, we must consider the conditions of a prime number.
                          1 isn't a prime number so first prime number must always begin at 2. This is
                          crucial to understand because every number is divisible by 1 and 1 by itself.

                          def is_prime(num):
                              'enter a number to check if its prime'
                              for i in range(2,num):
                                  if num%i != 0:
                                      print("True")
                                  else:
                                      print("False")
                                      
                          is_prime(5)
                          is_prime(6)
                          is_prime(8)

                          output: True
                                  False
                                  False

                          The function above is a handful to take in, so we will break it down into smaller
                          steps. As we are trying to check if a number (excluding 1) is prime, we must check
                          if that number is divisible by every number up till the number itself. This is
                          exactly what the for loop and range function achieves. Remember that the range
                          function iterates through every number starting from a specified point up till a
                          maximum number, excluding the maximum itself. The condition of a prime number is that
                          it cannot be divisible by any number, only by itself. Specifying the maximum range
                          as the number itself achieves this result because the number is excluded in the list of
                          possible values. A prime number is not divisible by any number apart from itself.
                          Therefore, the for loop satisfies our aim, enabling us to try every number in a
                          range starting from 2 (because 1 is excluded) until the only natural number before
                          the number itself. A way to check for the divisibility condition uses the modulo
                          function. If you're unfamiliar, the modulo function returns the remainder if
                          two numbers aren't mutiples of each other. If our number has a modulo that is not
                          equivalent to zero, it means that it leaves a remainder and that it isn't divisible
                          by that number. The for loop checks against all natural numbers until the user's
                          number, applying the modulo condition such that the modulo musn't be equivalent to zero.
                          This implies that the number is prime. The else condition suggests the reverse of a number
                          being prime, meaning that one iterable of all natural numbers until a number before
                          the specified number is a multiple of the user's number. The if statement is used in
                          this instance because we one the cycle to break when the first instance of this condition
                          is met, meaning that the number is no longer prime if it has even a single mutiple excluding
                          one and itself. In our example, the number 5 is prime because no integer from 2 until
                          4 is a multiple of 5. This returns a False as the if condition is unmet and an else
                          condition is supplied. The next two numbers are not prime so we expect a False as
                          shown above. However, the above function so to speak is not 'pythonic' because it
                          uses a for loop and we're required to command boolean operators True or False when the number
                          is prime or isn't. A much simpler function is as follows:

                          def is_prime(num):
                              'enter a number to check if its prime'
                              for i in range(2,num):
                                  return num%i != 0
                                      
                          print(is_prime(5))
                          print(is_prime(6))
                          print(is_prime(8))

                          Using python's default boolean, we do not need to supply additional if or else
                          statements to check whether a number is or isn't prime. If a condition is unmet,
                          python retuns False which is exactly the result we want to achieve. The only
                          step we added is the print function because returning a value creates a new variable
                          but to show the result we must print the value. This is a much more 'pythonic'
                          function only using a single return and for statement.''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 37:
            print('''
                     DOWNLOADING AND INSTALLING PYTHON TO YOUR COMPUTER
                     To download python into your computer, simply search for python on your browser,
                     find python.org and click download where it requested. When downloaded, read through
                     the package installer, click continue through the user agreement's and terms and condition
                     pages. When you double click on the installer it will install it to your computer''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                break
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 38:
            print('''
                     CREATING A REVERSE NUMBER TRIANGLE
                     The purpose of this episode is to create a number triangle that prints numbers
                     in ascending order following the format below:

                         1
                        12
                       123
                      1234
                     12345

                         1 
                        1 2 
                       1 2 3 
                      1 2 3 4 
                     1 2 3 4 5 ''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         The solution will be broken down in several steps.

                         To begin resolving this problem we must take a few things to mind.
                         We must construct a function that asks the user for a number that
                         indicates the size of their reverse number triangle.

                         def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'

                         The next step is considering the format of the spaces we expect to see
                         before the first number is printed to the screen. To create a condition
                         that iterates through a range of numbers and prints spaces given the size
                         of those numbers, we utilize the for loop and the range function, using the
                         user's number as the maximum range.

                         def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'
                             for i in range(num):
                                 print('i', end='')
                                 
                         rev_num_triangle(5)
                         
                         output: 01234

                         In this experiment, we iterate through numbers from 0 to the number specified
                         excluding itself. To print numbers starting from 1 to 5 we alter the starting
                         point of the range to 1.

                         def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'
                             for i in range(num):
                                 print('i', end='')
                                 
                         rev_num_triangle(5)
                         
                         output: 12345

                         We've obtained the desired numbers we want to print to the screen but the format
                         is still incorrect. We want numbers printed in ascending order after a number
                         of spaces equivalent to the size of the maximum number entered into the function.
                         The number of values is also incorrect because we require 15 numbers ranging from
                         1 to 5 printed to the screen. This requires a nested for loop with a separate
                         iterable 'j'.

                         def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'
                             for i in range(1,num):
                                 for j in range(num-i,1,-1):
                                     print(' ', end='')
                                 print('*')
                                 
                         rev_num_triangle(5)

                         output:   *
                                  *
                                 *
                                *

                         The format of the spacing has been achieved at this stage. The first for loop
                         iterates through numbers within a range starting from 1 up till the user's
                         number (excluding the number itself). The embedded for loop is required to print the
                         spaces at the correct positions. After the first number of the first for loop, we are
                         required to print the same amount of spaces as the number specified by the user in
                         descending order. In this example, 5 spaces then 4,3,2 and 1. The first instance is
                         number 1, as specified in the start argument of the first for loop. The second for loop
                         is related to the first but spaces are printed reversely, so we take the user's number
                         and subtract it with each value in the for loop printing the number of spaces equivalent
                         to the user's number and decrementing by 1 space every iteration through. In the first
                         instance, the user's number is equivalent to the number of spaces, which in the example
                         above is 5. Note that only four levels are currently visible. This is because we start at
                         1, 5 subtracted by 1 is 4 and this refers to the number of tiers printed to the screen. After
                         iterating through a number of spaces equivalent to the iterables instant size, the embedded
                         for loop is closed and an asterisk is printed as the placeholder of the 5th position. Five
                         tiers are required, so the format is still slightly incorrect.

                         def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'
                             for i in range(1,num):
                                 for j in range(num+1-i,1,-1):
                                     print(' ', end='')
                                 print('*')
                                 
                         rev_num_triangle(5)

                         output:    *
                                   *
                                  *
                                 *

                         This problem is resolved adding 1 to the embedded for loop. In this instance, instead
                         of starting from the number specified subtracted with the first number in for loop 1,
                         we subtract the number added to by 1 with the first iterable of the initial for loop.
                         This is equivalent to to 6-1 or 5, which is the required spaces in the formatting of the
                         reverse number triangle. The final solution is close, all that is left is printing the
                         numbers. Note that the numbers must be printed in ascending order after spacing. The
                         number values are also equivalent to the numbers we are expected to iterate through in
                         the first for loop. Therefore, we can manipulate this relationship to print a
                         descending amount of spaces, following an ascending value of numbers. This is made more
                         clear through visible results.

                         def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'
                             for i in range(1,num):
                                 for j in range(num+1-i,1,-1):
                                     print(' ', end='')
                                 for k in range(1,i+1):
                                     print(k, end='')
                                 print()

                        output:    1
                                  12
                                 123
                                1234
                               12345

                        The desired result is printed to the screen. In the above function, an extra embedded
                        for loop is required to not only loop through spaces but print values in a specified
                        manner in ascending order. Using a for loop with an identical range as the intial
                        loop, we iterate through numbers starting with 1 until the user's number (but excluding it).
                        We all parts together, we can explain what occurs to the first number of the function
                        to make light of the pattern applied to the remainders. The first value of for loop 1 is 1,
                        an embedded for loop iterates through the user's number added to 1 subtracted with the
                        first iterable in for loop 1. This is equivalent to 5. The first value is equivalent to 5,
                        so 5 spaces are printed to the screen. With the same indentation level as the previous loop,
                        a separate for loop iterates through values of the initial for loop up until the number
                        the user specifies (and excluding it). We want the numbers to print on a single line so
                        we supply an end argument to each embedded loop. When all iterables are exhausted for
                        both the spacing and ascending values of numbers in the triangle, the embedded loop is ended
                        and python reads the print() as printing each of these values and a new line. On this new line,
                        the embedded loop is restarted with a decremented space and with a larger value range of 2, so
                        4 spaces are printed followed by numbers ranging between 1 and 3. The numbers
                        within this range are 1 and 2 so 4 spaces and numbers 1 and 2 are printed on the same line. This
                        process continues until all values of the initial for loop are tried. This is identical to
                        the number specified. The second format in the solution to this problem is acquired by supplying
                        a space in the end argument of the second embedded loop.

                        def rev_num_triangle(num):
                             'enter a number indicating the size of your reverse number triangle'
                             for i in range(1,num):
                                 for j in range(num+1-i,1,-1):
                                     print(' ', end='')
                                 for k in range(1,i+1):
                                     print(k, end='')
                                 print()
                
                        output:     1 
                                   1 2 
                                  1 2 3 
                                 1 2 3 4 
                                1 2 3 4 5 ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 39:
            print('''
                     CREATING A TIMES TABLE
                     This episode asks us to produce a times table given the user's choice.''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    break
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
                    episode(x)
            else:
                print('''
                        The solution of this problem will be explained through several steps.

                        First, we must consider what exactly we are expected to construct. The
                        goal is to create a times table of the number specified by the user. To make
                        it more user friendly, we will ask the user for a prompt to enter a number and
                        a times table grid of all times tables of that number will be created.
                        This will be achieved using the nested for loop, the input function, and a
                        function to be applied to each value in the nested loop obtaining the desired
                        times table shape and values. The first step is the format. The user enters
                        a number so we define a new function with an input.

                        def times_table():
                            x = int(input("Enter a number: "))
                            for i in range(x+1):
                                print('*')

                        times_table()

                        output: Enter a number: 5
                        output: *****

                        As the above outcome demonstrates, the number of asterisks printed to the screen
                        is correct, but we require a times table grid equivalent to 5 rows and 5 colums of
                        25 values. We still require 20 more values. To achieve this outcome a supplemental
                        nested for loop is required. In each row we should print the number of columns
                        equivalent to the number entered. To do this we are required to add an embedded for
                        loop with a range equivalent to the initial loop.

                        
                        def times_table():
                            x = int(input("Enter a number: "))
                            for i in range(x+1):
                                for j in range(x+1):
                                    print('*', end='')
                                print()

                        times_table()

                        output: Enter a number: 2
                        output: ***
                                ***

                        In this example, the string format has been achieved. Now we must enter a function
                        that calculates the times table for the entered number. To do this we utilize the
                        asterisk multiplication between iterables of the nested and initial for loop.
                        
                        def times_table():
                            x = int(input("Enter a number: "))
                            for i in range(x+1):
                                for j in range(x+1):
                                    print('i*j', end='')
                                print()

                        times_table()

                        output: Enter a number: 2
                        output: 000
                                012
                                024

                        The correct times table has been created. When the value 2 is entered into
                        our function, the range of numbers that are printed to the screen is set
                        to the user's number, in which case is 2. This is neccessary to restrict
                        the size of the times table to the user's value and nothing larger or smaller.
                        Once the range is set, python iterates through values starting at zero until
                        2. As an embedded for loop is detected, the initial for loop is stopped at
                        zero. An equivalent range of values is applied to the embedded loop to generate enough
                        numbers in the format of a times table. There are typically the times table number
                        squared amount of values in a times table. For example, a times table of all numbers
                        ranging between 0 and 5 has 25 values. The above example illustrates that the 2 times
                        table has 4 values. The reason a 3 by 3 matrix of numbers is printed to the
                        screen concerns the case of zero's times with the numbers, which also result
                        to zero; hence, all the outcomes of the first row and column are equal to zero.
                        As python iterates through each value in the embedded loop up until the entered number,
                        the iterable 1 is fixed at zero and mutiplied by each iterable of the embedded loop.
                        After all iterables of the embedded loop are multiplied with the fixed iterable of
                        the first, python is instructed to print a new line and apply an identical reasoning
                        to the new line with the iterable of the first for loop incremented by 1. Once all
                        iterables of the first for loop are exhausted, the function breaks. This automates the
                        process because depending on the number entered originally, the size of the grid and
                        the stopping times table is related to the entered number. The first row and column
                        is always a row and column of zero's because zero multiplied with any number remains as
                        zero and for any value of an interable from the first for loop, multiplying it with zero
                        results to zero. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 40:
            print('''
                     LEAP YEAR FUNCTION
                     In this episode, a function that determines whether an entered year is a leap year will
                     be created. The basic conditions of a leap year is that it occurs every 4 years. Two
                     optional conditions that define a leap year are that leap years don't occur every 100 years and
                     they occur every 400 years''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    break
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                        As always, the solution is broken down through several simpler steps.
                      
                        First consider the conditions that a leap year must uphold. They must occur every
                        4 years and they optionally not occur every 100 years but do happen every 400 years.
                        We are defining a function because a user's input is required in this problem, specifying
                        whether the year entered is a leap year.

                        def leap_year(y):
                            'returns leap year if a leap year is entered and not leap year otherwise'

                        The function above takes in an input (the year to check) and now we must provide its
                        functionality. A key tool which is vital to resolving this problem is the modulo
                        function. If you're unfamiliar, there are other episodes that demonstrate the purposes
                        and applications of the modulo. In this instance, the modulo is neccessary to find
                        whether or not the year entered is a multiple of 4, whether it isn't a multiple of 100 and
                        is a multiple of 400. These are the neccessary conditions that define a leap year.

                        def leap_year(y):
                            'returns leap year if a leap year is entered and not leap year otherwise'
                            return y%4 == 0:
                            
                        leap_year(2000)
                        leap_year(1957)

                        output: True
                                False

                        The function returns the correct booleans given the year entered. 2000 is divisible by
                        4 and so the function tells us its a leap year. 1957 leaves a remainder of 1, so it
                        isn't a multiple of 4; and therefore, it doesn't satisfy the primary leap year condition.
                        We cannot utilize python's default return True or False statements like the above
                        example because extra conditions are required to properly define a leap year. That of
                        whether the year is not a multiple of 100 and is a multiple of 400.

                        def leap_year(y):
                            'returns leap year if a leap year is entered and not leap year otherwise'
                            if y%4 == 0:
                                if y%100 == 0:
                                    if y%400 == 0:
                                        print(str(y), 'is a leap year')
                            
                        leap_year(2020)
                        leap_year(1957)

                        output: None

                        Notice that for both entered years, the function doesn't print an output. This is
                        because an else statement wasn't provided to our function informing it of what to
                        execute in the instance of the failing condition of the initial if statement.

                        def leap_year(y):
                            'returns leap year if a leap year is entered and not leap year otherwise'
                            if y%4 == 0:
                                if y%100 == 0:
                                    if y%400 == 0:
                                        print(str(y), "is a leap year")
                                    else:
                                        print(str(y), "isn't a leap year")
                                else:
                                    print(str(y), "is a leap year")
                            else:
                                print(str(y), "isn't a leap year")
                                        
                        leap_year(2020)
                        leap_year(1957)

                        output: 2020 is a leap year
                                1957 isn't a leap year

                        This is the exact output we were looking for. 2020 is a leap year because it is
                        divisible by 4 and it isn't divisible by 100. What python does in this instance is
                        it compares our value against the first if statement, this is True as 2020 is
                        a multiple of 4, so our value is proceeded to the second tier, it is compared against
                        the second conditional if statement. 2020 leaves a remainder of 20 when divided with
                        100, but a year that isn't divisible by 100 is a leap year. The year entered doesn't
                        satisfy the second condition, so the else statement is executed, which says that
                        the year is a leap year because it doesn't occur every 100 years. For a year that
                        is both a multiple of 4 and 100 but not 400, the outcome isn't a leap year, following
                        the conditions of the third tier if statement which states that if the year doesn't occur
                        every 400 years, it isn't a leap year. This is true and our function works. Note that
                        the embedded else statements must be added to our function otherwise nothing is printed
                        to the screen because python's choices are cut if the initial if statement conditions are
                        unmet by the entered year.''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 41:
            print('''
                     CREATING A GRID OF VALUES
                     Producing a grid of the following formats:

                     + - - - - - + - - - - - + 
                     |           |           |           
                     |           |           |           
                     |           |           |           
                     |           |           |           
                     |           |           |           
                     + - - - - - + - - - - - + 
                     |           |           |           
                     |           |           |           
                     |           |           |           
                     |           |           |           
                     |           |           |
                     + - - - - - + - - - - - + 

                     + - - + - - + 
                     |     |     |     
                     |     |     |     
                     + - - + - - + 
                     |     |     |     
                     |     |     |     
                     + - - + - - +  ''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         The solution will be presented through a series of steps.

                         First, we must consider what we are expected to create. In both the formats
                         above, we are required to create a grid of '+' and '-' horizontally and
                         '|' vertically. To create this shape we should have a function that asks
                         the user to enter a number indicating the size of their grid. When 5 and 2 are
                         entered into our function, the following grids must be produced to verify whether
                         our function is working. The grid is comprised of two major formats. The first
                         major format is an addition sign followed by dash lines equivalent to the user's
                         number repeated three times. The second is a vertical line followed by spaces
                         equivalent to the number entered, also repeated thrice. We notice a pattern
                         emerging: the number of spaces between vertical lines and the number of dashes is
                         equal to the number entered.

                         def top(n):
                             'enter a number indicating grid size'
                             x = '+ '
                             y = '- '*n
                             print((x+y)*2 + x)

                         top(3)
                         top(5)

                         output: + - - - + - - - +
                                 + - - - - - + - - - - - +

                         The first major pattern has been achieved through our function. The function works
                         using string concatenation. We define a function taking one argument, namely the
                         size of the grid required. Two separate variables are defined within our function
                         that accomodate the entered number. The variable x is assigned the addition placeholder,
                         whilst the y variable is assigned the dash followed by a space multiplied by the
                         entered number. This is done because we want a number of dashes equal to the entered
                         number. Both these variables are of type string, so string concatenation is possible.
                         adding two strings with the addition symbol is equivalent to printing them one after
                         the other without spaces. We want a repeated pattern of an add sign, followed with a
                         number of dashes equal to the user's number. This is always repeated twice so we multiply
                         the concatenation of these string variables by 2. Doing this we miss an additional add
                         sign which is always going to occur. So we forcibly concatenate an extra x variable which
                         concatenates to the end of the last dashed line and creates the desired format. Now we
                         can consider the middle part of our box.
                         
                         def middle(num):
                             'enter a number indicating grid size'
                             x = '|'
                             y = '  '*n 
                             for i in range(num):
                                 print((x+y)*3)
                                 
                         middle(3)
                         
                         middle(5)

                         output:|      |      |
                                |      |      |
                                |      |      |

                                |           |          |
                                |           |          |
                                |           |          |
                                |           |          |
                                |           |          |

                        The second major format has been acquired. Assigning the vertical line placeholder
                        to variable x and a double space placeholder to variable y, we want to automate
                        the process the same number of times as the number entered into our function.
                        Therefore, using the for loop in the range of our number entered focuses the
                        number of repetitions to the number entered. Adding both the top and middle functions
                        into a box_top function we get the following:

                        def box_top(num):
                             'enter a number indicating grid size'
                             top(num)
                             middle(num)

                        box_top(3)

                        output:+ - - - + - - - +
                               |      |      |
                               |      |      |
                               |      |      |

                        As this step illustrates, the format of the middle function is one step off
                        the place of the top function. To match the two, we require to add an extra
                        space to the string variable y that handles the spaces in the middle function.

                        def top(n):
                             'enter a number indicating grid size'
                             x = '+ '
                             y = '- '*n
                             print((x+y)*2 + x)

                        def middle(num):
                             'enter a number indicating grid size'
                             x = '|'
                             y = '  '*n + ' '
                             for i in range(num):
                                 print((x+y)*3)

                        def box_top(numb):
                             'enter a number indicating grid size'
                             top(numb)
                             middle(numb)

                        box_top(3)

                        output:+ - - - + - - - +
                               |       |       |
                               |       |       |
                               |       |       |

                        We have obtained our desired format. Now we just need to repeat the box_top once more
                        and add another top to achieve the result:

                        def top(n):
                             'enter a number indicating grid size'
                             x = '+ '
                             y = '- '*n
                             print((x+y)*2 + x)

                        def middle(num):
                             'enter a number indicating grid size'
                             x = '|'
                             y = '  '*n + ' '
                             for i in range(num):
                                 print((x+y)*3)

                        def box_top(numb):
                             'enter a number indicating grid size'
                             top(numb)
                             middle(numb)

                        def box(number):
                            'enter a number indicating grid size'
                            box_top(number)
                            box_top(number)
                            top(number)

                        box(3)

                        output:+ - - - + - - - +
                               |       |       |
                               |       |       |
                               |       |       |
                               + - - - + - - - +
                               |       |       |
                               |       |       |
                               |       |       |
                               + - - - + - - - +

                        Entering any number into our function will designate the size of the grid
                        you want displayed to the screen. It also important to note at this point that
                        the same result can be achieved using embedded functions. The only important
                        thing to understand is embedded functions must be written in the way that python
                        is able to comprehend which function comes first. An example of this is defining
                        the box function before the top function. This is incomprehensible because
                        box takes in the top function and the oppposite is untrue. the top function doesn't
                        take in box so python doesn't know where the extra top function came from. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 42:
            print('''
                     FINDING THE NTH PRIME NUMBER
                     This episode discusses how one would find the nth prime number
                     given a specified number. For example, if the user wants to find
                     the first 5 prime numbers, the fifth prime number should be
                     printed to the screen''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                        Finding the nth prime number.

                        The solution to this problem will be broken down into a series
                        of logical steps.

                        The first step is to always understand what the expectation is.
                        We are required to create a function which, upon entering a
                        number, gives us the prime number in that position. This can
                        be confusing, so the example below illustrates the idea of
                        this function.

                        >>>nth_prime(3)
                        >>>5

                        >>>nth_prime(5)
                        >>>11

                        This tells us that the third prime number is 5 and the 5th prime number
                        is 11. We are now in a position to define a function which prints
                        the desired values. Within this function, we will be using an embedded
                        function is_prime, which was explained in a previous video. What is does
                        is return True if a number is prime and False otherwise. This is vital
                        to defining our current function because we need a condition that
                        tests for prime numbers.

                        def nth_prime(num):
                            'enter a number and the nth prime number will be printed'
                            nat = 3
                            prime = 2
                            if num == 1:
                                return 2

                        The step above provides a docstring to the user, guiding them around our
                        function and its applicabilities. The variable natural is aliased as nat,
                        which will be the starting position. The value 3 is the starting count
                        because 1 is not a prime, so it is excluded. We begin at the first prime
                        number after 2 which is 3. Now we need to think about some conditions.
                        We want to test all numbers in the range of the entered number and when
                        our prime count matches the entered number, the neccessary amount of
                        primes have been considered and we print our natural number nat at that point.
                        As for our natural number, we need to create an incrementation by some
                        value each time that number is prime. A typical prime number occurs every
                        second number. This could be the amount we increment our natural number
                        to focus our search on only prime numbers. There are some exceptions where
                        primes aren't split by 2 values such as 7 and 9, but for most cases the former
                        is true.

                        def is_prime(numb):
                            'returns True or False is a number is prime'
                            for i in range(numb):
                                return numb%i != 0

                        def nth_prime(num):
                            'enter a number and the nth prime number will be printed'
                            nat = 3
                            prime = 2
                            if num == 1:
                                return 2
                            while prime < num:
                                nat += 2
                                if is_prime(nat):
                                    prime += 1
                            return nat

                        print(nth_prime(3))
                        print(nth_prime(5))

                        output: 5
                                11

                        The function above is working, now for the explanation. If you haven't
                        watched the is_prime video already, go ahead and watch it. What the
                        is_prime does is returns True or False if the number entered is or isn't
                        prime. We want to expand that idea to test for all prime numbers, so
                        we formulated a new function which uses the previous function as a
                        condition that our numbers must satisfy to be considered prime. In our
                        function we used incrementation and a while loop. The while loop is used
                        in this situation because we want a recursive condition and an if
                        statement will only return the first instance of when the condition is met.
                        This would have ignored all the instances of primes after the first prime
                        met the condition of the if statement. The idea was to stop the loop when
                        we printed out all primes until the entered number. Therefore, we
                        assigned 2 to our prime counter variable, as the first prime number (because
                        1 is not a prime number). If our number entered is 2, we will obtain 3
                        because the while loop condition would have been unmet but our function
                        returns the first natural number which starts at 3. This is logical because
                        the second prime number is 3 as 1 is not prime. If the numb is greater
                        than 2, than we increment the natural number by 2, because prime numbers
                        are typically separated by 2 values. If the new natural number satisfies
                        the is_prime function, then the prime counter increases by 1. When the
                        prime counter is greater than our number the while loop ends and the
                        last natural number saved is printed. The values 5 and 11 printed are
                        equivalent to the 3rd and 5th prime numbers. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 43:
            print('''
                     CREATING A NUMBER DIAMOND
                     A number diamond should be printed to the screen in the following
                     formats. The user is also able to transform the size of the number diamond
                     by entering a number corresponding to that number diamond size.

                            1
                           121
                          12321
                         1234321
                        123454321
                         1234321
                          12321
                           121
                            1


                              1
                             121
                            12321
                           1234321
                          123454321
                         12345654321
                        1234567654321
                       123456787654321
                      12345678987654321
                     12345678910987654321
                      12345678987654321
                       123456787654321
                        1234567654321
                         12345654321
                          123454321
                           1234321
                            12321
                             121
                              1    ''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                          This problem will be separated into smaller steps.


                          The first issue to resolve is the formatting of our number diamond.
                          The shape of the number diamond looks similar to that of combined
                          reverse number triangles and number triangles. If you haven't seen
                          those episodes already, it might be an idea to see them because the
                          logic and formatting used to solve this problem is similar to the logic
                          used to solve those problems. We are interested in creating a function
                          which takes in values from the user and creates a number diamond.

                          def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num):

                          The first step is to create the function we are permitted to use and
                          enter the docstring guiding user's through the function. It is
                          neccessary to use at least one for loop in this problem because
                          we want to iterate through numbers to create the neccessary format
                          of how the numbers should print to the screen. The next step is formatting
                          the spaces.

                          def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  print('*')

                          num_diamond(5)

                          output:    *
                                    *
                                   *
                                  *
                                 *

                          At this stage, we are testing the formatting of the spaces for the
                          first reverse number triangle. The example above demonstrates where
                          the spaces will occur given by the asterisk placeholder. We can easily
                          change the placeholder to an empty space by providing an empty argument
                          to the last print function. The problem is nothing would be printed to
                          the screen, so we wouldn't know whether our spacing is correct or not.
                          Therefore, it is advised to create a placeholder to check whether the
                          first step or our function works appropriately. The next step is to print
                          the required numbers in the reverse number triangle. The numbers descend
                          starting from small to large. We require an extra for loop with different
                          iterating values, namely k.

                          
                          def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  print()

                          output:     1
                                     12
                                    123
                                   1234
                                  12345

                          A reverse number triangle has been printed to the screen. The number
                          of levels is equivalent to the specified number controlled by the
                          first for loop. The second embedded for loop controls the amount
                          of numbers that will be printed to the screen. We want the amount
                          of numbers to increase in ascending order until the number entered.
                          You may notice that the first for loop iterates through numbers until
                          the specified number. We use this fact to create the range for our
                          second embedded for loop. This limits the amount of numbers printed
                          to the screen at any one level. The numbers printed to the screen also
                          correspond to numbers that always start at 1 and increase until the
                          number associated with that level is met. The second for loop already
                          implements iterables from the first for loop, so if we simply print
                          iterables of this last loop we achieve our aim of printing numbers
                          in ascending order and in ascending amounts. The only additional step
                          is to add a starting point of 1 to our last loop so we create a number
                          triangle starting at 1 instead of zero. In a separate step we will think
                          about how to create a separate triangle that starts at the last number
                          of this number triangle. This triangle has the same amount of levels, and
                          amount of numbers a line, only that the numbers are descending.

                          def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  for h in range(1,k):
                                      print(h, end='')
                                  print()

                         num_diamond(5)

                         output:     1
                                    121
                                   12312
                                  1234123
                                 123451234

                         The outcome is not totally correct because the numbers in the second
                         triangle should be decrementing, not incrementing. To do so, we need
                         to transform the logic in the third embedded print function. Remember,
                         the third for loop range controls the number of values printed to the
                         screen in each level. We want this number to be a maximum of four in
                         the last level and begin at zero. Recognize that the second embedded,
                         with iterable k, also limits the number of values printed to the screen
                         in each level. This solves our problem because we can match the range
                         of printed numbers in this for loop to the range of the previous for
                         loop that achieves the same result. The last step is to alter the third
                         print function. Notice that the number entered is constant, but
                         our third iterable by the entered number creates an issue. The first
                         instance would be 5 (if the entered number was 5) subtracted with 1 which
                         is 4. However, we want the largest numbers to be on the last tier, not the
                         first. Using iterables that ascend in size would be precisely what we need
                         to decrement our last iterable by the right amount to print decrementing
                         numbers with smaller starting values.

                         def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  for h in range(1,k):
                                      print(k-h, end='')
                                  print()

                         num_diamond(5)

                         output:     1
                                    121
                                   12321
                                  1234321
                                 123454321

                         The result above shows us that our function works for the top layer
                         of the ultimate number diamond. Using iterables of the second embedded
                         loop solved our problem because the range of our second loop was one
                         point larger than the last loop. This meant that for each iteration
                         through the second loop, the numbers would get larger by one size extra than
                         the last and the iterables in the last loop get larger given a bigger range.
                         Subtracting numbers from the second loop with incrementing numbers of the
                         last loop, creates smaller values. Subtracting a big number by another large
                         number creates a small number. This is the same logic as the relationship
                         between the printed values of these for loops.

                         The second challenge is to print values corresponding to the bottom layer
                         of our number diamond. We assign new for loops with different iterables
                         because we desire extra sets of iterations and tiers in the potential
                         number diamond. Consider the format of the bottom layer. There are
                         an equivalent amount of spaces as the number entered by the user. The
                         same iterable cannot be used because it will detriment the work
                         accomplished in creating the first part of the number diamond. We assign
                         a new iterable, namely f, with the same indentation as the for loop of i
                         iterables. If you want to focus on the bottom part independent of the first
                         part, you could optionally comment the first part which reserves the code
                         already entered for a later use. However, in the breakdown of the solution,
                         I will use all parts already created in one fell swoop. At this point, we
                         can test the bottom layer of the number diamond with asterisks to test whether
                         the spacing is correct.

                         def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  for h in range(1,k):
                                      print(k-h, end='')
                                  print()
                              for f in range(num+1):
                                  for l in range(i):
                                      print(' ', end='')
                                  print('*')
                                  
                         num_diamond(5)

                         output:     1
                                    121
                                   12321
                                  1234321
                                 123454321
                                 *
                                  *
                                   *
                                    *
                                     *

                         The result above clearly illustrates that the spacing used is correct.
                         Unlike the reverse number triangle, we space in ascending order through
                         each level. This is identical to the value of iterable i through each
                         iteration of the first for loop. Applying this to our advantage, we
                         create the correct format of the first triangle of the bottom layer.
                         The values we want printed are the also identical to the iterable
                         values in the first for loop. However, we want a descending amount of
                         them printed to the screen in each level. Therefore, we are required to
                         change the range of a separate embedded loop which controls the amount of
                         values printed to the screen at any one level.

                         def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  for h in range(1,k):
                                      print(k-h, end='')
                                  print()
                              for f in range(num+1):
                                  for l in range(f):
                                      print(' ', end='')
                                  for p in range(num-f):
                                      print(p+1, end='')
                                  print()

                         num_diamond(5)

                        output:      1
                                    121
                                   12321
                                  1234321
                                 123454321
                                  1234
                                   123
                                    12
                                     1

                        We have evidently printed the appropriate triangle of which quite
                        nearly forms the entire diamond shape. To achieve this we used an extra
                        embedded loop with iterable p. The range was controlled by subtracting
                        our number with iterable f. This was done because iterable f ascends in
                        size through each full loop. In the first loop, iterable f was saved as
                        0, because a starting range of 1 wasn't provided. Subtracting 5 by zero
                        results to 5. So we print numbers in the range of 5 (excluding 5 itself).
                        We don't require 5 because the number entered should be the center of the
                        number diamond. Limiting the range was to out advantage. Through each
                        iteration iterable f is incremented by 1 and subtracting a constant number
                        by a larger number results to a smaller number. The result is the picture
                        as above. The last part of the diamond is created by making one last
                        consideration. We want numbers to print in descending orders of value and
                        by a descending amount in each level. Note that the iterables of the
                        second embedded loop decrease through the reverse range, starting at the
                        users number until 1. We can tie this to another embedded loop which sorts
                        the last quarter of the diamond. 
                                    
                        def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  for h in range(1,k):
                                      print(k-h, end='')
                                  print()
                              for f in range(num+1):
                                  for l in range(f):
                                      print(' ', end='')
                                  for p in range(num-f):
                                      print(p+1, end='')
                                  for t in range(1,p+1):
                                      print(num-f, end='')
                                  print()

                        num_diamond(5)

                        output:      1
                                    121
                                   12321
                                  1234321
                                 123454321
                                  1234555
                                   12344
                                    123
                                     1

                        Evidently, the format of the last quarter is correct, but the numbers
                        printed are not quite right. Note that subtracting our number by
                        first iterable f fixes the value printed to each level as one number
                        until the first loop is iterated through and decremented by 1, which
                        results in value one less than the previous level. To resolve this
                        problem, we need to subtract an extra iterable that increases each
                        iteration through. Recognize that iterable t increases each iteration
                        through. Subtracting by a larger number creates a smaller value.
                        Applying this logic, we can subtract the last variable by an extra
                        t.

                        def num_diamond(num):
                              'enter a number that indicates the size of your diamond'
                              for i in range(num+1):
                                  for j in range(num+1-i,1,-1):
                                      print(' ', end='')
                                  for k in range(1,i+1):
                                      print(k, end='')
                                  for h in range(1,k):
                                      print(k-h, end='')
                                  print()
                              for f in range(num+1):
                                  for l in range(f):
                                      print(' ', end='')
                                  for p in range(num-f):
                                      print(p+1, end='')
                                  for t in range(1,p+1):
                                      print(num-f-t, end='')
                                  print()

                        num_diamond(5)

                        output:      1
                                    121
                                   12321
                                  1234321
                                 123454321
                                  1234321
                                   12321
                                    121
                                     1

                        The full number diamond has successfully been created. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
                    episode(x)
        if x == 45:
            print('''
                     CREATING A SECONDS CONVERTER
                     This video requires the programmer to create a way of changing
                     seconds into days, hours, minutes and seconds''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                        The solution to this problem will be broken down into a series of
                        steps.

                        The first step is to understand what we're require to make. We need
                        to define a function that asks the users for seconds and returns a
                        string printing the amount of days, hours, minutes and seconds given the
                        total seconds they entered. 

                        def secs(sec):
                            'enter a number of seconds and the amount of days, hours, minutes and
                            seconds corresponding to those seconds will be returned'

                        We defined a function with one argument which is the number of seconds
                        in question. The next step is to create a way of changing seconds into
                        days, hours and minutes.

                        It is noteworthy to mention that one day has 24 hours, and each hour is
                        comprised of 60 minutes and each minute of 60 seconds. So multiplying
                        24 by 3600 tells us how many seconds there are in one day. The same
                        logic applies to the number of seconds in an hour (3600) and the amount of
                        seconds in a minute (60). This is a good point to introduce floor
                        division because it is vital in the solution to this problem.

                        When one / is applied, we take a number and divide it by another. Single
                        division can leave decimals as the output. But floor division// leaves a
                        whole number value. This will become more useful in later episodes.
                        For our current purposes, we require floor division because we are not
                        required to create decimals in the amount of days or hours or minutes.
                        The amount is only required, without any floating points.

                        >>> 5/2
                        >>> 2.5

                        >>>5//2
                        >>>2

                        >>> 7/2
                        >>> 3.5

                        >>> 7//2
                        >>> 3

                        The two examples shared above clearly highlight the applications and
                        differences between normal division and floor division. We will make use
                        of this idea at a later stage of this problem. A pre-requisite to this
                        video is also an understanding of the modulo function. What the modulo
                        does is return the remainder of divisions. For instance, 12 % 5 is 2
                        because the division of 12 by 5 leaves 2 as a remainder. Earlier episodes
                        make apparent the multiple usages of the modulo when determining, for
                        instance, whether a number is a multiple of another like in the is_prime
                        function and the nth prime of a given sequence. In our current problem,
                        floor division is used to obtain the remainder of some amount of seconds
                        when our argument is provided and the question asks to produce the
                        number of days equivalent to those seconds and from those remaining seconds,
                        the amount of hours, minutes and seconds left. Let us initially consider
                        an arbitrary amount of days, hours, minutes and seconds,
                        deconstructing these arbitrary amounts into a single unit of total
                        seconds.

                        >>> 4:3:20:15
                        >>> 4*24*3600 + 3*3600 + 20*60 + 15
                        >>> 357615 - 357615%216000

                        The arithmetic above proves that an amount of days, hours, minutes and seconds
                        can be decomposed into a total amount of seconds. Aforementioned, a day is comprised
                        of 24 hours and within those hours, 3600 seconds (converting those hours to minutes and
                        then seconds). The same logic applies to the hours in the day, where we multiply those
                        number of hours by 3600, considering that every hour contains those amount of seconds. A similar
                        idea is used in the conversion of minutes to seconds, whereby every minute is 60 seconds.
                        Converting multiple minutes to seconds requires each of those minutes in their seconds counterpart.
                        Denoted last is the seconds. As we want a conversion to seconds, it is not neccessary to
                        adapt our ouput and we leave seconds unaltered. A secondary step is to understand
                        how we can use our pre-requisites of floor division and modulo to construct our function.
                        Shown a number of seconds, we first require to change those number of seconds to an equivalent
                        number of days. To accomplish this result consider what floor division does. As we expect
                        to convert our number of seconds to days, we reverse the logic of days to seconds. Multiplying
                        24 hours in a day by 3600 seconds within those hours outputs 86400.

                        def secs(sec):
                            'enter a number of seconds and the amount of days, hours, minutes and
                            seconds corresponding to those seconds will be returned'
                            days = sec//86400

                        The user enters an arbitrary amount of seconds and to achieve the amount of days
                        within those seconds, we divide those seconds by the amount of seconds in a day (86400).
                        Now that we have a seconds to day conversion, we begin to think about a conversion between
                        seconds to hours, minutes and to seconds themself. The amount of seconds in an hour is 3600
                        But we want a certain amount of seconds in hours. To do so, we return to the modulo function.
                        Using the modulo, we ascertain a remainder when to digits divide by one another. Following this strain,
                        we want our total number of seconds in terms of hours. Supposing that we have seconds
                        equal to a number of days, hours and minutes, how do we do this? Taking the modulo
                        of those number of seconds provides us with the remainding hours, minutes and seconds. The
                        step we shall take is to use the modulo between our specified seconds and the amount
                        of seconds in a day, respectively 86400. This returns the remainding number of hours and
                        minutes in seconds, discounting the number of days already passed. Seeing as the outcome
                        is still in seconds, we're required to change these seconds into hours. Consequently,
                        floor division is utilized in this situation. Dividing those remainding seconds by 3600, we surmount
                        to a smaller value. This smaller value is indeed the number of hours equal to those seconds
                        given. Applying the similar train of thought enables us to calculate the amount of minutes and
                        seconds within our arbitrary total seconds.

                        def secs(sec):
                            'enter a number of seconds and the amount of days, hours, minutes and
                            seconds corresponding to those seconds will be returned'
                            days = sec//86400
                            hours = sec%86400//3600
                            minutes = sec%3600//60
                            seconds = sec%60
                        
                        The function above dictates the amount of days, hours, minutes and seconds with a single argument
                        of total seconds. Discussed above was the ideology of converting seconds to days and hours. Alike is
                        the method of changing seconds to minutes and seconds themself. Now that we've distinguished
                        86400 seconds in a day, we want the amount of seconds in minutes. The modulo of our seconds
                        and 3600 outputs a remainder of hours within our total seconds. The outcome is substantial because
                        an extra step is still needed. Doing the modulo simply calculates the number of hours given
                        our seconds. But, we want those remainding seconds in minutes. Alas, an extra step of floor division
                        need be to guarantee minutes. Obtaining seconds themselves only asks of us to do the modulo
                        between total seconds and 60 seeing as we don't need to further convert our values into seconds, as
                        they're pre-existing seconds. Our function doesn't ouput a result because we lack a final print
                        statement to do this for us. 

                        def secs(sec):
                            'enter a number of seconds and the amount of days, hours, minutes and
                            seconds corresponding to those seconds will be returned'
                            days = sec//86400
                            hours = (sec%86400)//3600
                            minutes = (sec%3600)//60
                            seconds = (sec%60)

                            print('days', 'hours', 'minutes', 'seconds')

                        It is noteworthy that a bracket is required to separate each step from the other. The bracket
                        corresponds to the directive needed to inform the system of our initial step.

                        ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 46:
            print('''
                     RECURSIVE FUNCTIONS
                     This episode will discuss, through a simple example, the application
                     of recursion, or recursive functions in python
                     A recursive function is one that repeats the same function to a set
                     of arguments or numbers. For example, we have a set of numbers and we want
                     to add them all together. There are two ways to achieve this result. One of
                     the ways is to create a multiple argument function, with the for loop and
                     we add each of those arguments in our for loop with each other.
 
                     def adder(*args):
                         'enter numerous digits for which the function will output a subtotal'
                         for arg in args:
                             num = 0
                             num += arg
                         print(num)

                     Through this function, we denote the asterisk which informs python that our function
                     needs multiple arguments, namely the numbers we expect to add together. These arguments
                     create a list of iterables. Storing our starting value num as zero, we iterate through
                     each digit in our list and add the consecutive number in our argument. Printing our
                     stored num outside the loop constructs the final subtotal of all our values added to each
                     other. For information about the asterisk and the python arithmetic shortcut +=, browse
                     through an alternate episode. In this episode, an alternate method will be demonstrated to
                     also add numbers together.

                     def adder(arg):
                         'enter a number and all numbers until that number will be subtotaled.'
                     if arg == 0:
                         return arg
                     else:
                         return arg + adder(arg-1)

                     print(adder(4))

                     output: 10
                    
                     The example above is not quite adding multiple random numbers to each other.
                     Instead, it stores the users number as arg. If the user's number is zero, it
                     returns the last stored number as arg. Otherwise, the user's number is added
                     to a number less by 1 passed through the function. It is important to place
                     an ending point to this function because without the initial if statement, the
                     function will iterate continuously through all numbers one less than the previous,
                     which is infinite. We are discounting negative numbers, so the last natural non-
                     negative number is zero; hence, our ending point. The number 4 is provided, to
                     which gives an output of 10. This is because, 4 added to 3 to 2 and 1 is 10. We
                     achieved the desired result so our function is working. This is a beautiful
                     application of recursion through python. A separate example of recursion is
                     through factorial. For those who are unfamiliar to the mathematics of factorials,
                     we require a number multiplied by a number one less than itself until 1.
                     For instance, 4 factorial is 4 times 3 times 2 times 1, which is 24. We desire
                     a function that constructs this output given any provided number argument. To
                     do this, two solutions will be presented, one more pythonic than the other. The
                     first will achieve the result using longer lines of code, whereas the second is
                     shorter.

                     def factorial(x):
                         'enter a number and obtain its factorial'
                         total = 1
                         while x > 0:
                             total *= x
                             x -= 1
                         print(total)

                     factorial(5)

                     output: 120

                     Five factorial is indeed 120, so the above function is woking properly. The function
                     requests the users' number and it stores value 1 to total. A while loop is required
                     because we want to apply our function to more than one instance of a condition. The
                     condition being that all numbers one less than the previous until 1 are multiplied by
                     each other. Therefore, our saved total must be altered through each instance of our condition.
                     The while loop condition is such that our number needs to be greater than zero because
                     we don't want negative numbers in our summative multiplier. The first instance of total is
                     1 and multiplying it by our number 5, we save the new total as 5. Then our number is subtracted
                     by 1 to 4, multiplied again by our stored value of 5, which outputs 20. This is repeated
                     until the last instance of 1 because subtracting 1 by 1 is zero. Ultimately, all numbers
                     one less than the previous until 1 are multiplied to each other cumulatively as the
                     factorial. This is a very long process which can be dramatically simplified using
                     recursion. The same result through a different method will be supplied below.

                     def factorial(x):
                         'enter a number and obtain its factorial'
                         if x == 1:
                             return 1
                         else:
                             return x * factorial(x-1)

                     print(factorial(4))

                     output: 24

                     We achieve the desired output confirming the vailidity of the function. The user
                     is again expected to enter a number, if the user's number is equivalent to one, an
                     if condition is met which returns 1 as the output. Otherwise, the user's number
                     is multiplied by one less than the user's number passed through the factorial
                     function until 1. The first instance of this function is 4, so x is stored as 4, the
                     number is larger than 1, so the initial if condition is unmet and the number is
                     multiplied by 3 passed through the function. This process is repeated until 2, when
                     the factorial of 1 meets the criteria of the first condition, returning 1 as the answer.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 47:
            print('''
                     DIR AND HELP
                     The dir and help string functions are used to command python when
                     you are uncertain about the utility of a certain function or method and
                     perhaps you want to read more about what the method of function achieves.
                     Directory aliased as dir, directs users to all the functions and methods
                     built-in to a certain module. This is pivotal when maneouvering across
                     different external modules like matplotlib or pandas in later videos.
                     In these modules, we can use the dir to check the extent of functions
                     and methods built-in to them. Help is more subtle in that it directs users
                     to the application, required arguments and outputs of all the functions
                     in a particular module or class. The string class has many methods like
                     print or format by which the help function tells users about what each of
                     those string functions does through an abstract case example.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        while x == 48:
            print('''
                     LIST POP METHOD
                     This episode concerns the list pop method in python and its
                     applications.
                     Within the list class in python, such a method exists that
                     cuts an iterable from a list at a certain index and adds it to
                     a new list. This method is also known as the list pop method and
                     can be used in many circumstances.

                     new = list()
                     names = ['john', 'max', 'jacob']
                     new.append(names.pop(2))

                     >>>names
                     >>>['john', 'max']
                     >>>new
                     >>>['jacob']

                     Illustrated in the example above, the list pop method extracts an
                     iterable of a list at a particular index, appending it to an empty
                     prexisting list as a new iterable. This is particularly useful when you
                     wish to move items between different lists through a click of a button.

                     question = True
                     names = []
                     while question:
                        query = input('Enter your name to add it to the list, del to delete or quit to end: ')
                        if query == 'del':
                            question_2 = input("which name do you wish to delete? ")
                            y = names.index(question_2)
                            names.pop(y)
                            print(names)
                        elif query == 'quit':
                            question = False
                        else:
                            names.append(query)
                            print(names)

                    The short code above implements the list append, pop and index method demonstrating
                    the sufficiency of the list pop method. A bit of sophisticated coding, but no less
                    harder to explain. The first question variable stores condition True. We want a
                    while loop because we want the user to amend the list continuosly until a quit
                    executable is entered. An if statement would be useless in this situation because
                    we want an infinite repetition of input prompts until specified otherwise. If the
                    while loop statement is met, we provide the directive to enter a name to the list,
                    delete an existing item with the del command or enter quit to end the loop. Achieving
                    the first criteria requires the most code in that we want to pop out an existing
                    name from the list at a certain position. Therefore, we prompt the user with a
                    second input, namely query_2, which asks them which name to delete. A wonderful
                    application of the index method is that it returns the index of a particular value. We
                    train the index method to return the index specified by the second prompt query_2.
                    Saving a separate variable y with this value, the pop method is applied to extract
                    that particular name value from the existing list specified by the user. But the
                    quit directive has not been supplied, so the while loop is executed again and requests
                    the user for another name. The elif statement is provided for a second condition. When
                    a quit command is entered, the question variable is saved as False. This is unmet by
                    the criteria of the while statement which strictly accepts True for variable question.
                    The loop is ended. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = list()
                help(x.pop)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 49:
            print('''
                     STRING FORMATTING
                     In python, string formatting is an efficient method of
                     collecting numerous names and valuable pieces of data from
                     a user without manually typing their values into the computer.
                     This episode will demonstrate the efficacy of such a convenient
                     string method.
                     Classically, string formatting is a method subscribed to
                     the string class. To create a clearer picture, an example is
                     always ample.

                     example 1) name = 'john'
                                attribute = 'tall'
                                print('{} is {}'.format(name,attribute))
                     output: john is tall

                     example 2) name = 'jack'
                                age = '16'
                                print('{} is {}'.format(name,age))
                     output: jack is 16

                     Clearly shown above, the string format can be very useful in situations
                     where you have a name and you want to automatically type in their information
                     into a coherent sentence without manually doing so. The brackets act as placeholders
                     for where you expect to place details of the person. In example 1, the variable name
                     stored value 'john', so the first bracket was a placeholder for the user's name.
                     Next, we wanted user 'john' to be attributed with an adjective. So we provide a
                     separate variable attribute with adjective tall. To replace the placeholders with
                     the required stored variables, we use the format method and parenthesis separating
                     stored variables with a comma. Order is important in this sense and if attribute was
                     entered before attribute, it would read 'tall is john'. The second example
                     elucidates how string integers and string letters are unified through string
                     formatting. Interesting examples of string formatting are provided below.

                     example 3) x = ['jack', 'john', 'samuel', 'sebastian']
                                y = 'tall'
                                for i in x:
                                    print('{} is {}'.format(i,y))
                     output: jack is tall
                             john is tall
                             samuel is tall
                             sebastian is tall

                     example 4) window = True
                                while window:
                                    comment = input("Enter an adjective about yourself: ")
                                    question = input("What is your name? ")
                                    print("{} is {}".format(question,comment))
                                    question_2 = input("quit or continue ")
                                    if question_2 == 'quit':
                                        window = False
                                    elif question_2 == 'continue':
                                        continue
                     output: Enter an adjective about yourself: cool
                             What is your name? Maz
                             Maz is cool
                             quit or continue: quit
                             >>>

                     The examples above present unique applications of the string format
                     method. The first example represents how string formatting can be
                     used to supply a common attribute among names of people in a list. In this
                     example, attribute tall was associated to each person in the list.
                     The second example is a more interactive version of string formatting.
                     Using the while loop and three questions that prompt the user for a
                     descriptive adjective, their names and whether they wish to continue, the
                     user is immersed into our simple code. The continue keyword is used to
                     produce concise coding to which continues the while loop and the set
                     of questions until a quit command is entered. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                help(x.format)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 50 or x == 51:
            print('''
                     COMMAND LINE HELLO
                     This episode delves deeper into the import keyword and the sys module
                     within python's default library. The method in question is the sys.argv
                     method. If you're curious as to how you could print a statement on you command
                     prompt, you are in the right place. If some of you are confused, this
                     package will be discussed in much further detail in later episodes. This
                     is a starter video of what is to come.

                     If you're unfamiliar with the command line, this is a great place to start.
                     The command line is another way of executing your python code to reaffirm
                     that its working. It is also the way to install external packages in later
                     videos, ones that aren't built-in to the python default libraries. You can
                     access the command line by locating your file directory and entering
                     cmd into the directory line. This is a bar above your files which
                     highlights your current directory, in other words which folder is currently
                     opened on your computer and the path to how you opened that folder; typically
                     through your desktop. So it should be desktop, an arrow and then if you're working
                     on the desktop, your current directory is your desktop. On this bar, if you enter
                     cmd (short for command) a redirect to the command line is iniatiated. This is a
                     useful method of accessing the command line for future uses.

                     import sys

                     if len(sys.argv) > 1:
                         print('hello {}'.format(sys.argv[1]))
                     else:
                         print('hello world')

                     The code above clearly highlights some of what the sys module does. Using
                     python conditions familiar to us (such as the if and else statements) we
                     manipulate the sys.argv method to print our names to the command line. When
                     you get to the command line, visible is your path to the current working python
                     directory, to which you need to apply the name of your python script file. This
                     is usually in the .py format. After this an additional argument is optional to
                     initialize our script. If additional arguments are not supplied, the first if
                     condition is unmet and 'hello world' is printed to the screen. Supposing more
                     than one additional argument is supplied, the condition of the first if statement
                     is met and in the placeholder of the string format bracket, we want the first
                     index of arguments to replace the placeholder. A useful way to think of additional
                     command line arguments is like a list. The first argument directing the python
                     script file name is item 1 of our list. Any additional arguments act as consecutive
                     numbers or indexes. The sys.argv argument is our list and we're manouevring it.
                     If the length of our list is one or smaller; in other words, if an optional argument
                     is not supplied, hello world is printed to the screen. This is a fun lesson on
                     sys.argv and some of the python's marvels. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                import sys
                help(sys.argv)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 52:
            print('''
                     NUMBER PYRAMID
                     In this episode, we expect to produce a number pyramid based upon
                     a number entered by the user. For example, if the user enters 5, a number
                     pyramid with size 5 will be produced. All is clarified through the examples
                     below.
 
                           0
                          010
                         01210
                        0123210
                       012343210
                      01234543210

                                0
                               010
                              01210
                             0123210
                            012343210
                           01234543210
                          0123456543210
                         012345676543210
                        01234567876543210
                       0123456789876543210
                      0123456789109876543210 ''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         The solution of this problem will be broken down into a series
                         of intuitive and explanatory steps.

                         First we consider what is expected of the user. The user should
                         be able to enter a number that produces a number pyramid of that
                         size. To do so, we return to the properties of a function. Docstring
                         is optional, providing a guide of our function.

                         def num_pyramid(num):
                             'enter a number indicating your number pyramid size'

                         A vital element to this problem is formatting. We expect to produce
                         an additional level of zero's to whatever pyramid size we enter. Therefore,
                         the function should take in a for loop in the range of our specified number.
                         This corresponds to the number of levels in our product. If we have a pyramid
                         of size 5, this number is expected to be 6 because we want one tier of one
                         zero and the rest of the numbers to follow the pattern.

                         def num_pyramid(num):
                             'enter a number indicating your number pyramid size'
                             for i in range(num+1):
                                 for j in range(i):
                                     print(j, end='')
                                 print()

                        num_pyramid(5)

                        output: 0
                                01
                                012
                                0123
                                01234
                                012345

                        The output above demonstrates that the number of levels and the
                        numbers printed are correct, but the formatting is still incorrect.
                        Shown above is a function using an initial for loop in the range of
                        the specified number added by 1. The additional 1 is required to
                        extend the level of every entered number by an additional tier because
                        we want a pyramid starting with a single zero at the tip.
                        The embedded for loop controls the numbers being printed to the screen.
                        In this situation, we want our pyramid to recurrently begin at zero and
                        ascend in order by a step of 1. After all numbers are printed in the range
                        of the first iterable from the first for loop, the embedded loop is
                        exhausted and python returns to a hanging print() statement, commanding
                        it to print to the next line. The process restarts until all iterables of
                        the first loop are exhausted. At this point, all levels are printed.
                        What remains is the formatting of descending spaces before each range
                        of numbers are printed on each level. Achieving this requires us to
                        introduce an extra for loop using a separate iterable k.

                        def num_pyramid(num):
                             'enter a number indicating your number pyramid size'
                             for i in range(num+1):
                                 for j in range(num+1-i):
                                     print(' ', end='')
                                 for k in range(i+1):
                                     print(k, end='')
                                 print()

                        num_pyramid(5)

                        output:      0
                                    01
                                   012
                                  0123
                                 01234
                                012345

                        The formatting is now correct, so we turn our focus to the second
                        part of the pyramid. The function above required an additional
                        embedded loop k to specify the numbers printed to the screen.
                        We add an extra 1 to the range of i for the k iterables because
                        i stops at one before the last number and because k is in the
                        range of i, k would stop at a number one before i and i stops
                        i before our number. This means that our iterable would potentially
                        stop 2 numbers before the user's number. This is unneccessary and
                        easily solved by adding an extra 1 to range of the second embedded loop.
                        The function of the j loop was transferred to k to pave way for the
                        formatting issue discussed ina previous step. The j iterable goes
                        before k because it now controls the spacing before the values are
                        printed to the screen. We want the spacing to descend in order through
                        each level. This required us to amend the j for loop by setting the
                        range from largest to smallest. After each level, we expect this spacing
                        to decrease by 1 to add extra space for new values. This is achieved
                        by using the iterables of the first for loop in the range of j. Subtracting
                        i in the range of j means that through each level, our range of spacing
                        is decreasing by 1. An additional one is required in the j range following
                        the same problem that arises with the k for loop mentioned earlier. A
                        final loop is neccessary to manage the second part of our number triangle.
                        This example makes use of an iterable named l.

                        def num_pyramid(num):
                             'enter a number indicating your number pyramid size'
                             for i in range(num+1):
                                 for j in range(num+1-i):
                                     print(' ', end='')
                                 for k in range(i+1):
                                     print(k, end='')
                                 for l in range(k):
                                     print(l, end='')
                                 print()

                        num_pyramid(5)

                        output:      0
                                    010
                                   01201
                                  0123012
                                 012340123
                                01234501234

                        The levels and the number of digits printed are correct, the issue
                        that pertains involves the format of the second part of the pyramid.
                        We require numbers descending in magnitude to be printed on each level.
                        This is resolved by using iterable k in the for loop of l. If we subtract
                        l from k in each iteration through l, we acquire decreasing numbers by
                        the correct magnitude. The reason for this is k begins at zero (so does l) and
                        zero subtracted by zero is zero.

                        def num_pyramid(num):
                             'enter a number indicating your number pyramid size'
                             for i in range(num+1):
                                 for j in range(num+1-i):
                                     print(' ', end='')
                                 for k in range(i+1):
                                     print(k, end='')
                                 for l in range(k):
                                     print(k-l, end='')
                                 print()

                        num_pyramid(5)

                        output:       0
                                     011
                                    01221
                                   0123321
                                  012344321
                                 01234554321

                        The outcome above is near the desired output. A last problem remains that
                        the second part starts at 1 on the second level, where it should start at
                        zero. This is easily resolved by subtracting an extra 1 from the last
                        iteration through the embedded loop l. This is caused becaused in the first
                        iteration through, iterable k is zero, so zero minus zero is zero and nothing
                        is printed to the screen. In the second iteration of k, the last value of
                        k is 1; and therefore, iterable l is zero because the range is 1 and all
                        natural numbers excluding one are printed. In which case, zero is the only
                        natural number less than 1 (not including negative numbers) and 1 minus
                        zero is 1, so only 1 number is printed to the screen. This is continued until
                        all i iterables are tried.

                        def num_pyramid(num):
                             'enter a number indicating your number pyramid size'
                             for i in range(num+1):
                                 for j in range(num+1-i):
                                     print(' ', end='')
                                 for k in range(i+1):
                                     print(k, end='')
                                 for l in range(k):
                                     print(k-l, end='')
                                 print()

                        num_pyramid(5)

                        output:       0
                                     010
                                    01210
                                   0123210
                                  012343210
                                 01234543210

                        Trying different numbers will produce different sized pyramids. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 53:
            print('''
                     INFINITE STRING INPUT AND STRIP METHODS
                     In this episode, string strip and split methods in the case of infinite
                     string inputs will be discussed in detail. List comprehension will be
                     introduced into the final product which is a method for users to enter
                     their names and print out a list of their respective names without trailing
                     or preceding whitespaces; hence, the string strip method. If you're
                     previously unfamiliar to the split method, a preceding video discusses that
                     in detail. In a nutshell, string split requests for one argument from the user,
                     namely the delimiter. The delimiter is something that detaches strings from
                     each other in a string variable. For example, white blank spaces detach words
                     from each other in a sentence. A sentence is string and in this situation, the
                     split method would produce a list of words in the sentence because when none
                     given, split defaults to detach words in a sentence via their blank spaces.
                     Creating a method to which asks users for as many words as they can possible
                     and producing a list of those words is within the rubric of the string split method.
                     This is made more apparent through extensive examples presenting unique applications
                     of string split. Strip will be mentioned later in the episode.

                     example 1) names = input("Enter names separated by spaces: ").split()

                                print(names)

                     output:Enter names separated by spaces: john jacob maxwell dina
                            ['john','jacob','maxwell','dina']

                     example 2) names = input("Enter names separated by commas: ").split(',')

                                print(names)

                     output:Enter names separated by commas: maz,jack,jacob,clark
                            ['maz','jack','jacob','clark']


                     A first example demonstrates the split method without supplying an additional
                     delimiter argument. We want the list and the inputs to both be printed to the
                     screen, so we store input variable as names and print names to check whether
                     the names entered are stored in a list. In the second example the optional
                     delimiter argument is provided and a directive is given for users to separate
                     their words using commas instead of spaces. The product is identical because
                     the split method works on detaching words using specified delimiters. This can
                     be more succint and customizable by using list comprehension. This method is
                     also applicable because the split method creates a list to which can be
                     iterated through using a for loop. The classical for loop is very lengthy and
                     list comprehension is a method of reducing space and improving efficacy.

                     example 3) names = [i for i in input("Enter names separated by commas: ").split(',')]

                                print(names)

                     output:Enter names separated by commas: maz,jack,jacob,clark
                            ['maz','jack','jacob','clark']

                     The output above shows the same result as previous examples. Therefore, list
                     comprehension is a suitable method in achieving an identical result. It is
                     more customizable because each entered name in the names list can be altered
                     whereas using a singular input presented in the first few examples apply a general
                     format to all inputs. This is an ideal moment to introduce the strip method.
                     Briefly hinted upon in the beginning of the episode, the string strip method
                     removes any trailing or preceding spaces in a string. For example, if the user
                     entered a space, a comma and then the next word, the output would be very untidy
                     in the sense that the split, if the delimiter was a comma, would detach words
                     via commas but white spaces would remain in places where extra spaces were added
                     after those commas. This is not ideal, but its a matter which is solvable using
                     list comprehension and the string strip method. Isolating each word in the list as
                     an iterable, we wave more control over the desired list output. If for instance,
                     we add an i.strip for each i in the list, this would strip all white spaces surrounding
                     each string word in our split string sentence.

                     example 4) names = [i.strip() for i in input("Enter names separated by commas: ").split(',')]

                                print(names)

                     output:Enter names separated by commas: maz, jack, jacob, clark
                            ['maz','jack','jacob','clark']

                     Example 4 clearly highlights why the strip method is so crucial. The user
                     entered a name followed by a comma and an extra blank space. This blank space,
                     unless specified, would be printed alongside the word in the list. The result
                     would be untidy and confusing to users. What strip did was remove all those
                     white spaces around the words where they were accidentally entered. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                q_4 = input('Where is help required? Enter split or input: ')
                if q_4 == 'split':
                    help(x.split)
                elif q_4 == 'input':
                    help(input)
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 54:
            print('''
                     IMPORT KEYWORD
                     Within each python library/module, there exists many methods and built-in
                     functions. Apart from the string, list and dictionary classes, separate
                     modules have many methods and functions, with methods within those methods
                     and same applies to functions. Python doesn't automatically read those
                     libraries for all those methods and functions that are potentially in your
                     disposable. To use those methods and functions from different python
                     libraries, the import statement is vital. Accomplishing more complicated
                     results will require use to become quite familiar with the import statement
                     and importing the appropriate libraries to our script to make use of their
                     utilities.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 55 or x == 56:
            print('''
                     GUESSING GAME
                     This episode concerns guessing numbers continuosly until one guesses the
                     correct number and the game ends. The user is expected to enter a number, if
                     the number entered is too large, a statement should print try a smaller number,
                     signalling them that the correct number is smaller than their guess. When a
                     number is too small, the computer should print try larger.''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         This problem will be deconstructed into a sequence of smaller instructions.

                         We're required to create a game which asks users for a number until
                         their number matches the correct number. The first step is to create a
                         method of printing random numbers from a set of numbers. At this point,
                         we shall import one of python's numerous libraries that generates
                         random numbers given a range. We don't use the range function purely
                         because numbers in the range function are not random in the sense that
                         they increase or decrease by a certain step through each iteration. The
                         library used for this problem will be the random library. This library
                         deals purely with generating random lists of numbers and adapting them.
                         Only one method from this library will be applied to our problem, the
                         randint method. Using this method, we are capable of generating random
                         numbers within a range of numbers including the largest number. This is
                         important to note mainly because the range function excludes the largest,
                         but such is different for the randint method.

                         import random

                         number = random.randint(1,30)
                         
                         guess = input("Guess a number: ")

                         Having imported the random library from python's set of libraries, we're
                         only interested in the randint library. But following python's format
                         you must put the name of the module/library dot the method you're
                         using. This is the way python understands where to retrieve the method
                         from. The randint method takes the same arguments as range which is
                         the first and last numbers of a range, including the last number
                         specified. A crucial difference is that randint chooses numbers randomly
                         within that range. This is stored as the number which we are expected to
                         guess correctly. Variable guess is saved as the input which prompts the
                         user to guess a number as per our game. The next step is to enlist the
                         criteria and print statements that guide our user to the right guess. To
                         do so we consider the if and else statements to provide the appropriate
                         criteria at which point those statements print to the screen.

                         import random

                         number = random.randint(1,30)
                         print(number)
                         guess = input("Guess a number: ")
                         while guess != number:
                            if guess < number:
                                print('Try a larger number.')
                            else:
                                print('Try a smaller number.')
                         else:
                             print('You guessed correct.')

                         output: 12
                                 Guess a number: 5
                                 Try a larger number.

                         Based on the outcome, the criterion clearly applies to the guesses, but after
                         the initial prompt, the user cannot make a second guess once their guess is
                         incorrect. This is resolved using a second prompt in the criteria if their
                         guess is incorrect.

                         import random

                         number = random.randint(1,30)
                         print(number)
                         guess = input("Guess a number: ")
                         while guess != number:
                            if guess < number:
                                print('Try a larger number.')
                                guess = input("Guess a number: ")
                            else:
                                print('Try a smaller number.')
                                guess = input("Guess a number: ")
                         else:
                             print('You guessed correct.')

                         output: 12
                                 Guess a number: 5
                                 Try a larger number.
                                 Guess a number: 10
                                 Try a larger number.
                                 Guess a number: 12
                                 You guessed correct.

                         The outcome demonstrates that our guessing game is approaching our desired
                         result. Two problems remain: if the user doesn't enter a number, we want
                         to prompt our user to enter a number and try another guess and once guessed
                         correct the game shall end. To resolve these problems the while loop and
                         try and except statements are neccessary.

                         import random

                         number = random.randint(1,30)
                         print(number)
                         finished = False
                         while not finished:
                             try:
                                 guess = int(input("Guess a number: "))
                                 while guess != number:
                                    if guess < number:
                                        print('Try a larger number.')
                                        guess = int(input("Guess a number: "))
                                    else:
                                        print('Try a smaller number.')
                                        guess = int(input("Guess a number: "))
                                 else:
                                     print('You guessed correct.')
                                     finished = True
                             except ValueError:
                                 print('Enter a number.')

                        The main differences with the lines above and the previous code is the
                        try and except loops and the additional while loop to end the
                        game once guessed correct. If you want to make a complete guessing game,
                        it is possible to delete the initial print number statement so we have
                        no idea of our random number. An extra while loop is used to control the
                        point to which the guess is correct and the user no longer plays our game.
                        It is important to introduce this additional while loop before the try, except
                        and the second while loop that compares our guess to the actual number displaying
                        guidelines of how small or large we're required to guess.
                        The except loop checks for ValueError which is a common error arising from
                        entering values that don't fulfil the desired string value for the input.
                        When you're expected to enter a number and you enter a letter, python
                        produces a value error because the input statement is surrounded by an int
                        which changes it to a number. A string letter cannot be a number so python
                        misunderstands this and produces value error accordingly. The reason we
                        enter the try and except after the first while loop follows the idea that
                        the game hasn't yet ended if the user enters a letter, so we don't want
                        the user to be discouraged by their mistake and be capable of playing the game
                        if they enter a letter where a number was needed. Until they guessed
                        correct, the finished variable is changed to True which is no longer True
                        because our criteria is 'not' the finished variable. If finished is changed
                        to True, not finished is now not True which is False. False doesn't meet the
                        condition of while loop number 1 and consequently the game ends. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 57 or x == 59 or x == 60:
            print('''
                     DICTIONARIES
                     These episodes will delve into one of python's three main classes which
                     are strings, lists and dictionaries. Dictionaries comprise of two main
                     items: keys and values. Think of dictionaries as safes. A safe has a key
                     that locks a valuable item. The difference is, dictionary keys don't
                     discriminate whether an item is precious enough to be locked, a python
                     dictionary always associates a key to a respective item. Certain dictionaries
                     can also contain keys to dictionaries within themselves. So keys to dictionaries,
                     within of which have their own keys. All this and more will be the discussion
                     of these episodes.The basics of python dictionaries surround a key value pair.
                     Examples will classify between keys and values to really facilitate you're understanding
                     of dictionaries and these pairs amongst them.

                     example 1) names = {'john':1,'mark':2,'jacob':3}

                     output:names
                            {'john':1,'mark':2,'jacob':3}

                     example 2) specific = {}
                                specific['names'] = names

                     output:specific
                            {'names':{'john':1,'mark':2,'jacob':3}}

                     The first example sheds light on the keys and values within a dictionary. Variable
                     names stores a dictionary containing names as the keys and their associated number
                     values. A formative difference between lists and dictionaries follows the dictionary
                     brackets, which are of a curly kind, whereas list brackets are the typical [] kind
                     brackets. The second examples shows a dictionary which contains a dictionary
                     within itself. To add keys to empty dictionaries the square brackets are used
                     pertaining to the key and an equal sign that assigns the value to the dictionary
                     with that key. This is similar to storing a value to a variable, only that a dictionary
                     contains a key associated with that value so we require the extra square bracket
                     indicating that key. In the second example, the dictionary specific contains a single
                     key value pair with key 'names' and value names. But names is another dictionary with
                     its own keys and values. Therefore dictionary 'specific' with key 'names' assigns the
                     dictionary names to its value. Dictionaries can also become tuples (will be discussed
                     in a later episode) by invoking the items method.

                     example 3) names = {'john':1,'mark':2,'jacob':3}
                                names_1 = names.items()
                               
                                print(names_1)
                     output: dict_items([('john', 1), ('mark', 2), ('jacob', 3)])

                     example 4) names = {'john':1,'mark':2,'jacob':3}
                                names_1 = names.items()
                            
                                for k,v in names_1:
                                    print(k, ':', v)
                     output:john : 1
                            mark : 2
                            jacob : 3

                     The above examples illustrate the fundamental characteristics of dictionaries.
                     The first example saves a dictionary of people's names and their number values
                     to a variable entitled 'names'. We store the 'items' method of this dictionary under
                     a new variable called names_1. The print function prints variable names_1 to the
                     screen containing the items of the dictionary as dict_items. These items are
                     actually in the form of a tuple, where the keys and values are stored as independent
                     iterables of list. Due to this fact, we can treat those key and value pair
                     items of variable names 1 as iterables off a list. Enabling us to control the
                     items in the tuple is the for loop. Note however that we cannot maintain an i
                     as the iterable through our tuple. Instead, keys and values are both iterated
                     simultaneously through the dictionaries items. These keys and values are
                     aliased k and v for convenience. The last example prints each key value iterable
                     from the dictionary items onto individual lines separated by colons.

                     Dictionaries are powerful tools for counting the amount of times a word repeats
                     in a string sentence, a book or a story of some sort. Instead of manually counting
                     words in a sentence or a story, dictionaries help to assign values to a specified
                     key which we can manipulate for this purpose. Assigning a counter to the dictionary
                     values and words as keys enables us to increase the counter of each word repeated
                     in our story.

                     file = 'jack and jill went on a ride. The ride was apocalyptic because jack and
                             jill hated it. They detested it. They loathed it. They absolutely reeked
                             vengeance against it. It was the bane of their existence. So cruel and so
                             malicious and so distasteful and so horrible, absolutely gruelling, problematic
                             and jack and jill just were so angry, horrified, terrified, disaligned from
                             such a putrid experience of a disparaging trip.'
                            
                     story = file.split()

                     words = {}
                     for i in story:
                         if i in words:
                             words[i] += 1
                         else:
                             words[i] = 1

                     del story

                     words = words.items()

                     sort_words = sorted(words)

                     for i in sort_words:
                         print(i[0], ':', i[1])

                     output:It : 1
                            So : 1
                            The : 1
                            They : 3
                            a : 3
                            absolutely : 2
                            against : 1
                            and : 7
                            angry, : 1
                            apocalyptic : 1
                            bane : 1
                            because : 1
                            cruel : 1
                            detested : 1
                            disaligned : 1
                            disparaging : 1
                            distasteful : 1
                            existence. : 1
                            experience : 1
                            from : 1
                            gruelling, : 1
                            hated : 1
                            horrible, : 1
                            horrified, : 1
                            it. : 4
                            jack : 3
                            jill : 3
                            just : 1
                            loathed : 1
                            malicious : 1
                            of : 2
                            on : 1
                            problematic : 1
                            putrid : 1
                            reeked : 1
                            ride : 1
                            ride. : 1
                            so : 4
                            such : 1
                            terrified, : 1
                            the : 1
                            their : 1
                            trip. : 1
                            vengeance : 1
                            was : 2
                            went : 1
                            were : 1

                    The script above is a way one can count the amount of words in a given dictionary. We
                    assign an empty dictionary to value words. This is where we expect to create a key
                    value pair of words and their frequencies in our story. First we create the story. Any
                    such string input story can be used, in this scenario we saved our story under variable
                    file, which illustrates a couple and their horrible road trip. After assigning a variable
                    file to our story, an extra string split is required to detach words from our story
                    into their own items of a list. This is assigned to another variable story which is a
                    list of words from our story. An empty dictionary is neccessary as placeholder to where
                    the words will be keys to their frequency value pair. The del keyword is used to delete the
                    file containing the story, because we no longer need the story in the sense that our
                    story is deconstructed into its words and stored as the story variable. To create our
                    key value word frequency counter, the for loop and if else statements are used
                    to determine whether our word is in the story list and if repeated more than once, the
                    frequency will increase by 1. Otherwise, the word will store a value of 1 which means
                    that it only occurs once in our story. Dictionary formatting is used in this stage where we
                    iterate through our story list with iterable i. The condition being that if i is in the
                    story list, or that particular word is in the story, the words dictionary is given a new
                    key value pair being the specific word, if repeated more than once, its frequency added
                    by 1, otherwise the word's value is newly assigned 1. To iterate through our new
                    dictionary of words and their frequencies we need to create a tuple of items in the
                    dictionary. This is done by overwriting the stored words dictionary with a tuple of
                    its items. The sorted function is used to sort the words in alphabetical order which
                    makes our output more neat. We assign a new variable sort_words to this alphabetically
                    sorted list of key value word frequency pair items. The last step is to iterate through
                    those key value pairs in the list of sorted dictionary items. Instead of directly
                    unpacking two iterables k v in a for loop, another method is to iterate with a single
                    i variable and use list indexing to obtain the first key of the iterable in the list and
                    its corresponding value. There are only two iterables for each item in the sorted list.
                    Therefore the maximum index is 1. So i[0] prints the word for each key value pair in the
                    list and i[1] prints its value. The for loop prints this for all tuple items.

                    If instead we wanted to sort the values in a certain order, we could assign a different
                    key to the sorted function. The defaulted key is none, so the sorted function organizes
                    items in ascending order. To do so with the values, we define a short function that
                    returns the last item in a list, in the case of a tuple, the value in each key value
                    word frequency pair. Without specifying the reverse to True, the values will be
                    printed in ascending order of their frequency. Turning reverse to True sorts those
                    values in descending order of frequency.

                    file =   'jack and jill went on a ride. The ride was apocalyptic because jack and
                              jill hated it. They detested it. They loathed it. They absolutely reeked
                              vengeance against it. It was the bane of their existence. So cruel and so
                              malicious and so distasteful and so horrible, absolutely gruelling, problematic
                              and jack and jill just were so angry, horrified, terrified, disaligned from
                              such a putrid experience of a disparaging trip.'
                            
                    story = file.split()

                    words = {}
                    for i in story:
                        if i in words:
                            words[i] += 1
                        else:
                            words[i] = 1

                    del story

                    def last(x):
                        return x[-1]

                    words = words.items()

                    sort_words = sorted(words,key=last,reverse=True)

                    for i in sort_words:
                        print(i[0], ':', i[1])

                    output: and : 7
                            it. : 4
                            so : 4
                            jack : 3
                            jill : 3
                            a : 3
                            They : 3
                            was : 2
                            absolutely : 2
                            of : 2
                            went : 1
                            on : 1
                            ride. : 1
                            The : 1
                            ride : 1
                            apocalyptic : 1
                            because : 1
                            hated : 1
                            detested : 1
                            loathed : 1
                            reeked : 1
                            vengeance : 1
                            against : 1
                            It : 1
                            the : 1
                            bane : 1
                            their : 1
                            existence. : 1
                            So : 1
                            cruel : 1
                            malicious : 1
                            distasteful : 1
                            horrible, : 1
                            gruelling, : 1
                            problematic : 1
                            just : 1
                            were : 1
                            angry, : 1
                            horrified, : 1
                            terrified, : 1
                            disaligned : 1
                            from : 1
                            such : 1
                            putrid : 1
                            experience : 1
                            disparaging : 1
                            trip. : 1

                    ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = dict()
                q_4 = input("Do you need help for dictionaries, sorted, items, for loop or functions? ")
                if q_4 == 'dictionaries':
                    help(x)
                elif q_4 == 'sorted':
                    help(sorted)
                else:
                    help()
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 58:
            print('''
                     FUNCTIONS WITH MULTIPLE ARGUMENTS AND DEFAULTS
                     Functions in python can have more than a single argument supplied, some
                     of which can be defaulted to a certain value preventing further not enough
                     argument errors. This episode aims to make light of this and more.
                     Previous episodes discussed in detail the methods of constructing a function,
                     using functions with multiple arguments through the asterisk. But none of
                     them shed light on functions with different arguments that enable them to
                     be more customizable. Arithmetic functions such as multiplication or
                     addition have previously taken in the user's number and added or multiplied
                     them to another.

                     example 1) def adding(x):
                                   'enter a number to add to 5'
                                   return x + 5

                                print(adding(5))
                     output:10

                     The example above is a single argument function that simply adds any number
                     entered to 5. What if the user was given more independence and wanted to
                     add any two numbers together. This can be achieved using the asterisk for
                     multiple numbers. But two numbers require only two arguments which are the
                     two numbers the user enters to add together.

                     example 2) def adding(x,y):
                                   'enter two numbers to add'
                                   return x + y

                                print(adding(5,10))
                     output:15

                     We reached the desired output and our function supplied the user with more
                     customizable options such as numbers of their choosing instead of 5. If we
                     wanted to stick to 5 without changing the number of arguments to 1 (like the
                     first example) we can assign a default value to the second argument (5 in this
                     case) to add to any number entered in place of the first argument.

                     example 3) def adding(x,y=5):
                                   'enter two numbers to add'
                                   return x + y

                                print(adding(5))

                    output:10

                    example 4)def adding(x,y):
                                 'enter two numbers to add'
                                 return x + y

                              print(adding(5))

                    TypeError: adding() missing 1 required positional argument: 'y'

                    The above examples demonstrate a fact about multiple arguments: you are able
                    to have a function with more than one argument if and only if you default
                    the arguments that aren't in use to a specified value. This informs python
                    whenever you have an instance of more than one argument but one is supplied,
                    the unused argument will take on the defaulted value and nothing else. If
                    this is not clearly specified, python returns a type error misunderstanding
                    where the second argument lies if your function has 2 arguments provided.
                    Defaulting arguments of functions is commonplace in python used in a variety
                    of classes and modules. Famously, the print statement has many defaulted values,
                    one of them being the new line delimiter which prints every iterable in a for loop
                    to a new line unless told otherwise. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 61:
            print('''
                     MAX AND MIN FUNCTIONS
                     The list max and minimum functions are methods to which
                     find the largest integer in a given list. This is a shorcut to
                     finding the greatest number in a given list without using
                     extensive coding and criteria to achieve the result.
                     To facilitate your understanding of the max and min functions
                     it is useful to observe some examples.

                     example 1) numbers = [50,25,46,75,68]
                                print(max(numbers))

                     output:75

                     example 2) numbers = [50,25,46,75,68]
                                print(min(numbers))

                     output:25

                     def max(*numbers):
                        count = 0
                        for arg in numbers:
                            if arg > count:
                                count = arg
                            elif arg < 0 and count == 0:
                                count = arg
                            else:
                                continue      
                        return count

                     print(max(-1,2,-3,6,-8,7))

                     output:7

                     def min(*numbers):
                        count = 0
                        for arg in numbers:
                            if arg < count:
                                count = arg
                            else:
                                continue      
                        return count

                     print(min(-1,-10,-3,6,-8,7))

                     output: -10

                     The above functions clearly demonstrate why manually
                     finding a max and min function are quite the challenge,
                     whereas using the built-in max and min functions are
                     drastically easier and more efficient. The first
                     function uses the asterisk taking in multiple numbers
                     arguments. We create conditions that check whether numbers
                     in our list of number arguments are greater than their
                     preceding number. This is achieved by assigning a count
                     variable that compares iterables in the list to one another.
                     If the number is greater than count, then count is saved as
                     that number. Otherwise, the number is skipped through the
                     continue statement. Problems arise when dealing with
                     negative numbers because count starts at zero and negative
                     numbers are all less than zero so count never changes
                     and zero is printed to the screen even when all entered
                     numbers are negative. To resolve this issue (and the issue
                     when more than one negative number is entered into the
                     arguments), we create two conditions which only the first
                     negative number of our list fulfills. After this point,
                     count is back to normal because it stores this negative
                     number and none of the other iterables fulfill this criteria,
                     so the first criteria is checked against all remaining
                     iterables. The second min function uses a similar idea negating
                     the extra negative number condition mainly because negative numbers
                     are always less than zero. However, the max function
                     when supplied with all negative numbers, had to be
                     conditioned appropriately to deal with the situation to hand. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                q_4 = input("Specify where extra help is neccessary: max or min? ")
                if q_4 == 'max':
                    help(max)
                elif q_4 == 'min':
                    help(min)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 62:
            print('''
                      TUPLES
                      This episode is about the tuple class in python. Tuples are
                      similar to lists with a few major differences. Tuple items
                      are not appendable and they cannot be removed. This is
                      a key difference between lists and tuples where lists can
                      be extended and appended to. Tuples have a different format
                      in that they're found in () brackets instead of [] brackets.
                      Tuples can be explained more thoroughly through examples.

                      example 1) names = ('mark','jacob','june')
                                 print(names)

                      output:('mark','jacob','june')

                      example 2) names = {'mark':1,'jacob':2,'june':3}
                                 names = names.items()
                                 print(names)

                      output:dict_items[(mark,1),(jacob,2),(june,3)]

                      example 3) names = ('mark','jacob','june')
                                 names.append('randy')

                      AttributeError: tuple object has no attribute 'append'

                      The three examples above demonstrate the applications and characteristics
                      of tuples. The first example stores a tuple under variable names. We
                      print variable names and the tuple is produced. The second example sheds
                      light on tuples and dictionaries associativity. The dictionary items
                      method creates a tuple of the key value pairs of that dictionary. For
                      example, variable names associates peoples names to a number. This is
                      stored as a dictionary. We then overwrite names to names.items(). This
                      eradicates the key value dictionary format and creates iterables of
                      key values shown in the output. This is not a classical tuple in the
                      sense that it is preceded by dict_items. A last example is written to
                      present why tuples aren't appendable and how they're dissociated from
                      lists. It is expected that item randy would be added to the end of the
                      tuple. However, an AttributeError is generated instead, which clearly
                      outlines that tuple class has no attribute append. This also can be
                      discovered by using the dir/directory function on the variable names or
                      any tuple. Dir provides users with all the methods and functions of
                      a specific module or class. Because append is not a method of the tuple
                      class, it cannot be invoked in any cases; hence, example 3 is dysfunctional.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = ()
                help(x)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 63:
            print('''
                     ZIP METHOD FOR LISTS
                     Whenever you want to collect two lists together without manually
                     creating a function to do it, within the python list class, there
                     is a useful and productive function known as zip that does exactly
                     that. To glorify the zip function, we'll first create a function
                     that does what zip does in one line.
                     Our function and the zip function will be provided through
                     examples.

                     names = ['mark','kyle','anthony']

                     numbers = [20,35,73]

                     names_2 = []
                     count = 0
                     for i in names:
                         names_2.append((i,numbers[count]))
                         count += 1

                     print(names_2)

                     output:[('mark', 20), ('kyle', 35), ('anthony', 73)]

                     The following demonstration shows just how difficult it is
                     to compile items from two lists into a tuple of their
                     individual items together. This is exactly what the zip function
                     accomplishes.

                     names = ['mark','kyle','anthony']

                     numbers = [20,35,73]

                     names_2 = list(zip(names,numbers))

                     print(names_2)

                     output:[('mark', 20), ('kyle', 35), ('anthony', 73)]

                     The zip function takes in two or more lists and categorizes
                     their iterables into a tuple of their items. In the
                     example above, variable names and numbers are both lists
                     with three items. It is important to note that zip two
                     lists together requires that both lists have the same amount
                     of items. Otherwise, one list has more items and the other less and
                     the extra items of one list cannot be zipped with an empty
                     slot for where the second list has no items. This means that
                     the zip will only work for the items with a matching pair.

                     names = ['mark','kyle']

                     numbers = [20,35,73]

                     names_2 = list(zip(names,numbers))

                     print(names_2)

                     output: [('mark', 20), ('kyle', 35)]

                     The example above highlights the occurence when two lists of
                     with unequal items are zipped. The iterables of the names list
                     are only zipped for its first two items with that of list
                     numbers. The last number in numbers was not zipped because
                     a matching pair wasn't identified by python. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(zip)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 64:
            print('''
                     ENUMERATE LIST METHOD
                     If you ever encounter a python list and you desire to number
                     each item in the list by an index, there is a built-in list
                     method that does this indexing automatically. It is more
                     casually known as the enumerate method. Enumerate can be
                     manually written, but it is less efficient to do so when
                     a method already exists that achieves the same end.
                     The enumerate method is made more attainable through rigorous
                     example.

                     names = ['kylie','hopkins','juliet']

                     count = 0
                     enumerate = []
                     for i in names:
                         enumerate.append((i,count))
                         count += 1

                     print(enumerate)

                     output:[('kylie', 0), ('hopkins', 1), ('juliet', 2)]

                     The above method associates an ascending order of numbers to
                     each person's name in the 'names' list. This is achieved manually
                     by starting a count variable at zero, then applying a for loop
                     iterating through the names list. For each iterable, appending
                     the iterable and the count (which begins at zero) to a new list
                     called enumerate (short for what the enumerate function does
                     automatically) creates a tuple of the name and the count. The
                     first instance of enumerate starts when count is zero. We want
                     the count to increase for each iterable. Therefore, we add 1
                     to the count variable after each iteration which enumerates the
                     numbers in our list by 1. If you require the first item to be
                     enumerate by 1, simply start the count at 1 instead of zero.

                     names = ['kylie','hopkins','juliet']
                     names_enum = list(enumerate(names))

                     output:[(0, 'kylie'), (1, 'hopkins'), (2, 'juliet')]

                     The enumerate function achieves the same result as the manual
                     method of creating a new list and appending to that list with
                     a for loop. It is important to not however that enumerate creates
                     an enumerate object, so this object needs to be transformed into
                     a list to be read correctly. This goes the same for the zip method
                     which also creates a zip object and requires that object to be
                     within a list function like the above. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(enumerate)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 65:
            print('''
                     ABSOLUTE VALUE ABS FUNCTION
                     if you're inundated with negative numbers and you want to
                     change a negative number positive, python has a built in function
                     known as abs alias for absolute, which for those of you who are
                     mathematicians understand, every negative number is transformed
                     positive if we're only intrested in its absolute version. The
                     absolute works the same way and transforms negative numbers
                     positive. There is a manual way of checking this, but to skip
                     the hassle it's recommended to use the abs function instead of
                     entering a code that does this.
                     The absolute functions does want written on the tin. In other words
                     it converts negative numbers positive. Written manually, you
                     ask for a negative number and we would need to create counditions
                     that if and only if the number is negative, our function makes
                     it positive. If a number is positive it remains positive.

                     def abs(x):
                         'makes negative numbers positive and leaves positive numbers
                          as they are'
                          if x < 0:
                              return (0-x)
                          else:
                              return x

                     print(abs(-9))
                     print(abs(10))

                     output:9
                            10

                     The above function changes negative numbers positive and leaves positive
                     numbers as they are. We entered the condition that if the number is less
                     than zero (or negative) the number is subtracted from zero. Any number
                     subtracted from zero remains as the same number. The sign is important
                     because zero minus our negative number is always positive. Two negatives
                     make a positive. When our input is non-negative for any number that doesn't
                     meet the initial condition (or is greater than or equal to zero) it is
                     remained as is. This work can be dramatically shortened by using python's
                     built-in abs function.

                     print(abs(-9))
                     print(abs(10))

                     output:9
                            10

                     The results are identical to the manually entered function only that
                     abs does the calculations without requiring further conditions and
                     return statements. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(abs)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 66:
            print('''
                     EVALUATE FUNCTION
                     Making calculations using strings result in errors unless the
                     the string is converted into a integer using the int function
                     and wrapping the string between it. The eval function (short for
                     evaluate) does the calculations for string integers without
                     turning those strings into integers
                     This is evident through examples.

                     example 1) question = input('Enter a calculation: ')
                                print(question)

                     output:Enter a calculation: 5*5
                            5*5

                     The example proves that when a string is entered into an input
                     variable question, the string is printed out as it was entered.
                     What we expect in the outcome is a calculation. In this situation,
                     we want 5 multiplied by 5 which is 25. If the eval function is
                     used around the input, the string integers will be calculated duly.

                     example 2) question = eval(input('Enter a calculation: '))
                                print(question)

                     output:Enter a calculation: 5*5
                            25

                     The outcome above demonstrates what the eval function does. It
                     evaluates the string integer inputs and treats them as numbers,
                     enabling us to manipulate them and calculate using them. In this
                     sense, we can do arithmetic calculations using string inputs
                     by attaching an eval (short for evaluate) around the input. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(eval)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 67:
            print('''
                     STRING COUNT FUNCTION
                     The string count function is a useful tool for counting the
                     frequency of repeated instances of sub-strings within that
                     string. For example, if you have a string sentence, the occurence
                     of a certain word in that string sentence can be found using the
                     count method. As usual, manual methods are available that achieve the
                     same outcome, but it is highly recommended to use python's built-in
                     tools to accomplish results in the most highly efficient and logical
                     manner.

                     story = 'jack hit jill, they had a ball, they loved it,
                                         they hated it, it was fun, maybe it wasn't,
                                         maybe it was, who knows?'
                                         
                     count = 0
                     for i in story:
                         if i == 't'
                             count += 1

                     print(count)

                     output:11

                     In out story, there are 3 repetitions of the letter 't' and so our
                     method for counting the number of occurences of a certain sub-string in
                     our string works. This can be dramatically reduced by using the short
                     string.count method which takes one argument (the sub-string you wish
                     to count) and counts the number of times it identifies that argument
                     in the string. The method above is also available by which takes a for
                     loop counts the occurences if that particular string matches an iterable
                     of the main string in search and increments stored variable count if
                     a match is found, otherwise countinues the search. After searching through
                     the whole string for the required sub-string, we print the last count stored
                     which is the number of sub-string occurences of the required sub-string
                     't'.

                     story = 'jack hit jill, they had a ball, they loved it,
                                         they hated it, it was fun, maybe it wasn't,
                                         maybe it was, who knows?'

                     print(story.count('t'))

                     output:11

                     We obtain an identical output to the time we used a manual method of
                     counting sub-string occurences within a string. It is important to note
                     that sub-strings are the spaces and letters within the string and not
                     specific words. If, for instance, one tries to count the number of
                     'they' strings in the main string story, this will be zero because
                     python counts the singular letters as iterables and not the letters that
                     form the word they. In this instance, it would be better to create a list
                     of the words in the string using the string split method and count iterables
                     (or the words in the list) by starting a counter and incrementing the
                     counter whenever that iterable is found again.

                     story = 'jack hit jill, they had a ball, they loved it,
                                         they hated it, it was fun, maybe it wasn't,
                                         maybe it was, who knows?'

                     story = story.split()
                     
                     count = 0
                     for i in story:
                         if i == 'they':
                             count += 1

                     print(count)

                     output:3

                     Instead of treating the spaces and letters of the variable string story,
                     the split method creates a list of sub-strings split via a given delimiter.
                     Because a delimiter isn't provided, python is informed to split the string
                     via a default space. This creates a list of all string words in our sentence
                     story. We count the frequency of the iterable 'they' in the string split
                     list story and whenever repeated, the counter is incremented by 1. The
                     process continues for all sub-string words in our sentence and we print
                     the counter with all iterables considered. It is always important to
                     understand what you want achieved and what you're trying to achieve in
                     your script. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                help(x.count)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 68:
            print('''
                     STRING MODULE IN PYTHON
                     Within python there exists a string module that contains ascii
                     letters within the alphabet both uppercase and lowercase (because
                     python is case insensitive). The string module enables one to
                     have more access to strings and manipulate them even more
                     To demonstrate the utilities of the string module, its important to
                     understand some of its methodology and functions.

                     import string

                     alphabets = string.ascii_letters

                     lower_case = string.ascii_lowercase

                     upper_case = string.ascii_uppercase

                     print(alphabets)
                     print(lower_case)
                     print(upper_case)

                     output:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
                            abcdefghijklmnopqrstuvwxyz
                            ABCDEFGHIJKLMNOPQRSTUVWXYZ

                     The code above shows some of the methods within the string module in
                     python. Instead of typing in individual letters of the alphabet,
                     whether upper or lower case, python has a module with which contains
                     upper case and lower case letters printed consecutively without blank
                     spaces in one string. This involves invoking the ascii_letters
                     method which takes no arguments;hence, no extra brackets were provided.
                     The lower case and upper case alphabets can be printed by invoking
                     ascii_lowercase and uppercase separately as methods. When python is
                     informed of ascii_letters it simply prints both cases together. Always
                     remember to import the appropriate library for the functions you intend
                     to use. In the example, the string module was our intended use and so
                     we imported it. The string module can also sustain many more functions
                     which can be found using the directory (dir for short) in the IDLE shell
                     where the code is executed. Doing this allows users to comprehend the
                     scope of the libraries many functions and methods. Some interesting
                     methods are the hexdigit and ocdigit which are different ways of
                     passing string text into python. More can be found by reading the help
                     on the module or particular functions from this module that spark your
                     interest. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                import string
                help(string)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 69:
            print('''
                     ZIPPING A PYTHON DICTIONARY
                     In this episode, we will attempt to zip a python dictionary
                     of ascii_letters with associated numbers to number letters
                     in the alphabet from 1 to 26, corresponding to the number of
                     letters in the alphabet.
                     To do so, we must first comprehend what the task asks of us.

                     The zip method is useful in this context because it is
                     an efficient method of compiling iterables from 2 separate
                     dictionaries into one obedient and intuitive model. We
                     need to import the string module which contains the relevant
                     method string.ascii_lowercase (as we're primarily concerned
                     with small alphabets; remembering that python is case insensitive).

                     import string

                     alphabets = string.ascii_lowercase

                     A next step is to generate a a string of numbers associating the
                     alphabets to those numbers. The range function is useful in this
                     situation because we can specify a starting point, an ending point
                     and by which step we wish our numbers to be counted in.

                     import string

                     alphabets = string.ascii_lowercase

                     numbers  = range(1,27)

                     The final step is to zip the two string lists together using the
                     built-in zip function.

                     import string

                     alphabets = string.ascii_lowercase

                     numbers  = range(1,27)

                     alphabets_num = zip(alphabets,numbers)

                     The variable alphabets_num now exists as an object. What remains to
                     be done is wrap it around whatever format we wish to perceive the
                     object in. Instead of a list, we'll use a dictionary to contain the
                     zipped object.

                     import string

                     alphabets = string.ascii_lowercase

                     numbers  = range(1,27)

                     alphabets_num = dict(zip(alphabets,numbers))

                     print(alphabets_num)

                     output:{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                             'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                             'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                             's': 19,'t': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                             'y': 25, 'z': 26}

                     Illustrated in the last script, we have achieved a tidy outlet for
                     associating alphabets to ascending order numbers from 1 to 26. This
                     helps us better understand the alphabet through practical indexing.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(zip)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 70:
            print('''
                       PYTHON UNICODE
                       The python language is typically written in unicode, which gives
                       a number referring to the character of a string (including lower
                       and upper case alphabets). This number can be extracted through
                       a function known as ord, which provides the order of number of that
                       string as a character in the unicode list.
                       Examples will highlight exactly what the ord function does.

                       name = 'jack'

                       for i in name:
                          print(ord(i))

                       output: 106
                               97
                               99
                               107
                               
                       The example shows us how the ord function works on particular letters
                       within a string. We use the for loop to iterate through letters of
                       the string name which stores value 'jack'. We wrap the iterables by
                       the ord function which shows to the screen the associated unicode number
                       of that particular letter within the table of all characters. It is
                       interesting to note that letters nearer the start of the alphabet have
                       lower values, whereas letters like j or k store higher values. This
                       is the way python understands and distinguishes between different
                       letters of the alphabet. If one enters a boolean operator such as whether
                       a letter is greater than another, python uses the unicode list of numbers
                       to characters to test whether that particular letter's number is greater
                       than another.

                       >>> 'j' > 'a'
                       True
                       >>> 'j' < 'a'
                       False

                       Built-in to python's boolean is True whenever a number follows
                       the given operation and False if it doesn't. The example above
                       proposes that the letter 'a' is less than letter 'j', which
                       makes no sense unless these letters are associated with a number
                       value, in which case python checks against the associated numbers
                       to ask whether one is larger than the other. The checklist of
                       comparing letters with some associated number is the unicode list,
                       where python sees that letter a is 97 whereas j is 106. Therefore,
                       j is larger than a and python responds with a True statement for
                       verification. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(ord)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 71 or x == 72:
            print('''
                     STRING VALUE USING DICTIONARY
                     This episode will put into practice everything about the string
                     module and creating a way of summing string values given a dictionary
                     of alphabets and their corresponding values
                     First we consider how to create a dictionary of alphabets to
                     numbers. In a previous episode, the string module was introduced
                     to provide us with more flexibility with strings and their functions.

                     import string

                     letters = string.ascii_lowercase

                     numbers = range(1,27)

                     alpha_nums = dict(zip(letters,numbers))

                     output:{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                             'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                             'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                             's': 19,'t': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                             'y': 25, 'z': 26}

                    Now that we have a dictionary of letters in the alphabet to
                    ascending numbers starting from 1 to 26, we can sum the values
                    of the letters with each other using a simple for loop and then
                    a more sophisticated list comprehension method.

                    import string

                    letters = string.ascii_lowercase

                    numbers = range(1,27)

                    alpha_nums = dict(zip(letters,numbers))

                    count = 0

                    word = input('Enter a word: ')

                    for i in word:
                        count += alpha_nums[i]

                    print(count)

                    output:Enter a word: john
                    47

                    The script above is a long method of summing values of alphabets in
                    a given word. This can be compressed using list comprehension. What occurs
                    above is we save letters as the letters of the alphabet, alpha_nums stores
                    a dictionary of those letters of the alphabet enumerated from 1 to the last
                    letter. A count is started which is how we approach the summation. The word
                    is an input function which prompts the user to enter a word. The for loop
                    iterates through the letters of the word which is added to the count variable
                    through the iterable keys of the entered word. As the for loop iterates
                    through letters of the word, it checks against the key value pair of the
                    stored enumerated dictionary of letters in the alphabet. After each iteration,
                    count is slowly added and we print the last stored number of count.

                    import string

                    letters = string.ascii_lowercase

                    numbers = range(1,27)

                    alpha_nums = dict(zip(letters,numbers))

                    count = [alpha_nums[i] for i in input('Enter a word: ')]

                    print(count)

                    output:Enter a word: john
                           [10, 15, 8, 14]

                    The code above creates a list of the associated numbers to
                    the alphabets of the word 'john' by list comprehension and
                    a straightforward input variable instead of storing the
                    input as an extra variable in the script. The last step is to
                    sum the items in the list using the handy sum function which
                    adds all iterables in a list to one another.

                    import string

                    letters = string.ascii_lowercase

                    numbers = range(1,27)

                    alpha_nums = dict(zip(letters,numbers))

                    count = [alpha_nums[i] for i in input('Enter a word: ')]

                    print(count)

                    output:Enter a word: john
                           47

                    List comprehension is an elegant way of shortening long for loops
                    and tedious variables into one line of code. The sum function
                    added all numbers in the count list. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = dict()
                y= list()
                q_4 = input("Where is extra help needed? Zip, dictionaries, range, string module, lists? ")
                if q_4 == "Zip":
                    help(zip)
                elif q_4 == 'dictionaries':
                    help(x)
                elif q_4 == 'string module':
                    import string
                    help(string)
                elif q_4 == 'lists':
                    help(y)
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 73:
            print('''
                     REVERSE NUMBER TRIANGLE FORMATTED")
                     Create a triangle with the following format:

                                    1
                                 1  2
                              1  2  3
                           1  2  3  4
                        1  2  3  4  5

                                                   1
                                                1  2
                                             1  2  3
                                          1  2  3  4
                                       1  2  3  4  5
                                    1  2  3  4  5  6
                                 1  2  3  4  5  6  7
                              1  2  3  4  5  6  7  8
                           1  2  3  4  5  6  7  8  9
                        1  2  3  4  5  6  7  8  9 10   ''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''This problem will be broken down into constitutive parts.

                         A first step is to understand what we're expected to
                         generate. The user is allowed to enter a number and in doing
                         so, they're able to generate a formatted number triangle the
                         sized to their liking. To do this, we require a function
                         that takes in a single argument, namely the size of the
                         triangle to print.

                         def num_triangle(x):
                             'enter a number as the size of your triangle'

                         We want to print the number of levels equivalent to the
                         size of the triangle, so a for loop in the range of our
                         number fixes the number of levels in the triangle to
                         the user's input.

                         def num_triangle(x):
                             'enter a number as the size of your triangle'
                             for i in range(x):
                                 print(i, end='')

                         num_triangle(5)

                         output: 01234

                         A single for loop prints the corresponding amount of
                         numbers on a single line to the screen. We require
                         those amount of numbers printed to the number of levels
                         entered by the user. This presents an opportunity to
                         introduce an embedded for loop with a different iterable
                         j. The embedded loop controls the numbers printed to the
                         screen, but we really want descending order spaces followed
                         by ascending numbers. Achieving this allows us to invoke
                         an additional loop that controls the numbers printed to the
                         screen after the required spaces. In each level, we want the
                         number of spaces to decrease by 1. Recognize that the iterables
                         of the first for loop increase by that size, so the first iterable
                         is the smallest. Therefore, subtracting from the increasing iterables
                         from the first loop decreases the size of the embedded loop. The
                         problem remains fixed on the spacing. Subtracting our number by
                         the increasing iterables always leaves an extra space because
                         the range of the first loop is always one less than the number,
                         so subtracting our number by one less always leaves a remainder of 1,
                         or 1 space. Subtracting an extra 1 from the range of the embedded
                         loop confirms no spaces before the last level of numbers are added
                         to the screen. As for the k iterables, we also manipulate the
                         ascending order i iterables to become the range of the k for
                         loop. This prints the number required amount of numbers to the
                         screen on each level. Because for loop 1 starts at zero, we're
                         required to add 1 to each iterable of k printed to the screen.
                         This completes the reverse number triangle. A more detailed
                         explanation can be found in previous videos, where number triangles and
                         diamonds are also explored. 
        
                         def num_triangle(x):
                             'enter a number as the size of your triangle'
                             for i in range(x):
                                 for j in range(x-i-1):
                                     print(' ', end='')
                                 for k in range(i):
                                     print(k+1, end='')
                                 print()
                                 
                         num_triangle(5)

                         output:    1
                                   12
                                  123
                                 1234
                                12345

                        The spacing format is achieved by using the string format method
                        in the print statement that controls the numbers on each level
                        shown to the screen. This is controlled by the k iterables. If
                        you use the string format or '{}'.format() with the desired iterable
                        within the brackets, you can format the spacing by providing the
                        following arguments between the dictionary brackets.

                        1) {:3d}
                        2) {:2d}

                        The numbers control the amount of spacing between each number on a
                        level. 3d is short for 3 digits which spaces numbers by 2 spaces
                        before the next number. Similarly, 2d is 2 digits and spaces numbers
                        by 1 space before the next. Python's default setting is 1d which is
                        visible where no spaces are printed between numbers. When
                        we print with spacing, it is also important to change our
                        spacing with the j iterables by the corresponding number of
                        spaces between numbers. If we're using 3d, then we shall add
                        3 spaces instead of a single space in line of the print statement
                        for j iterables. This is clarified below.

                        def num_triangle(x):
                             'enter a number as the size of your triangle'
                             for i in range(x):
                                 for j in range(x-i-1):
                                     print('   ', end='')
                                 for k in range(i):
                                     print('{:3d}'.format(k+1), end='')
                                 print()
                                 
                         num_triangle(5)

                         output:               1
                                            1  2
                                         1  2  3
                                      1  2  3  4
                                   1  2  3  4  5
            
                         def num_triangle(x):
                             'enter a number as the size of your triangle'
                             for i in range(x):
                                 for j in range(x-i-1):
                                     print('  ', end='')
                                 for k in range(i):
                                     print('{:2d}'.format(k+1), end='')
                                 print()
                                 
                         num_triangle(5)

                         output:         1
                                       1 2
                                     1 2 3
                                   1 2 3 4
                                 1 2 3 4 5

                         The reason for the extra spacing before the last string
                         of numbers is due to the spacing argument. Before each
                         number 2 spaces are printed if :3d is used and 1 if :2d
                         is used. This means that 2 spaces will always be printed
                         before the 1 in the last level of the triangle. This
                         kind of formatting is beneficial when 2 digit numbers are
                         entered into our function and we want the numbers to be
                         methodically arranged.
                       
                         def num_triangle(x):
                             'enter a number as the size of your triangle'
                             for i in range(x):
                                 for j in range(x-i-1):
                                     print(' ', end='')
                                 for k in range(i):
                                     print(k+1, end='')
                                 print()
                                 
                         num_triangle(10)

                         output:         1
                                        12
                                       123
                                      1234
                                     12345
                                    123456
                                   1234567
                                  12345678
                                 123456789
                                12345678910

                         The example above shows number 10 is out of sorts on the last
                         line of out triangle. To manage these large digits, more spacing is
                         required between numbers. For 2 digit numbers, 1 space is not enough
                         because it will take up the space of that 1 space and the space of
                         where the number sits. Therefore, :3d or 2 spaces guarantee that an
                         extra space is left before the 2 digit number takes up two more spaces.
            
                         def num_triangle(x):
                             'enter a number as the size of your triangle'
                             for i in range(x):
                                 for j in range(x-i-1):
                                     print('   ', end='')
                                 for k in range(i):
                                     print('{:3d}'.format(k+1), end='')
                                 print()
                                 
                         num_triangle(10)

                         output:                             1
                                                          1  2
                                                       1  2  3
                                                    1  2  3  4
                                                 1  2  3  4  5
                                              1  2  3  4  5  6
                                           1  2  3  4  5  6  7
                                        1  2  3  4  5  6  7  8
                                     1  2  3  4  5  6  7  8  9
                                  1  2  3  4  5  6  7  8  9 10

                         Depending on the size of the largest number, spacing can be
                         altered to your liking by changing the number from {:3d}
                         to whatever number of spaces you desire. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 74:
            print('''
                     STRING VALUE UNICODE
                     In this episode, we'll discuss a method in adapting the unicode
                     values of alphabets into more pragmatic and intuitive values.
                     These values begin at 1 until the last letter of the alphabet.
                     Using this new means of classifying alphabets, the sum of letters
                     in a given word will be calculated and printed to the screen.
                     Once the user enters a word, they should be given access to enter
                     another word which prints the sum of values associated to the letters
                     in that word.''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    break
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         Solving this problem means breaking down the solution into
                         a various number of smaller steps.

                         We first define a method of continuously prompting users
                         for their word until they decline or enter a quit, whereby
                         the program ends and the user's are stripped of program's
                         usability. To do this a while loop must be used with which
                         ends given a command word like quit.

                         done = True
                         while done:
                             question = input('Enter a word to receive letter sums. Press quit to end. ')
                             if question == 'quit':
                                 done = False

                         The next step is to create a method to process the value of the word
                         using an arithmetic function that adapts the unicode value of that
                         alphabet into our own class of values. Within the unicode table, it
                         is important to remember that alphabets begin at value 97 until 123
                         associated with the last letter in the alphabet. If we require our
                         values to begin at 1, subtracting 96 from all those numbers generates
                         the value of that number classified using our own table of values.

                         done = True
                         while done:
                             question = input('Enter a word to receive letter sums. Press quit to end. ')
                             if question == 'quit':
                                 done = False
                             count = 0
                             for i in question:
                                 count += ord(i) - 96
                             print(count)

                         output:Enter a word to receive letter sums. Press quit to end. happy
                                66
                                Enter a word to receive letter sums. Press quit to end. good
                                41
                                Enter a word to receive letter sums. Press quit to end. tell
                                49
                                Enter a word to receive letter sums. Press quit to end. quit
                                67

                         The program above is functioning as we desire, the only problem remains that
                         the code is not as pythonic as possible. Instead of a for loop, we can use
                         list comprehension and sum the numbers within that list. This removes the
                         requirement of the counter.

                         done = True
                         while done:
                             question = input('Enter a word to receive letter sums. Press quit to end. ')
                             if question == 'quit':
                                 done = False
                             count = sum([ ord(i) - 96 for i in question])
                             print(count)

                         output:Enter a word to receive letter sums. Press quit to end. happy
                                66
                                Enter a word to receive letter sums. Press quit to end. good
                                41
                                Enter a word to receive letter sums. Press quit to end. tell
                                49
                                Enter a word to receive letter sums. Press quit to end. quit
                                67

                         Achieving the same outcome with shorter lines of code is always the
                         recommended approach for solving a problem. Instead of using the for loop
                         and a counter which is incremented by the values stored by letter iterables
                         in the word entered, we use the sum function which adds all the numbers
                         in the list count; comprised of the values of the letters of the
                         alphabet using our classifier.''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 75:
            print('''
                     LIST SUM FUNCTION
                     When you're provided with a list of numbers and you want to
                     add the numbers in that list without manually creating a counter
                     and iterating through the list with a for loop and incrementing
                     the counter by the iterables of the for loop, the sum function
                     takes in a single argument, namely the list, it adds all the
                     numbers within that list together and prints out the sum.
                     Before we appreciate the simplicity and pragmatism of the sum
                     function, it is neccessary to manually creating a sum function
                     using a list.

                     x = [1,3,5,8,9,10]

                     count = 0
                     for i in x:
                         count += i
                     print(count)

                     output:36

                     Undoubtedly, the sum of all the numbers in the list is 36. But
                     we used more lines of code than required. Instead we invoke the
                     sum function and pass in the list x to add all numbers in that
                     list together.

                     x = [1,3,5,8,9,10]
                     print(sum(x))

                     output:36

                     In two lines of code, we achieved the same result. It is highly
                     recommended to use the sum function in adding numbers together
                     instead of creating a for loop and a counter. Saving space and
                     time is invaluable in python and one should do so as often as
                     possible. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(sum)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 76:
            print('''
                     KEYWORDS AND OR
                     In the context of python conditional statements, the keywords and or
                     are distinctly different and its important for one to comprehend
                     the true differences between these two keywords.
                     The main differences are illustrated through various examples and
                     lots of practice.

                     example 1) name = 'jacob'
                                for i in name:
                                    if i == 'j' and i == 'a':
                                        print(name)
                                    else:
                                        print(i)

                     output:j
                            a
                            c
                            o
                            b

                     example 2) name = 'jacob'
                                for i in name:
                                    if i == 'j' or i == 'a':
                                        print(name)
                                    else:
                                        print(i)

                     output:jacob
                            jacob
                            c
                            o
                            b

                     The chosen examples are similar with one crucial difference, the
                     keyword statements and or. The first example is a common application
                     of the for loop, if and else statements which stores a name 'jacob'
                     and checks each letter of the name if that letter is equivalent to
                     the required letter it prints the whole name, otherwise just the letter
                     of the name. One might expect that j and a are both iterables of the
                     name 'jacob', so why does the outcome show different? Why are letters
                     printed separately on individual lines when we expect j and a to
                     meet the if condition and in so doing print the whole name on one line?
                     The reason for this is a key distinction between the and or keyword
                     statements. In the second example, we observe that in line of the
                     iterables j and a, the whole word is printed to our expectation. This
                     is because the or statement creates a condition which checks if any one
                     of the two conditions listed is met, whereas the and statement checks
                     that if and only if both conditions are met, the whole name will be printed.
                     Iterables j and a are not both found on the same line where our for loop
                     is concerned. If you understand the for loop, the letters of the word are
                     independently printed to new lines of the screen. Therefore, letter j is
                     printed and on a new line letter a. Because both letters never coexist,
                     the and statement is never initiated and the result is identical to printing
                     iterables under the for loop. The or statement is met twice in the for loop
                     because the first iterable is j, so the condition is met a first time and the
                     whole name is printed on the first line to the screen. The next letter of the
                     name jacob is a; therefore the name is also printed to the next line on the
                     screen. This condition is not fulfilled by sucessive letters because iterables
                     are never again equivalent to j or a so the independent letters are printed to
                     separate lines. These are crucial yet subtle differences between keywords and
                     or that one must completely understand before proceeding to topics of difficulty''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 77:
            print('''
                     LOWEST DENOMINATOR
                     The concern of this episode is to establish a form of asking
                     a user for two argument numbers and creating conditions that
                     always divide the largest of the numbers entered by the
                     smallest''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''Cracking this problem requires one to solve the problem
                         piece by piece.

                         Understanding the problem is first and foremost. We want to
                         create a way of prompting the user to enter two numbers and
                         adding conditions to these numbers. A function of two arguments
                         is ample for this problem.

                         def lowest_denominator(x,y):
                             'enter two numbers and the highest will divide the lowest'

                         A next step is to devise a condition that for any numbers entered,
                         the largest is always divided by the smallest. An if statement with
                         the condition that when x (the first number) is larger than y,
                         x will divide by y because x is the greater number. The opposite
                         of this is when x is smaller than y, where y shall divide x instead.

                         def lowest_denominator(x,y):
                             'enter two numbers and the highest will divide the lowest'
                             if x > y:
                                 return x/y
                             else:
                                 return y/x

                         print(lowest_denominator(18,3))
                         print(lowest_denominator(8,4))
                         print(lowest_denominator(5,6))

                         output:6.0
                                2.0
                                1.2

                        The above function works properly, but we should always consider a
                        simplified and neater method of acquiring the intended result with
                        less lines of code.

                        def lowest_denominator(x,y):
                             'enter two numbers and the highest will divide the lowest'
                             return max(x,y) / min(x,y)

                        print(lowest_denominator(18,3))
                        print(lowest_denominator(8,4))
                        print(lowest_denominator(5,6))
                        
                        output:6.0
                               2.0
                               1.2

                        Instead of using conditional if and else statements, within python's library
                        there exists functions that find the largest and smallest of entered
                        number arguments. These are the max and min functions. Reducing the code
                        to one line is also the recommended approach. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 78:
            print('''
                     IN DEPTH RANGE FUNCTION
                     This episode is a deep dive into the range function, its many
                     arguments and how and when to use it in different situations and
                     with different functions.
                     The range function is beneficial in generating numbers following
                     an ascending or descending sequence. Examples below.

                     example 1) numbers = list(range(1,10))
                                print(numbers)

                     output:[1,2,3,4,5,6,7,8,9]

                     example 2) numbers = list(range(1,10))
                                for i in numbers:
                                    print(i)

                     output:1
                            2
                            3
                            4
                            5
                            6
                            7
                            8
                            9

                    example 3) for i in range(1,10):
                                    print(i)
                    output:1
                           2
                           3
                           4
                           5
                           6
                           7
                           8
                           9

                    example 4) numbers = list(range(1,11))
                               print(numbers)

                    output:[1,2,3,4,5,6,7,8,9,10]

                    Above are some useful demonstrations of the range function in
                    collaboration with the for loop and the list function. If we
                    stored the range as numbers without the list, the range would
                    be printed to the screen again. The requirement of the list
                    is to inform python as to how the numbers will be stored.
                    Storing them in a list is ideal because we're generating more
                    than one number and a python immediately understands to store
                    each number in the range of numbers into independent items of
                    the list. Recognize that the numbers end at 9 but 10 was
                    entered in the range. A reason for this is from the way the
                    range function was created. The stop number or the maximum
                    number in our range is not included in the outcome. In example
                    4, number 11 was the stopping point and this allowed 10 numbers
                    to print to the screen. The starting point is also important in
                    the range function. It gives the neccessary information as to
                    where we expect our numbers to begin from in a given range.
                    Because the range function always starts at zero, the range of
                    numbers must be equivalent to the maximum number enlisted in the
                    stopping point. Therefore, the maximum number itself is not
                    included in the range to make way for the extra zero that the range
                    begins with. In our examples we start at 1: and therefore, we need
                    to end at 11 instead of 10 because the zero is neglected in our
                    range. Other applications of range include its relationship to the
                    len function.

                    example 5) numbers = list(range(1,11))
                               for i in range(len(numbers)):
                                   print(i)
                     output:0
                            1
                            2
                            3
                            4
                            5
                            6
                            7
                            8
                            9

                     example 6) name = 'john'
                                for i in range(len(name)):
                                    print(i)
                     output:0
                            1
                            2
                            3

                     The two example above prove how the range function responds to
                     the len function and created astonishing outcomes. The first
                     example is not elegant in the manner that we repeated the
                     same method in two different ways to reach the same outcome.
                     Simply storing numbers as a list of range 1 to 10 and printing
                     the result in a for loop produces an equal result, but for
                     the purpose of demonstration, the above method highlights range
                     applications. In the final example, we present variable 'john'
                     and iterate using the len function across the letters of the
                     name 'john'. There are 4 letters in the name john which informs
                     python of the range 4 because the len function on a string word
                     dictates the amount of letters in that word. As the range is 4,
                     the number 4 is excluded in the range and numbers starting from
                     zero (because a starting point was left unspecified) until 3. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(range)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 79:
            print('''
                     LOWEST COMMON DENOMINATOR
                     Through this episode, one is expected to devise a way of finding the
                     lowest common denominator where two number arguments are supplied.''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    break
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''This problem will be decomposed into smaller, more managable, steps.

                         In tackling this problem, one must consider what we want for the user
                         to do. The user should be able to enter two numbers and find the lowest
                         common denominator of those two numbers. The lowest common denominator
                         is a common multiple between the two numbers entered. First and foremost,
                         we should create a function.

                         def lcd(x,y):
                             'enter two numbers to find the lowest common denominator'

                         In a previous episode, we found a way of dividing the largest by the smallest
                         number supplied with two numbers. This was easily accomplished by taking the
                         maximum of the two and dividing by the minimum. In this function, we
                         know that 1 is a multiple of every number. Therefore, we should start
                         selecting numbers from 2 onwards. As we're expecting to test multiple
                         numbers we require a range function and a for loop. The numbers within our
                         range should begin at 2 and end at the minimum of the two numbers. As
                         we want to include the minimum in the range we add 1. The condition is that
                         if both the maximum and minimum of our numbers are divisible by numbers
                         in the range up to and including the minimum number starting from 2, this
                         number is the lowest common denominator of the 2 numbers. To devise a function
                         we need only add one condition with the and keyword.

                         def lcd(x,y):
                             'enter two numbers to find the lowest common denominator'
                             for i in range(2,min(x,y)+1):
                                 if max(x,y)%i == 0 and min(x,y)%i == 0:
                                     print(i)
                                     break

                         lcd(18,3)
                         lcd(24,8)

                         output:3
                                2

                         The outcome is an anticipated. Its also important to remember a method of
                         checking for multiples of numbers. A crucial way to check if a number is
                         a multiple of another is using the modulo. The modulo returns the remainder
                         when two numbers are divided by each other. Therefore, the remainder is
                         always zero if a number is a multiple of another becayse there is no
                         remainder. In our function, we required both the max and minimum number
                         to have a remainder of zero for the number to be a multiple of both
                         numbers. The first instance this is true, we print the value and break to
                         stop the for loop. This is due to the fact that numbers in the range start
                         from lowest to highest and as a result, the earliest number that meets the
                         condition is the lowest multiple of both numbers; and hence, the lowest
                         common denominator. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 80:
            print('''
                     LEN FUNCTION
                     This episode will discuss the len function in detail
                     The len function is used for various purposes. These purposes are made
                     more apparent through different examples.

                     example 1) name = 'john'
                                print(len(name))
                     output:4

                     example 2) names = ['john','jacob','jill']
                                print(len(names))
                     output:3

                     example 3) numbers = [1,2,5,6]
                                print(len(numbers))
                     output:4

                     example 4) numbers = list(range(1,10))
                                print(len(numbers))
                     output:9

                     example 5) names = {'a':1,'b':2,'c':3}
                                print(len(names))
                     output:3

                     The examples above demonstrate the key features of the len function. The len
                     function informs users of the number of items in a list, a dictionary or a
                     range function wrapped between a list. The range function also provides information
                     about the amount of letters in a word if the variable stored was a string. The len
                     function is typically used in the context of example 4 and in the sense of changing
                     words into number outputs.

                     example 6) name = 'john'
                                for i in range(len(name)):
                                    print(i)
                     output:0
                            1
                            2
                            3

                     This example shows an alternative approach using the len function. If you require
                     the index of certain letters in a word printed to a new line. The for loop and print
                     function shows the iterables of a list to a new line. Because we used the len
                     function on the variable name, the len function calculates the number of letters in
                     the string name which is 4. This is passed through a range function printing numbers
                     up until 4 but not including 4. The range function begins at zero and the for loop
                     prints each number from 0 to 3 in a new line. This informs users that if they want
                     to index the name 'john', the maximum index is 3.

                     name = 'john'
                     print(name[3])

                     output:n

                     name = 'john'
                     print(name[4])

                     IndexError: string index out of range.

                     The test above demonstrates that the maximum index of variable name storing
                     'john' is 3. This is identified using the previous example with the for loop
                     and the len(range()) function. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(len)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 81:
            print('''
                     ASSIGNING MULTIPLE VARIABLES IN A LINE
                     In python, it is possible to assign multiple variables on a single line
                     following certain procedures. In assigning multiple variables per line, it
                     is important for one to understand that the number of variables assigned must
                     match the number of values which those variables are assigned. This is made
                     evident with some examples.

                     example 1) names, numbers = ['john','mark','jack'],[1,2,4]

                                print(names)
                                print(numbers)

                     output:['john','mark','jack']
                            [1,2,4]

                     example 2) names, numbers = [1,2,4]

                     ValueError: too many values to unpack (expected 2)

                     example 3) names = [1,2,4], ['john','mark','jack']
                                print(names)

                     output:([1, 2, 4], ['john', 'mark', 'jack'])

                     The three example listed above are key lessons on list unpacking. The
                     first example is a crucial lesson in that two lists are assigned
                     values on a single line and we want to print each individual list to
                     check if those values were stored correctly. The outcome confirms that
                     both variables stored list values accordingly. The second example makes
                     light of list unpacking fundamentals. If one decides to assign 2
                     variables to one value, python doesn't unpack those variables properly
                     because both variables compete for the same value. This leads to a
                     ValueError where there are too many values to unpack because there aren't
                     enough values associated with the number of variables. There should
                     always be equivalent number of values to variables for multiple variable
                     assignments to work properly. The last example shows what were to happen
                     if one variable is assigned two values, or for example one variable were
                     assigned more than a single value. In this situation, the variable is
                     stored as a tuple of all the values assigned to that variable. Because
                     variable names is assigned 2 lists, a tuple of 2 lists is generated when
                     we print variable names to the screen. Multiple reassignments are useful
                     in many circumstances to save space and time.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(str)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 82:
            print('''
                     LEN WITH FOR LOOP AND BREAK
                     The aim of this episode is to share an approach of using the len
                     function in conjunction to the for loop to print a sub-string
                     onto the screen multiple times until a condition is untrue and
                     the loop is broken
                     For starters, one should remember both the functionality of the len
                     and for loop functions. The for loop enables us to iterate through a list,
                     a dictionary, a range and the letters in a string. The for loop is a way
                     of decomposing an item of several components or items (like a list or word)
                     into its constituent parts; such as letters of a word or individual objects
                     of a list. The range function allows users to generate numbers in a logical
                     manner. That is, generate the numbers in ascending or descending orders with
                     customizable steps by which the numbers in the list are to follow. For example, it
                     is not recommended to type numbers 1 to 10 to the screen, but use a range of
                     1 to 11 (remembering that the maximum number is excluded in the range). This
                     creates an object of numbers. To show all the numbers to the screen, it is
                     advisable to wrap this object by a list function, putting numbers 1 to 10 as
                     individual numbers of that list. Now that we know how these functions respond
                     to arguments, we consider conjoining them.

                     x = 'abcdefghij'
                     y = ''
                     for i in x:
                         if len(x) < 4:
                             y += i
                         print(y)

                     output:a
                            ab
                            abc
                            abcd
                            abcd
                            abcd
                            abcd
                            abcd
                            abcd
                            abcd

                     The code above uses the for loop and the len function in one full swoop. We store
                     the letters of the alphabet until j as variable x and y is an empty string
                     variable. The for loop iterates through the independent letters of x. Then the
                     if statement checks whenever the len of y is less than 4 characters. When this
                     occurs, an extra letter is appended to variable y. Because the condition only
                     holds when the length of y is less than 4 (or when there are less than 4 letters
                     in the string y) 'abcd' is printed to the screen for the remainder of iterables in
                     the string x. For the first 4 letters of x, the empty string y is appended to
                     because the length of y is less than 4. When the number of letters in y reaches
                     4, the condition is unmet and the number of letters remaining in the string x
                     is the amount of times the four letters appended to string y are printed to the
                     screen. To stop these extra instances of 'abcd' from being printed to the screen,
                     one should introduce a break in the loop at the first instance that the if
                     condition is unfulfilled. Introducing an else with a break redirects the iterables
                     after the length is less than 4 to a break statement, ending the program.

                     x = 'abcdefghij'
                     y = ''
                     for i in x:
                         if len(x) < 4:
                             y += i
                         else:
                             break
                         print(y)

                     output:a
                            ab
                            abc
                            abcd

                     The example above shows the break function working to our advantage. The first
                     instance where the length of sub-strings in y is 4 initiates the else statement.
                     This in turn breaks the loop and ends the program.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 83:
            print('''
                     WHILE LOOP WITH LEN FUNCTION
                     In this episode, an alternate method of isolating sub-strings from
                     string words will be shown. This method will manipulate the len function
                     and the while loop to print sub-strings of string to separate lines on the
                     screen.
                     To achieve this goal, one must consider how to use the while loop and len
                     function together. If we create a variable x that stores letters of the
                     alphabet and empty string variable y, we can iterate through letters of string
                     x using a for loop and ammend to empty string y by enlisting the appropriate
                     conditions. This method involves indexing values and printing the empty string
                     y each instance the index is increased.

                     x = 'abcdefgh'
                     y = ''
                     count = 0
                     while len(y) < 3:
                         y += x[count]
                         count += 1
                     print(y)

                     output:abc

                     In this code, we set the counter to zero corresponding to the first letter of the
                     variable x. As variable y stores an empty string and the value of count is zero,
                     indexing count from variable x indexes the letter in place zero from string x. This
                     is the first letter of string x. Then count is incremented by 1, but the length
                     of string y is still less than three because only the first letter of string
                     x has been ammended to y. This process is continued until there are 3 letters inside
                     y, in which case, the while loop condition is disatisfied and the loop is stopped. We're
                     interested in the last stored value that y take. The expected value of y is the first
                     three letters of the alphabet at the point the while loop ends. If the condition is changed
                     to 4 instead of 3. The third index of string x (the fourth letter of the alphabet) is
                     appended to string y and so the last stored value of y is the first four letters of
                     the alphabet. The condition can only be ammended until the len of string x which
                     is 8 equivalent to the first 8 letters of the alphabet. If the len is changed to 8
                     instead of 3, 'abcdefgh' would be printed to the screen instead of 'abc'. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 84:
            print('''
                     COUNT SUB-STRINGS
                     If you've wondered of a way to count sub-strings from a string
                     using a manual method involving the range, len and for loop, this
                     episode explains that method you're in search of.
                     The first thing to do is store the string variable that holds the
                     string which you want to count the frequency of the sub-strings from.
                     Assign another variable which starts at zero corresponding to the
                     counter of the sub-strings from that first string variable.

                     names = 'jackfredjacksamsamdadfreddad'
                     count = 0

                     Now that we've assigned both these variables, its time to consider how
                     to create conditions that somehow count the instances of sub-string names
                     from the main string variable names and increment the count function to
                     store the frequencies of these sub-string names. For example, if we wanted
                     to count the number of times 'fred' occurs in string names, the outcome should
                     be 2. To do so, we invoke the for loop in the range of the string names to
                     consider individual letters from that string. We manipulate string indexing
                     to consider strings in a range of the particular index. For example the first
                     three letters of the string names can be indexed [0:3] (remembering that the
                     maximum number in the index is excluded). Indexing 0:3 means the first second
                     and third letters of the string because indexes begin at zero to the penultimate
                     string in a given index range. As we want to index four sub-strings (or four
                     letters) from string names, we need to specify an index range of 4 and increase
                     the range to accomodate all the sub-strings of 4 letters in the string names.
                     Using the for loop and iterables, this can be achieved by indexing through
                     string names using a range index of the iterable until the iterable plus 4. This is
                     done so that for every iterable in the length of our main string, the sub-string
                     will start at that index and end 4 letters from that index which guarantees that
                     we always receive 4 letter words throughout the string. Creating the condition that
                     for each of these 4 letter words, we want them to be equivalent to a name within
                     the main string, say 'fred'. When this is satisfied, the count is incremented by 1
                     and this process continues until all 4 letter words that are equivalent to the
                     condition add an extra 1 to the counter. We print the count outside the loop to
                     show the last stored value of count which should be the amount of time python
                     identifies the equivalences in our string.

                     names = 'jackfredjacksamsamdadfreddad'
                     count = 0
                     for i in range(len(names)):
                         if names[i:i+4] == 'fred':
                             count += 1
                     print(count)

                     output:2

                     As we expect, the output is 2 because the sub-string 'fred' is only twice repeated
                     in string names. If we wanted to change the selection to name 'sam', we wouldn't use
                     indexing for the first 4 letters, but three letters instead because the word same
                     is comprised of three letters. The indexing used is highly dependent on the number of
                     letters in the word. We adapted the range and len functions to iterate through numbers
                     from 0 to the number of letters in the string names. If we changed for loop to names
                     only, the conditions won't apply because indexing only works using numbers and not strings.
                     This shows a TypeError because python doesn't understand how to index sub-strings from the
                     string 'names'. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 85:
            print('''
                     BOOLEAN SHORTCUT
                     If you want to create a shortcut of identifying even and odd numbers
                     by using a function, this episode outlines that shortcut you could use
                     Finding an odd or even number requires us to create conditions that print
                     odd if our number is true or false if our number is even. An odd number is
                     not divisible by 2 whereas an even number are all divisible by 2. This provides
                     the defining conditions of odd and even numbers. We define a function with an
                     if else statement that checks if the modulo of the specified number argument is
                     with 2 is equal to zero, the number should print True if we have an even function;
                     hence, our number is even. Else, the number is odd. On the other hand, if the
                     function is to check for odd numbers and the number is divisible by 2, the statement
                     is False because the number is not odd but even. In our example, we will anticipate
                     an odd function.

                     def odd(num):
                         'enter a number to find if its odd or even'
                         if num%2 == 0:
                            return False
                         else:
                             return True

                     print(odd(5))
                     print(odd(6))
                     print(odd(3))

                     output:True
                            False
                            True

                     The conditions supplied are responding correctly because 5 is odd and so the
                     output is True. Six is even; and therefore the output is False. The main issue
                     remains that the function is undesirably long when it could in fact be shortened
                     to a much simpler condition. Recognizing that python has built-in boolean statements
                     provided a conditional statement. For instance, if one were to enter on interactive
                     python whether 1 > 2, the output would be False. Reason being, python understands
                     and checks against the statements provided following logic. The same applies to
                     the modulo function which determines the remainders of numbers and whether those
                     remainders are equal to zero meaning that the number is a multiple of the other.
                     Using this fact, we delibarately simplify our function to a single condition and return
                     statement.

                     def odd(num):
                         'enter a number to find if its odd or even'
                         return num%2 == 0

                     print(odd(5))
                     print(odd(6))
                     print(odd(3))

                     output:True
                            False
                            True

                     We obtained the desired result. Congratulations on simplifying the function.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 86:
            print('''
                     STRING FIND METHOD
                     The onus of string find is to return the index of a sub-string from a string
                     entered into the argument of str.find(). This is made apparent through
                     various examples.
                     The first examples will expand on the functionality of the str.find() method.

                     example 1) names = 'jackjilljackgillgillianfredfrederickderekisabella'
                                print(names.find('jack'))

                     output:0

                     example 2) names = 'jackjilljackgillgillianfredfrederickderekisabella'
                                print(names.find('jack',1))

                     output:8

                     example 3) names = 'jackjilljackgillgillianfredfrederickderekisabella'
                                print(names[names.find('jack',1)])

                     output:j

                     The three examples above prove how the str.find() method requires a sub-string
                     argument and returns the index of that sub-string. An optional number argument
                     is required to return the nth repeat of that particular sub-string. For example 2,
                     we used the string find method to identify the index of sub-string 'jack'.
                     The second example is different from the first in that the output is 8, why is this?
                     Explained above, the optional number argument informs python of which repeat of
                     that sub-string we want to find the index of. String 'jack' is repeated twice, so if we
                     want the index of the second 'jack' we use the optional number argument with the
                     string find method to isolate our search to that particular instance of 'jack'. The
                     output is 8, which corresponds to the index of the first letter of sub-string 'jack'
                     repeated once from string 'names'. If we enter 2 instead of 1, we would need to find the
                     index of 'jack' from the lowest index 1 in string 'names'. In this case, python responds by returning
                     returning the lowest index of the last sub-string 'jack' from 'names'. Provided with the
                     starting point one, python disregards any sub-string jack which has a lowest index
                     zero. The only instance of this is the first 'jack' in 'names'. Entering numbers up to
                     8 will continuously return the position of the lowest index of the first repetition of
                     'jack' in names because we are directing python to consider sub-strings from those indexes
                     until the lowest index of the next repetition of the sub-string we're searching for. When
                     values larger than 8 are entered, python slices the string from 8 onwards and attempts
                     to locate the sub-string index from 8 onwards. This results in failure because 8 is the
                     maximum index of where 'jack' can be found as jack is only repeated once at that position.
                     Entering larger numbers results in failure and returns -1.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                help(x.find)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 87:
            print('''
                     SUB-STRING FIND METHOD
                     This episode intends to explain a method of finding the number of
                     sub-strings from a string using the string find method and other
                     python statements.
                     To do this, it is highly recommended to read the previous episode which
                     outlines the main functions of the string find method. For those who
                     haven't done this, the string find method has one neccessary argument and
                     an optional argument. A neccessary argument is the sub-string your in
                     search of. For example, if there is a long string of names written without
                     spaces stored as variable 'names' and you intend to find the amount of
                     'john' sub-strings in name, the string find method can iterate through
                     this long string and isolate the instances of the sub-string 'john' if the
                     sub-string argument provided into the find method is 'john'. If john is
                     repeated more than once, perhaps twice in the string names, then the
                     string find method can also help with that by supplying an optional index
                     argument, which informs the find method to locate the particular repetition
                     of that sub-string. Supposing that 'john' is repeated again in index 8 in 'names'
                     and we want the first repetition of 'john' in names with lowest index 8, we enter 1
                     as the optional index in the string find method for 'john'. This returns the lowest
                     sub-string index from 1 onwards.To locate the frequency of a particular sub-string we
                     need to define a counter variable and a placement variable which changes as we iterate
                     through the main string. A while loop is used in this situation because we want to create
                     a condition that continues to check sub-strings throughout the entire string. The place
                     variable is used to provide the correct index of the particular sub-string in our main
                     string 'names'. Because we want the place index to find all instances throughout
                     the whole string where the sub-string matches our condition, we need to increment
                     our place index each time a match is found to set the index from that sub-string
                     onward. This will make more sense when the full code is provided and we discuss
                     the process of what occurs throughout the code.

                     names = 'jackjilljackgillgillianfredfrederickderekisabella'
                     place, count = 0,0
                     while names.find('jack',place) >= 0:
                         place = names.find('jack', place) + 1
                         count += 1
                     print(count)

                     output:2

                     The method above stores people's names (with repetitions) as variable 'names'. Then
                     we set a place and count variable to zero to count moving total of repetitions of a
                     specific sub-string from 'names'. The first instance where a sub-string is located is
                     when place and count are zero, so the condition of the while loop is satisfied, variable
                     place is then incremented by 1 because the lowest index of sub-string 'john' using the string
                     find method is 0 as the optional index argument is zero (so we're focused on finding
                     sub-string 'john' without repetitions). This variable is incremented by 1 and count is
                     also increased by 1. The condition is still satisfied because the position of the lowest
                     index of sub-string zero with a one repetition is 8. The first 'j' is at index zero and
                     if you count starting from zero to the next 'jack' starting with j, you will find that the
                     second j of sub-string 'jack' is in the eight position. Because 8 is still greater than
                     zero, the while loop continues and place and count variables are incremented by 1. After
                     the second instance of 'jack', place is now 9. Because there is only one repetition of
                     'john' at index 8, any optional index greater than 8 results in failure returning -1. This
                     value doesn't meet the while condition and so the cycle stops. We print the last value of
                     count before the cycle stops which is 2. This 2 informs us of the number of times our
                     string find method found the lowest index of the sub-string we were in search of. In other
                     words, it returns the frequency of that particular sub-string in our main 'names' variable. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 88:
            print('''
                     SUB-STRING FUNCTION
                     In this episode, we will discuss a function for finding sub-strings from
                     a string variable. The tools we'll be using our already at our disposal and
                     we will change them slightly to create a function for executing this action.
                     To achieve our intentions, we will be using the code supplied in the previous
                     episode with a slight adjustment.

                     def sub_string(word,string):
                         'enter a sub-string word and the string which you want to count the
                          sub-string from'
                          count, place = 0,0
                          while string.find(word,place) >= 0:
                              place = string.find(word,place) + 1
                              count += 1
                          print('{} is repeated {} times in {}'.format(word,count,string))

                     sub_string('jack','jackjilljackgillgillianfredfrederickderekisabella')
                     sub_string('fred','jackjilljackgillgillianfredfrederickderekisabella')
                     sub_string('jill','jackjilljackgillgillianfredfrederickderekisabella')
                     sub_string('gillian','jackjilljackgillgillianfredfrederickderekisabella')

                     output:jack is repeated 2 times in jackjilljackgillgillianfredfrederickderekisabella
                            fred is repeated 2 times in jackjilljackgillgillianfredfrederickderekisabella
                            jill is repeated 1 times in jackjilljackgillgillianfredfrederickderekisabella
                            gillian is repeated 1 times in jackjilljackgillgillianfredfrederickderekisabella
        
                     The function above is complicated at first glance, but in reality it is much more
                     intuitive than it looks. We defined a sub-string function that informs us of the
                     sub-string and the amount of times it is repeated in a string format statement.
                     The function starts a count and a place variable at zero. If the index of the string
                     supplied in the argument is greater than or equal to zero, the while loop continues
                     to increment the counter by 1. If the lowest index of the sub-string we're in search of
                     is not found, the string find method returns -1 on failure, which is less than zero and
                     so our while loop is broken. The last stored value of the count, place and string is
                     printed in a format statement which breaks down all the required information into a single
                     line. This is also a good function if you have a story and you want to count the instances
                     of something from that story. In a previous example, a story about jack and jills frustrating
                     car ride journey was stored as variable story. If we used variable story in out function
                     and wanted to find the instance of the word 'they' from that story, our function would also
                     work to that end.

                     def sub_string(word,string):
                         'enter a sub-string word and the string which you want to count the
                          sub-string from'
                          count, place = 0,0
                          while string.find(word,place) >= 0:
                              place = string.find(word,place) + 1
                              count += 1
                          print('{} is repeated {} times'.format(word,count))

                     story = 'jack and jill went on a ride. The ride was apocalyptic because jack and
                              jill hated it. They detested it. They loathed it. They absolutely reeked
                              vengeance against it. It was the bane of their existence. So cruel and so
                              malicious and so distasteful and so horrible, absolutely gruelling, problematic
                              and jack and jill just were so angry, horrified, terrified, disaligned from
                              such a putrid experience of a disparaging trip.'

                     sub_string('They', story)
                     sub_string('jack', story)
                     sub_string('and', story)
                     sub_string('jill', story)

                     output:They is repeated 3 times
                            jack is repeated 3 times
                            and is repeated 7 times
                            jill is repeated 3 times

                    The function was adapted slightly to prevent printing the whole story on each line
                    of the output. ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 89:
            print('''
                     WHY NOT STRING COUNT
                     Another method for counting sub-strings of strings is using the count
                     method. While some might argue that the count method is the recommended
                     method for counting the number of sub-strings from a string, it is not
                     entirely true because of one caveat associated to the count method. The
                     count method for finding sub-strings will be featured in this episode, so
                     will the limitations of such a solution.
                     The string count method, like string find, is needs one argument which is
                     the sub-string in question. Following a previous example, if you were to
                     store consecutive names with repetitions in a continuous line stored as
                     variable 'names' and say the name 'fred' was one of the names within the
                     'names'. Supposing that you wanted to find the number of times 'fred' is
                     repeated in 'names', then you would use the count method and the result
                     returned would be this number. So, why the trouble of using a while loop,
                     string indexing and the place and count assignments used in previous methods?
                     A subtle detail about the count method is that it counts occurences of a sub-string
                     that isn't overlapping. Meaning that palindromic names like 'bob' if written
                     like 'bobob' would be considered as 1, where in fact bob is repeated twice in
                     this example. Therefore, we construct separate methods of counting sub-string
                     frequencies from string variables.

                     example 1) names = 'jackjilljackgillgillianfredfrederickderekisabella'

                                print(names.count('jack'))
                                print(names.count('jill'))
                                print(names.count('isabella'))
                                print(names.count('gill'))

                     output:2
                            1
                            1
                            2

                     example 2) names = 'bobobmamamjackjilljohnjosephjack'
                                print(names.count('bob'))

                     output:1

                     As we expect, the outputs are numbers. These numbers refer to the number of occurences
                     of sub-string names from string 'names'. We observe that name 'jack' is repeated twice,
                     'jill' and 'isabella' once and 'gill' twice, first in 'gill' and second as part of
                     the name 'gillian'. Depending on your expectation and desires, apply the count method
                     in caution. If you want to generally count sub-strings where you know there won't be
                     overlapping occurences of the sub-string, the count method is highly recommended. On the
                     contrary, situations that involve overlapping sub-strings require more intrinsic methods and
                     where you should apply the while loop and string find methods to isolate the particular
                     index of certain sub-strings. This is featured in the second example where sub-
                     string bob is repeated twice in 'names', but the count method produces 1 because
                     the second occurence of 'bob' is an overlapping string.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                x = 'name'
                help(x.count)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 90:
            print('''
                     SQUARE FUNCTION
                     This episode challenges one to create a way of prompting a user for a
                     number and with this number returning its square. For example, 2 could be
                     entered and we expect 4 as the output. If 3 is entered, 9 is anticipated.''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         This problem will be deconstructed into several menial steps.

                         First, we define a function of one argument which is the user's number.
                         We're expected to square this number and return the value back to
                         the user.

                         def square(number):
                             'enter a number and acquire its square'
                             return number**2

                         print(square(3))
                         print(square(4))
                         print(square(5))

                         output:9
                                16
                                25

                         The function above is logical. We created a function that returns the
                         square of the number. In python, squaring a number is presented using
                         the double asterisk and multiplication through a single asterisk.
                         Another method of squaring numbers could be by assigning 2 arguments and
                         fixing the second to 2. Why do we do this? This is more customizable
                         because the user can personalize the second argument to whatever value
                         they want. If they require cubes, change the second argument to 3 instead
                         of 2. Quartic values can are obtained by changing the second argument to 4
                         and for higher powers, we change the second argument to the powers we
                         desire to use.

                         def pow(number,power=2):
                             'enter a number and a power to return the number to that power. Powers will
                             be defaulted to 2.'
                             return number**power

                         print(pow(3))
                         print(pow(4,3))
                         print(pow(5,4))

                         output:9
                                64
                                625

                         Another method would be to invoke a multiple argument function, iterate
                         through the list of numbers and multiply each number by the next.

                         def pow(*numbers):
                            'enter a number to return the number to that power. Powers will be defaulted to
                            2.'
                            count = 0
                            new = 1
                            for i in numbers:
                                if count < len(numbers):
                                    new *= i
                                    count += 1
                            return new

                         print(pow(5,5,5,5))
                         print(pow(4,4,4))
                         print(pow(3,3,3))

                         output:625
                                64
                                27

                         Instead of 2 arguments, the function could take multiple number arguments and
                         multiply them by each other. If the numbers in those arguments are identical, then
                         we are simply squaring, cubing or raising that number to a power equal to the
                         number of arguments of that number entered. We can check that 4 cubed is 64, which
                         is equivalent to 4 multiplied by itself thrice. This is not the best method for
                         raising numbers to powers, but its an option from many.''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 91:
            print('''
                     SQUARE ROOT
                     The opposite of the squared function is square root. Create a function that
                     prompts a user for a number or numbers and returns the square root. Bonus
                     challenge is to root any number to any power.''')
            query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
            if query == 'yes':
                print('''Congratulations on solving this problem! Your well on your way to becoming
                         a programmer''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    break
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
            else:
                print('''
                         The solution to this problem is discussed through a series of simpler stages.

                         First consider how to root a number. You may think that rooting a number
                         requires that square root sign and where would one tend to find that
                         root sign on python? The answer to that question is changing the way you
                         think about the square root. The root of any number doesn't neccessarily
                         mean that it needs to have that divisive sign, it is a number to a fractional
                         power. For example, the square root of a number is that number to a half. The
                         same applies for the 3rd or 4th root which is the number to the power of a
                         third or quarter. Now we understand a method of rooting a number, the time
                         has arrived to create a function that does this action. Primarily, our function
                         should prompt for one argument, namely the number which you want to square root.
                         There are several ways to do so. We could create a simple function of one number
                         argument. An alternative is a double argument function with a fixed second power
                         argument to 1/2. Another method is a multiple argument function which roots the
                         number to the arguments provided.

                         def root(number):
                             'enter a number to find its square root'
                             return number**(1/2)

                         print(root(4))
                         print(root(25))
                         print(root(9))
                         print(root(65))

                         output:2.0
                                5.0
                                3.0
                                8.06225774829855

                         The function returns the square root of the number provided as we desired.
                         This is checked by finding the actual square roots of the numbers provided and
                         comparing them with the result acquired through our code. The square root of
                         25 is 5 and the root of 4 is 2. These are unique cases of numbers that return
                         whole number values when they're square rooted. The last number is not quite
                         a square number and so the value is a rational number of many decimal places.
                         A separate method of finding the square root of a number is through the supply
                         of 2 arguments, one of the number and the root to which you want to raise that
                         number to. We can fix the second argument to 1/2 to square root the number, but
                         this method gives us greater access to different roots and powers.

                         def root(number, root=2):
                             'enter a number to find its square root'
                             return number**(1/root)
                
                         print(root(4))
                         print(root(64,3))
                         print(root(81))
                         print(root(729,3))

                         output:2.0
                                3.9999999999999996
                                9.0
                                8.999999999999998

                         From the outcome above, we achieved the results we wanted. The square root
                         of 4 is 2, the cubed root of 64 is 4 and the cubed root of 729 is 9. If you
                         want to disable the decimals in the output, wrap the entire function by an
                         int statement which changes the outcome from floating point numbers to
                         whole number values.
                         
                         def root(number, root=2):
                             'enter a number to find its square root'
                             return int(number**(1/root))

                         print(root(4))
                         print(root(64,3))
                         print(root(81))
                         print(root(729,3))

                         output:2
                                3
                                9
                                8

                         In this function, we obtained whole number values instead of floating
                         point numbers by changing the function to an integer instead of a float.
                         This is a more functional method of finding the square root of a number
                         because we can change the power of our root. The last method consists of
                         creating a function with a multiple argument prompt, iterating through
                         these numbers and doing something with each of them.

                         def root(*numbers):
                         count = 0
                         start = 1
                         for i in numbers:
                             if count <= len(numbers):
                                 start *= i
                                 count += 1
                         return start

                         print(root(64,1/2,1/2,1/2,1/2,1/2))
                         print(root(16,1/2,1/2,1/2))

                         output:2
                                2

                         The output is anticipated. This is not a highly recommended method to use
                         because it requires multiple arguments and each of these arguments are
                         fractions that divide our arguments by consecutively. The problem with
                         this method stems from its complex nature. If we wanted to square root
                         a number, we would need to divide that number by as many fractions in
                         consecutive arguments to find a number that multiplies by itself to
                         equal the number we're square rootinf. For example, if we wanted to square
                         root 16, consider a number when multiplied by itself is equal to 16. That
                         number is 4. But this function would not display 4 unless one enters 2
                         fractional 1/2 arguments, which when multiplied together become 1/4.
                         This fraction times 16 is 4 and that is how you would use this method for
                         finding square roots or higher roots of numbers. It is not the best approach,
                         but an optional one. ''')
                question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
                if question == "help":
                    help()
                    q_2 = input("Do you wish to learn more, enter yes or no: ")
                    if q_2 == 'yes':
                        x = int(input("Enter another episode you wish to learn about: "))
                    else:
                        break
                if question == "quit":
                    window = False
                if question == "more":
                    x = int(input("Enter another episode you wish to learn about: "))
        if x == 92:
            print('''
                     DIVISORS
                     This episode highlights a way of finding divisors of numbers through
                     a function. The function prompts the user for a two number argument
                     required to find whether the second number is a multiple of the first.
                     We create a function that returns True if a number is a divisor of
                     another and False if it isn't. We use python's default boolean True and
                     False operators given a single conditional statement to create this function.

                     def divisor(num_1, num_2):
                         'enter two numbers to check whether the second is a multiple of the first'
                         return num_1%num_2 == 0

                     print(divisor(12,4))
                     print(divisor(14,7))
                     print(divisor(9,2))

                     output:True
                            True
                            False

                     In this function, we're manipulating python's pre-existing logical operators
                     which checks conditions and returns True or False depending on whether the
                     condition's satisfied or isn't. We can check for whether our function works
                     by actually considering the numbers entered into our function. Number 12 is
                     divisible by 4 and we expect True. 14 is a multiple of 7 and the same applies so
                     True should be printed. The last example is False because 9 is not a multiple of
                     2 and returns a remainder of 1 when divided by 2. Because we have a remainder, the
                     condition wasn't satisfied and False is returned instead of True. This is a short
                     and nifty function which checks all numbers using this condition.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                break
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 93 or x == 94:
            print('''
                     FACTORS WITH A FOR LOOP
                     This episode is centred around finding a way to devise factors of numbers
                     using a for loop. Within this episode, we will put into practice all that we
                     learnt including lists, the append method, the for loop and list comprehension.
                     If you're unfamiliar with those topics, it is advised to check out those episodes
                     before continuing to this episode.
                     Finding the factors of numbers requires us to provide a sufficient enough
                     condition that checks for these factors. As we want a place to store all these
                     factors, a list is needed for this application. To find all relevant factors
                     we need some way to iterate through a range of numbers and add numbers which
                     are factors to our list until all numbers are identified and our list is
                     returned to the user. Achieving our aim needs a for loop with a condition that
                     checks for factors of numbers until our number and returns all factors in a
                     list to the user. The condition used previously and which is highly advised for
                     this context is the modulo function. Checking whether the modulo of that number
                     is equal to zero is a sufficient way to find that dividing by that number leaves
                     no remainders; and therefore, the number is a factor of our number. Having been
                     found, the number is stored in our active list.

                     def factor(number):
                         'returns all factors of our number'
                         d = list()
                         for i in range(2,number+1):
                             if number%i == 0:
                                 d.append(i)
                         return d

                     print(factor(27))
                     print(factor(4))
                     print(factor(30))

                     output:[3, 9, 27]
                            [2, 4]
                            [2, 3, 5, 6, 10, 15, 30]

                     As we anticipated, the product is a list of factors for that number including
                     itself because the number is always a factor of itself. The range begins at 2
                     instead of 1 because 1 is a factor of every number. Depending on yourself,
                     starting at 1 or 2 is entirely up to the programmer, but it doesn't drastically
                     augment the function. The code is functional but it is quite long to achieve
                     a simple task. As programmers, it is highly advised to find shorter methods of
                     achieving the same aim. Instead of using a for loop we could have used list
                     comprehension which would achieve the same goal in less space and time.

                     def factor(number):
                         'returns all factors of our number'
                         d = [i for i in range(2,number+1) if number%i == 0]
                         return d

                     print(factor(27))
                     print(factor(4))
                     print(factor(30))

                     output:[3, 9, 27]
                            [2, 4]
                            [2, 3, 5, 6, 10, 15, 30]

                     As expected, the output enlists all possible factors of the number like the
                     previous function. The main difference is that this function is 2 line long with     th
                     an embedded for loop and if statement within the same line of list comprehension.
                     If you're unfamiliar to list comprehension and using conditional statements
                     inside a list comprehension, then use the previous function instead of the function
                     above. But try your level best to understand list comprehension and apply the
                     second function instead of the first for saving space and processing time.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 95 or x == 96 or x == 97 or x == 98:
            print('''
                     THE GREATEST COMMON DIVISOR
                     Several episodes will entail finding the greatest common divisor
                     for any set of two numbers. To achieve our aim, we will apply our
                     knowledge on factors of numbers, the for loop, max and min functions,
                     list comprehension, append method, conditional statements and the
                     modulo to string together our function.
                     Using the lessons from the previous episodes on finding factors of
                     numbers, we think of a solution to finding a common divisor of
                     two numbers. Unlike the lowest common divisor, the greatest common
                     divisor constitutes the largest number possible that is a factor
                     of both numbers entered. Consider first all the factors of a number
                     using our factor function in a previous episode.

                     def factor(number):
                         'returns all factors of our number'
                         d = [i for i in range(2,number+1) if number%i == 0]
                         return d

                     for i in factor(27):
                         print(i)

                     output:3
                            9
                            27

                     The three factors of 27 are 3, 9 and the number 27 itself. The greatest
                     factor of this number is 27 and the same applies for all numbers unless
                     the last number is excluded from the range. if we intended to find the
                     second greatest factor of that number, the answer would be 9 and instead
                     of range(2,number+1) we adapt this to a range of 2 until the number because
                     range excludes the maximum number from the range. If we wanted to find the
                     greatest common factor of 2 numbers, say 4 and 30, we would need to create
                     a sufficient enough condition that iterates through the factors of the
                     greater number and if an iterable of the smaller number is within also
                     inside the list of factors of the bigger number, we print this number and
                     break the loop. This is where the max and min functions come into handy
                     because they immediately isolate the greatest and smallest number from the
                     numbers supplied to them. Using these functions, the for loop and if
                     statements we configure a solution to finding the greatest common factor
                     for two numbers.

                     def factor(number):
                         'returns all factors of our number'
                         d = [i for i in range(number+1,0,-1) if number%i == 0]
                         return d

                     def gcd(x,y):
                        'enter 2 numbers and find their greatest common divisor'
                        for i in factor(max(x,y)):
                            if i in factor(min(x,y)):
                                print('{} is the greatest common divisor of {} and {}'.format(i,max(x,y),min(x,y)))
                                break
                             
                     print(factor(30))
                     print(factor(4))
                     gcd(30,4)

                     output:[30, 15, 10, 6, 5, 3, 2, 1]
                            [4, 2, 1]
                            2 is the greatest common divisor of 30 and 4

                    Our function works because the first common factor of 30 and 4 shown is 2 following
                    the outcome from the factor function. There are a few minor adjustments neccessary yo
                    find the greatest common factor of 2 numbers. The first is a minor ammendment to the
                    factor function which we change from an ascending to descending order of range. This is
                    because we want the greatest factor of our number listed in descending order of
                    magnitude. This is so that the first instance where the greatest common divisor is
                    found will break the loop and print the value to the screen. If the factor list started
                    with the smallest to largest numbers, then we would be considering the smallest common
                    divisor of the two numbers. Given our aims, we change the range to fit our application.
                    The max and min functions are used to first iterate through all the numbers of the
                    maximum number of the 2 numbers supplied to our function. The first instance where one
                    of the iterables from the factors of the minimum number is found in the factors of the
                    maximum number prints that iterable to the screen using the print format function.
                    We then break the for loop to discard any other iterables that conform to this condition
                    because our only interest is the greatest common divisor and not the second or third
                    greatest common divisors. The result can also be accomplished using list
                    comprehension.

                    def factor(number):
                        'returns all factors of our number'
                        d = [i for i in range(number+1,1,-1) if number%i == 0]
                        return d

                    def gcd(x,y):
                        'enter 2 numbers and find their greatest common divisor'
                        l = [print('{} is the greatest common divisor of {} and {}'.format(i,max(x,y),min(x,y))) for i in factor(max(x,y)) if i in factor(min(x,y))]
                        return l

                    print(factor(30))
                    print(factor(4))
                    gcd(30,4)

                    output:[30, 15, 10, 6, 5, 3, 2]
                           [4, 2]
                           2 is the greatest common divisor of 30 and 4

                    A greater practice would be to create a function that generates the greatest
                    common divisor using the 'or' keyword statement and 'while' loop.

                    def gcd(x,y):
                        'enter 2 numbers and find their greatest common divisor'
                        common = min(x,y)
                        while x%common != 0 or y%common != 0:
                            common -= 1
                        return common

                    print(gcd(30,4))
                    print(gcd(15,20))

                    output:2
                           5

                    The following function works like any of the previous functions but in a
                    more systematic way. Instead of creating two lists of factors, iterating
                    through one of them and finding factors of the smaller number in the larger
                    number, this function uses a while loop and stores a common variable as the
                    minimum of the two numbers. In our examples the minimum of 30 and 4 is 4.
                    So common stores value 4. The while loop checks for the condition that if
                    either one of our numbers isn't a multiple of the minimum number then the
                    minimum number is decremented by 1. This process is continued until the
                    common variable is stores a value that is a multiple of both numbers. When
                    this number is found, the while loop is stopped and the function returns the
                    first number which is a multiple of both numbers. Because 4 is not a multiple
                    of 30, the common variable is decremented. Value 3 is neither a multiple of
                    30 or 4, so the common variable is decremented again. Two is a multiple of
                    30 and 4 and its the very first. Therefore, it breaks the while loop and prints
                    to the screen. The reason we start with the minimum number and not the maximum
                    as common is due to the fact that the greatest common divisor of both numbers
                    is not ever going to be larger than the minimum number of both numbers, whereas
                    using the maximum number allows the possibility that the greatest common divisor
                    is a greater than the minimum number. So we test all values starting from the
                    minimum number until a value that is divisible by both numbers is located. This
                    is a more efficient manner for finding the gcd of 2 numbers. One can also use
                    the alternate methods if they resonate more closely to you. It highly depends on
                    the programmer.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        if x == 99:
            print('''
                     ROUND FUNCTION
                     This episode is dedicated to the round function in python. The round function
                     changes irrational or multi decimal place numbers to numbers of a certain
                     decimal place. Round is helpful in the sense that it shortens very long
                     output values to less decimal places and a more readable format.
                     The round function is best demonstrated through numerous examples of
                     its applications and comparing round values with irrational values.

                     example 1)def multiply(x,y):
                                 'multiplies 2 values together'
                                 return x*y

                                 print(multiply(14.70,15.60))
                                 print(multiply(15.66,17.31))

                     output:229.32
                            271.0746

                     example 2)def multiply(x,y):
                                 'multiplies 2 values together'
                                 return round(x*y,2)

                                print(multiply(14.70,15.60))
                                print(multiply(15.66,17.31))

                     output:229.32
                            271.07

                     The examples above outline key principles about the round function. It takes
                     2 arguments, one neccessary and another optional. For the round function, a
                     neccessary argument is the digit we expect to round. This is typically a
                     floating point number of multiple decimal places which we expect to reduce
                     to a more manageable amount of decimals, say 2. In our examples, we take 2
                     numbers of 2 decimal places and multiply them by each other using a
                     multiply function. The first example neglects the optional argument specifying
                     to what number of decimal places we wish to round our number 2. Therefore, the
                     second value is rounded to 4 decimal places. Realistically, a monetary value is
                     at maximum 2 decimal places and we need to find a way of reducing our 4 decimal
                     value to 2 decimals. Using the round function and entering 2 does this, featured
                     in the second example.''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help(round)
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    break
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
    if x == 100:
        print('''
                 BONUS EPISODE ON CREATING A CROWN:

                 In this episode we expect to create the shape of a crown using a function. This function will
                 prompt the user for a number and a crown corresponding to that number will be printed.The crown
                 should follow the format below.

                 >>>crown()
                    Enter a number: 4
                    1            1            1
                      12        121        21
                        123    12321    321
                          123412343214321
                           1234123214321
                            12341214321
                             123414321
                    Try again? y/n y
                    Enter a number: 5
                    1                1                1
                      12            121            21
                        123        12321        321
                          1234    1234321    4321
                            1234512345432154321
                             12345123432154321
                              123451232154321
                               1234512154321
                                12345154321
                    Try again? y/n 
                 ''')
        query = input('''If you prefer to solve this problem independently enter yes, otherwise
                             enter no: ''')
        if query == 'yes':
            print('''Congratulations on solving this problem! Your well on your way to becoming
                     a programmer''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    pass
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
        else:
            print('''This problem can be thought of in 3 parts.

                     The first part of this problem is trying to create a the tip of the crown. The second concerns the
                     crown's body and bottom.

                     We will deal with each of these parts individually with headings provided.

                     TIP OF CROWN:

                     For dealing with the crown's tip, one should consider a few things. Firstly, the format of the tip. Unlike
                     a number triangle, the tip of the crown follows a format with numerous amounts of spaces, then the numbers,
                     more spaces and more numbers. While it may look intimidating, it is nothing out of your grasp. Crucially,
                     all this formatting is an adaptation of the number and reverse number triangle problems. The biggest problem
                     is trying to find enough iterables to assign to automate this process. Because we're dealing with spaces,
                     numbers, a number triangle, more spaces and numbers, the way to solve this is to tackle each part of the
                     tip of this crown.

                     Primarily, we'll define a function called crown() which takes in a number variable as an input.

                     def crown():
                         num = int(input("Enter a number from 5 onwards: "))
                         print(num)
                         
                         num = input("Try again? y/n ")
                         if num == 'y':
                             crown()
                         elis num == 'n':
                             pass

                     output:Enter a number from 5 onwards: 5
                            5
                            Try again? y/n y
                            Enter a number from 5 onwards:

                     Based on the outcome, we've created a looping function which continues to prompt a user for a number, prints
                     the number, asks whether they want to try another number and if 'y' is entered, restarts the function and
                     prompt's them for another number. Now we can operate on the separate parts of the crown's tip. First we will
                     create a number triangle.

                     def crown():
                        num = int(input("Enter a number from 5 onwards: "))
                        for i in range(num):
                            for j in range(i):
                                print('  ', end='')
                            for k in range(i+1):
                                print(k+1, end='')
                            print()

                        num = input("Try again? y/n ")
                        if num == 'y':
                            crown()
                        elif num == 'n':
                            pass

                      output:Enter a number from 5 onwards: 5
                             1
                               12
                                 123
                                   1234
                                     12345
                              Try again? y/n

                      Our function is responding as anticipated. The function above will be explained in shorter
                      steps. Notice that the first loop with iterable i is in the range of the entered number. This
                      controls the amount of levels in our output. Because we want the user to be able to control
                      the number of levels printed to the screen, we implement the user's number into the range of
                      the first loop. The embedded loop controls the number of spaces before a number appears to
                      screen. For each level, the number of spaces ascends in order. Notice that the first loop
                      also ascends in order of magnitude after each level. Using this fact, we alter the range
                      of the second loop to the iterables from the first for loop so that the number of spaces
                      incrases harmonically. But for each level, we want two spaces to be printed before the
                      numbers appear. This gives a longer shape for the edges of the crown top. Now that the
                      spaces and levels are in control, we want ascending  numbers to appear on each level. This is
                      manipulated using a particular range, the same range as the first loop. Why? The reason for
                      this is the very same reason we use the first loop as the range of the second loop. We intend
                      to print ascending amounts of numbers to each line after a certain quantity of spaces. The
                      next step is to create a number triangle at the centre of each line. To do so, we need to
                      make some observations. Because we want descending amounts of spaces followed by ascending
                      amounts of numbers, we can also manipulate iterables from the first for loop to achieve our
                      ideals. A number triangle requires an additional 3 for loops which is neccessary to alter
                      the spaces and the 2 sets of numbers within the triangle.

                      def crown():
                          num = int(input("Enter a number from 5 onwards: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('  ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              print()

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                      output:Enter a number from 5 onwards: 5
                             1        1
                               12      12
                                 123    123
                                   1234  1234
                                     1234512345
                              Try again? y/n

                       From the displayed outcome, we perceive that the attempted number triangle was not quite
                       achieved. The reason for due to the spacing. Since we're using spacing equal to
                       the user's number added an extra space, printed to the screen will be a maximum spacing of
                       8. Remember that the range function excludes the last number in that range. For a range
                       of the user's number subtracted by the first iterable i minus an extra 1 (to remove any
                       spaces from the lowest level) the answer is 4. Starting with a range of 4, the number of spaces 
                       correspond to the amount of numbers in the range. Therefore 8 spaces are printed because for
                       each number in the range 2 spaces are printed. So 4 numbers multiplied by 2 spaces is 8
                       spaces. Idealistically, we want more than 8 spaces between the number triangle and the first
                       set of numbers. Perhaps we should try extending the range to double the range, or print
                       a greater number of spaces in our embedded loop to produce more spaces between the numbers.
                       We can try both alternatives and discuss which is better to use and why.

                       Alternative 1) Double the range itself.

                       def crown():
                          num = int(input("Enter a number from 5 onwards: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num*2-i-1):
                                  print('  ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              print()

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                      output: Enter a number from 5 onwards: 5
                              1                  1
                                12                12
                                  123              123
                                    1234            1234
                                      12345          12345
                              Try again? y/n 
                         
                      Alternative 2)  Adding more spaces to the print function

                      def crown():
                          num = int(input("Enter a number from 5 onwards: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('    ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              print()

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                      output: Enter a number from 5 onwards: 5
                              1                1
                                12            12
                                  123        123
                                    1234    1234
                                      1234512345
                              Try again? y/n 

                      Based on the outcomes, it seems that the second alternative of extending the spaces for
                      the print function works better. The question is why? Answering this question is best
                      accomplished by considering the process of our function using the provided example.
                      In the first alternative, when we double the range it is 5 (following our example) multiplied
                      by 2 which is 10, subtracted by 0 and 1. This leaves us with 9. But for each number we're
                      printing 2 spaces, so 9 multiplied with 2 is 18. This is too many spaces for the first
                      level spacing the numbers. A second problem occurs in the last level of the output. At this
                      point we expect our i iterable to be 4. So the maths is 10 minus 4 minus 1 which is 5.
                      Therefore, 2 spaces for every number equals 10. This is far from our requirements as we want
                      no spaces on the last line. Another problem is that for greater numbers entered, the
                      number of spaces on the lowest level increases, which is undesired because we want no
                      spaces on that level. In the second alternative, we add more spaces to the print function
                      which generates the expected outcome. Why? Think about the first and last iterables of our
                      function to make sense of this outcome. The first iterable is 0, so 5 minus 0 minus 1 is 4.
                      We expect 4 numbers and 4 spaces to each of this numbers. This is 16 in total which is
                      double what we received last time (and what we expect). For the last iterable, i takes the
                      value 4 and 4 minus 4 is zero, so a range of zero prints nothing to the screen; and
                      therefore, no spaces are printed on the lowest level. This works for higher numbers too
                      because we're not adapting the range so there will never be a point where more spaces are
                      printed to the lowest level. Having solved this problem, we shoulder the problem of the
                      second part of our number pyramid. Think about how one would print descending amounts and
                      numbers on each line. We could use the iterable i seeing as it decreases for each level of
                      our function. So we try it.

                      def crown():
                          num = int(input("Enter a number from 5 onwards: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('    ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              for l in range(k):
                                  print(k-l, end='')
                              print()

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                      output: Enter a number from 5 onwards: 5
                              1                1
                                12            121
                                  123        12321
                                    1234    1234321
                                      12345123454321
                              Try again? y/n

                      In the example above, the number entered prints the correct tip of the crown. How was this
                      made? Instead of using the range of iterable 1, we adapted it to the range k. You might
                      ask why? The reason is because k is always stored as 1 value greater than i in the range
                      and this is exactly what we want as the first level should have nothing printed as k is
                      zero and l is zero, so printing in the range of zero means nothing is printed to the
                      screen. For the second level, the last iterable of k is 1, so only 1 variable is printed.
                      Subtracting 1 from zero leaves 1, which is the intended value. This process continues until
                      all iterables of i, k and l are exhausted. Having printed the pyramid, we introduce two
                      more emdedded loops that control the last set of spaces and numbers. The first for loop must
                      control the spaces and the second the numbers. We want a descending amount of spaces and
                      descending numbers and amounts in each level. This is similar to the j and k for loops,
                      so maybe something similar must be done. We'll try.

                      def crown():
                          num = int(input("Enter a number: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('    ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              for l in range(k):
                                  print(k-l, end='')
                              for s in range(num-i-1):
                                  print('    ', end='')
                              for t in range(i+1):
                                  print(k-t+1, end='')
                              print()

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                      output: Enter a number from 5 onwards: 5
                              1                1                1
                                12            121            21
                                  123        12321        321
                                    1234    1234321    4321
                                      1234512345432154321
                               Try again? y/n

                      We've now created a function that prints the top of a star given any number. A few
                      adjustments were made to the range and prints statements of iterables j and k to
                      guarantee this outcome. Because we wanted spaces equivalent to iterable p, the code
                      of p was copied in place of a new iterable s. As for iterable t (which controls the
                      numbers) a requirement was for ascending amounts of descending numbers to be shown
                      on the screen. Seeing as the range controls the amount of numbers for each level, we
                      use iterable i added by 1 to print the correct number of numbers to the screen. But
                      a descending value of numbers requires something to subtract iterable t for each
                      level. Like the print statement in iterable l, where k subtracts l, something similar
                      is done here, except an extra 1 is needed for each iterable t. Why? Consider the flow
                      of the for loop. The first iterable t is zero and so is iterable k. By this logic,
                      zero minus zero is zero. Therefore, zero is printed to the screen. But we want 1
                      to print to the screen. Adding one to zero is one and only one number is printed in the
                      range of 1. We obtain the correct outcome this way.

                      CROWN BODY:

                      This section explains how to produce the body of a crown using a function. As always, first
                      ponder the spacing and then the numbers. We want to generate spaces equivalent to the number
                      of spaces on the lowest level of the tip of the crown. Then we want to create ascending
                      numbers of spaces for each level of the crown. So we introduce 2 for loops controlling spaces:
                      one maintains the spacing of the lowest tier from the crown's tip and the other produces an
                      ascending number of spaces.

                    
                      def crown():
                          num = int(input("Enter a number: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('    ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              for l in range(k):
                                  print(k-l, end='')
                              for s in range(num-i-1):
                                  print('    ', end='')
                              for t in range(i+1):
                                  print(k-t+1, end='')
                              print()
                          for i_1 in range(num-1)
                              for j_1 in range(k):
                                  print('  ',end='')
                              for k_1 in range(i_1+1):
                                  print(' ',end='')
                              print('*')

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                      output: Enter a number: 5
                              1                1                1
                                12            121            21
                                  123        12321        321
                                    1234    1234321    4321
                                      1234512345432154321
                                       *
                                        *
                                         *
                                          *
                                           *
                              Try again? y/n

                      What did we do? Because we wanted to print an ascending amount of spaces on each level,
                      starting with one space until 4 spaces, we need to create an appropriate range to do so.
                      The last stored value of k is 4 because of the way for loop works. It iterates
                      through the closest loop in the sequence of the function. Therefore, i comes before i_1 and
                      every embedded loop within i comes before the embedded loops in i_1. As the range of k
                      takes the user's number added by 1, on the lowest level of the crown's tip, the value of k
                      takes the largest value because the i iterable would have been largest at the bottom and k
                      uses i+1 as its range. So where i stops at 4 (remembering that the range function excludes the
                      maximum range) k ends at 4 plus 1 which is 5. So j_1 iterates through a range of 4 and for
                      each number in the range, 2 spaces are printed. This guarantees that for any number entered
                      by the user, an equivalent number of spaces will be printed to the star's body. But we don't
                      stop here. Why? Implementing k as the range of j_1 values prints 8 spaces on every line of
                      our star body. But we want these spaces plus an ascending amount of spaces following the
                      descending shape of the star. To accomplish this aim, another for loop is required for
                      controlling the extra spaces. On the first line of the body, we require 1 space so that the
                      first number is indented by a space following the diagonal 1 pattern. The last line requires
                      4 spaces to meet the 1 starting our number pyramid on the crown's tip. We require a range that
                      starts at 1 space and ends 1 number before the user's number. If we use i_1, the first iterable
                      is 0 and the last is 3 because the range ends a number less than the entered number (which is 4)
                      and 4 is excluded in the range. Consequently, it ends at 3. Following a range of i_1 is also
                      flawed as the first number is zero and a range of zero displays no numbers to the screen. This
                      is resolved by adding a one to the range which disciplines our function to print an extra space
                      to begin with and an extra space to the lowest level of the body; printing spaces equal to the
                      entered number. Testing whether our function works, an extra print statement outside the embedded
                      loop prints asterisk's where the strings would normally start and end.

                      Now that the spacing is controlled, we consider the numbering of the body. The first
                      thing neccessary is a descending quantity of ascending numbers. In other words, numbers starting
                      from 1 to the user's number on every line and reducing by one number until the last line. On
                      the last line, there should be 1 number left. But for formatting reasons, we want the last line
                      to end on the penultimate line of a number triangle. So a line before the last with two numbers
                      following the format of numbers starting from 1 to the number, but because its the penultimate line
                      the two numbers should print 1 and 2. 

                      def crown():
                          num = int(input("Enter a number: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('    ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              for l in range(k):
                                  print(k-l, end='')
                              for s in range(num-i-1):
                                  print('    ', end='')
                              for t in range(i+1):
                                  print(k-t+1, end='')
                              print()
                          for i_1 in range(num-1)
                              for j_1 in range(k):
                                  print('  ',end='')
                              for k_1 in range(i_1+1):
                                  print('  ',end='')
                              for p_1 in range(num-i_1):
                                  print(p_1+1, end='')
                              print()

                          num = input("Try again? y/n ")
                          if num == 'y':
                              crown()
                          elif num == 'n':
                              pass

                         output:Enter a number: 5
                                1                1                1
                                  12            121            21
                                    123        12321        321
                                      1234    1234321    4321
                                        1234512345432154321
                                         12345
                                          1234
                                           123
                                            12
                                Try again? y/n

                       We achieved the desired outcome, how? Noticing that i_1 ends at two numbers before our number.
                       When 5 is entered, i_1 ends at a range of 4. Manipulating this to our advantage allows us to transform
                       the range of an embedded for loop with iterable p_1 in the range of our number subtracted by i_1. This
                       is done as we need a number greater than the i_1 iterable so that the range descends for each level.
                       Thinking back to the example, i_1 begins at zero, so 5 subtracted by zero is 5, which means numbers in
                       the range of 5 are printed. Because no starting point is specified, the first number will be 0 until 4,
                       excluding 5 from the search. But we expect 1 through to 5. Adding one to the iterable of the print
                       statement adds 1 to the first number zero and one to the last 4. Now the for loop prints 1 to 5. First
                       step done. The next step is to find a method of stopping one level before the last. You might wonder why
                       the outcome seems to have done this automatically. It can be observed that for loop with iterable i_1
                       sticks to a range one less than our number. As a result, the number of levels will always be one less
                       than our number and using iterables from this for loop will always end one level preceding our number.But
                       the end goal is  far from over because we've only completed the first set of numbers with the appropriate
                       format.

                       In the next stage a method of printing ascending amounts of ascending numbers starting with
                       numbers ending on for loop p_1 will be explored in detail. What this entails is finding a way to
                       always start at a point where the previous loop ends. Seeing as k_1 always ends at a number
                       greater than the user's number by 1, we can use this fact to subtract from our number and obtain
                       decreasing results. A range of i_1 can be used in this for loop because i_1 begins at zero, so
                       nothing is expected on screen in the first line; which is anticipated. This is an exacting format.
                       Trying our number subtracted by k_1 means that on the second line k_1 will store value 1
                       and only 4 will be printed (5 minus 1). On the next line, it will be 3 printed twice and the same
                       pattern of 3 twos on the last line. So, we're getting closer but not quite there. It seems that
                       k_1 is a constant value on each level, but we need another iterable which subtracts from the k_1
                       to slowly increase values for each level. If we implement the iterable from the actual for loop
                       which we can denote l_1, the maximum value it takes on the second level is 0 and k is value 1.
                       If we add one to the mix its zero minus 1 plus 1, which leaves our number. On the third level:
                       k is 2 and l_1 is a maximum of one. In the first instance its 5 minus 2 plus 1, which is 4. The
                       next instance is 3 because k is 2, l is 1 and we add an extra one which equals 5. Why does this
                       method work? It works as l_1 increases in each iteration, k stays at a maximum value of one less
                       than i_1 on the level. Subtracting greater values from this constant means that less is subtracted
                       from our number; and therefore, we induce the expected pattern.

                       def crown():
                           num = int(input("Enter a number: "))
                           for i in range(num):
                               for j in range(i):
                                   print('  ', end='')
                               for k in range(i+1):
                                   print(k+1, end='')
                               for p in range(num-i-1):
                                   print('    ', end='')
                               for q in range(i+1):
                                   print(q+1, end='')
                               for l in range(k):
                                   print(k-l, end='')
                               for s in range(num-i-1):
                                   print('    ', end='')
                               for t in range(i+1):
                                   print(k-t+1, end='')
                               print()
                           for i_1 in range(num-1)
                               for j_1 in range(k):
                                   print('  ',end='')
                               for k_1 in range(i_1+1):
                                   print('  ',end='')
                               for p_1 in range(num-i_1):
                                   print(p_1+1, end='')
                               for l_1 in range(i_1):
                                   print(num+l_1-k_1+1, end='')
                               print()

                           num = input("Try again? y/n ")
                           if num == 'y':
                               crown()
                           elif num == 'n':
                               pass

                      output:Enter a number: 5
                             1                1                1
                               12            121            21
                                 123        12321        321
                                   1234    1234321    4321
                                     1234512345432154321
                                      12345
                                       12345
                                        12345
                                         12345
                             Try again? y/n

                      In this step we'll be adding an extra 2 for loops to create the pattern of a upside down
                      number pyramid. The first loop creates numbers of increasing magnitude and decreasing quantity.
                      Another for loop will establish numbers of decreasing magnitude and quantity. Because the
                      first for loop should end at a number before the user's number, we transform the range of its
                      for loop by subtracting an extra one. As we require a decreasing quantity of
                      increasing numbers why not use our number subtracted by i_1 minus 1 in the range of the present for
                      loop. Printing this iterable does the correct job, but because a starting point of 1 hasn't
                      been specified through the range, we need to add one in the print statement of this for loop.
                      Through the next for loop, the quantity of numbers and their magnitude decrease, so we create
                      a decrementing range by specifying the last value we expect our range to reach as the starting
                      point; and the amount we want to reduce the number's in the range after each iteration. This
                      value is negative one because our number should decrease by one each iteration through the
                      for loop. Augmenting this for loop slightly to subtract an extra 2 creates a reverse number
                      pyramid that always begins with a number less by 2. Let's test it now.

                      def crown():
                          num = int(input("Enter a number: "))
                          for i in range(num):
                              for j in range(i):
                                  print('  ', end='')
                              for k in range(i+1):
                                  print(k+1, end='')
                              for p in range(num-i-1):
                                  print('    ', end='')
                              for q in range(i+1):
                                  print(q+1, end='')
                              for l in range(k):
                                  print(k-l, end='')
                              for s in range(num-i-1):
                                  print('    ', end='')
                              for t in range(i+1):
                                  print(k-t+1, end='')
                              print()
                          for i_1 in range(num-1):
                              for j_1 in range(k):
                                  print('  ',end='')
                              for k_1 in range(i_1+1):
                                  print(' ',end='')
                              for p_1 in range(num-i_1):
                                  print(p_1+1, end='')
                              for l_1 in range(i_1):
                                  print(num+l_1-k_1+1, end='')
                              for q_1 in range(num-i_1-1):
                                  print(q_1+1, end='')
                              for s_1 in range(num-i_1-2,0,-1):
                                  print(s_1, end='')
                              print()

                           num = input("Try again? y/n ")
                           if num == 'y':
                               crown()
                           elif num == 'n':
                               pass

                       output:Enter a number: 5
                              1                1                1
                                12            121            21
                                  123        12321        321
                                    1234    1234321    4321
                                      1234512345432154321
                                       123451234321
                                        1234512321
                                         12345121
                                          123451
                              Try again? y/n 


                       Now we require an additional 2 for loops to finish the body of the crown. The first for loop
                       should create a sequence of descending numbers from the second line onwards. As for the
                       second for loop: it should create numbers of descending magnitude and quantity. This can
                       be easily done using what we learned so far. The range of i_1 creates ascending quantities
                       of numbers on each line. We want to subtract iterables using this range by a larger quantity,
                       namely our number. By doing so, we'll decrement the numbers printed from the second line
                       onwards by 1 and repeat the pattern through to the last iterable from i_1. The second for
                       loop will do something similar to s_1 but without subtracting from 2 because we want to
                       start with a range of our number and not 2 less. We can now test whether this theory works.

                       def crown():
                           num = int(input("Enter a number: "))
                           for i in range(num):
                               for j in range(i):
                                   print('  ', end='')
                               for k in range(i+1):
                                   print(k+1, end='')
                               for p in range(num-i-1):
                                   print('    ', end='')
                               for q in range(i+1):
                                   print(q+1, end='')
                               for l in range(k):
                                   print(k-l, end='')
                               for s in range(num-i-1):
                                   print('    ', end='')
                               for t in range(i+1):
                                   print(k-t+1, end='')
                               print()   
                           for i_1 in range(num-1):
                               for j_1 in range(k):
                                   print('  ',end='')
                               for k_1 in range(i_1+1):
                                   print(' ',end='')
                               for p_1 in range(num-i_1):
                                   print(p_1+1, end='')
                               for l_1 in range(i_1):
                                   print(num+l_1-k_1+1, end='')
                               for q_1 in range(num-i_1-1):
                                   print(q_1+1, end='')
                               for s_1 in range(num-i_1-2,0,-1):
                                   print(s_1, end='')
                               for t_1 in range(i_1):
                                   print(num-t_1, end='')
                               for y_1 in range(num-i_1,0,-1):
                                   print(y_1, end='')
                               print()
                                
                           num = input("Try again? y/n ")
                           if num == 'y':
                               crown()
                           elif num == 'n':
                               pass

                       output:Enter a number: 5
                              1                1                1
                                12            121            21
                                  123        12321        321
                                    1234    1234321    4321
                                      1234512345432154321
                                       12345123432154321
                                        123451232154321
                                         1234512154321
                                          12345154321
                              Try again? y/n

                      We've successfully created the crown tip and body. Now we'll consider the last segment which is the
                      bottom.  ''')
            question = input("For more information use the help() function. Enter help and you will be redirected, quit to end module ")
            if question == "help":
                help()
                q_2 = input("Do you wish to learn more, enter yes or no: ")
                if q_2 == 'yes':
                    x = int(input("Enter another episode you wish to learn about: "))
                else:
                    pass
            if question == "quit":
                window = False
            if question == "more":
                x = int(input("Enter another episode you wish to learn about: "))
            
            
            
            
            









        

                

                
