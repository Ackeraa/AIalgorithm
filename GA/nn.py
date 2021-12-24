import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = nn.Linear(n_innput, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, n_hidden)
        self.predict

