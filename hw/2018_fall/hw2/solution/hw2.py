import pandas as pd
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# part 1
print("part 1")
fname = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
fname = "../abalone.data"
df = pd.read_csv(fname,
    names=["sex", "length", "diam", "height", "wt_whole", "wt_shucked", "wt_viscera", "wt_shell", "rings"],
    index_col=False)

# part 2
print("part 2")
y, X = dmatrices("rings ~ C(sex) + length + diam + height + wt_whole + wt_shucked + wt_viscera + wt_shell",
                 df, return_type="dataframe")

X.drop(X[['Intercept']], axis=1, inplace=True)

# part 3
print("part 3")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# part 4
print("part 4")
model = LinearRegression()
model.fit(X_train, y_train)

predicted = model.predict(X_test)

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

ax.scatter(predicted, y_test)

ax.set_xlabel(r'predicted')
ax.set_ylabel(r'true')
ax.set_title("Number of Rings in Abalone")


plt.savefig('regression.png')
