import numpy as np

n = int(input())

A = np.array([list(map(int, input().split()))])
B = np.array([list(map(int, input().split()))])

AA = np.sort(A)
BB = np.sort(B)[::-1]


