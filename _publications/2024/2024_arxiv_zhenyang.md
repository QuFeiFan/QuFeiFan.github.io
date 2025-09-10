---
title:          "Point Resampling and Ray Transformation Aid to Editable NeRF Models"
date:           2024-05-06 00:01:00 +0800
selected:       false
pub:            "arXiv preprint"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
# pub_last:       ' <span class="badge badge-pill badge-publication badge-success">Spotlight</span>'
pub_date:       "2024"

abstract: >-
  In NeRF-aided editing tasks, object movement presents difficulties in supervision generation due to the introduction of variability in object positions. Moreover, the removal operations of certain scene objects often lead to empty regions, presenting challenges for NeRF models in inpainting them effectively. We propose an implicit ray transformation strategy, allowing for direct manipulation of the 3D object's pose by operating on the neural-point in NeRF rays. To address the challenge of inpainting potential empty regions, we present a plug-and-play inpainting module, dubbed differentiable neural-point resampling (DNR), which interpolates those regions in 3D space at the original ray locations within the implicit space, thereby facilitating object removal & scene inpainting tasks. Importantly, employing DNR effectively narrows the gap between ground truth and predicted implicit features, potentially increasing the mutual information (MI) of the features across rays. Then, we leverage DNR and ray transformation to construct a point-based editable NeRF pipeline PR^2T-NeRF. Results primarily evaluated on 3D object removal & inpainting tasks indicate that our pipeline achieves state-of-the-art performance. In addition, our pipeline supports high-quality rendering visualization for diverse editing operations without necessitating extra supervision.
cover:          assets/images/covers/2024_arxiv_zhenyang.png
authors:
  - Zhenyang Li
  - Zilong Chen
  - Feifan Qu 
  - Mingqing Wang
  - Yizhou Zhao
  - Kai Zhang
  - Yifan Peng
links:
  # Code: https://github.com/zhou-wb/3D-HoloNet
  Paper: https://arxiv.org/abs/2405.07306
---
