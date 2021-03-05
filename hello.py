import numpy as np
from argparse import ArgumentParser
import torch

parser = ArgumentParser()
parser.add_argument('--number', default=0, type=int)
parser.add_argument('--food_item', default='burgers', type=str)
args = parser.parse_args()

print('-' * 50)
print('hello world')
print(f'There are {torch.cuda.device_count()} GPUs on this machine')
print('-' * 50)
print(f'I want to eat: {args.number} {args.food_item}')
print('i can run any machine learning library like numpy, pytorch lightning, sklearn pytorch, keras, tensorflow')
print(torch.rand(1), np.random.rand(1))
