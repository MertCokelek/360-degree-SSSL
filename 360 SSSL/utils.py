import os
import scipy.io
import scipy
import numpy as np
import pandas as pd


def get_saliency_ratios(path):
    saliency_mat = os.path.join(path)
    sal = scipy.io.loadmat(saliency_mat, verify_compressed_data_integrity=False)['audio_in_seconds']
    sal = sal.reshape(-1, 6)

    p1 = sal[:,0]
    n1 = sal[:,1]
    p2 = sal[:,2]
    n2 = sal[:,3]
    p3 = sal[:,4]
    n3 = sal[:,5]

    ch1_seconds = p1 - n1
    ch2_seconds = p2 - n2
    ch3_seconds = p3 - n3

    return ch1_seconds, ch2_seconds, ch3_seconds


def to_unit_vector(v):
    return v / np.linalg.norm(v)


def xyz2uv(P):
    unit_vec = P
    dx, dy, dz = -unit_vec[0], unit_vec[1], unit_vec[2]
    u = np.arctan2(dx, dz) / (2 * np.pi) + 0.5
    v = 0.5 - np.arcsin(dy) / np.pi
    return u, v



def uv_to_csv(saliencies_as_UV_form, out_path, fps):
    pred = pd.DataFrame(saliencies_as_UV_form)
    pred.insert(0, "time", range(pred.shape[0]))
    divisor = 48000/fps
    # for sec in range(25):
    #     pred = pred.drop(pred[(pred['time'] > (sec-1)*48000)  & (pred['time'] < sec * 48000 - 24000)].index)
    # pred['time'] /= 48000
    pred['time'] /= divisor
    pred = pred.rename(columns={0: "2dmu", 1: "2dmv"})
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    pred.to_csv("{}/pred.csv".format(out_path), index=False)