import input_data

dim = input_data.Dimentions

def t_svertka(tenz):
    temp_comp = tenz['comp']
    vals = tenz['vals']
    doubles = {}
    i = 0
    for com in temp_comp:
        if temp_comp.count(com) > 1:
            doubles[i] = com
        i=i+1
    for com in doubles.values():
        temp_comp.remove(com)
    if len(doubles) == 2:
        if len(temp_comp) == 2:
            temp_vals = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            if 0 in doubles.keys() and 1 in doubles.keys():
                for i in range(0,3):
                    for j in range(0,3):
                        for k in range(0,3):
                            for l in range(0,3):
                                temp_vals[k][l]+=vals[i][j][k][l]
            elif 0 in doubles.keys() and 2 in doubles.keys():
                for i in range(0, 3):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            for l in range(0, 3):
                                temp_vals[j][l] += vals[i][j][k][l]
            elif 0 in doubles.keys() and 3 in doubles.keys():
                for i in range(0, 3):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            for l in range(0, 3):
                                temp_vals[j][k] += vals[i][j][k][l]
            elif 1 in doubles.keys() and 2 in doubles.keys():
                for i in range(0, 3):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            for l in range(0, 3):
                                temp_vals[i][l] += vals[i][j][k][l]
            elif 1 in doubles.keys() and 3 in doubles.keys():
                for i in range(0, 3):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            for l in range(0, 3):
                                temp_vals[i][k] += vals[i][j][k][l]
            elif 2 in doubles.keys() and 3 in doubles.keys():
                for i in range(0, 3):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            for l in range(0, 3):
                                temp_vals[i][j] += vals[i][j][k][l]
        elif len(temp_comp) == 1:
            temp_vals = [0, 0, 0]
            if 0 in doubles.keys() and 1 in doubles.keys():
                for i in range(0,3):
                    for j in range(0,3):
                        for k in range(0,3):
                            temp_vals[k]+=vals[i][j][k]
            if 0 in doubles.keys() and 2 in doubles.keys():
                for i in range(0,3):
                    for j in range(0,3):
                        for k in range(0,3):
                            temp_vals[j]+=vals[i][j][k]
            if 1 in doubles.keys() and 2 in doubles.keys():
                for i in range(0,3):
                    for j in range(0,3):
                        for k in range(0,3):
                            temp_vals[i]+=vals[i][j][k]
        elif len(temp_comp) == 0:
            temp_vals = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    temp_vals+= vals[i][j]
        temp_tenz = {'comp': temp_comp, 'vals': temp_vals}
        return temp_tenz

    elif len(doubles) > 2:
        print("В данном тензере более 2-х компонент по которым производится свёртывание, разбейте процесс на подзадачи")
        return tenz
    else:
        print("В данном тензере нет повторющийхся компонент, свёртка невозможна!")
        return tenz


def t_sum(tenz1, tenz2):
    comp1 = tenz1['comp']
    comp2 = tenz2['comp']
    vals1 = tenz1['vals']
    vals2 = tenz2['vals']
    temp_comp = comp1
    temp_vals = vals1
    if len(comp1) == len(comp2):
        if len(comp1) == 4:
            for i in range(0, 3):
                for j in range(0, 3):
                    for k in range(0, 3):
                        for l in range(0, 3):
                            temp_vals[i][j][k][l] += vals2[i][j][k][l]
        elif len(comp1) == 3:
            for i in range(0, 3):
                for j in range(0, 3):
                    for k in range(0, 3):
                        temp_vals[i][j][k] += vals2[i][j][k]
        elif len(comp1) == 2:
            for i in range(0, 3):
                for j in range(0, 3):
                    temp_vals[i][j] += vals2[i][j]
        elif len(comp1) == 1:
            for i in range(0, 3):
                temp_vals[i] += vals2[i]
        temp_tenz = {'comp': temp_comp, 'vals': temp_vals}
        return temp_tenz

    else:
        print("У данных тензоров различное число компонент!")


def t_mult(tenz1, tenz2):
    have_to_svert = check_comp(tenz1, tenz2)
    if have_to_svert:
        if len(have_to_svert) == 2:
            for val in have_to_svert.values():
                temp_comp = tenz1['comp']
                temp_comp.remove(val)
            vals1 = tenz1['vals']
            vals2 = tenz2['vals']
            if len(temp_comp) == 2:
                temp_vals = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                if 0 in have_to_svert.keys() and 1 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                for l in range(0,3):
                                    temp_vals[k][l]+=vals1[i][j][k][l]*vals2[i][j]
                elif 0 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                for l in range(0,3):
                                    temp_vals[j][l]+=vals1[i][j][k][l]*vals2[i][k]
                elif 0 in have_to_svert.keys() and 3 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                for l in range(0,3):
                                    temp_vals[j][k]+=vals1[i][j][k][l]*vals2[i][l]
                elif 1 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                for l in range(0,3):
                                    temp_vals[i][l]+=vals1[i][j][k][l]*vals2[j][k]
                elif 1 in have_to_svert.keys() and 3 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                for l in range(0,3):
                                    temp_vals[i][k]+=vals1[i][j][k][l]*vals2[j][l]
                elif 2 in have_to_svert.keys() and 3 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                for l in range(0,3):
                                    temp_vals[i][j]+=vals1[i][j][k][l]*vals2[k][l]
            elif len(temp_comp) == 1:
                temp_vals = [0, 0, 0]
                if 0 in have_to_svert.keys() and 1 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                temp_vals[k]+=vals1[i][j][k]*vals2[i][j]
                elif 0 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                temp_vals[j]+=vals1[i][j][k]*vals2[i][k]
                elif 1 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            for k in range(0,3):
                                temp_vals[i]+=vals1[i][j][k]*vals2[j][k]
            elif len(temp_comp) == 0:
                temp_vals = 0
                for i in range(0,3):
                    for j in range(0,3):
                        temp_vals+=vals1[i][j]*vals2[i][j]
        elif len(have_to_svert) == 1:
            for val in have_to_svert.values():
                temp_comp = tenz1['comp']
                temp_comp.remove(val)
            vals1 = tenz1['vals']
            vals2 = tenz2['vals']
            if len(temp_comp) == 2:
                temp_vals = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                if 0 in have_to_svert.keys():
                    for i in range(0, 3):
                        for j in range(0, 3):
                            for k in range(0, 3):
                                temp_vals[j][k]+=vals1[i][j][k] * vals2[i]
                elif 1 in have_to_svert.keys():
                    for i in range(0, 3):
                        for j in range(0, 3):
                            for k in range(0, 3):
                                temp_vals[i][k]+=vals1[i][j][k] * vals2[j]
                elif 2 in have_to_svert.keys():
                    for i in range(0, 3):
                        for j in range(0, 3):
                            for k in range(0, 3):
                                temp_vals[i][j]+=vals1[i][j][k] * vals2[k]
            elif len(temp_comp) == 1:
                temp_vals = [0, 0, 0]
                if 0 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            temp_vals[j]+=vals1[i][j] * vals2[i]
                elif 1 in have_to_svert.keys():
                    for i in range(0,3):
                        for j in range(0,3):
                            temp_vals[i]+=vals1[i][j] * vals2[j]
            elif len(temp_comp) == 0:
                temp_vals = 0
                for i in range(0,3):
                    temp_vals+=vals1[i]*vals2[i]
    else:
        comp1 = tenz1['comp']
        comp2 = tenz2['comp']
        vals1 = tenz1['vals']
        vals2 = tenz2['vals']
        temp_comp = comp1 + comp2
        if len(comp1) == 2 and len(comp2) == 2:
            temp_vals = [[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]]
            for i in range(0,3):
                for j in range(0,3):
                    for k in range(0,3):
                        for l in range(0,3):
                            temp_vals[i][j][k][l]=vals1[i][j]*vals2[k][l]
        elif len(comp1) == 3 and len(comp2) == 1:
            temp_vals = temp_vals = [[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]]
            for i in range(0,3):
                for j in range(0,3):
                    for k in range(0,3):
                        for l in range(0,3):
                            temp_vals[i][j][k][l]=vals1[i][j][k]*vals2[l]
        elif len(comp1) == 2 and len(comp2) == 1:
            temp_vals = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
            for i in range(0,3):
                for j in range(0,3):
                    for k in range(0,3):
                        temp_vals[i][j][k]= vals1[i][j]*vals2[k]
        elif len(comp1) == 1 and len(comp2) == 1:
            temp_vals = [[0,0,0],[0,0,0],[0,0,0]]
            for i in range(0,3):
                for j in range(0,3):
                    temp_vals[i][j]=vals1[i]*vals2[j]
    temp_tenz = {'comp': temp_comp, 'vals': temp_vals}
    return temp_tenz


def check_comp(tenz1, tenz2):
    numbers = {}
    i = 0
    comp1 = tenz1['comp']
    comp2 = tenz2['comp']
    for comp in comp1:
        if comp in comp2:
            numbers[i] = comp
        i = i+1
    if len(numbers) > 0:
        return numbers
    else:
        return False


def ask_for_choise():
    choise = input("Введите номер задания которое необходимо решить (1,2,3,4)\nДля завершения работы используйте команду exit\n")

    if choise == '1':
        print(f"Ответ: {t_mult(input_data.Aij, input_data.Bk)}")
        ask_for_choise()
    elif choise == '2':
        first_part = t_mult(input_data.Aij, input_data.bj)
        second_part = t_mult(input_data.Akl, input_data.bl)
        print(f"Ответ: {t_sum(first_part, second_part)}")
        ask_for_choise()
    elif choise == '3':
        print(f"Ответ: {t_svertka(input_data.Tljl)}")
        ask_for_choise()
    elif choise == '4': #подтвердил расчётами на бумаге правильность работы, есть сомнение в правильности записи леви-чевиты
        first_part = t_mult(input_data.Ajkl,input_data.Bjl)
        sf = t_mult(input_data.eps, input_data.aj)
        second_part = t_mult(sf,input_data.bk)
        print(f"Ответ: {t_sum(first_part, second_part)}")
        ask_for_choise()
    elif choise == 'exit':
        return 1
    else:
        print("Введен некорректный номер")
        ask_for_choise()


ask_for_choise()

