from matplotlib import pyplot as plt

models = [
    'hs_SRS_snr_dense',
    'hs_SRS_snr_nodense'
]


for model in models:
    file_path = '../save_model/' + model + '/test/SSIM.csv'
    with open(file_path, 'r') as fp:
        SSIM_str = fp.read()

    ssims = []
    for line in SSIM_str.split('\n'):
        if line :   ssims.append(float(line))
    plt.plot(ssims, label=model)
plt.legend()
plt.show()