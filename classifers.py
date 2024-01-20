import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the CSV file
df = pd.read_csv('SDN_traffic.csv')

# Drop the 'id_flow' column as it's not needed for classification
df = df.drop('id_flow', axis=1)

# Encode categorical variable 'category'
label_encoder = LabelEncoder()
df['category'] = label_encoder.fit_transform(df['category'])

# Split the data into features and target variable
X = df.drop('category', axis=1)
y = df['category']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ID3 Decision Tree
id3_classifier = DecisionTreeClassifier(criterion='entropy')
id3_classifier.fit(X_train, y_train)
id3_predictions = id3_classifier.predict(X_test)

# Evaluate ID3 model
print("ID3 Accuracy:", accuracy_score(y_test, id3_predictions))
print("ID3 Classification Report:\n", classification_report(y_test, id3_predictions))
print("ID3 Confusion Matrix:\n", confusion_matrix(y_test, id3_predictions))

# CART Decision Tree
cart_classifier = DecisionTreeClassifier(criterion='gini')
cart_classifier.fit(X_train, y_train)
cart_predictions = cart_classifier.predict(X_test)

# Evaluate CART model
print("\nCART Accuracy:", accuracy_score(y_test, cart_predictions))
print("CART Classification Report:\n", classification_report(y_test, cart_predictions))
print("CART Confusion Matrix:\n", confusion_matrix(y_test, cart_predictions))
