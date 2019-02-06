list_lenN = int(input("enter the length of the list : "))

list_of_numbers = []
print(len(list_of_numbers))
for number in range(0,list_lenN):
    new_num = int(input("enter {} no.:".format(number+1)))
    list_of_numbers.append(new_num)
print(list_of_numbers)

list_lenQ = int(input("enter the number of quries"))
list_of_quiries = []
for quries in range(0,list_lenQ):
    new_query = int(input("enter query no {}:".format(quries + 1)))
    list_of_quiries.append(new_query)
print(list_of_quiries)

# comparision





#