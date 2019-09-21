import torch
import torch.nn as nn #modules
import torch.optim as optim #auto-optimizer

# Tensor, express all 3+ D elements
# a = torch.empty(3,3) #random 3x3
# b = torch.zeros(3,3) # all zero 3x3
# c = torch.ones(3,3) # all one 3x3
# d = torch.rand(3,3) # random 3x3


# # specify value type
# e = torch.ones(3, 3, dtype = torch.int64)
# f = torch.ones(3, 3, dtype = torch.float32)

# # specify values
# g = torch.Tensor([[3,3,3],[2,1,2],[0,0,0]])
# g1 = torch.FloatTensor([[3,3,3],[2,1,2],[0,0,0]])
# g2 = torch.LongTensor([[3,3,3],[2,1,2],[0,0,0]])
# # print(g1)
# # print(g2)

# # operation on tensors
# # print(c+d)
# # add a dimention at specific dimention
# d = d.unsqueeze(2).expand(3,3,5) #add to the 3rd dimention, repeat 5x
# print(d)

# auto grad


# ----------------- manual module ------------------
# lr = 0.5 #learning rate parameter
# x = torch.rand(5, 1)
# y = torch.rand(10,1)
# w = torch.rand(10, 5, requires_grad = True)
# y_hat = torch.mm(w,x) # matrix multiplication
# L = 0.5 * sum((y-y_hat) * (y-y_hat)) / 10 # lost function
# L.backward() # knowing x was cal from w

# with torch.no_grad():
# 	print(w.grad)
# 	w = w - lr * w.grad #算梯度
# --------------------------------------------------

# ------------------ with nn module ----------------
linear = nn.Linear(5,10)

lr = 0.05 #learning rate parameter

opt = optim.Adam(linear.parameters(), lr = lr)
 
# it's linear, so just array
x = torch.rand(5) 
y = torch.rand(10)

for i in range(10):
	opt.zero_grad() #梯度清零
	y_hat = linear(x) #forward function, could be user-defined function
	L = 0.5 * sum((y-y_hat) * (y-y_hat)) / 10 # lost function

	L.backward(retain_graph = True) #算梯度
	opt.step() # 更新权重 same as "with troch.no_grad: w = w - lr * w.grad"
	print(L.item())


	# conclution:
	# define a forward, which is a function, from input to output,
	# then, calc the lost, then cal the 梯度(backward)
	# update weight
	
# --------------------------------------------------









