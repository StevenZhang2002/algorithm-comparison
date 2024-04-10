import numpy as np
from scipy.stats import entropy, chisquare, kstest

# Normalize histogram to obtain probabilities
probabilities = hist.flatten() / np.sum(hist)

# Calculate entropy
entropy_value = entropy(probabilities, base=2)
print("Entropy:", entropy_value)

# Calculate variance
mean = np.arange(len(hist))
variance = np.sum((mean - np.mean(hist)) ** 2 * probabilities)
print("Variance:", variance)

# Calculate expected frequencies assuming uniformity
expected_frequencies = np.sum(hist) / len(hist)

# Perform chi-square test
chi2_stat, p_value = chisquare(hist.flatten(), f_exp=expected_frequencies)
print("Chi-square statistic:", chi2_stat)
print("p-value:", p_value)

# Perform Kolmogorov-Smirnov test
ks_stat, p_value = kstest(np.cumsum(probabilities), 'uniform')
print("Kolmogorov-Smirnov statistic:", ks_stat)
print("p-value:", p_value)