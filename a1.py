'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions.

- You MUST complete the functions defined below, except the ones that are already defined.
'''
def show_menu():
    '''
	Description: Prints the menu as shown in the PDF

	Parameters: No paramters

	Returns: No return value
	'''
    design=""
    print(design.center(168, '='))
    store_name="MY BAZAAR\n"
    print(store_name.center(172, " "))
    design=""
    print(design.center(168, '='))
    print("  Hello! Welcome to my grocery store!\n\n",end=(""))
    print("  Following are the products available in the shop:\n\n",end=(""))
    design=""
    print(design.center(168, '-'))
    menu='     CODE | DESCRIPTION | CATEGORY     | COST (Rs)\n'
    print(menu.ljust(170))
    design=""
    print(design.center(168, '-'))
    print('''
      0   | Tshirt      | Apparels     | 500

      1   | Trousers    | Apparels     | 600

      2   | Scarf       | Apparels     | 250

      3   | Smartphone  | Electronics  | 20,000

      4   | iPad        | Electronics  | 30,000

      5   | Laptop      | Electronics  | 50,000

      6   | Eggs        | Eatables     | 5

      7   | Chocolate   | Eatables     | 10

      8   | Juice       | Eatables     | 100

      9   | Milk        | Eatables     | 45  \n\n ''')

    design=""
    print(design.center(168, '-'))


def get_regular_input():
    '''
	Description: Takes space separated item codes (only integers allowed).
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: No parameters

	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''

    print('-'*160)
    print('  REGULAR CUSTOMER  '.center(168,'#'))
    print('\n ENTER THE ITEMS YOU WISH TO BUY::\n')
    print('-'*160)
    n = int(input(" Enter number of items you wish to buy: "))
    en_items= list(map(int,input("\nEnter the item codes (space-separated):: ").strip().split()))
    quantities=(en_items)[:n]
    print(list(sorted(quantities)))

    print_order_details(quantities)

def get_bulk_input():

    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer.
    For details, refer PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    quantities=[]
    bulk_in=[]
    bulk_quan=[]

    print('  BULK CUSTOMER  '.center(168,'#'))
    print('-'*160)
    print('\n ENTER THE ITEMS YOU WISH TO BUY::\n')
    print('-'*160)

    while True:
        try:
           bulk_in , bulk_quan=map(str,input('Enter code and quantity (leave blank to stop):').split() or (' ',' '))
        except:
            while bulk_in not in (0,9):
                print('\n Invalid code. Try again')
                break
            while bulk_quan not in (0,):
                print('\n Invalid code. Try again')
                break

        for x in bulk_in:

            if '0' in bulk_in:
                print('You added {} Tshirts'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '1' in bulk_in:
                print('You added {} Trousers'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '2' in bulk_in:
                print('You added {} Scarf'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '3' in bulk_in:
                print('You added {} Smartphone'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '4' in bulk_in:
                print('You added {} iPad'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '5' in bulk_in:
                print('You added {} Laptop'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '6' in bulk_in:
                print('You added {} Eggs'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '7' in bulk_in:
                print('You added {} Chocolate'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '8' in bulk_in:
                print('You added {} juice'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if '9' in bulk_in:
                print('You added {} Milk'.format(bulk_quan))
                quantities.append([bulk_in,bulk_quan])

                continue

            if ' ' in bulk_in:
                print('\n Your Order has been finalized')
                exit()

            print(sorted(quantities))


def print_order_details(quantities):
    '''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.

	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.

	Returns: No return value
	'''

    print('\n')
    print('-'*160)
    print('  ORDER DETAILS::\n')
    print('-'*160)
    for i in range(0,10):

        for j in range(i):

            if i==1 in quantities:
                  print([i]," Trousers x", quantities.count(i), '= RS 600 *',quantities.count(i),'= RS',600 *(quantities.count(i)))
                  break
            if i==2 in quantities:
                  print([i]," Scarf x", quantities.count(i), '= RS 250 *',quantities.count(i),'= RS',250 *(quantities.count(i)))
                  break
            if i==3 in quantities:
                  print([i]," Smartphone x", quantities.count(i), '= RS 20,000 *',quantities.count(i),'= RS',20000 *(quantities.count(i)))
                  break
            if i==4 in quantities:
                  print([i]," iPad x", quantities.count(i), '= RS 30,000 *',quantities.count(i),'= RS',30000 *(quantities.count(i)))
                  break
            if i==5 in quantities:
                  print([i]," Laptop x", quantities.count(i), '= RS 50,000 *',quantities.count(i),'= RS',50000 *(quantities.count(i)))
                  break
            if i==6 in quantities:
                  print([i]," Eggs x", quantities.count(i), '= RS 5 *',quantities.count(i),'= RS',5 *(quantities.count(i)))
                  break
            if i==7 in quantities:
                  print([i]," Chocolate x", quantities.count(i), '= RS 10 *',quantities.count(i),'= RS',10 *(quantities.count(i)))
                  break
            if i==8 in quantities:
                  print([i]," Juice x", quantities.count(i), '= RS 100 *',quantities.count(i),'= RS',100 *(quantities.count(i)))
                  break
            if i==9 in quantities:
                  print([i]," Milk x", quantities.count(i), '= RS 45 *',quantities.count(i),'= RS',45 *(quantities.count(i)))
                  break
        else:
            if i==0 in quantities:
                  print([i]," Tshirt x", quantities.count(i), '= RS 500 *',quantities.count(i),'= RS',500 *(quantities.count(i)))
                  pass
    calculate_category_wise_cost(quantities)


def calculate_category_wise_cost(quantities):
    '''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.

	Returns: A 3-tuple of integers in the following format:
	(apparels_cost, electronics_cost, eatables_cost)
	'''
    global apparels_cost
    global eatables_cost
    global electronics_cost
    print('\n')
    print('-'*160)
    print('  CATEGORY-WISE COST::\n')
    print('-'*160)

    a=0
    b=0
    c=0
    for i in range (0,3):
        if i==0 in quantities:
            a=(500 *(quantities.count(i)))
        if i==1 in quantities:
            b=(600 *(quantities.count(i)))
        if i==2 in quantities:
            c=(250 *(quantities.count(i)))
        else:
            pass
    apparels_cost=(a+b+c)
    print('\n  Apparels = Rs',apparels_cost)
    d=0
    e=0
    f=0
    for i in range (3,6):
        if i==3 in quantities:
            d=(20000 *(quantities.count(i)))
        if i==4 in quantities:
            e=(30000 *(quantities.count(i)))
        if i==5 in quantities:
            f=(50000 *(quantities.count(i)))
        else:
            pass
    electronics_cost=(d+e+f)
    print('\n  Electronics = Rs',electronics_cost)
    g=0
    h=0
    k=0
    l=0
    for i in range (6,10):
        if i==6 in quantities:
            g=(5 *(quantities.count(i)))
        if i==7 in quantities:
            h=(10 *(quantities.count(i)))
        if i==8 in quantities:
            k=(100 *(quantities.count(i)))
        if i==9 in quantities:
            l=(45 *(quantities.count(i)))
    eatables_cost=(g+h+k+l)
    print('\n  Eatables = Rs',eatables_cost)

    calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)
    return (apparels_cost, electronics_cost, eatables_cost)

def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    # I found that we don't need to do anything here, just pass on the values to the paramters in calculate_discounted_prices() function

    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the discounted category-wise price, if applicable.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'

	Returns: A 3-tuple of integers in the following format:
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
	'''

    global discounted_apparels_cost
    global discounted_eatables_cost
    global discounted_electronics_cost
    global disc1
    global disc2
    global disc3
    global total_cost



    print('\n')
    print('-'*160)
    print('  DISCOUNTS \n')
    print('-'*160)

    if apparels_cost >= 2000:
        cost=apparels_cost
        discounted_apparels_cost=(cost-get_discount(cost, 0.10))
        print('\n  [Apparels]  = Rs',apparels_cost,'- Rs',(0.10*apparels_cost),'= Rs',discounted_apparels_cost)
        disc1=get_discount(cost, 0.10)

    if electronics_cost>= 25000:
        cost=electronics_cost
        discounted_electronics_cost=(cost-get_discount(cost, 0.10))
        print('\n  [Electronics] = Rs',electronics_cost,'- Rs',(0.10*electronics_cost),'= Rs',discounted_electronics_cost)
        disc2=get_discount(cost, 0.10)

    if eatables_cost>= 500:
        cost=eatables_cost
        discounted_eatables_cost=(cost-get_discount(cost, 0.10))
        print('\n  [Eatables] = Rs',eatables_cost,'- Rs',(0.10*eatables_cost),'= Rs',discounted_eatables_cost)
        disc3=get_discount(cost, 0.10)

    total_discount=(disc1+disc2+disc3)

    if disc1>0 and disc2>0 and disc3>0:
        total_cost=(discounted_apparels_cost+discounted_electronics_cost+discounted_eatables_cost)

    if disc1>0 and disc2<=0 and disc3<=0:
        total_cost=(discounted_apparels_cost+electronics_cost+eatables_cost)

    if disc1<=0 and disc2>0 and disc3<=0:
        total_cost=(apparels_cost+discounted_electronics_cost+eatables_cost)

    if disc1<=0 and disc2<=0 and disc3>0:
        total_cost=(apparels_cost+electronics_cost+discounted_eatables_cost)

    if disc1>0 and disc2>0 and disc3<=0:
        total_cost=(discounted_apparels_cost+discounted_electronics_cost+eatables_cost)

    if disc1<=0 and disc2>0 and disc3>0:
        total_cost=(apparels_cost+discounted_electronics_cost+discounted_eatables_cost)

    if disc1>0 and disc2<=0 and disc3>0:
        total_cost=(discounted_apparels_cost+electronics_cost+discounted_eatables_cost)

    if disc1<=0 and disc2<=0 and disc3<=0:
        total_cost=(apparels_cost+electronics_cost+eatables_cost)


    print('\n  TOTAL DISCOUNT = Rs',total_discount)
    print('\n  TOTAL COST = Rs',total_cost)

    calculate_tax(apparels_cost, electronics_cost, eatables_cost)
    return total_cost
    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)

def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    # I found that we don't need to do anything here, just pass on the values to the paramters in calculate_tax() function

    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 2-tuple of integers in the following format:
    (total_cost_including_tax, total_tax)
    '''

    print('\n')
    print('-'*160)
    print('  TAX \n')
    print('-'*160)

    global tax1
    global tax2
    global tax3


    if apparels_cost :
        if discounted_apparels_cost>0:
            cost=discounted_apparels_cost
            tax1=get_tax(cost,0.10)
            print('\n  [Apparels]  Rs',discounted_apparels_cost,'* 0.10','= Rs',tax1)

        else:
            cost=apparels_cost
            tax1=get_tax(cost,0.10)
            print('\n  [Apparels]  Rs',apparels_cost,'* 0.10','= Rs',tax1)


    if electronics_cost :
        if discounted_electronics_cost>0:
            cost=discounted_electronics_cost
            tax2=get_tax(cost,0.15)
            print('\n  [Electronics]  Rs',discounted_electronics_cost,'* 0.15','= Rs',tax2)

        else:
            cost=electronics_cost
            tax2=get_tax(cost,0.15)
            print('\n  [Electronics]  Rs',electronics_cost,'* 0.15','= Rs',tax2)


    if eatables_cost :
        if discounted_eatables_cost>0:
            cost=discounted_eatables_cost
            tax3=get_tax(cost,0.05)
            print('\n  [Eatables]  Rs',discounted_eatables_cost,'* 0.05','= Rs',tax3)

        else:
            cost=eatables_cost
            tax3=get_tax(cost,0.05)
            print('\n  [Eatables]  Rs',eatables_cost,'* 0.05','= Rs',tax3)

    total_tax=(tax1+tax2+tax3)
    total_cost_including_tax=(total_cost+total_tax)
    print('\n')
    print('\n TOTAl TAX = Rs ',total_tax)
    print('\n TOTAL COST = Rs',total_cost_including_tax)
    apply_coupon_code(total_cost_including_tax)
    return (total_cost_including_tax, total_tax)


def apply_coupon_code(total_cost_including_tax):
    '''
    Description: Takes the coupon code from the user as input (case-sensitive).
    For details, refer the PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: The total cost (integer) on which the coupon is to be applied.

    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)

    '''
    global total_coupon_discount

    print('\n')
    print('-'*160)
    print('  COUPON CODE \n')
    print('-'*160)
    print('\n',''''
          TOTAL COST >= 50,000 --> [ CHILL50 ]

          TOTAL COST >= 25,000 --> [ HELLE25 ]
            ''')

    if total_cost_including_tax>=50000:

        while True:
            try:
                coupon=(input('\nEnter coupon code (else leave blank) : ').split() or ' ')
            except:
                continue

            if 'CHILL50' in coupon:
                discount_on_tax=min(10000,total_cost_including_tax*0.50)
                total_cost_after_coupon_discount=(total_cost_including_tax-discount_on_tax)
                print('\n [ CHILL50 ] min(10000, Rs',total_cost_including_tax,'* 0.50)= Rs ',discount_on_tax )
                print('\n TOTAL COUPAN DISCOUNT = Rs ',discount_on_tax)
                print('\n TOTAL COST = Rs',total_cost_after_coupon_discount)
                exit()

            if ' ' in coupon:
                discount_on_tax=0
                total_cost_after_coupon_discount=total_cost_including_tax
                print('\n No Coupon code applied..')
                print('\n TOTAL COUPAN DISCOUNT = Rs ',discount_on_tax)
                print('\n TOTAL COST = Rs',total_cost_after_coupon_discount)
                exit()

            else:
                print("\n Invalid coupon code. TRY AGAIN..\n")



    if total_cost_including_tax>=25000:
        while True:
            try:
                coupon=(input('\nEnter coupon code (else leave blank) : ').split() or ' ')
            except:
                continue


            if 'HELLE25' in coupon:
                discount_on_tax=min(5000,total_cost_including_tax*0.25)
                total_cost_after_coupon_discount=(total_cost_including_tax-discount_on_tax)
                print('\n [ HELLE25 ] min(5000, Rs',total_cost_including_tax,'* 0.25)= Rs ',discount_on_tax)
                print('\n TOTAL COUPAN DISCOUNT = Rs ',discount_on_tax)
                print('\n TOTAL COST = Rs',total_cost_after_coupon_discount)
                exit()

            if ' ' in coupon:
                discount_on_tax=0
                print('\n No Coupon code applied..')
                print('\n TOTAL COUPAN DISCOUNT = Rs ',discount_on_tax)
                total_cost_after_coupon_discount=total_cost_including_tax
                print('\n TOTAL COST = Rs',total_cost_after_coupon_discount)
                exit()

            else:
                print("\n Invalid coupon code. TRY AGAIN..\n")


    if total_cost_including_tax<25000:
        print('NOT VALID TO APPLY coupon code !!')
        total_cost_after_coupon_discount=total_cost_including_tax
        print('\n TOTAL COST = Rs',total_cost_after_coupon_discount)

    return (total_cost_after_coupon_discount, total_coupon_discount)




apparels_cost=0
eatables_cost=0
electronics_cost=0
discounted_eatables_cost=0
discounted_apparels_cost=0
discounted_electronics_cost=0
disc1=0
disc2=0
disc3=0
cost=0
discount_rate=0
total_cost=0
tax1=0
tax2=0
tax3=0
total_coupon_discount=0

def main():
    '''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate
	print statements to match the output with the screenshots provided in the PDF.

	Parameters: No parameters

	Returns: No return value
	'''

    show_menu()

    while True:
        try:
            Bulk_Or_Regular=input('Would you like to buy in bulk? (y or Y / n or N): N:')
        except:
            continue

        if Bulk_Or_Regular in ('y','Y'):
            print("\n")
            get_bulk_input()
            print_order_details(quantities)
        elif Bulk_Or_Regular in ('n','N'):
            print("\n")
            return get_regular_input()
        else:
            print('\nYOU Entered an Invalid Input !!!!!!!!!!!!!!!!!!!!')
            print('\nENTER AGAIN--\n')



if __name__ == '__main__':
    main()
