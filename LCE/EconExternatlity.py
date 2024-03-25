import matplotlib.pyplot as plt
import numpy as np

# Define cost function
def marginal_cost(q):
    return 5 + 0.2 * q

# Define social cost function (includes marginal cost and marginal social cost)
def social_cost(q):
    return marginal_cost(q) + 2 * q

# Given market price
market_price = 20

# (i) Find firm's production level with only marginal cost
mc = np.arange(0, 50, 0.1)  # Range of possible production levels
profit = market_price - marginal_cost(mc)  # Profit at each production level

optimal_production_mc = mc[np.argmax(profit)]  # Production level for maximum profit

# (ii) Find optimal production level considering social cost
optimal_production_sc = np.interp(market_price, social_cost(mc), mc)  # Production where MC=MB

# (iii) Graph results
plt.figure(figsize=(8, 6))

# Plot marginal cost and social cost curves
plt.plot(mc, marginal_cost(mc), label='Marginal Cost (MC)')
plt.plot(mc, social_cost(mc), label='Social Cost (SC)')

# Plot market price line
plt.axhline(y=market_price, color='r', linestyle='--', label='Market Price')

# Label axes and title
plt.xlabel('Daily Drink Can Production')
plt.ylabel('Cost (£)')
plt.title('Marginal Cost, Social Cost, and Market Price')

# Mark optimal production points with annotations
plt.scatter(optimal_production_mc, market_price, marker='o', color='b', label='MC-Profit Maximization')
plt.scatter(optimal_production_sc, market_price, marker='o', color='g', label='SC-Optimal Level')

# Add legend
plt.legend()

# Show annotations
plt.annotate(
    f"MC Equilibrium ({int(optimal_production_mc)})",
    (optimal_production_mc, market_price),
    xytext=(optimal_production_mc + 5, market_price + 1),
    textcoords="offset points",
    fontsize=8,
    arrowprops=dict(facecolor='black', shrink=0.05),
)
plt.annotate(
    f"SC Equilibrium ({int(optimal_production_sc)})",
    (optimal_production_sc, market_price),
    xytext=(optimal_production_sc - 5, market_price + 1),
    textcoords="offset points",
    fontsize=8,
    arrowprops=dict(facecolor='black', shrink=0.05),
)

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()

# (iii) Calculate excise tax
excise_tax = market_price - social_cost(optimal_production_sc)
print(f"Optimal excise tax: £{excise_tax:.2f}")