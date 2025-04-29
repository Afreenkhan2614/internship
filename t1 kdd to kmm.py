import matplotlib.pyplot as plt

# Example data for Kodad to Khammam
actual_hours = [0, 3, 6, 9]  # Time of day (in hours)
actual_traffic = [50, 100, 550, 790]  # Actual traffic volume
predicted_traffic = [0, 250, 400, 700]  # Predicted traffic volume

plt.figure(figsize=(8, 6))

# Scatter plot for actual traffic
plt.scatter(actual_hours, actual_traffic, color='blue', label='Actual', zorder=3)

# Line plot for predicted traffic
plt.plot(actual_hours, predicted_traffic, color='red', label='Predicted', linewidth=2)

# Labels and Title
plt.title("Traffic Volume (Kodad to Khammam)", fontsize=14)
plt.xlabel("Time of Day (Hour)", fontsize=12)
plt.ylabel("Traffic Volume", fontsize=12)

# Make sure Y-axis starts at 0
plt.ylim(0, max(max(actual_traffic), max(predicted_traffic)) + 100)

# Annotate the starting and ending points with location names
plt.text(actual_hours[0], predicted_traffic[0], 'Kodad', fontsize=12, color='black', ha='right', va='bottom')
plt.text(actual_hours[-1], predicted_traffic[-1], 'Khammam', fontsize=12, color='black', ha='left', va='top')

# Grid, legend, and display
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
