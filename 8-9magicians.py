magicians = ['tctxc', 'asuka', 'shanjun', 'Lily', 'Jay', 'niniKing']
great_magicians = []

def show_magicians(magicians):
    """
    魔术师打印出来
    :param magicians: 需要打印的魔术师
    :return: 打印
    """
    for magician in magicians:
        print(magician)


def make_great(magicians, great_magicians):
    """
    给魔术师the great 的头衔
    :param magicians: 魔术师原列表
    :param great_magicians: 魔术师加头衔列表
    :return: 返回加头衔的列表
    """
    for magician in magicians:
        great_magician = 'the Great ' + magician
        great_magicians.append(great_magician)
    return great_magicians


make_great(magicians, great_magicians)  # 对魔术师列表加头衔


show_magicians(magicians)  # 展示原列表
print(magicians)  # 对比展示原列表

show_magicians(great_magicians)  # 展示加头衔列表