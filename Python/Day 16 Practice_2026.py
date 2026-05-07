"""#Day 16 | Project 3 (Flight Price Prediction EDA)

## Flight Price Exploratory Data Analysis

## 1. Introduction
In this project, we perform an exploratory data analysis (EDA) on a dataset of domestic flight prices in India. The goal is to uncover the key factors that influence airfare, detect patterns and anomalies, and derive insights that could guide a predictive model for flight price forecasting.

## 2. Dataset Overview
- **Source file:** `flight_price.xlsx`
- **Total records:** 10,683  
- **Time period covered:** March 1, 2019 – June 27, 2019  
- **Features (11):**
  - `Airline` – Name of the airline (12 unique carriers)
  - `Date_of_Journey` – Date of travel (dd/mm/yyyy)
  - `Source` – Departure city (5 unique)
  - `Destination` – Arrival city (6 unique)
  - `Route` – Sequence of stops (128 unique combinations)
  - `Dep_Time` – Departure time (HH:MM)
  - `Arrival_Time` – Arrival time (HH:MM, sometimes with a different date)
  - `Duration` – Total travel duration (e.g. “2h 50m”)
  - `Total_Stops` – Number of stops (non-stop, 1, 2, 3, 4 stops; some missing)
  - `Additional_Info` – Miscellaneous notes (e.g., “In-flight meal not included”, “1 Short layover”)
  - `Price` – Ticket price in Indian Rupees (target variable)

## 3. Objectives
1. **Understand data quality**  
   - Identify and handle missing or inconsistent values  
   - Parse dates and times into machine-readable formats  
2. **Feature engineering**  
   - Extract day, month, weekday from `Date_of_Journey`  
   - Convert `Duration` into total minutes  
   - Break down `Dep_Time` and `Arrival_Time` into hour and minute components  
   - Encode `Total_Stops` as numeric  
3. **Univariate and bivariate analysis**  
   - Distribution of ticket prices  
   - Price variation by Airline, Source, Destination, Stops  
   - Seasonal trends (monthly/weekday patterns)  
4. **Multivariate exploration**  
   - Correlation matrix and heatmap to spot inter-feature relationships  
   - Interaction of multiple factors (e.g., Airline vs. Stops vs. Price)  
5. **Key findings & insights**  
   - Summarize which factors drive higher or lower fares  
   - Highlight any surprising patterns or outliers  
6. **Next steps**  
   - Prepare cleaned & feature-rich data for modeling  
   - Prototype a regression model for price prediction

## 4. Data Cleaning & Preprocessing
- **Missing values:**  
  - Some `Total_Stops` and `Additional_Info` entries are null or inconsistent (e.g., “No info” vs “No Info”)
- **Date parsing:**  
  - Convert `Date_of_Journey` to `datetime`
- **Time parsing:**  
  - Split `Dep_Time`/`Arrival_Time` into hour/minute; handle cases where arrival date differs
- **Duration normalization:**  
  - Extract hours and minutes; compute total duration in minutes
- **Categorical encoding:**  
  - Map `Total_Stops` to integer (non-stop→0, 1 stop→1, …)
  - One-hot encode or label-encode other nominal features

## 5. Preliminary Insights (to be filled in after analysis)
- **Price distribution:** e.g., skewness, outliers  
- **Top 3 most expensive routes**  
- **Airlines with consistently lower fares**  
- **Impact of number of stops on price**  
- **Seasonal effects:** cheapest/most expensive months and weekdays  

---

*This EDA will lay the foundation for building a robust flight price prediction model by revealing the underlying structure and key drivers in the data.*
"""

import pandas as pd

"""## 1) Overall Analysis

### 1.1) Loading the dataset
"""

!git clone "https://github.com/HarshvardhanSingh-13/Datasets"

df = pd.read_excel('/content/Datasets/Flight Prices/flight_price.xlsx')

df





