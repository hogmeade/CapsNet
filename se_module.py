from torch import nn


class SELayer(nn.Module):
    def __init__(self, channel, reduction=16):
        super(SELayer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        ).cuda()

    def forward(self, x):
        b, c, _, _ = x.size() # 128, 256, 6, 6
        y = self.avg_pool(x).view(b, c) # 128, 256
        y = self.fc(y).view(b, c, 1, 1) # 128, 256, 1, 1
        return x * y.expand_as(x)

class SELayer8x8(nn.Module):
    def __init__(self, channel, reduction=4):
        super(SELayer8x8, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        ).cuda()

    def forward(self, x):
        b, c, d, _, _ = x.size() # 8, 8, 6
        y = self.avg_pool(x).view(b, c, d) 
        y = self.fc(y).view(b, c, d, 1, 1)
        return x * y.expand_as(x)

class SELayer10x16(nn.Module):
    def __init__(self, channel, reduction=32):
        super(SELayer10x16, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        ).cuda()

    def forward(self, x):
        b, c, _, _ = x.size() # 128, 1152, 10, 16
        y = self.avg_pool(x).view(b, c) # 128, 1152
        y = self.fc(y).view(b, c, 1, 1) # 128, 1152, 1, 1
        return x * y.expand_as(x)

class SELayer1x8(nn.Module):
    def __init__(self, channel, reduction=4):
        super(SELayer1x8, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
            nn.Linear(channel, channel // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channel // reduction, channel, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size() # 128, 1152, 10, 16
        y = self.avg_pool(x).view(b, c) # 128, 1152
        y = self.fc(y).view(b, c, 1, 1) # 128, 1152, 1, 1
        return x * y.expand_as(x)