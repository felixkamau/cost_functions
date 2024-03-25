import numpy as np


# we have correct values of x and y and
#  we want to derive the best fit line using m and b

def gradient_descent(x, y):
    # we start with some value of m and b
    # and take steps to reach the global minimum
    m_curr = b_curr = 0

    # Number of baby steps to take
    iterations = 10000
    n = len(x)
    # I can  adjust thr lr
    learning_rate = 0.08
    for i in range(iterations):
        # y = mx + b
        y_predicted = m_curr * x + b_curr

        # to now how well you are doing print out cost
        cost = (1 / n) * sum([val**2 for val in (y-y_predicted)])

        # calculate m derivative and b derivative

        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        # Then adjust m_curr
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b{}, cost {} iteration {}".format(m_curr, b_curr, cost, i))


x = np.array([1, 2, 3, 4, 5])

y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
