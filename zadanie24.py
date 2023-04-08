
def avtosadovnik():
    kustov = int(input("введи количество кустов :"))
    yagod_lst = []
    for i in range(kustov):
        yagod_lst.append(int(input("ягод на i-том кусте:")))

    print(yagod_lst)
    max_yagod =0
    pos = 0
    for i in range(1, kustov-1):
        curr_yagod = yagod_lst[i-1] + yagod_lst[i]+ yagod_lst[i+1]
        if max_yagod<curr_yagod:
            max_yagod = curr_yagod
            pos = i


    print("максимальное количество ягод {0} на {1}(i) кусте".format(max_yagod,pos))

avtosadovnik()