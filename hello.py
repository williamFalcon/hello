import numpy as np
from argparse import Argumentparser

parser = Argumentparser()
parser = parser.add_arguments('--number', default=0, type=int)
args = parser.parse_args()

print('hello world, ', args.number)
print(np.random.rand(10))
