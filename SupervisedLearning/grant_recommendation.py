import os
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# WARNING: Defalut is 'Warn'
pd.options.mode.chained_assignment = None

# Get data
data = pd.read_csv('grant_recommendation.csv')

# Ensure data is well formatted
print("Row Data: -----------------------")
print(data)

# Feture selection
features = ['OverallGrade','Obedient','ResearchScore','ProjectScore']
training_features = data[features]

outcome_name = ['Recommend']
outcome_labels = data[outcome_name]

print("----------------------- Training Feature Data: -----------------------")
# Show training features
print(training_features)

print("----------------------- Outcome Label Data: -----------------------")
# Show outcome labels
print(outcome_labels)

# Features based on type.
numeric_feature_names = ['ResearchScore','ProjectScore']
categorical_feature_names = ['OverallGrade','Obedient']

ss = StandardScaler()
ss.fit(training_features[numeric_feature_names])

# Scale features now
training_features[numeric_feature_names] = ss.transform(training_features[numeric_feature_names])

print("----------------------- Scaled Training Feature Data: -----------------------")
# View updated feature set.
print(training_features)

# Convert categorical features into dummy variables
training_features = pd.get_dummies(training_features, columns=categorical_feature_names)

print("----------------------- Dummied categorical Training Data: -----------------------")
print(training_features)

# Derive new engineered categorical columns
categorical_engineered_column = list(set(training_features.columns) - set(numeric_feature_names))

""" Logistic Regression Model """
# Fit Logistic regression model
lr = LogisticRegression(solver='warn')
model = lr.fit(training_features, outcome_labels['Recommend'])
# Show the model parameters
print("----------------------- Logistic Regression Model : -----------------------")
print(model)

""" Predict Label with Logistic Regression Model """
pred_labels = model.predict(training_features)
actual_labels = np.array(outcome_labels['Recommend'])

""" Evaluate Model Performance """
print('Accuracy: ',float(accuracy_score(actual_labels, pred_labels))*100,'%')
print('Classification Status : ')
print(classification_report(actual_labels,pred_labels))

""" Save Model and Scaler for later use """
if not os.path.exists('GrantRecommendationModel'):
    os.mkdir('GrantRecommendationModel')
if not os.path.exists('GrantRecommendationScaler'):
    os.mkdir('GrantRecommendationScaler')

joblib.dump(model, r'GrantRecommendationModel/grant_recommendation_model.pickle')
joblib.dump(ss, r'GrantRecommendationScaler/grant_recommendation_scaler.pickle')


""" Load Model and Scaler from job lib """
model = joblib.load(r'GrantRecommendationModel/grant_recommendation_model.pickle')
scaler = joblib.load(r'GrantRecommendationScaler/grant_recommendation_scaler.pickle')

new_data = pd.DataFrame([{'Name':"Nathan",'OverallGrade':'F','Obedient':'N','ResearchScore':'30','ProjectScore':'20'},
                        {'Name':"Thomas",'OverallGrade':'A','Obedient':'Y','ResearchScore':'80','ProjectScore':'78'}])


new_data = new_data[['Name','OverallGrade','Obedient','ResearchScore','ProjectScore']]

# Show generated data.
print("----------------------- Generated Data: -----------------------")
print(new_data)

prediction_features = new_data[features]
prediction_features[numeric_feature_names] = scaler.transform(prediction_features[numeric_feature_names])

prediction_features = pd.get_dummies(prediction_features, columns=categorical_feature_names)

print("----------------------- Prediction Feature Data: -----------------------")
print(prediction_features)

current_categorical_engineered_column = set(prediction_features.columns) - set(numeric_feature_names)
missing_features = set(categorical_engineered_column) - current_categorical_engineered_column

for feature in missing_features:
    prediction_features[feature] = [0] * len(prediction_features)

# View final feature set, which should have the 0 in place for features that are not in generated data.
print("----------------------- Final Feature Set: -----------------------")
print(prediction_features)

""" Now predict with our model """
predictions = model.predict(prediction_features)

new_data['Recommend'] = predictions

# Show predictions on new data
print("----------------------- Predictions on New Set: -----------------------")
print(new_data)

""" Evaluate Model Performance """
print("----------------------- Accuracy on predicted labels: -----------------------")
print('Accuracy: ',float(accuracy_score(new_data['Recommend'], ['No','Yes']))*100,'%')
print('Classification Status : ')
print(classification_report(new_data['Recommend'], ['No','Yes']))
