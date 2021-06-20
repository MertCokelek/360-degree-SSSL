import numpy as np
import glob
import os
import pdb
import py360convert
import imageio
import math
import scipy.ndimage as ndi
import argparse
from pathlib import Path
import cv2

SALIENCY_FOLDER = '/content/output/saliency/'


view_angle_degree = 5
view_angle_radian = math.radians(view_angle_degree)
r = 300/np.pi
gau_filter = int(np.round(view_angle_radian*r))


def saliency(fixmap_input):

    (h, w) = fixmap_input.shape
    equi_output = np.zeros((h,w,3))

    for shf in range(0, 360, 10):
        fixmap_l = fixmap_input[:, 0:int(shf/360*w)]
        fixmap_r = fixmap_input[:, int(shf/360*w):w]
        fixmap = np.concatenate((fixmap_r, fixmap_l), axis=1)
             
        fixmap[fixmap>0] = 255
        fixmap = np.expand_dims(fixmap, axis=2)
        fixmap = np.concatenate((fixmap,fixmap,fixmap), axis=2)
        cube_list   = py360convert.e2c(fixmap, cube_format='list')

        cube_list_b = cube_list
                
        for c_key in range(6):
            cimg = cube_list[c_key]
            blur = ndi.gaussian_filter(cimg , gau_filter) 
            cube_list_b[c_key] = blur

        equi_b = py360convert.c2e(cube_list, h, w,  cube_format='list')
        equi_b_l = equi_b[:, 0:w-int(shf/360*w), :]
        equi_b_r = equi_b[:, w-int(shf/360*w):w, :]
        equi_b = np.concatenate((equi_b_r, equi_b_l), axis=1)
        
        equi_output =  equi_output + equi_b 
    equi_output = equi_output/36.0
    equi_output = equi_output/equi_output.max()

    return equi_output    

def generate_saliencymap(fixation_maps, segment_no, output_folder):
    print(":::...Saliency map estimation")

    # global_saliency_map = np.ze
    # create a folder for fixation
    salmap_folder = os.path.join(SALIENCY_FOLDER, output_folder)
    Path(salmap_folder).mkdir(parents=True, exist_ok=True)

    for seg_count, fixmap in enumerate(fixation_maps):
        saliency_map = saliency(cv2.imread(os.path.join('/content/output/fixations/ambix/8feS1rNYEbg', fixmap), 0))
        cv2.imwrite(os.path.join(salmap_folder,'salmap_f_' + str(seg_count) + '.png'), saliency_map)


if __name__ == '__main__':
    generate_saliencymap(os.listdir('/content/output/fixations/ambix/8feS1rNYEbg'), 1, 'ambix/8feS1rNYEbg/')