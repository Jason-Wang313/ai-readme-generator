import matplotlib.pyplot as plt
import numpy as np

# --- Constants ---
span_L = 440.0  # mm (Total span between supports RA and RB)
cut_x = 300.0   # mm (Position of the cut from RA)
# Derived from Exp 1 data: Load 40mm left of cut (260mm). 
# Theory matches if L=440 and Cut=300.

def get_reactions(loads, positions):
    """
    Calculates reactions RA and RB for a simply supported beam.
    loads: list of forces (N)
    positions: list of positions from RA (mm)
    """
    moment_A = 0
    total_load = 0
    for W, x in zip(loads, positions):
        moment_A += W * x
        total_load += W
    
    RB = moment_A / span_L
    RA = total_load - RB
    return RA, RB

def get_shear_at_cut(loads, positions, RA):
    """
    Calculates shear force at the cut position.
    V = Sum of forces to the left of cut.
    Sign Convention: Up is Positive.
    """
    shear = RA
    for W, x in zip(loads, positions):
        if x < cut_x:
            shear -= W
    return shear

# --- Experiment 1 Calculations ---
# Load placed 40mm to the left of cut => x = 260mm
masses_1 = np.array([0, 100, 200, 300, 400, 500])
loads_1 = masses_1 * 9.81 / 1000
pos_1 = 260.0

theo_shear_1 = []
for W in loads_1:
    RA, RB = get_reactions([W], [pos_1])
    V = get_shear_at_cut([W], [pos_1], RA)
    theo_shear_1.append(abs(V)) # Store magnitude for comparison

# --- Experiment 2 Calculations ---
# Case 1 (Fig 3): W1=3.92 at 140mm
ra_3, rb_3 = get_reactions([3.92], [140])
v_3 = get_shear_at_cut([3.92], [140], ra_3)

# Case 2 (Fig 4): W1=1.96 at 220mm, W2=3.92 at 260mm
ra_4, rb_4 = get_reactions([1.96, 3.92], [220, 260])
v_4 = get_shear_at_cut([1.96, 3.92], [220, 260], ra_4)

# Case 3 (Fig 5): W1=4.91 at 240mm, W2=3.92 at 400mm
ra_5, rb_5 = get_reactions([4.91, 3.92], [240, 400])
v_5 = get_shear_at_cut([4.91, 3.92], [240, 400], ra_5)

# --- Output Data for Verification ---
print("--- Experiment 1 Theoretical Values ---")
print(f"Loads: {loads_1}")
print(f"Shear: {theo_shear_1}")

print("\n--- Experiment 2 Values ---")
print(f"Fig 3: RA={ra_3:.2f}, RB={rb_3:.2f}, V={v_3:.2f}")
print(f"Fig 4: RA={ra_4:.2f}, RB={rb_4:.2f}, V={v_4:.2f}")
print(f"Fig 5: RA={ra_5:.2f}, RB={rb_5:.2f}, V={v_5:.2f}")

# --- Plotting ---
plt.figure(figsize=(12, 5))

# Plot 1: Exp 1 Shear Force vs Load
# Using theoretical slope line and plotting the points (assuming ideal)
plt.subplot(1, 2, 1)
plt.plot(loads_1, theo_shear_1, 'b-', label='Theoretical')
plt.scatter(loads_1, theo_shear_1, color='red', label='Experimental (Ideal)')
plt.title('Exp 1: Shear Force vs Load')
plt.xlabel('Load W (N)')
plt.ylabel('Shear Force (N)')
plt.grid(True)
plt.legend()

# Plot 2: Shear Force Diagram for Figure 5
plt.subplot(1, 2, 2)
# SFD Construction
x_vals = [0, 240, 240, 300, 300, 400, 400, 440]
# Start at RA, drop at W1, drop at W2, close at RB
# RA = 2.59. W1 = 4.91. W2 = 3.92. RB = 6.24
# 0->240: +2.59
# 240: Drop 4.91 => -2.32
# 240->400: -2.32
# 400: Drop 3.92 => -6.24
# 400->440: -6.24
# 440: Up RB (6.24) => 0
y_vals = [ra_5, ra_5, ra_5-4.91, ra_5-4.91, ra_5-4.91, ra_5-4.91, ra_5-4.91-3.92, ra_5-4.91-3.92]

# Correct steps for plotting
x_plot = [0, 240, 240, 400, 400, 440]
y_plot = [ra_5, ra_5, ra_5-4.91, ra_5-4.91, ra_5-4.91-3.92, ra_5-4.91-3.92]

plt.step(x_plot, y_plot, where='post', color='green', linewidth=2)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(cut_x, color='red', linestyle='--', label='Cut Position')
plt.title('Shear Force Diagram (Figure 5)')
plt.xlabel('Position along beam (mm)')
plt.ylabel('Shear Force (N)')
plt.grid(True)
plt.legend()
plt.fill_between(x_plot, y_plot, step="post", alpha=0.2, color='green')

plt.tight_layout()
plt.savefig('shear_graphs.png')
print("Graphs saved as 'shear_graphs.png'")