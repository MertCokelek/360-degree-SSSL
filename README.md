# 360-degree-SSSL
This repository is the official implementation of the MVA2021 paper: [Leveraging Frequency Based Salient Spatial Sound Localization to Improve 360◦ Video Saliency Prediction](http://www.mva-org.jp/Proceedings/2021/papers/O1-3-4.pdf). 

## Dependencies
1. **GNU Octave-5.2.0**
3. **Python 3.6 (see `requirements.txt` for required packages.)**
4. **FFMPEG**

## Requirements
```setup
python3 -m pip install -r requirements.txt
```

## 3D Mel-Cepstrum-Based Spectral Residual Saliency 
```
octave -W  MCSR/Main.m
```
## Produce saliency-time curves for each channel
```
python3 ambisonic_saliency/main.py <<path containing *_saliency.mat>> <<output path>> 
```

## Get Audio Saliency Maps
```
python3 uv_visualization/fixmap2salmap.py -i ambisonic_saliency_predictions/pred_<<video name>> -o <<folder containing videos/video name/>> -r <<output height x width>>
```

## (Optional) Fuse with existing (audio-)visual saliency model predictions
```
python3 fusion.py
```
