list_lenN = int(input("enter the length of the list : "))

if list_lenN >=1 and list_lenN <= 10**5 :
    list_of_numbers = []
    print(len(list_of_numbers))
    for number in range(0,list_lenN):
        new_num = int(input("enter {} no.:".format(number+1)))
        list_of_numbers.append(new_num)
    print(list_of_numbers)
    # ===================================quries=====================
    list_lenQ = int(input("enter the number of quries"))
    list_of_quiries = []
    if list_lenQ <= 10**5 and list_lenQ >=1:
        for quries in range(0, list_lenQ):
            new_query = int(input("enter query no {}:".format(quries + 1)))
            if new_query >= 0 and new_query<=1000:
                list_of_quiries.append(new_query)
            else:
                print("the query is larger than 1000")
        print(list_of_quiries)
    else:
        print("too large query set")

    query_result = []
    # comparision
    for num in range(0, len(list_of_quiries)):
        i = 0
        for num_q in range(0, len(list_of_numbers)):
            if list_of_quiries[num] == list_of_numbers[num_q]:
                i += 1
            else:
                pass
        query_result.append(i)
    print(query_result)
else:
    print("number too large")








#