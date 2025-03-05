# Psychedelics in Functional Disorders: Data Visualization

This repository contains code for creating publication-quality visualizations for a scoping review of psychedelics in functional disorders. The visualizations include study type distributions, psychedelic usage timelines, and physiological system improvements.

## Visualizations

### 1. Study Types Distribution
![Study Types Distribution](study_types.png)
- A bar chart showing the distribution of different study types
- Features vintage-colored bars with clear value labels
- Includes grid lines for easy value reading
- Uses enhanced typography with bold titles and labels

### 2. Psychedelic Usage Timeline
![Psychedelic Timeline](psychedelic_timeline.png)
- A scatter plot showing psychedelic usage across time
- Points sized and colored by study type
- Includes horizontal reference lines for each psychedelic
- Includes vertical reference lines for years
- Enhanced with vintage color palette
- Clear legend and axis labels

### 3. Physiological System Improvements
![System Improvements](system_improvements.png)
- Dual-panel visualization showing:
  - Left: Bar chart of improvement percentages by system
  - Right: Bubble chart showing improvement rates vs. sample sizes
- Color-coded using vintage palette
- Includes sample size information
- Clear typography and labels

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/psychedelics-visualization.git
cd psychedelics-visualization
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Required Packages
The following Python packages are required:
- pandas (>= 2.0.0): Data manipulation and analysis
- matplotlib (>= 3.7.0): Core plotting functionality
- seaborn (>= 0.12.0): Statistical data visualization
- openpyxl (>= 3.1.0): Excel file support

## Usage

1. Place your data file (Key_results_output_1.2.xlsx) in the project directory
2. Run the visualization script:
```bash
python visualize_data.py
```

The script will generate three PNG files:
- `study_types.png`
- `psychedelic_timeline.png`
- `system_improvements.png`

## Data Format

The input Excel file should contain the following columns:
- Study: Study identifier
- Study type: Type of study
- Year: Year of study
- Psychedelic: Type of psychedelic used
- Additional columns for system improvements data

## Customization

The visualizations can be customized by modifying:
- Color palettes in the `wes_colors` dictionary
- Figure sizes and dimensions
- Font sizes and styles
- Grid properties
- Output DPI and file format

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Color palettes inspired by Wes Anderson films
- Visualization design based on modern data visualization best practices
- Seaborn and Matplotlib libraries for powerful Python plotting 