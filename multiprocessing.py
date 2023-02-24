import itertools
from multiprocessing import Pool
ip_list = []


def append_to_list(params):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    ip_list.append(f'{a}.{b}.{c}.{d}')


print('starting')
# processes = [Process(target=append_to_list)]
i = range(10)
j = range(10)
k = range(10)
l = range(10)
paramlist = list(itertools.product(i, j, k, l))

with Pool(10) as pool:

# Distribute the parameter sets evenly across the cores
    res = pool.map(append_to_list, paramlist)
    print(ip_list)
    print('done')
