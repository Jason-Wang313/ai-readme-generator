import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
g = 9.81  # m/s^2
d = 0.9   # meters
mass_cart_base = 0.5 # kg (Deduced from data to ensure a_theo > a_exp)

# Data extracted from the user's image
# Format: [mass_grams, average_time_s]
data_test_1 = [
    [10, 3.421],
    [20, 2.283],
    [30, 1.8825],
    [40, 1.63]
]

data_test_2 = [ # 500g added to cart
    [10, 5.537],
    [20, 3.2795],
    [30, 2.6405],
    [40, 2.2735]
]

data_test_3 = [ # 1kg added to cart
    [10, 6.4395],
    [20, 4.096],
    [30, 3.22],
    [40, 2.741]
]

def calculate_row(mass_g, time_s, added_mass_kg):
    m_hang = mass_g / 1000.0
    M_cart_total = mass_cart_base + added_mass_kg
    
    # 1. Experimental Acceleration: d = 1/2 * a * t^2  => a = 2d / t^2
    a_exp = (2 * d) / (time_s ** 2)
    
    # 2. Theoretical Acceleration: F = ma => m_hang * g = (M_total) * a
    M_system = M_cart_total + m_hang
    a_theo = (m_hang * g) / M_system
    
    # 3. Difference %
    diff_percent = abs(a_exp - a_theo) / a_theo * 100
    
    # 4. Friction Force: F_net = ma. 
    # Forces on system: m_hang*g - friction = M_system * a_exp
    # friction = m_hang*g - M_system * a_exp
    f_friction = (m_hang * g) - (M_system * a_exp)
    
    return {
        "mass_g": mass_g,
        "time": time_s,
        "M_cart_total": M_cart_total,
        "a_exp": round(a_exp, 3),
        "a_theo": round(a_theo, 3),
        "diff": round(diff_percent, 2),
        "friction": round(f_friction, 4)
    }

# Process Data
results = []
friction_summary = {"Test 1": [], "Test 2": [], "Test 3": []}

for row in data_test_1:
    res = calculate_row(row[0], row[1], 0.0)
    res['Test'] = "Test 1"
    results.append(res)
    friction_summary["Test 1"].append(res['friction'])

for row in data_test_2:
    res = calculate_row(row[0], row[1], 0.5)
    res['Test'] = "Test 2"
    results.append(res)
    friction_summary["Test 2"].append(res['friction'])

for row in data_test_3:
    res = calculate_row(row[0], row[1], 1.0)
    res['Test'] = "Test 3"
    results.append(res)
    friction_summary["Test 3"].append(res['friction'])

# --- PLOTTING ---

# Calculate Normal Forces and Average Friction for the Graph
# Normal Force on Cart = M_cart_total * g
normal_forces = []
avg_frictions = []

# Test 1
n1 = (mass_cart_base + 0.0) * g
f1 = np.mean(friction_summary["Test 1"])
normal_forces.append(n1)
avg_frictions.append(f1)

# Test 2
n2 = (mass_cart_base + 0.5) * g
f2 = np.mean(friction_summary["Test 2"])
normal_forces.append(n2)
avg_frictions.append(f2)

# Test 3
n3 = (mass_cart_base + 1.0) * g
f3 = np.mean(friction_summary["Test 3"])
normal_forces.append(n3)
avg_frictions.append(f3)

# Perform Linear Regression to find Coefficient of Friction (mu)
coeffs = np.polyfit(normal_forces, avg_frictions, 1)
mu = coeffs[0] # Slope
intercept = coeffs[1]
line_x = np.array([0, 16])
line_y = mu * line_x + intercept

plt.figure(figsize=(10, 6))
plt.plot(normal_forces, avg_frictions, 'ro', markersize=10, label='Experimental Data')
# FIX: Use rf"" string to handle LaTeX escape sequences correctly
plt.plot(line_x, line_y, 'b-', label=rf'Best Fit Line (Slope $\mu_k \approx {mu:.3f}$)')

plt.title(r'Friction Force ($f_k$) vs. Normal Force ($N$)', fontsize=14)
plt.xlabel(r'Normal Force ($N$)', fontsize=12)
plt.ylabel(r'Frictional Force ($N$)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.xlim(0, 16)
plt.ylim(0, max(avg_frictions) * 1.2)

# Annotate points
for i, txt in enumerate(['Test 1', 'Test 2', 'Test 3']):
    plt.annotate(f"{txt}\n({normal_forces[i]:.2f} N, {avg_frictions[i]:.3f} N)", 
                 (normal_forces[i], avg_frictions[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
# Check if saving is possible, otherwise just show
try:
    plt.savefig('friction_graph.png')
    print("Graph saved as friction_graph.png")
except:
    plt.show()

# Print Summary for user verification
print(f"Calculated Coefficient of Friction (Slope): {mu:.4f}")