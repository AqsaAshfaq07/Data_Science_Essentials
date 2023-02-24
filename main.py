# Statistics for Data Science
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# data
learning_hours = [1, 2, 6, 4, 10]
scores = [3, 4, 6, 5, 6]

print("Mean of Learning Hours: " + str(np.mean(learning_hours)))
print("Median: " + str(np.median(learning_hours)))
print("Mean and Median of Scores: " + str(np.mean(scores)) + ", " + str(np.median(scores)))
print("Standard Dev: " + str(np.std(learning_hours)) + ", " + str(np.std(scores)))
print("Correlation Coefficient: " + str(np.corrcoef(learning_hours, scores)))
print(plt.boxplot(scores))
A = learning_hours
B = scores

# P(A and B) = P(A) * P(B) --probability of independent events
# P(A and B) = P(A) & P(B after A has occurred) --probability of dependent events

# P(A and B) = 0 --mutually exclusive events
# P(A or B) = P(A) + P(B)

# Bayes Theorem -- P(A|B) = (P(B|A) * P(A)) / P(B)

# Distributions
x = np.random.rand(100)
y = np.random.normal(size = 100)
print(sns.histplot(x))
print(sns.histplot(y))