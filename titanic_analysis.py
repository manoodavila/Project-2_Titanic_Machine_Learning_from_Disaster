import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Carregar os dados
train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

# Análise básica
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women) / len(women)
print("% of women who survived:", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men) / len(men)
print("% of men who survived:", rate_men)

# Preparar os dados para o modelo
y = train_data["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

# Salvar as previsões
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
