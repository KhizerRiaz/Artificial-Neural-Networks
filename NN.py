from matplotlib.font_manager import _Weight
from sklearn.model_selection import learning_curve
from vine import Thenable

# Neurons
# then
# neurons * weights = sum function
# Thenable
# apply activation function


# Activation Functions:

# 1:Step Function:
# output : 0 or 1
# if >0 then 1 , if <0 then 0

# 2:Sigmoid Function:
# output : in range [0 , 1]

# 3:Hyperbolic Tangent Function:
# output : in range [-1 , 1]


# We have a cost function with w dimensions and we want to find the optimal w weights such that the error is as small as possible
# We have to find the minima for the L(w) cost function:
# L(w)= loss function or cost function

# 1: Gradient Descent
# 2: Stochastic Gradient Descent
# 3: Meta-heuristic approaches (genetics algo etc)

# We have to calculate the partial derivative of the loss function in order to get the minima of the loss function

# Learning Rate:
# Defines how fast our algo will learn
# if it is too high : fast but not accurate
# if low : accurate but slow

# Momentum:
# we can escape local minimums with this
# high : helps to increase the speed , but it can overshoot the minimum
# low : cannot avoid local minimum and slows down the training

# Backpropagation calculaes the gradient of the error function(RMSE) with respect to _Weight

#
