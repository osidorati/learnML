import torch
from torch.utils.data import Dataset, DataLoader


class MNISTDataset(Dataset):
    def __init__(self, *args, **kwargs):
        pass

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass


dataset = MNISTDataset(path=..., transforms=...)

DataLoader(dataset=dataset, batch_size=32, shuffle=True)


