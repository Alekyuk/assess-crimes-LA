# LAPD Crime Analysis Project

## Business Problem

This project aims to address the following question: **How can police resources be optimally allocated based on crime trend patterns in Los Angeles?**

By analyzing crime data from 2020 to 2023, we seek to identify crime patterns that could enable authorities to better plan their interventions.

## Project Objectives

- Identify temporal and geographic trends in criminal activities
- Provide recommendations for police resource allocation
- Develop a predictive model for anticipating crime types

## Project Structure

```
.
├── data/                 # Raw and processed data
|  └── download_data.py   # Script to download crime data
├── assets/               # Images, maps, and other assets
├── requirements.txt      # Project dependencies
├── README.md             # This file
└── main.ipynb            # Jupyter notebook with analysis and visualizations
```

## Data Science Methodology

1. **Data Exploration**
2. **Data Cleaning and Preparation**
3. **Exploratory Data Analysis**
4. **Predictive Modeling**
5. **Model Evaluation and Validation**

## Technologies Used

- Python 3.8+
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Folium for mapping

## Installation

```bash
pip install -r requirements.txt
```

## Data Download

This project includes a Python script `data/download_data.py` that is needed to download crime data from the official data.lacity.org website. The script fetches data from the Los Angeles Police Department's open data portal and processes it for analysis.

To run the data download:
```bash
python data/download_data.py
```

## Usage

To run the complete analysis:
```bash
python src/main.py
```

## Results and Recommendations

Analysis reveals that "Theft" and "Burglary" crimes are more frequent in certain areas during specific hours. Key recommendations include:

1. Increase police presence in high-risk zones
2. Implement awareness campaigns
3. Optimize response scheduling

## Authors

Alexander Kyng - Data Scientist

## License

This project is licensed under the MIT License.