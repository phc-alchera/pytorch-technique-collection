import argparse

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-test', type=bool, action='store_true')