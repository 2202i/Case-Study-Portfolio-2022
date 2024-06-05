#Singson, John Florence M.      ICT - 101

def main_menu():
    print (2 * "=" , "SINGSON, JOHN FLORENCE M.  ICT - 101" , 2 * "=")
    print (10 * "=" , "MAIN MENU" , 10 * "=")
    print ("[1] PRELIM")
    print ("[2] MIDTERM")
    print ("[3] FINALS")
    print ("[4] Exit")
    print (26 * "=")
choice = 0
loop = 1

while loop == 1:         
    main_menu()    
    choice = int(input("Enter choice : ")) 
    if choice == 1:

        print ("[1] Prelims Assignment 1 - 6compro2L")
        print ("[2] PLE1 : Decision Structure: If statement, if..else, nested")
        print ("[3] Prelim Seatwork 1 - 6compro2L")
        print ("[4] Exit")

        choose = int(input("Enter choice : "))

        if choice == 1:
            print ('Programs must be carefully designed before they are written. During the process, programmers use tools such as "pseudocode and flowcharts" to create models of programs.')
            print (" ")
            print ("“Programs must be carefully designed before they are written.")
            print ("During")
            print ("the design process,")
            print ("programmers use tools such as “pseudocode and")
            print ("flowcharts” to create models of programs.")
            print (" ")
            print('“Programs must be carefully designed before they are written.')
            print('During\nthe design process,\nprogrammers use tools such as “pseudocode and')
            print('flowcharts” to create models of programs.')
            print (" ")
            chosen_character = input("Input a character: ")
            word1 = input("Word 1: ")
            word2 = input("Word 2: ")
            word3 = input("Word 3: ")
            word4 = input("Word 4: ")
            word5 = input("Word 5: ")
            word6 = input("Word 6: ")
            print("Result:", word1 + chosen_character + word2 + chosen_character + word3 + chosen_character + word4 + chosen_character + word5 + chosen_character + word6)
            print (" ")
            num = input("Enter floating no : ")

            print(num, "is floating point number")

            converted = int(float(num))

            print("from float to integer " , num , "to" , converted) 
            print("from integer to String:")

            print("Binary" , converted , "to" , bin(converted))
            print("Octal" , converted , "to" , oct(converted))
            print("Hexadecimal" , converted , "to" , hex(converted))

            print (" ")
            a = int(input("Input value for a: "))
            n = int(input("Input value for n: "))
            d = int(input("Input value for d: "))
            ex1 = n / 2; ex2 = 2 * a;ex3 = (n - 1) * d
            result = ex1 * ex2 + ex1 * ex3
            print("Result:",round(result,2))

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break  

        elif choice == 2:
            d = input("Distance Traveled(km):")

            t = input("Duration of Ride(minutes):")

            distance = int(float(d))
            time = int(float(t))

            oras = time * 60

            cover = distance * 4.50

            fee = oras / 120 + cover

            totalfee = fee + 60

            print ("Total Fare:",totalfee)
            print (" ")
           
            name = input("Enter student name:")
            year = input("Enter Year Level :")
            code = input("Enter Course Code:")
            units = int(input("Enter the Number of units:"))
            labs = int(input("Enter the Number of Labs:"))
            payment = input("Enter amount on Terms of Payment:")


            print("Student Name:",name)
            print("Year Level (1-5):",year)
            print("Course Code:",code)
            print("Number of Units:",units)
            print("Number of Labs:",labs)
            print("Terms of Payment:",payment)

            print("==========================")
            print("Breakdown of Fees:")

            if year == '1':
                year1 = 1325.00
            elif year == '2':
                year1 = 1240.00
            elif year == '3':
                year1 = 1195.00
            elif year == '4':
                year1 = 1085.00
            elif year == '5':
                year1 = 1085.00

            if code == 'IT':
                code1 = 4325.00
            elif code == 'N':
                code1 = 4500.00
            elif code == 'E':
                code1 = 3987.00
            elif code == 'C':
                code1 = 4113.00
    
            if code == 'it':
                code1 = 4325.00
            elif code == 'n':
                code1 = 4500.00
            elif code == 'e':
                code1 = 3987.00
            elif code == 'c':
                code1 = 4113.00
    

            tfee = year1 * units
            lfee = labs * code1
            mfee = tfee * 0.067
            due = tfee + lfee + mfee

            if payment == '1':
                payment1 = 2000.00
                ipay = due - payment1
                baip = ipay - ipay
            elif payment == '2':
                payment1 = 1000.00
                ipay = due - payment1
                baip = (due - payment1) / 2  
            elif payment == '3':
                payment1 = 0.00
                ipay = due - payment1
                baip = due / 10  

            print ("Tuition Fee: P",tfee)
            print ("Laboratory Fee: P",lfee)
            print ("Miscellaneous Fee: P",mfee)
            print ("Total Amount Due: P",due)
            print ("Discount: P",payment1)
            print ("Initial Payment: P",ipay)
            print ("Balance after initial payment:",baip)

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break  

                        
        elif choice == 3:
            num = int(input("Enter floating no : "))



            if num < 0:
              raise Exception("Numbers below zero are prohibited")

            print(num, "is floating point number")

            converted = int(float(num))

            print("from float to integer " , num , "to" , converted) 
            print("from integer to String:")

            print("Binary" , converted , "to" , bin(converted))
            print("Octal" , converted , "to" , oct(converted))
            print("Hexadecimal" , converted , "to" , hex(converted))

            print (" ")

            a = int(input("Input value for a: "))
            n = int(input("Input value for n: "))
            d = int(input("Input value for d: "))

            if a < 0:
              raise Exception("Numbers below zero are prohibited")

            if n < 0:
              raise Exception("Numbers below zero are prohibited")

            if d < 0:
              raise Exception("Numbers below zero are prohibited")

            ex1 = n / 2; ex2 = 2 * a;ex3 = (n - 1) * d
            result = ex1 * ex2 + ex1 * ex3
            print("Result:",round(result,2))

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break  
            
        elif choice == 4:    
            print ("End of program")
            loop = 0
            break

        



        
    elif choice == 2:

        print ("[1] Midterm Lab Exercise Assignment1 - Repetition Structure")
        print ("[2] Midterm Lab Exercise 1 - Looping Structure")
        print ("[3] Midterm Seatwork 1 - Strings")
        print ("[4] Midterm Lab Exercise 3 - Functions -2 (ICT-101)")
        print ("[5] Exit")

        choose = int(input("Enter choice : "))

        if choice == 1:
            
            initial_inv = float(input("Enter initial investment        :  Php "))
            annual_inv = float(input("Enter annual investment         :  Php "))
            annual_interest_rate = float(input("Enter annual interest rate (%)  :  "))
            years = int(input("Enter number of years           :  "))

            print("")
            print("Year\t\tAnnual Investment\tSavings")

            annual_interest_rate /= 100
            savings = 0

        for y in range(0, years):
            if savings == 0:
                total_inv = initial_inv + annual_inv
                annual_interest = initial_inv * annual_interest_rate
                savings = total_inv + annual_interest
                y += 1
            else:
                annual_interest = savings * annual_interest_rate
                savings += annual_inv
                savings += annual_interest
                y += 1
            print(y,"\t\tPhp {0:.2f}".format(annual_interest),"\t\tPhp {0:.2f}".format(savings))

        print(" ")
        print("At the end of",years,"years, your savings is Php {0:.2f}".format(savings))
        print (" ")
        again = (input("Do you want to try again? Answer [Y/N]:"))
        if again == 'y':
            loop = 1
        elif again == 'Y':
            loop = 1    
        elif again == 'n': 
            print ("End of program")
            break
        elif again == 'N': 
            print ("End of program")
            break
            
        elif choice == 2:

            try:
                a = float(input("Enter Amount:\tPhp "))
            except KeyboardInterrupt:
                    print("Error")
            except ValueError:
                    print("Invalid")
      
            a1 = 0
            a2 = 0
            a3 = 0
            items = 1
            percent = 0.12



        try:
    
            print("Enter your expenses:    ")
            while (a2 <= a):
                a1 = float(input("Item\t"+str(items)+" : Php\t"))
                items += 1
                php = a1 + a2
                a2 = php
        
        
        
            if (a2 > a):
                print("Last item cannot be added. Insufficient cash.")
    

    
        except ValueError:
            print("Error")


        total = a2 - a1
        change = a - total    
        tax = total * percent



        print("Your total tax\t\t:Php {0:,.2f}".format(tax))
        print("Your total expenses\t:Php {0:,.2f}".format(total))
        print("Your change\t\t:Php {0:,.2f}".format(change))
        print("")
                    
        print (" ")
        again = (input("Do you want to try again? Answer [Y/N]:"))
        if again == 'y':
            loop = 1
        elif again == 'Y':
            loop = 1    
        elif again == 'n': 
            print ("End of program")
            break
        elif again == 'N': 
            print ("End of program")
            break
            
        elif choice == 3:

            sentence = input("Input a Sentence : ")
            words = sentence.split()

            allwords = len(words)
            print ("Word count:", allwords)


            letter = len(sentence) - sentence.count(' ')
            print ("Letter Count:", letter)



            count = 0
            for letter in sentence:
                if letter in ['a','e','i','o','u','A','E','I','O','U']:
                    count += 1
            print ('Vowel Occurences:' + str(count))

            count1 = 0
            for letter in sentence:
                if letter in 'qwrtypsdfghjklzxcvbnm':
                    count1 += 1
            print ('Consonant Occurences:' + str(count1))
            
            print (" ")

        elif choice == 4:

            try:
                pasok1 = float(input("Enter Credit Card available balance :\tPhp "))
                pasok2 = float(input("Enter Amount of new purchase :\tPhp "))
            except KeyboardInterrupt:
                    print("Error")
            except ValueError:
                    print("Invalid")

            print (54 * "*" , "Summary" , 5 * "*")


            c_interest = pasok2 * 0.08
            c_balance = pasok1 - pasok2 - c_interest
            c_total = pasok1 - c_balance

            print ("Credit Card current available balance : Php ", pasok1)
            print ("Amount of new purchase : Php ", pasok2)
            print ("Interest of new purchase : Php ", c_interest)
            print ("Total amount of payment : Php ", c_total)
            print ("Remaining balance of credit card : Php ", c_balance)
            
            print (" ")    

            print ("Conversion Menu")
            print ("[1]\tInch to Centimeter")
            print ("[2]\tCentimeter to Inch")
            print ("[3]\tKilogram to Pound")
            print ("[4]\tPound to Kilogram")
            print ("[5]\tMeter to Feet")
            print ("[6]\tFeet to Meter")
            print ("[7]\tExit")
            print (50 * "*")

            choice = 0
            loop = 1

            while loop == 1:           
                choice = int(input("Enter choice : ")) 
                if choice == 1:
                    print ("Menu1")
                    
                    inch = float(input("Enter Length of inch to convert to cm : "))
                    cm = inch*2.54
                    print ('Equivalent centimeter :','{:.2f}'.format(cm))

                    print (50 * "*")
                    loop = 1


                elif choice == 2:
                    print ("Menu2")

                    cm = float(input("Length of cm to convert to inch : "))
                    inch = cm/2.54
                    print ('Equivalent Inch :','{:.2f}'.format(inch))
                    
                    print (50 * "*")
                    loop = 1        


                elif choice == 3:
                    print ("Menu3")

                    kg = float(input('Enter weight in kg to convert to pound : '))
                    pound = kg * 2.2046
                    print ('Equivalent pound:','{:.2f}'.format(pound))
                    
                    print (50 * "*")
                    loop = 1
                    
                elif choice == 4:
                    print ("Menu4")

                    pound = float(input('Enter weight in pound to convert to kg : '))
                    kg = pound * 0.453592
                    print ('Equivalent kilogram:','{:.2f}'.format(kg))
                    
                    print (50 * "*")
                    loop = 1
                    
                elif choice == 5:    
                    print ("Menu5")

                    meter = float(input('Enter length in meter to convert to feet : '))
                    feet = meter/0.3048
                    print ('Equivalent feet:','{:.2f}'.format(feet))
                    
                    print (50 * "*")
                    loop = 1
                    
                elif choice == 6:
                    print ("Menu6")

                    meter = float(input('Enter length in feet to convert to meter : '))
                    meter = feet *0.3048
                    print ('Equivalent meter:','{:.2f}'.format(meter))
                    
                    print (50 * "*")
                    loop = 1
                    
                elif choice == 7:
                    print ("Program terminating")
                    loop = 0
                    break

                else:
                    print ("Invalid Choice")
                    loop = 1
                    print (50 * "*")
                    

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break


            
        elif choice == 5:
            
            print ("End of program")
            loop = 0
            break
        
    elif choice == 3:

        print ("[1] Finals lab Exercise 1 - Lists")
        print ("[2] Finals LE - Assignment1")
        print ("[3] Finals 6COMPRO2L Lab Exercise 2 - Dictionary, Set and File Handling")
        print ("[4] Exit")

        choose = int(input("Enter choice : "))

        if choice == 1:
            print (" ")
            hours1 = float(input("Enter Hours worked for employee 1: "))
            hours2 = float(input("Enter Hours worked for employee 2: "))
            hours3 = float(input("Enter Hours worked for employee 3: "))
            hours4 = float(input("Enter Hours worked for employee 4: "))
            hours5 = float(input("Enter Hours worked for employee 5: "))
            hours6 = float(input("Enter Hours worked for employee 6: "))
            hours7 = float(input("Enter Hours worked for employee 7: "))

            list1 = hours1, hours2, hours3, hours4, hours5, hours6, hours7
            print("List of Hours worked : ",list1)

            gross1 = hours1 * 675.75
            gross2 = hours2 * 675.75
            gross3 = hours3 * 675.75
            gross4 = hours4 * 675.75
            gross5 = hours5 * 675.75
            gross6 = hours6 * 675.75
            gross7 = hours7 * 675.75

            print ("Gross Pay for employee 1 : Php ",'{:.2f}'.format(gross1))
            print ("Gross Pay for employee 2 : Php ",'{:.2f}'.format(gross2))
            print ("Gross Pay for employee 3 : Php ",'{:.2f}'.format(gross3))
            print ("Gross Pay for employee 4 : Php ",'{:.2f}'.format(gross4))
            print ("Gross Pay for employee 5 : Php ",'{:.2f}'.format(gross5))
            print ("Gross Pay for employee 6 : Php ",'{:.2f}'.format(gross6))
            print ("Gross Pay for employee 7 : Php ",'{:.2f}'.format(gross7))
            print (" ")
            def score(numeros):
                totalinput = int(input('How many test scores do you want to enter? : '))
                
                for t in range(totalinput):
                    numeros.append(int(input('Enter Student Score: ')))
                again = (input("Would you like to input more? [Y/N]:"))
                if again == 'y':
                    score(numeros)
                elif again == 'Y':
                    score(numeros)    
                elif again == 'n': 
                    print (numeros)
                    return numeros
                elif again == 'N': 
                    print (numeros)
                    return numeros


            def average(numeros):
                numeros.remove(min(numeros))
                numeros = (sum(numeros))/len(numeros)

                return numeros

            def end(numeros):
                numba = numeros + numeros
                thecarpenters = numeros * 10 / 2
                print ('Sum of all the scores :  ',numba)
                print ('Sum of all the scores minus the min value :  ', thecarpenters)
                print('Average of all the scores minus the min value :  ', numeros)

            def main():
                scores = []
                score(scores)
                final = average(scores)
                end(final)





            main()

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break
        

        
        elif choice == 2:

            try:
                # User inputs the years covered in the sales report, giving the start and end years covered.
                def input_years():
                    starting_year = int(input("\nInput starting year covered : "))
                    ending_year = int(input("Input ending year covered   : "))
                    return starting_year, ending_year

                # User inputs the corresponding quarterly sales per year and the program will display the total sales annually.
                def input_sales(s,e):
                    years = e - s
                    sales_list = []
                    for y in range(0,years+1):
                        print("\nSales for",s,":")
                        sales_list.append([])
                        quarter = 1
                        for q in range(0,4):
                            sales_list[y].append(0)
                            sales_list[y][q] = float(input("Quarter " + str(quarter) + " Sales : Php "))
                            quarter += 1
                        annual_total = sales_list[y][0] + sales_list[y][1] + sales_list[y][2] + sales_list[y][3]
                        print("Total Sales for",s,": Php {0:,.2f}".format(annual_total))
                        s += 1
                    return sales_list

                # The program computes for the total sales within the years covered.
                def compute_total(years,sales_list):
                    total = 0
                    for y in range(0,years+1):
                        for q in range(0,4):
                            total += sales_list[y][q]
                    return total

                # The program identifies which year had the highest sale.
                def identify_highest(years,s,sales_list):
                    annual_list = []
                    for y in range(0,years+1):
                        annual = sales_list[y][0] + sales_list[y][1] + sales_list[y][2] + sales_list[y][3]
                        annual_list.append(annual)
                    y_highest = s + annual_list.index(max(annual_list))
                    return y_highest

                # The program displays which quarter/s in the year with the highest annual sales had the highest quarterly sales.
                def display_highest(s,sales_list,highest):
                    highest_sales = sales_list[highest-s]
                    if max(highest_sales) == highest_sales[3]:
                        q_highest = "Quarter 4"
                        if highest_sales[3] == highest_sales[2]:
                            q_highest = "Quarters 3 and 4"
                            if highest_sales[3] == highest_sales[1]:
                                q_highest = "Quarters 2, 3, and 4"
                                if highest_sales[3] == highest_sales[0]:
                                    q_highest = "All quarters have the same amount of sales"
                            elif highest_sales[3] == highest_sales[0]:
                                q_highest = "Quarter 1, 3, and 4"
                        elif highest_sales[3] == highest_sales[1]:
                            q_highest = "Quarter 2 and 4"
                            if highest_sales[3] == highest_sales[0]:
                                q_highest = "Quarter 1, 2, and 4"
                        elif highest_sales[3] == highest_sales[0]:
                            q_highest = "Quarter 1 and 4"
                    elif max(highest_sales) == highest_sales[2]:
                        q_highest = "Quarter 3"
                        if highest_sales[2] == highest_sales[1]:
                            q_highest = "Quarter 2 and 3"
                            if highest_sales[2] == highest_sales[0]:
                                q_highest = "Quarter 1, 2, and 3"
                        elif highest_sales[2] == highest_sales[0]:
                            q_highest = "Quarter 1 and 3"
                    elif max(highest_sales) == highest_sales[1]:
                        q_highest = "Quarter 2"
                        if highest_sales[1] == highest_sales[0]:
                            q_highest = "Quarter 1 and 2"
                    elif max(highest_sales) == highest_sales[0]:
                        q_highest = "Quarter 1"
                    return q_highest

                # The program determines which quarter/s in the year with the highest annual sales had the lowest quarterly sales.
                def display_lowest(s,sales_list,highest):
                    highest_sales = sales_list[highest-s]
                    if min(highest_sales) == highest_sales[3]:
                        q_lowest = "Quarter 4"
                        if highest_sales[3] == highest_sales[2]:
                            q_lowest = "Quarters 3 and 4"
                            if highest_sales[3] == highest_sales[1]:
                                q_lowest = "Quarters 2, 3, and 4"
                                if highest_sales[3] == highest_sales[0]:
                                    q_lowest = "All quarters have the same amount of sales"
                            elif highest_sales[3] == highest_sales[0]:
                                q_lowest = "Quarter 1, 3, and 4"
                        elif highest_sales[3] == highest_sales[1]:
                            q_lowest = "Quarter 2 and 4"
                            if highest_sales[3] == highest_sales[0]:
                                q_lowest = "Quarter 1, 2, and 4"
                        elif highest_sales[3] == highest_sales[0]:
                            q_lowest = "Quarter 1 and 4"
                    elif min(highest_sales) == highest_sales[2]:
                        q_lowest = "Quarter 3"
                        if highest_sales[2] == highest_sales[1]:
                            q_lowest = "Quarter 2 and 3"
                            if highest_sales[2] == highest_sales[0]:
                                q_lowest = "Quarter 1, 2, and 3"
                        elif highest_sales[2] == highest_sales[0]:
                            q_lowest = "Quarter 1 and 3"
                    elif min(highest_sales) == highest_sales[1]:
                        q_lowest = "Quarter 2"
                        if highest_sales[1] == highest_sales[0]:
                            q_lowest = "Quarter 1 and 2"
                    elif min(highest_sales) == highest_sales[0]:
                        q_lowest = "Quarter 1"
                    return q_lowest

                # main
                start,end = input_years()
                sales = input_sales(start,end)
                total_sales = compute_total(end-start,sales)
                year_highest = identify_highest(end-start,start,sales)
                quarter_highest = display_highest(start,sales,year_highest)
                quarter_lowest = display_lowest(start,sales,year_highest)

                print("\nTotal Sales                    : Php {0:,.2f}".format(total_sales))
                print("Year with Highest Annual Sales :",year_highest)
                print("Quarter/s with Highest Sales   :",quarter_highest)
                print("Quarter/s with Lowest Sales    :",quarter_lowest)
                print()

            except:
                print("Invalid. Try again.")
            
            print (" ")
            try:
                # The program displays the elements of the tuple.
                def display_tuple(t):
                    print("\nTuple contains : ",end="")
                    l = (len(t)) - 1
                    for e in t:
                        if e != t[l]:
                            print(e,end=", ")
                        if e == t[l]:
                            print(e)

                # User inputs starting and ending values that the program will use as index in tuple slicing.
                def tuple_slicing(t):
                    print("\nSlicing in tuples:")
                    s = int(input("  Enter starting value : "))
                    e = int(input("  Enter ending value   : "))
                    l = e - 1
                    print("  Elements : ",end="")
                    for e in t[s:e]:
                        if e != t[l]:
                            print(e,end=", ")
                        if e == t[l]:
                            print(e)

                # The program displays the length of the tuple.
                def display_length(t):
                    print("\nDisplay the length of a tuple")
                    length = len(t)
                    print("  Length :",length)

                # User inputs a number and the program will display the element having that inputted number as index.
                def display_element(t):
                    print("\nDisplay element:")
                    num = int(input("  Enter negative number : "))
                    element = t[num]
                    print("  Element : ",element)

                # User inputs an element and the program will display the count of that element in the tuple.
                def count_element(t):
                    print("\nCount in tuple")
                    element = input("  Enter an element : ")
                    cnt = t.count(element)
                    print("  Count :",cnt)

                # User inputs an index (number) and the program will display which element has that index.
                def display_index(t):
                    print("\nDisplay index:")
                    element = input("  Enter element : ")
                    ind = t.index(element)
                    print("  Index :",ind)

                # User inputs an element and the program will check if that element is in the tuple. 
                def check_element(t):
                    print("\nElement in tuple:")
                    val = input("  Input value : ")
                    if val in t:
                        print("  Output : True")
                    else:
                        print("  Output : False")

                # The program displays the element with the highest value.
                def display_max(t):
                    print("\nMaximum")
                    print("  Output :",max(t))

                # The program displays the element with the lowest value.
                def display_min(t):
                    print("\nMaximum")
                    print("  Output :",min(t))
                    print()

                # main
                my_tuple = ("l", "h", "a", "me", "s", "i", "w", "r", "l", "j")
                display_tuple(my_tuple)
                tuple_slicing(my_tuple)
                display_length(my_tuple)
                display_element(my_tuple)
                count_element(my_tuple)
                display_index(my_tuple)
                check_element(my_tuple)
                display_max(my_tuple)
                display_min(my_tuple)

            except:
                print("Invalid. Try again.")

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break
            
        elif choice == 3:

            d1={'6COMPRO2L' : ['SJH-608', 'Arcely Napalit', '10:15 a.m.'],

                '6HCI'      : ['SJH-609', 'Adrian Magcalas', '7:00 a.m.'],

                '6NETFUN'   : ['SJH-610', 'Paul Calimoso', '3:40 p.m.'],

                '6DMS'      : ['SJH-605', 'Ma. Louella Salenga', '1:30 p.m.'],

                '6CSEC'     : ['MGN-202', 'Marlon Tayag', '2:35 p.m.'],

                '6DRAW1'    : ['SJH-607', 'Kahil Makisig Yu', '4:45 p.m.'] }


                
            loop = 1
            while loop == 1:
                meow = str(input("Enter the course : "))
                print(d1[meow])

               

            
            print (" ")

            bonIver = set(open("word.txt").read().split("\n"))

            amsterdam = ""

            amsterdam = amsterdam.join(bonIver).lower()

            print (amsterdam)

            amsterdam = amsterdam.split(" ")


            for dior in amsterdam:
                astonMartin = amsterdam.count(dior)
                print (dior, " = ", astonMartin)
            

            again = (input("Do you want to try again? Answer [Y/N]:"))
            if again == 'y':
                loop = 1
            elif again == 'Y':
                loop = 1    
            elif again == 'n': 
                print ("End of program")
                break
            elif again == 'N': 
                print ("End of program")
                break


        elif choice == 4:    
            print ("End of program")
            loop = 0
            break
        
    elif choice == 4:    
        print ("End of program")
        loop = 0
        break
