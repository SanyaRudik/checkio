"""
# Подручные дроны Софии - это не какие-то тупые, бесчувственные железяки. Более того - они умеют дружить. На самом деле,
#  они уже даже делают свою социальную сеть, только для дронов! София вытащила оттуда данные о всех связях между дронами
#   и теперь хочет изучить эти взаимосвязи подробнее.
# Дан массив прямых связей между дронами - кто с кем дружит. Каждая такая связь представлена, как строка с двумя именами
#  разделеными дефисом. Для примера: "dr101-mr99" означает что dr101 и mr99 дружат между собой. Кроме этого даны два
#   имени.
#   Попробуйте определить, связаны ли они через других дронов, вне зависимости от глубины этих связей. Для примера:
#   Если у  двух дронов есть общий друг или друзья, у которых есть общий друг и так далее.
# Давайте рассмотрим примеры:
# scout2 и scout3 оба дружат с scout1, так что они связаны. super и scout2 связаны между собой через sscout,
#  scout4 и scout1. Но вот dr101 и sscout никак не взаимосвязаны друг с другом.
# Ввод: Три аргумента: информация о друзьях, как кортеж (tuple) строк (str); первое имя, как строка (str);
# второе имя, как строка (str).
# Вывод: Связаны ли указанные дроны между собой, как булево значение (bool).
# Предусловие: len(network) ≤ 45
# если "name1-name2" в network, то "name2-name1" не в network
# 3 ≤ len(drone_name) ≤ 6
# first_name и second_name всегда в network.
"""

def check_connection(network, first, second):
    for i in network:
        if (first in i) and (second in i):
            # print('FOUND')
            return True
        if (first == i.split('-')[0]) or (first == i.split('-')[1]):
            if check_connection(list(filter(lambda kv: kv != i, network)), i.replace('-', '').replace(first, ''),
                                second):
                return True
    return False


if __name__ == '__main__':
    print(check_connection(("night-nikola",), "nikola", "night"))

    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout4", "scout5-scout1", "scout2-scout1",
         "scout3-scout1", "scout4-sscout",
         "sscout-super"),
        "scout2", "scout3"))
    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout3-scout1", "scout1-scout2",
         "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2"))
    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout"))
