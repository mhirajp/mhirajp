import numpy as np
import pandas as pd
from sklearn.datasets import make_classification

# Set a seed for reproducibility
np.random.seed(0)

# Define the number of samples and the number of features
n_samples = 1000
n_features = 10

# Generate a binary classification dataset with a 30% minority class
X, y = make_classification(n_samples=n_samples, n_features=n_features, weights=[0.7, 0.3])

# Convert the numerical features to categories for the first 5 features
for i in range(5):
    bins = np.linspace(min(X[:, i]), max(X[:, i]), np.random.randint(2, 6))
    X[:, i] = np.digitize(X[:, i], bins)

# Create a DataFrame from the features and target
df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(n_features)])
df['target'] = y

df.head(10)
