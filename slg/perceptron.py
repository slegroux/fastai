#!/usr/bin/env pythonw
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from IPython import embed

def generate_data():
    n_samples = 100
    mean1 = [2,2]
    cov1 = [[1,0],[0,1]]
    mean2 = [-2,-2]
    cov2 = [[1,0],[0,1]]
    X1 = np.random.multivariate_normal(mean1, cov1, n_samples)
    y1 = np.ones(n_samples)
    X2 = np.random.multivariate_normal(mean2, cov2, n_samples)
    y2 = np.zeros(n_samples)
    X = np.concatenate((X1,X2))
    y = np.concatenate((y1,y2))
    return (torch.tensor(X).float(),torch.tensor(y).float().unsqueeze(1))


class Perceptron(nn.Module):
    def __init__(self, input_dim):
        # input_dim: n_in_features
        super(Perceptron, self).__init__()
        self.fc1 = nn.Linear(input_dim,1)
    
    def forward(self, x_in):
        # x_in: (batch,n_in_features)
        return(torch.sigmoid(self.fc1(x_in)))


def main():
    n_epochs = 10
    n_batches = 30
    X, y = generate_data()
    p = Perceptron(2)
    optimizer = optim.Adam(params=p.parameters(), lr=0.01)
    bce_loss = nn.BCELoss()
    losses = []

    for epoch in range(n_epochs):
        for batch in range(n_batches):
            p.zero_grad()
            y_pred = p(X)
            loss = bce_loss(y_pred,y)
            loss.backward()
            optimizer.step()
            loss_value = loss.item()
            losses.append(loss_value)
            print(loss_value)






if __name__ == '__main__':
    main()