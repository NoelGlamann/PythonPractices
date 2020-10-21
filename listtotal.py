#!/usr/bin/python3
#07 September 2019
#Noel Glamann

'''For Loop Example'''

#Program Functions
def total(a_list):
    total = 0
    for i in range(len(a_list)):
        total += a_list[i]
    return total 

#Main Section
if __name__ == "__main__":
    bill_items = [1, 2, 3, 4]
    total_bill = total(bill_items)
    print(total_bill)
    
    