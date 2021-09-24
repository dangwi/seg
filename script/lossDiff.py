from matplotlib import pyplot as plt
import numpy as np

file_path = [
    '../save_model/hs_SRS_de_control/losses.csv',
    '../save_model/hs_SRS_de_noDense/losses.csv'
]

datas = [None,None]
for i,file in enumerate(file_path):
    with open(file, 'r') as fp:
        content = fp.read()

    lines = content.split('\n')[1:]
    data = []
    for line in lines:
        if line == '':  continue
        data.append(float(line.split(',')[1]))

    datas[i] = np.array(data[:10000])

diff = datas[0] - datas[1]

plt.plot(diff)
plt.show()