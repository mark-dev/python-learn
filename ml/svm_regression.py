print(__doc__)

import math
import random

from sklearn import model_selection
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR

def secret_function(xarg: int, yarg:int ) -> float:
    return xarg + yarg
    # return math.sin(xarg) + 0.2 * math.sqrt(yarg)

# #############################################################################
# Generate sample data
X = []
y = []
for i in range(0,100):
    xarg = random.randrange(100)
    yarg = random.randrange(100)
    y.append(secret_function(xarg,yarg))
    X.append([xarg,yarg])

#############################################################################

# #############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_lin = SVR(kernel='linear', C=100, gamma='auto')
svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=10, epsilon=.1,coef0=1,max_iter=1000)

# #############################################################################
# Look at the results
lw = 2

svrs = [svr_rbf, svr_lin, svr_poly]
kernel_label = ['RBF', 'Linear', 'Polynomial']

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=0.2, random_state=7)
for ix, svr in enumerate(svrs):
    print("Training %s classifier " % (kernel_label[ix]))
    svr.fit(X_train,Y_train)
    predictions = svr.predict(X_validation)
    print(f"error = {mean_squared_error(Y_validation, predictions)}")
    print("="*80)