import argparse


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-test', type=bool, action='store_true')
    parser.add_argument('-data', type=str)

    # batch size
    # lr
    # optimizer

    # data_definition
    # args parameter: dataset name, batch_size, shuffle, num_worker
    parser.add_argument('-data', typ=str)
    parser.add_argument('-batch_size', typ=int)
    parser.add_argument('-num_worker', typ=int)

