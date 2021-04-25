import data

def main():

    result_cultures = []

    S = float(input("Площадь, га: "))
    soil_type = input("Тип почвы: ")
    last_cult = input("Предыдущая культура: ")
    water_dist = float(input("Близость воды, км: "))
    city_dist = float(input("Близость населенного пункта, км: "))
    my_ph = float(input("Кислотность почвы, pH: "))

    # выбираем культуры под данную почву
    if (soil_type in data.SOIL.keys()):
        for i in data.SOIL[soil_type]:
            if (data.SOIL[soil_type][i]):
                # print(i)
                result_cultures.append(i)

    # сверяем совместимость культур с предыдущей; если не указано, пропускаем
    if (last_cult):
        tmp = []
        for i in range(len(data.PRED[last_cult])):
            if (data.PRED[last_cult][i] in result_cultures):
                # print(data.PRED[last_cult][i])
                tmp.append(data.PRED[last_cult][i])
        result_cultures.clear()
        result_cultures.extend(tmp)
        del tmp

    for i in result_cultures:
        if (my_ph >= data.pH[i][0] and my_ph <= data.pH[i][1]):
            print("Оптимальная культура - " + i)

main()