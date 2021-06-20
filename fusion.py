import numpy as np
import sys
import os


def N(image):
    from scipy.ndimage.filters import maximum_filter
    M = 8.
    image = cv2.convertScaleAbs(image, alpha=M/image.max(), beta=0.)
    w,h = image.shape
    maxima = maximum_filter(image, size=(w/10,h/1))
    maxima = (image == maxima)
    mnum = maxima.sum()
    maxima = np.multiply(maxima, image)
    mbar = float(maxima.sum()) / mnum
    return image * (M-mbar)**2

def normalize_1(s_map):
	norm_s_map = (s_map - np.min(s_map)) / (s_map.max() - s_map.min())
	return 2*norm_s_map -1 

def normalize_map(s_map):
	norm_s_map = (s_map - np.min(s_map)) / (s_map.max() - s_map.min())
	return norm_s_map    

def fuse(out, video_name, frame):

    pred_audio_saliency = cv2.imread('/content/drive/MyDrive/output/audio_saliency_enlarged_new/{}/salmap_f_{}.png'.format(video_name, frame), 0)
    pred_mms = cv2.imread('/content/drive/MyDrive/related_work_predictions/MMS/mono_-{}/{}.png'.format(video_name, frame), 0)
    pred_mms = cv2.resize(pred_mms, (384, 192))

    output_path0 = out + '/{}/'.format("MMS") + video_name + '/{}'.format("itti")
    output_path1 = out + '/{}/'.format("MMS") + video_name + '/{}'.format("expo1")
    output_path2 = out + '/{}/'.format("MMS") + video_name + '/{}'.format("expo2")
    output_path3 = out + '/{}/'.format("MMS") + video_name + '/{}'.format("avg")

    if not os.path.exists(output_path0):
        os.makedirs(output_path0)
    if not os.path.exists(output_path1):
        os.makedirs(output_path1)
    if not os.path.exists(output_path2):
        os.makedirs(output_path2)
    if not os.path.exists(output_path3):
        os.makedirs(output_path3)

    pred_itti = 0.5*N(pred_mms) + 0.5*N(pred_audio_saliency)
    pred_expo1 = pred_mms * np.exp(normalize_1(pred_audio_saliency))
    pred_expo2 = pred_mms * np.exp(normalize_map(pred_audio_saliency))
    pred_avg = 0.5 * pred_mms + 0.5 * pred_audio_saliency

    p0 = output_path0 + '/{:05d}.png'.format(frame)
    p1 = output_path1 + '/{:05d}.png'.format(frame)
    p2 = output_path2 + '/{:05d}.png'.format(frame)
    p3 = output_path3 + '/{:05d}.png'.format(frame)

    cv2.imwrite(p0, pred_itti)
    cv2.imwrite(p1, pred_expo1)
    cv2.imwrite(p2, pred_expo2)
    cv2.imwrite(p3, pred_avg)