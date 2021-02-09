import random

presents_list_example = [(1, 'Björn'), (2, 'Timon'), (3, 'Björn'), (4, 'Björn'),
                        (5, 'Manuela'), (6, 'Julian'), (7, 'Manuela'), (8, 'Manuela'), 
                        (9, 'Timon'), (10, 'Timon'), (11, 'Timon'), (12, 'Timon'), 
                        (13, 'Timon'), (14, 'Julian'), (15, 'Manuela'), (16, 'Timon'), 
                        (17, 'Julian'), (18, 'Julian'), (19, 'Julian'), (20, 'Julian'),
                        (21, 'Julian'), (22, 'Julian'), (23, 'Julian'), (24, 'Julian'),
                        (25, 'Björn'), (26, 'Timon'), (27, 'Julian'), (28, 'Julian'),
                        (29, 'Julian')]
presents_name_list = ['Björn', 'Timon', 'Björn', 'Björn', 'Manuela', 'Julian', 'Manuela', 'Manuela', 'Timon', 
                    'Timon', 'Timon', 'Timon', 'Timon', 'Julian', 'Manuela', 'Timon', 'Julian', 'Julian', 
                    'Julian', 'Julian', 'Julian', 'Julian', 'Julian', 'Julian', 'Björn', 'Timon', 'Julian',
                    'Julian', 'Julian']
name_list = ['Timon', 'Julian', 'Manuela', 'Björn']
count_list = []
probability_list = []


def count_presents_per_person(presents_list):
    count = 0
    for i in range(len(name_list)):
        for j in presents_list:
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


def set_present_sequence(interval_info):
    dist_list = []
    present_location = 0
    present_name = ''
    for i in range(len(interval_info)):
        present_name = interval_info[i][2]
        count = int(interval_info[i][0])
        for j in range(count):
            dist_tuple = (present_location, present_name)
            dist_list.append(dist_tuple)
            present_location += float(interval_info[i][1])
        present_location = 0
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
        for j in presents_list_example:
            if(i == j[1]):
                ids.append(j[0])
        random.shuffle(ids)
        single_tuple = (i, ids)
        id_list.append(single_tuple)
    return id_list


def create_distribution_list():
    count_presents_per_person(presents_list_example)
    distribution_order = set_present_sequence(get_interval())
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