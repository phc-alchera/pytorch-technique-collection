import os
import pandas as pd
from torch.utils.data import Dataset
from torch.utils.data.dataset import IterableDataset
from torchvision import datasets
import torchvision
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torchvision.io import read_image

# Map-style Datasets
# class CustomDataset(Dataset):
#     def __init__(self) -> None:
#         super().__init__()
#         pass

#     def __len__(self):
#         pass
    
#     def __getitem__(self, index) -> T_co:
#         return super().__getitem__(index)


# Iterable Dataset
# class CustomIterableDataset(IterableDataset):
#     def __init__(self) -> None:
#         super().__init__()
#         pass
    
#     def __iter__(self) -> Iterator[T_co]:
#         return super().__iter__()
#         pass


# Dataset Downloader
def DatasetDownloader(args, transformer) -> Dataset:
    torchvision_dataset = ['CIRFAR10', 'CIFAR100', 'MNIST', 'VOC', 'CelebA', 'CocoDetection', 'Cityscapes']
    assert args.data in torchvision_dataset
    dataset = torchvision.datasets.__dict__[args.data]

    NotImplemented
    return 0

