import tifffile
import numpy as np

for i in range(1, 81):
    if i==68: continue

    path = f'../dataset/highSNR/mask/{i}.tif'

    tif = tifffile.TiffFile(path)
    tif_np = tif.asarray()
    dst_np = np.array([tif_np,tif_np,tif_np,tif_np,tif_np])

    # print(dst_np.shape)
    # print(tif_np.shape)
    tifffile.imsave(path, dst_np)