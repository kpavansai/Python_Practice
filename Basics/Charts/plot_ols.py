from matplotlib.pyplot import (plot, scatter, show, xticks, yticks)
from numpy import newaxis
from sklearn import (datasets, linear_model)
from sklearn.metrics import (mean_squared_error, r2_score)

if __name__ == "__main__":
    diabetes = datasets.load_diabetes()

    diabetes_X = diabetes.data[:, newaxis, 2]

    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    regr = linear_model.LinearRegression()

    regr.fit(diabetes_X_train, diabetes_y_train)

    diabetes_y_pred = regr.predict(diabetes_X_test)

    print('Coefficients: \n', regr.coef_)
    print("Mean squared error: %.2f" % mean_squared_error(
        diabetes_y_test, diabetes_y_pred))
    print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

    scatter(diabetes_X_test, diabetes_y_test, color='black')
    plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

    xticks(())
    yticks(())

    show()
