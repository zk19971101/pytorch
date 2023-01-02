import torch
import torch.nn as nn
import torchvision


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.register_parameter('p1', torch.nn.Parameter(torch.zeros((2)), requires_grad=True))
        # self.register_parameter('p2', torch.zeros((3)))
        self.register_buffer('mean', torch.zeros((1)), persistent=True)
        model = Module1()
        self.add_module('model', model)
        # self.register_module("model1", model)
    def forward(self, inputs):
        return inputs


class Module1(nn.Module):
    def __init__(self):
        super(Module1, self).__init__()
        self.register_parameter('model1', torch.nn.Parameter(torch.ones((2)), requires_grad=True))

    def forward(self, inputs):
        return inputs


if __name__ == '__main__':
    net = Net()
    print('parameter', list(net.parameters()))
    print(net.state_dict())
    print(net.state_dict()['p1'])
    print('buffer', net.get_buffer('mean'))
    sub_model = net.get_submodule('model')
    for para in sub_model.state_dict().values():
        para.require_grad = False
    print('model', sub_model.state_dict())
    p1 = net.get_parameter('p1')
    print('p1', p1)