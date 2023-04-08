def massive_bezpovtorov():
    m = int(input("кол-во элементов первого множестава:"))
    n = int(input("кол-во элементов второго множестава:"))
    lst_m = []
    lst_n = []
    for i in range(m):
        lst_m.append(int(input("введите элемент {0} первого множества : ".format(i))))
    for i in range(n):
        lst_n.append(int(input("введите элемент {0} второго множества : ".format(i))))
    lst_m_1 = list(set(lst_m))
    lst_n_1 = list(set(lst_n))
    lst_m_1.sort()
    lst_n_1.sort()
    print(lst_m_1)
    print(lst_n_1)
massive_bezpovtorov()