
import torch
from torch import nn
import random

def mystery(a,b):
  return torch.tensor(a+3*b)

model = nn.Sequential(nn.Linear(2,1))

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

for i in range(1000):
  a = random.random()
  b = random.random()
  desiredOutput = mystery(a,b)

  output = model(torch.tensor(([a,b])))
  loss = criterion(output.squeeze(), desiredOutput)

  if (i % 100)==0:
    print(f"Loss: {loss.item()}")

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

a = 1.0
b = -1.0
output = model(torch.tensor([a,b]))
print(output.item())
mystery(a,b)

