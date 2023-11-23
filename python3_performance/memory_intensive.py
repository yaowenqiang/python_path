@profile
def create_big_list():
    return 10_100_100 * [0]

@profile
def create_hub_list():
    return 30_100_100 * [0]

create_big_list()
create_hub_list()

