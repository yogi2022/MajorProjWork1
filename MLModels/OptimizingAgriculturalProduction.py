import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('data.csv')
y = data['label']
x = data.drop(['label'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

model = LogisticRegression(max_iter=1000)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

data.head()

prediction = model.predict((np.array([[90, 40, 40, 20, 80, 7, 200]])))

print("Accuracy : ",model.score(x_test, y_test)*100, '%')

savedModel = 'savedModel.sav'
joblib.dump(model, savedModel)
