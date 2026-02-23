#nama:dorothy dores kelas:c02
#Creating a program that accepts 5 integer input values from the user and is stored in a list

#fungtion name
def sort_numbers():
    #empty list
    num =[]
    
    #to get 5 input
    for i in range (1,6):
        number = int(input(f"Enter number{i} : ")) 
        num.append(number)

        #to sort number , calculate sum and fing largest
        ascending_order = sorted (num)
        total = sum(num)
        largest = max(num)

    return (f"Number in ascending order: {ascending_order} \nSum of all numbers: {total} \nLargest number: {largest}")

 #call fungtion   
print(sort_numbers())