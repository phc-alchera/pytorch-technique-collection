import os
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.dataset import IterableDataset
from torchvision import datasets
import torchvision
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torchvision.io import read_image


# Map-style Datasets
class CustomDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
        pass

    def __len__(self):
        pass
    
    def __getitem__(self, index):
        return super().__getitem__(index)


# Iterable Dataset
class CustomIterableDataset(IterableDataset):
    def __init__(self):
        super().__init__()
        pass
    
    def __iter__(self):
        return super().__iter__()
        pass

    def __getitem__(self, index):
        return super().__getitem__(index)


# load dataset
def load(args, mode: str, **kwargs) -> [Dataset, DataLoader]:
    if mode == 'download' and "former" in kwargs.keys():
        return dataset_downloader(args, kwargs["former"])
    elif mode == 'db' and "former" in kwargs.keys():
        NotImplemented
    elif mode == 'ICDAR 2015' and "former" in kwargs.keys():
        NotImplemented
    NotImplemented


# Dataset Downloader
# args parameter: dataset name, batch_size, shuffle, num_worker
def dataset_downloader(args, former: str) -> [Dataset, DataLoader]:
    torchvision_dataset = ['CIFAR10', 'CIFAR100', 'MNIST', 'VOC', 'CelebA', 'CocoDetection', 'Cityscapes']
    assert args.data in torchvision_dataset
    exe_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'DATA')
    if os.path.exists(exe_path) is False:
        os.mkdir(exe_path)

    dataset = torchvision.datasets.__dict__[args.data](root=exe_path, train=args.train,
                                                       download=True, transform=former)

    data_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=args.batch_size, shuffle=args.shuffle,
                                              num_workers=args.num_worker, pin_memory=True)
    
    return dataset, data_loader


# test
def simulate():
    class Test:
        def __init__(self):
            self.data = 'COCO'
            self.train = True
            self.batch_size = 2
            self.shuffle = False
            self.num_worker = 0
    args = Test()
    mode = 'download'
    return args, mode


a, m = simulate()
former = None
load(a, m, former=former)
