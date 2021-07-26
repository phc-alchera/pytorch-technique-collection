import os
import pandas as pd
import torch
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
# args parameter: dataset name, batch_size, shuffle, num_worker
# torchvision_dataset = ['CIRFAR10', 'CIFAR100', 'MNIST', 'VOC', 'CelebA', 'CocoDetection', 'Cityscapes']
def DatasetDownloader(args, former) -> [Dataset, dataloader]:
    torchvision_dataset = ['CIRFAR10', 'CIFAR100', 'MNIST', 'VOC', 'CelebA', 'CocoDetection', 'Cityscapes']
    assert args.data in torchvision_dataset
    exe_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'DATA')
    if os.path.exists(exe_path) is False:
        os.mkdir(exe_path)

    dataset = torchvision.datasets.__dict__[args.data](root=exe_path, train=args.train, download=True, transforme=former)

    dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=args.batch_size, shuffle=args.shuffle, num_workers=args.num_worker, pin_memory=True)
    
    return dataset, dataloader