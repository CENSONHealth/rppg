import numpy as np
import torch
import torchvision.transforms as transforms
from torch.utils.data import Dataset


class PhysNetDataset(Dataset):
    def __init__(self, video_data, label_data, target_length):
        # assert np.abs(1.0 - np.max(video_data)) < 0.2, 'Video data is not normalized 0~1'
        # assert np.abs(np.min(video_data) - 0.0) < 0.2, 'Video data is not normalized 0~1'
        self.video_data = (video_data - 0.5) * 2
        self.label_data = label_data

    def __getitem__(self, index):
        if torch.is_tensor(index):
            index = index.tolist()

        video_data = torch.tensor(np.transpose(self.video_data[index], (3, 0, 1, 2)), dtype=torch.float32)
        label_data = torch.tensor(self.label_data[index], dtype=torch.float32)

        if torch.cuda.is_available():
            video_data = video_data.to('cuda')
            label_data = label_data.to('cuda')

        # label_data = (label_data - torch.mean(label_data)) / torch.std(label_data)

        return video_data, label_data

    def __len__(self):
        return len(self.label_data)
