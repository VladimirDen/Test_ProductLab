def check_relation(net, first, second):
    net_list = list(net)
    net_set_1 = set()
    net_set_2 = set()
    first_list_1 = []
    first_list_2 = []
    count = len(net)

    while count > 0:
        for i in net:
            if first in i and second in i:
                return True
            if first in i:
                first_list_1.append(i)
                net_list.remove(i)
            if second in i:
                first_list_2.append(i)
                net_list.remove(i)

        for i in first_list_1:
            for j in i:
                if j is not first:
                    net_set_1.add(j)

        for i in first_list_2:
            for j in i:
                if j is not second:
                    net_set_2.add(j)

        crossing = net_set_1 & net_set_2
        if len(crossing) >= 1:
            return True

        first = list(net_set_1)[0]
        second = list(net_set_2)[0]
        net = net_list
        net_set_1.discard(first)
        net_set_2.discard(second)
        count -= 1

    return False


if __name__ == '__main__':

    net = (

        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
