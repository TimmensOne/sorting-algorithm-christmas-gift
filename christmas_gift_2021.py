import random

gift_list_example = [(1, 'Bernd'), (2, 'Timon'), (3, 'Bernd'), (4, 'Bernd'),
                        (5, 'Lisa'), (6, 'Justin'), (7, 'Lisa'), (8, 'Lisa'), 
                        (9, 'Timon'), (10, 'Timon'), (11, 'Timon'), (12, 'Timon'), 
                        (13, 'Timon'), (14, 'Justin'), (15, 'Lisa'), (16, 'Timon'), 
                        (17, 'Justin'), (18, 'Justin'), (19, 'Justin'), (20, 'Justin'),
                        (21, 'Justin'), (22, 'Justin'), (23, 'Justin'), (24, 'Justin'),
                        (25, 'Bernd'), (26, 'Timon'), (27, 'Justin'), (28, 'Justin'),
                        (29, 'Justin')]
gift_name_list = [e[1] for e in gift_list_example]
name_list = ['Timon', 'Justin', 'Lisa', 'Bernd']
count_list = []
probability_list = []


def count_gift_per_person(gift_list):
    count = 0
    for i in range(len(name_list)):
        for j in gift_list:
            if(name_list[i] == j[1]):
                count += 1
        single_tup = (count, name_list[i])
        count_list.append(single_tup)
        count = 0
    # highest component at the beginning
    count_list.sort(reverse=True)


def get_interval():
    intervals = []
    for i in range(len(count_list)):
        # attention if count_list-1 = 0
        f = 1/((count_list[i][0])-1)
        single_tup = (count_list[i][0], f, count_list[i][1])
        intervals.append(single_tup)
    return intervals


def set_gift_sequence(interval_info):
    dist_list = []
    gift_location = 0
    gift_name = ''
    for i in range(len(interval_info)):
        gift_name = interval_info[i][2]
        count = int(interval_info[i][0])
        for j in range(count):
            dist_tuple = (gift_location, gift_name)
            dist_list.append(dist_tuple)
            gift_location += float(interval_info[i][1])
        gift_location = 0
    dist_list.sort()
    # check double turn
    for i in range(len(dist_list)-1):
        if(dist_list[i][1] == dist_list[i+1][1]):
            temp_tuple = dist_list[i+1]
            dist_list[i+1] = dist_list[i+2]
            dist_list[i+2] = temp_tuple
    return dist_list
    

def create_id_list():
    id_list = []
    for i in name_list:
        ids = []
        for j in gift_list_example:
            if(i == j[1]):
                ids.append(j[0])
        random.shuffle(ids)
        single_tuple = (i, ids)
        id_list.append(single_tuple)
    return id_list


def create_distribution_list():
    count_gift_per_person(gift_list_example)
    distribution_order = set_gift_sequence(get_interval())
    id_list = create_id_list()
    final_list = []
    for i in distribution_order:
        for j in range(len(id_list)):
            if(i[1] == id_list[j][0]):
                single_tuple = (i[1], id_list[j][1][0])
                del id_list[j][1][0]
                final_list.append(single_tuple)
    print(final_list)


create_distribution_list()
