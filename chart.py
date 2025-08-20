import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer support response times
def generate_support_data():
    """Generate synthetic customer support response time data across different channels"""
    
    # Define support channels with different response time characteristics
    channels = {
        'Live Chat': {'mean': 5, 'std': 2, 'size': 800},      # Fast response
        'Email': {'mean': 24, 'std': 12, 'size': 1200},       # Moderate response
        'Phone': {'mean': 8, 'std': 4, 'size': 600},          # Quick response
        'Social Media': {'mean': 18, 'std': 8, 'size': 400},  # Variable response
        'Ticket System': {'mean': 48, 'std': 20, 'size': 500} # Slower response
    }
    
    data = []
    
    for channel, params in channels.items():
        # Generate response times using log-normal distribution for realistic skew
        response_times = np.random.lognormal(
            mean=np.log(params['mean']), 
            sigma=0.5, 
            size=params['size']
        )
        
        # Add some variation and cap at reasonable maximum
        response_times = np.clip(response_times, 0.5, 120)  # 0.5 to 120 hours
        
        # Create DataFrame entries
        for time in response_times:
            data.append({
                'Support_Channel': channel,
                'Response_Time_Hours': time,
                'Channel_Type': 'Real-time' if channel in ['Live Chat', 'Phone'] else 'Asynchronous'
            })
    
    return pd.DataFrame(data)

# Generate the dataset
df = generate_support_data()

# Set up professional styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

# Create figure with specified dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create the violin plot with professional styling
violin_plot = sns.violinplot(
    data=df,
    x='Support_Channel',
    y='Response_Time_Hours',
    palette='Set2',
    inner='quartile',
    linewidth=1.5
)

# Customize the plot for executive presentation
plt.title('Customer Support Response Time Distribution by Channel\nSchoen Rippin and Wilderman Analytics', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=14, fontweight='semibold')
plt.ylabel('Response Time (Hours)', fontsize=14, fontweight='semibold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Customize y-axis to show key time ranges
plt.ylim(0, 100)

# Add subtle background color
plt.gca().set_facecolor('#fafafa')

# Add professional styling touches
for spine in plt.gca().spines.values():
    spine.set_color('#cccccc')
    spine.set_linewidth(0.8)

# Add summary statistics as text annotation
stats_text = f"Dataset: {len(df):,} support interactions\nAnalysis Period: Q4 2024"
plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
         verticalalignment='top', fontsize=10, 
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# Ensure tight layout
plt.tight_layout()

# Save the chart with exactly 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# Display basic statistics
print("Customer Support Response Time Analysis")
print("="*50)
print(f"Total interactions analyzed: {len(df):,}")
print("\nResponse Time Statistics by Channel (Hours):")
print(df.groupby('Support_Channel')['Response_Time_Hours'].describe().round(2))

plt.show()