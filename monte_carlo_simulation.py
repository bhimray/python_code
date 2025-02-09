import numpy as np
import matplotlib.pyplot as plt

# Given parameters
B = 100
mu_0 = 0
mu_1 = 0.1
sigma_0 = 0.4
sigma_1 = 0.4
num_samples = 10000  # Number of Monte Carlo simulations

# Generate random price samples from log-normal distributions
p_0_samples = np.random.lognormal(mean=mu_0, sigma=sigma_0, size=num_samples)
p_1_samples = np.random.lognormal(mean=mu_1, sigma=sigma_1, size=num_samples)

print("p_o_samples", p_0_samples[:5]);
print("p_1_samples", p_1_samples[:5]);
# Expected values
E_p0 = np.exp(mu_0 + (sigma_0**2) / 2)
E_p1 = np.exp(mu_1 + (sigma_1**2) / 2)

# 1. Prescient case: Sell everything in the round with the higher price
revenues_prescient = np.maximum(B * p_0_samples, B * p_1_samples)
print("revenues_prescient", revenues_prescient);

# 2. No Knowledge case: Use optimal fraction alpha_star
x0_no_knowledge = B if E_p0 > E_p1 else 0
revenues_no_knowledge = x0_no_knowledge * p_0_samples + (B - x0_no_knowledge) * p_1_samples;

# 3. Partial Knowledge case: Compute x0 dynamically based on observed p0
# x0_partial_knowledge = round(B * (p_0_samples / (p_0_samples + E_p1)))
x0_partial_knowledge = np.where(p_0_samples > E_p1, B, 0)
print("x0_partial_knowledge", x0_partial_knowledge);
revenues_partial_knowledge = x0_partial_knowledge * p_0_samples + (B - x0_partial_knowledge) * p_1_samples

# Compute expected revenues
E_revenue_prescient = np.mean(revenues_prescient)
E_revenue_no_knowledge = np.mean(revenues_no_knowledge)
E_revenue_partial_knowledge = np.mean(revenues_partial_knowledge)
# Print expected revenues
print(f"Expected Revenue (Prescient): {E_revenue_prescient:.2f}")
print(f"Expected Revenue (No Knowledge): {E_revenue_no_knowledge:.2f}")
print(f"Expected Revenue (Partial Knowledge): {E_revenue_partial_knowledge:.2f}")

# Plot histograms
plt.figure(figsize=(12, 6))
plt.hist(revenues_prescient, bins=50, alpha=0.6, label=f'Prescient (E[R] = {E_revenue_prescient:.2f})', density=True)
plt.hist(revenues_no_knowledge, bins=50, alpha=0.6, label=f'No Knowledge (E[R] = {E_revenue_no_knowledge:.2f})', density=True)
plt.hist(revenues_partial_knowledge, bins=50, alpha=0.6, label=f'Partial Knowledge (E[R] = {E_revenue_partial_knowledge:.2f})', density=True)
plt.xlabel('Total Revenue')
plt.ylabel('Density')
plt.legend()
plt.title('Revenue Distribution for Different Information Cases')
plt.show();


