import numpy as np
import os
import sys
from utils import *


def work(video_path, output_path, fps):

    if not os.path.exists(os.path.join(output_path, 'ambix')):
        os.makedirs(os.path.join(output_path, 'ambix')

    video_name = video_path.split('/')[-1]

    saliency_mat_path = os.path.join(video_path, '{}_saliency.mat'.format(video_name))
    #print("FPS:", fps, "Path:", saliency_mat_path)

    ch1_seconds, ch2_seconds, ch3_seconds = get_saliency_ratios(saliency_mat_path)    
    directional_saliencies = np.asarray([ch1_seconds, ch2_seconds, ch3_seconds]).T

    saliencies_as_unit_vector = np.apply_along_axis(to_unit_vector, 1, directional_saliencies)

    saliencies_as_UV_form = np.apply_along_axis(xyz2uv, 1, saliencies_as_unit_vector)
    uv_to_csv(saliencies_as_UV_form, os.path.join(output_path, 'ambix', video_name), fps)

if __name__ == '__main__':
    work(sys.argv[1], sys.argv[2], int(sys.argv[3]))