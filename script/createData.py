with open("../data/hs_SRS_snr.csv", 'w') as fp:
    fp.write('path_signal,path_target' + '\n')
    for i in range(1, 41):
        fp.write('/root/train/Low_SNR/'+str(i)+'.tif,' + \
            '/root/train/High_SNR/'+str(i)+'.tif' + '\n')
        
    fp.close()

