# Remote Biosensing

[![GitHub license](https://img.shields.io/github/license/remotebiosensing/rppg)](https://github.com/remotebiosensing/rppg/blob/main/LICENSE)
[![Slack](https://img.shields.io/badge/Chat-Slack-red)](https://join.slack.com/t/remobebiosensing/shared_invite/zt-1u3kjfhf9-xWw_XQ8hGd7qFZymCSzUtg)

Remote Biosensing (`rPPG`) is a framework for non-contact algorithms for remote photoplethysmography (rPPG) and for
non-invasive blood pressure measurement algorithms (CNIBP) technology.
We aim to implement a deep learning-based remote photoplethysmography (rPPG) model and continuous non-invasive blood
pressure (CNIBP) using PyTorch.

### Quick Start with our examples

- #### rPPG( remote PPG) models
| Implementation |       model       |                                             example                                              |                                                config                                                 |                                           paper                                            | 
|:--------------:|:-----------------:|:------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------:|
|      :o:       |     DeepPhys      | [example](https://github.com/remotebiosensing/rppg/blob/main/rppg/examples/physnet_ubfc_ubfc.py) | [config](https://github.com/remotebiosensing/rppg/blob/main/rppg/configs/FIT_DEEPPHYS_UBFC_UBFC.yaml) |                         [paper](https://arxiv.org/abs/1805.07888)                          |
|      :x:       |       MTTS        |                                             example                                              |                                                config                                                 | [paper](https://papers.nips.cc/paper/2020/file/e1228be46de6a0234ac22ded31417bc7-Paper.pdf) |
|      :o:       |      PhysNet      | [example](https://github.com/remotebiosensing/rppg/blob/main/rppg/examples/physnet_ubfc_ubfc.py) | [config](https://github.com/remotebiosensing/rppg/blob/main/rppg/configs/FIT_PHYSNET_UBFC_UBFC.yaml)  |                         [paper](https://arxiv.org/abs/1905.02419)                          |
|      :x:       | 2D PhysNet + LSTM |                                             example                                              |                                                config                                                 |                         [paper](https://arxiv.org/abs/1905.02419)                          |
 |      :o:       |      APNETv2      | [example](https://github.com/remotebiosensing/rppg/blob/main/rppg/examples/apnetv2_ubfc_ubfc.py) |                                                config                                                 |                                           paper                                            |

- #### rPPG datasets
| Implementation |  Dataset   | DIFF | CONT | example | config | link |
|:--------------:|:----------:|:----:|:----:|:-------:|:------:|:----:|
|      :x:       |    ALL     | :o:  | :o:  | example | config | link |
|      :o:       |    UBFC    | :o:  | :o:  | example | config | link |
|      :o:       |  COHFACE   | :o:  | :o:  | example | config | link |
|      :o:       |    LGGI    | :o:  | :o:  | example | config | link |
|      :o:       | MAHNOB_HCI | :o:  | :o:  | example | config | link |
|      :o:       |  VIPL-HR   | :o:  | :o:  | example | config | link |
|      :o:       |    PURE    | :o:  | :o:  | example | config | link |
|      :o:       |    V4V     | :o:  | :o:  | example | config | link |




- #### CNIBP (Continuous non-invasive blood pressure)
- [ ] PP-Net exmaple [paper](https://ieeexplore.ieee.org/document/9082808)

### Documentation(TBD)

### Performance Comparison

- rPPG

| MODEL | Train/val Dataset | Test Dataset | lr  | MAE | RMSE | MAPE | r   |
|-------|-------------------|--------------|-----|-----|------|------|-----|

- CNIBP

## Community

Our community is eagerly waiting for researchers and developers interested in non-contact/non-invasive algorithm
research and development
to [join](https://join.slack.com/t/remobebiosensing/shared_invite/zt-1u3kjfhf9-xWw_XQ8hGd7qFZymCSzUtg) us.

<a href="https://github.com/remotebiosensing/rppg/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=remotebiosensing/rppg" />
</a>

## Contacts

- Dae Yeol Kim, spicyyeol@gmail.com
- Kwangkee Lee, kwangkeelee@gmail.com

## Funding

This work was partly supported by the ICT R&D program of
MSIP/IITP. [2021(2021-0-00900), Adaptive Federated Learning in Dynamic Heterogeneous Environment]

