
# Leveraging Frequency Based Salient Spatial Sound Localization to Improve 360° Video Saliency Prediction
### 2021, 17th International Conference on Machine Vision and Applications
[Mert Cokelek](https://scholar.google.com/citations?user=wTsdq_cAAAAJ&hl=en), [Nevrez Imamoglu](https://scholar.google.com/citations?user=VJgx61MAAAAJ&hl=en), [Cagri Ozcinar](https://scholar.google.com/citations?user=KHuC72wAAAAJ&hl=en), [Erkut Erdem](https://scholar.google.com/citations?user=eALwl74AAAAJ&hl=en), [Aykut Erdem](https://scholar.google.com/citations?user=-xA1_OAAAAAJ&hl=en)

<p align="center">
  <img src="sample.gif"/>
</p>

## **Overview**
Virtual and augmented reality (VR/AR) systems dramatically gained in popularity with various application areas such as gaming, social media, and communication. It is therefore a crucial task to have the knowhow to efficiently utilize, store or deliver 360◦ videos for end-users. Towards this aim, researchers have been developing deep neural network models for 360◦ multimedia processing and computer vision fields. In this line of work, an important research direction is to build models that can learn and predict the observers’ attention on 360◦ videos to obtain so-called saliency maps computationally. Although there are a few saliency models proposed for this purpose, these models generally consider only visual cues in video frames by neglecting audio cues from sound sources. In this study, an unsupervised frequency-based saliency model is presented for predicting the strength and location of saliency in spatial audio. The prediction of salient audio cues is then used as audio bias on the video saliency predictions of state-of-the-art models. Our experiments yield promising results and show that integrating the proposed spatial audio bias into the existing video saliency models consistently improves their performance.

## **Paper and Code**
[![Paper](pdflogo100.png)](http://www.mva-org.jp/Proceedings/2021/papers/O1-3-4.pdf) [![Code](githublogo.png)](https://github.com/MertCokelek/360-degree-SSSL)    

Please cite our work if you find it helpful for your research:

    @inproceedings{cokelek2021leveraging,
      title={Leveraging Frequency Based Salient Spatial Sound Localization to Improve 360° Video Saliency Prediction},
      author={Cokelek, Mert and Imamoglu, Nevrez and Ozcinar, Cagri and Erdem, Erkut and Erdem, Aykut},
      booktitle={2021 17th International Conference on Machine Vision and Applications (MVA)},
      pages={1--5},
      year={2021},
      organization={IEEE}
    }


## **Acknowledgements**
This work was supported in part by GEBIP 2018 Award of the Turkish Academy of Sciences to E. Erdem, BAGEP 2021 Award of the Science Academy to A. Erdem, and by TUBITAK-1001 Program Award No. 120E501.
