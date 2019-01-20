import joblib
import pandas as pd

""" Feature selection """
features = ['OverallGrade','Obedient','ResearchScore','ProjectScore']
outcome_name = ['Recommend']
# Type based features
numeric_feature_names = ['ResearchScore','ProjectScore']
categorical_feature_names = ['OverallGrade','Obedient']

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

categorical_engineered_column = list(set(prediction_features.columns) - set(numeric_feature_names))
current_categorical_engineered_column = set(categorical_engineered_column) - set(numeric_feature_names)
missing_features = set(categorical_engineered_column) - current_categorical_engineered_column

for feature in missing_features:
    prediction_features[feature] = [0] * len(prediction_features)

# View final feature set
print("----------------------- Final Feature Set: -----------------------")
print(prediction_features)
