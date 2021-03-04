import numpy as np
from argparse import Argumentparser
import torch

parser = Argumentparser()
parser = parser.add_arguments('--number', default=0, type=int)
parser = parser.add_arguments('--food_item', default='burgers', type=str)
args = parser.parse_args()

print('hello world')
print(f'I want to eat: {args.number} {args.food_item}')
print('i can run any machine learning library like numpy, pytorch lightning, sklearn pytorch, keras, tensorflow')
print(torch.rand(1), np.random.rand(1))
