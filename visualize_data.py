import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Set the style for better-looking graphs
plt.style.use('seaborn-v0_8')
sns.set_theme()

# Wes Anderson inspired color palette - updated with more muted tones
wes_colors = {
    'muted': ['#96613D', '#3C6E47', '#4F6D7A', '#6B4E71', '#8B575C'],
    'vintage': ['#9B8357', '#7D9B76', '#7B92A8', '#957D8D', '#A67F81']
}

def load_data():
    """Load data from Excel file"""
    try:
        df = pd.read_excel('Key_results_output_1.2.xlsx')
        print("Available columns in the Excel file:")
        print(df.columns.tolist())
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def create_study_type_bar_chart(df):
    """Create a bar chart showing distribution of study types"""
    plt.figure(figsize=(10, 6))
    study_counts = df['Study type'].value_counts()
    
    # Create bar plot with Wes Anderson colors
    bars = plt.bar(study_counts.index, study_counts.values, color=wes_colors['vintage'])
    
    # Set white background and black axes
    plt.gca().set_facecolor('white')
    plt.gcf().set_facecolor('white')
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['right'].set_color('black')
    
    # Customize the plot with larger, bolder fonts
    plt.title('Distribution of Study Types', pad=20, fontsize=16, fontweight='bold')
    plt.xlabel('Study Type', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Studies', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Add a subtle grid
    plt.grid(True, axis='y', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('study_types.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_psychedelic_timeline(df):
    """Create a timeline visualization of psychedelic usage"""
    plt.figure(figsize=(12, 6))
    
    # Set white background and black axes
    plt.gca().set_facecolor('white')
    plt.gcf().set_facecolor('white')
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['right'].set_color('black')
    
    # Add horizontal reference lines for each psychedelic
    unique_psychedelics = df['Psychedelic'].unique()
    for i, psychedelic in enumerate(unique_psychedelics):
        plt.axhline(y=psychedelic, color='gray', linestyle=':', linewidth=0.5, alpha=0.3)
    
    # Add vertical reference lines for each year
    unique_years = sorted(df['Year'].unique())
    for year in unique_years:
        plt.axvline(x=year, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # Create the main scatter plot with vintage colors
    sns.scatterplot(data=df, x='Year', y='Psychedelic', 
                   hue='Study type', size='Study type',
                   sizes=(100, 200), alpha=0.8,
                   palette=wes_colors['vintage'])
    
    # Customize the plot with larger, bolder fonts
    plt.title('Psychedelic Usage Timeline by Study Type', pad=20, fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14, fontweight='bold')
    plt.ylabel('Psychedelic', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    # Add a legend with larger font
    plt.legend(title='Study Type', bbox_to_anchor=(1.05, 1), loc='upper left',
              title_fontsize=14, fontsize=12)
    
    plt.tight_layout()
    plt.savefig('psychedelic_timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_system_improvements(improvements_data):
    """Create an enhanced visualization of improvements by physiological system"""
    # Sample data structure (you'll need to replace this with your actual data)
    data = {
        'System': [
            'Neurological', 'Musculoskeletal', 'Systemic', 'Cardiovascular',
            'Gastrointestinal', 'Dermatological', 'Genitourinary & reproductive', 'Nonspecific'
        ],
        'Improvement_Percentage': [63, 52, 80, 80, 100, 100, 73, 82],
        'Sample_Size': [45, 25, 30, 35, 40, 20, 28, 32]  # Example sample sizes
    }
    df = pd.DataFrame(data)
    
    # Create figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    # First subplot: Enhanced bar chart
    bars = ax1.bar(df['System'], df['Improvement_Percentage'], 
                  color=wes_colors['vintage'])
    
    # Customize first subplot
    ax1.set_title('Improvements by Physiological System', pad=20, 
                 fontsize=16, fontweight='bold')
    ax1.set_xlabel('Physiological System', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Percentage of Participants Improved (%)', 
                  fontsize=14, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}%', ha='center', va='bottom',
                fontsize=12, fontweight='bold')
    
    # Add grid to first subplot
    ax1.grid(True, axis='y', linestyle='--', alpha=0.3)
    ax1.set_ylim(0, 110)  # Give some space for the percentage labels
    
    # Second subplot: Bubble chart
    sizes = df['Sample_Size'] * 20  # Scale the bubble sizes appropriately
    scatter = ax2.scatter(df['Improvement_Percentage'], range(len(df)),
                         s=sizes, alpha=0.6,
                         c=np.arange(len(df)),
                         cmap='RdYlBu')
    
    # Customize second subplot
    ax2.set_title('Improvement Rate vs. Sample Size', pad=20,
                 fontsize=16, fontweight='bold')
    ax2.set_xlabel('Improvement Percentage (%)', fontsize=14, fontweight='bold')
    ax2.set_yticks(range(len(df)))
    ax2.set_yticklabels(df['System'], fontsize=12)
    
    # Add a legend for bubble sizes
    legend_elements = [plt.scatter([], [], s=size, 
                                 label=f'n={int(size/20)}',
                                 c='gray', alpha=0.6)
                      for size in [min(sizes), np.median(sizes), max(sizes)]]
    ax2.legend(handles=legend_elements, title='Sample Size',
              title_fontsize=12, fontsize=10)
    
    # Add grid to second subplot
    ax2.grid(True, linestyle='--', alpha=0.3)
    
    # Adjust layout
    plt.tight_layout()
    plt.savefig('system_improvements.png', dpi=300, bbox_inches='tight',
                facecolor='white')
    plt.close()

def main():
    # Load the data
    df = load_data()
    if df is None:
        return
    
    # Create visualizations
    create_study_type_bar_chart(df)
    create_psychedelic_timeline(df)
    create_system_improvements(df)
    
    print("Visualizations have been created and saved as PNG files.")

if __name__ == "__main__":
    main() 