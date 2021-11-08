import re

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
                for i in range(0,dim):
                    for j in range(0,dim):
                        for k in range(0,dim):
                            for l in range(0,dim):
                                temp_vals[k][l]+=vals[i][j][k][l]
            elif 0 in doubles.keys() and 2 in doubles.keys():
                for i in range(0, dim):
                    for j in range(0, dim):
                        for k in range(0, dim):
                            for l in range(0, dim):
                                temp_vals[j][l] += vals[i][j][k][l]
            elif 0 in doubles.keys() and dim in doubles.keys():
                for i in range(0, dim):
                    for j in range(0, dim):
                        for k in range(0, dim):
                            for l in range(0, dim):
                                temp_vals[j][k] += vals[i][j][k][l]
            elif 1 in doubles.keys() and 2 in doubles.keys():
                for i in range(0, dim):
                    for j in range(0, dim):
                        for k in range(0, dim):
                            for l in range(0, dim):
                                temp_vals[i][l] += vals[i][j][k][l]
            elif 1 in doubles.keys() and dim in doubles.keys():
                for i in range(0, dim):
                    for j in range(0, dim):
                        for k in range(0, dim):
                            for l in range(0, dim):
                                temp_vals[i][k] += vals[i][j][k][l]
            elif 2 in doubles.keys() and dim in doubles.keys():
                for i in range(0, dim):
                    for j in range(0, dim):
                        for k in range(0, dim):
                            for l in range(0, dim):
                                temp_vals[i][j] += vals[i][j][k][l]
        elif len(temp_comp) == 1:
            temp_vals = [0, 0, 0]
            if 0 in doubles.keys() and 1 in doubles.keys():
                for i in range(0,dim):
                    for j in range(0,dim):
                        for k in range(0,dim):
                            temp_vals[k]+=vals[i][j][k]
            if 0 in doubles.keys() and 2 in doubles.keys():
                for i in range(0,dim):
                    for j in range(0,dim):
                        for k in range(0,dim):
                            temp_vals[j]+=vals[i][j][k]
            if 1 in doubles.keys() and 2 in doubles.keys():
                for i in range(0,dim):
                    for j in range(0,dim):
                        for k in range(0,dim):
                            temp_vals[i]+=vals[i][j][k]
        elif len(temp_comp) == 0:
            temp_vals = 0
            for i in range(0, dim):
                for j in range(0, dim):
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
            for i in range(0, dim):
                for j in range(0, dim):
                    for k in range(0, dim):
                        for l in range(0, dim):
                            temp_vals[i][j][k][l] += vals2[i][j][k][l]
        elif len(comp1) == dim:
            for i in range(0, dim):
                for j in range(0, dim):
                    for k in range(0, dim):
                        temp_vals[i][j][k] += vals2[i][j][k]
        elif len(comp1) == 2:
            for i in range(0, dim):
                for j in range(0, dim):
                    temp_vals[i][j] += vals2[i][j]
        elif len(comp1) == 1:
            for i in range(0, dim):
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
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                for l in range(0,dim):
                                    temp_vals[k][l]+=vals1[i][j][k][l]*vals2[i][j]
                elif 0 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                for l in range(0,dim):
                                    temp_vals[j][l]+=vals1[i][j][k][l]*vals2[i][k]
                elif 0 in have_to_svert.keys() and dim in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                for l in range(0,dim):
                                    temp_vals[j][k]+=vals1[i][j][k][l]*vals2[i][l]
                elif 1 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                for l in range(0,dim):
                                    temp_vals[i][l]+=vals1[i][j][k][l]*vals2[j][k]
                elif 1 in have_to_svert.keys() and dim in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                for l in range(0,dim):
                                    temp_vals[i][k]+=vals1[i][j][k][l]*vals2[j][l]
                elif 2 in have_to_svert.keys() and dim in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                for l in range(0,dim):
                                    temp_vals[i][j]+=vals1[i][j][k][l]*vals2[k][l]
            elif len(temp_comp) == 1:
                temp_vals = [0, 0, 0]
                if 0 in have_to_svert.keys() and 1 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                temp_vals[k]+=vals1[i][j][k]*vals2[i][j]
                elif 0 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                temp_vals[j]+=vals1[i][j][k]*vals2[i][k]
                elif 1 in have_to_svert.keys() and 2 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            for k in range(0,dim):
                                temp_vals[i]+=vals1[i][j][k]*vals2[j][k]
            elif len(temp_comp) == 0:
                temp_vals = 0
                for i in range(0,dim):
                    for j in range(0,dim):
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
                    for i in range(0, dim):
                        for j in range(0, dim):
                            for k in range(0, dim):
                                temp_vals[j][k]+=vals1[i][j][k] * vals2[i]
                elif 1 in have_to_svert.keys():
                    for i in range(0, dim):
                        for j in range(0, dim):
                            for k in range(0, dim):
                                temp_vals[i][k]+=vals1[i][j][k] * vals2[j]
                elif 2 in have_to_svert.keys():
                    for i in range(0, dim):
                        for j in range(0, dim):
                            for k in range(0, dim):
                                temp_vals[i][j]+=vals1[i][j][k] * vals2[k]
            elif len(temp_comp) == 1:
                temp_vals = [0, 0, 0]
                if 0 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            temp_vals[j]+=vals1[i][j] * vals2[i]
                elif 1 in have_to_svert.keys():
                    for i in range(0,dim):
                        for j in range(0,dim):
                            temp_vals[i]+=vals1[i][j] * vals2[j]
            elif len(temp_comp) == 0:
                temp_vals = 0
                for i in range(0,dim):
                    temp_vals+=vals1[i]*vals2[i]
    else:
        comp1 = tenz1['comp']
        comp2 = tenz2['comp']
        vals1 = tenz1['vals']
        vals2 = tenz2['vals']
        temp_comp = comp1 + comp2
        if len(comp1) == 2 and len(comp2) == 2:
            temp_vals = [[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]]
            for i in range(0,dim):
                for j in range(0,dim):
                    for k in range(0,dim):
                        for l in range(0,dim):
                            temp_vals[i][j][k][l]=vals1[i][j]*vals2[k][l]
        elif len(comp1) == dim and len(comp2) == 1:
            temp_vals = temp_vals = [[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]]
            for i in range(0,dim):
                for j in range(0,dim):
                    for k in range(0,dim):
                        for l in range(0,dim):
                            temp_vals[i][j][k][l]=vals1[i][j][k]*vals2[l]
        elif len(comp1) == 2 and len(comp2) == 1:
            temp_vals = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
            for i in range(0,dim):
                for j in range(0,dim):
                    for k in range(0,dim):
                        temp_vals[i][j][k]= vals1[i][j]*vals2[k]
        elif len(comp1) == 1 and len(comp2) == 1:
            temp_vals = [[0,0,0],[0,0,0],[0,0,0]]
            for i in range(0,dim):
                for j in range(0,dim):
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


def check_vals(n, vals, gg=0):
    if vals[len(vals)-1] == " ":
        vals= vals[0:len(vals)-2]
    mass_string_vals = vals.split(" ")
    kek = re.findall(r'\d', vals)
    if len(kek) != len(mass_string_vals):
        print("обнаружено некорректное значение, перепроверьте входные данные")
        ask_for_choise(gg)
    else:
        if len(mass_string_vals) == dim**n:
            temp_vals =[0]
            if n == 1:
                temp_vals = input_data.shablon_1_comp
                c = 0
                for i in range(0, dim):
                    temp_vals[i] = int(mass_string_vals[c])
                    c += 1
            elif n == 2:
                temp_vals = input_data.shablon_2_comp
                c = 0
                for i in range(0, dim):
                    for j in range(0, dim):
                        temp_vals[i][j] = int(mass_string_vals[c])
                        c += 1
            elif n == 3:
                temp_vals = input_data.shablon_3_comp
                c = 0
                for i in range(0, dim):
                    for j in range(0, dim):
                        for k in range(0, dim):
                            temp_vals[i][j][k] = int(mass_string_vals[c])
                            c += 1
            return temp_vals
        else:
            print("кол-во элементов не соответствует ожидаемому для данного тензора")
            ask_for_choise(gg)





def ask_for_choise(gg=0):
    if gg == 0:
        choise = input("Введите номер задания которое необходимо решить (1,2,3,4)\nДля завершения работы используйте команду exit\n")
    else:
        choise = f'{gg}'

    if choise == '1':
        print("Хотите ввести свои данные (если нет, будут использоваться данные по умолчанию")
        conf = input("Y/N\n")
        if conf == 'Y':
            Aij_vals = input("Введите все значения тензора Aij в одну строку через пробел\n")
            Aij_vals = check_vals(2,Aij_vals,1)
            Aij_comps = ['i','j']
            Aij = {'comp': Aij_comps, 'vals': Aij_vals}
            Bk_vals = input("Введите все значения тензора Bk в одну строку через пробел\n")
            Bk_vals = check_vals(1, Bk_vals, 1)
            Bk_comps = ['k']
            Bk = {'comp': Bk_comps, 'vals': Bk_vals}
            print(f"Ответ: {t_mult(Aij, Bk)}")
            ask_for_choise()
        elif conf == 'N':
            print(f"Ответ: {t_mult(input_data.Aij, input_data.Bk)}")
            ask_for_choise()
        else:
            ask_for_choise(1)
    elif choise == '2':
        print("Хотите ввести свои данные (если нет, будут использоваться данные по умолчанию")
        conf = input("Y/\n")
        if conf == 'Y':
            Aij_vals = input("Введите все значения тензора Aij в одну строку через пробел\n")
            Aij_vals = check_vals(2, Aij_vals, 2)
            Aij_comps = ['i', 'j']
            Aij = {'comp': Aij_comps, 'vals': Aij_vals}
            Bj_vals = input("Введите все значения тензора Bj в одну строку через пробел\n")
            Bj_vals = check_vals(1, Bj_vals, 2)
            Bj_comps = ['j']
            Bj = {'comp': Bj_comps, 'vals': Bj_vals}
            first_part = t_mult(Aij, Bj)
            Akl_vals = input("Введите все значения тензора Akl в одну строку через пробел\n")
            Akl_vals = check_vals(2, Akl_vals, 2)
            Akl_comps = ['k', 'l']
            Akl = {'comp': Akl_comps, 'vals': Akl_vals}
            Bl_vals = input("Введите все значения тензора Bl в одну строку через пробел\n")
            Bl_vals = check_vals(1, Bl_vals, 2)
            Bl_comps = ['l']
            Bl = {'comp': Bl_comps, 'vals': Bl_vals}
            second_part = t_mult(Akl, Bl)
            print(f"Ответ: {t_sum(first_part, second_part)}")
            ask_for_choise()
        elif conf == 'N':
            first_part = t_mult(input_data.Aij, input_data.bj)
            second_part = t_mult(input_data.Akl, input_data.bl)
            print(f"Ответ: {t_sum(first_part, second_part)}")
            ask_for_choise()
        else:
            ask_for_choise(2)
    elif choise == '3':
        print("Хотите ввести свои данные (если нет, будут использоваться данные по умолчанию")
        conf = input("Y/N\n")
        if conf == 'Y':
            Tljl_vals = input("Введите все значения тензора Tljl в одну строку через пробел\n")
            Tljl_vals = check_vals(3, Tljl_vals, 3)
            Tljl_comps = ['l', 'j', 'l']
            Tljl = {'comp': Tljl_comps, 'vals': Tljl_vals}
            print(f"Ответ: {t_svertka(Tljl)}")
            ask_for_choise()
        elif conf == 'N':
            print(f"Ответ: {t_svertka(input_data.Tljl)}")
            ask_for_choise()
        else:
            ask_for_choise(3)
    elif choise == '4': #подтвердил расчётами на бумаге правильность работы, есть сомнение в правильности записи леви-чевиты
        print("Хотите ввести свои данные (если нет, будут использоваться данные по умолчанию")
        conf = input("Y/N\n")
        if conf == 'Y':
            Ajkl_vals = input("Введите все значения тензора Ajkl в одну строку через пробел\n")
            Ajkl_vals = check_vals(3, Ajkl_vals, 4)
            Ajkl_comps = ['j', 'k', 'l']
            Ajkl = {'comp': Ajkl_comps, 'vals': Ajkl_vals}
            Bjl_vals = input("Введите все значения тензора Bjl в одну строку через пробел\n")
            Bjl_vals = check_vals(2, Bjl_vals, 4)
            Bjl_comps = ['j', 'l']
            Bjl = {'comp': Bjl_comps, 'vals': Bjl_vals}
            first_part = t_mult(Ajkl, Bjl)
            Aj_vals = input("Введите все значения тензора Aj в одну строку через пробел\n")
            Aj_vals = check_vals(1, Aj_vals, 4)
            Aj_comps = ['j']
            Aj = {'comp': Aj_comps, 'vals': Aj_vals}
            sf = t_mult(input_data.eps, Aj)
            Bk_vals = input("Введите все значения тензора Bk в одну строку через пробел\n")
            Bk_vals = check_vals(1, Bk_vals, 4)
            Bk_comps = ['j']
            Bk = {'comp': Bk_comps, 'vals': Bk_vals}
            second_part = t_mult(sf, Bk)
            print(f"Ответ: {t_sum(first_part, second_part)}")
            ask_for_choise()
        elif conf == 'N':
            first_part = t_mult(input_data.Ajkl, input_data.Bjl)
            sf = t_mult(input_data.eps, input_data.aj)
            second_part = t_mult(sf, input_data.bk)
            print(f"Ответ: {t_sum(first_part, second_part)}")
            ask_for_choise()
        else:
            ask_for_choise(4)
    elif choise == 'exit':
        return 1
    else:
        print("Введен некорректный номер")
        ask_for_choise()


ask_for_choise()

