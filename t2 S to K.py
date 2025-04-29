import matplotlib.pyplot as plt

# Example data for Ananthagiri to Kodad
actual_hours = [0, 6, 10, 15]  # Time of day (in hours)
actual_traffic = [200, 450, 50, 550]  # Actual traffic volume
predicted_traffic = [20, 250, 200, 400]  # Predicted traffic volume

plt.figure(figsize=(8, 6))

# Scatter plot for actual traffic
plt.scatter(actual_hours, actual_traffic, color='green', label='Actual', zorder=3)

# Line plot for predicted traffic
plt.plot(actual_hours, predicted_traffic, color='orange', label='Predicted', linewidth=2, marker='o')

# Add location name annotations on predicted line
plt.text(actual_hours[0], predicted_traffic[0] - 30, "From: Ananthagiri", color='black', fontsize=10, ha='left')
plt.text(actual_hours[-1], predicted_traffic[-1] + 30, "To: Kodad", color='black', fontsize=10, ha='right')

# Labels and Title
plt.title("Traffic Volume (Ananthagiri to Kodad)", fontsize=14)
plt.xlabel("Time of Day (Hour)", fontsize=12)
plt.ylabel("Traffic Volume", fontsize=12)

# Y-axis range
plt.ylim(0, max(max(actual_traffic), max(predicted_traffic)) + 100)

# Custom x-tick labels
plt.xticks(actual_hours, ['12 AM', '6 AM', '10 AM', '3 PM'])       


# Grid, legend, layout
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
ax = plt.gca()
def format_coord(x, y):
    hour = int(round(x))
    if hour == 0:
        x_str = "12 AM"
    elif hour < 12:
        x_str = f"{hour} AM"
    elif hour == 12:
        x_str = "12 PM"
    else:
        x_str = f"{hour - 12} PM"
    return f"(x, y) = ({x_str}, {y:.1f})"

ax.format_coord = format_coord

plt.show()
