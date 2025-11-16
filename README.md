# OIBC-Challenge-2024


This repository contains the full codebase, analysis notebooks, data pipelines, and presentation materials used for the **OIBC (One-Inch Bigdata Competition) Challenge 2024** (https://dataen.ai/challenge).  
The project focuses on forecasting solar power generation, electricity market prices, and weather-related variables using a combination of geospatial information, time-series modeling, and automated data collection.

I ranked 6th among 200 participants at this competition and received encouragement award. 

More specific process of this competiton is in pdf file on OIBC_presentation.pdf

---

## 📂 Repository Structure

```bash
OIBC-Challenge-2024/
│
├── OIBC_GEO.ipynb            # Main notebook: EDA + Geospatial analysis
├── OIBC_GEO.R                # R-based geospatial & statistical analysis
│
├── actual_weather.py         # Weather data crawler (real-time / forecast)
├── electric_capacity.py      # Script for collecting regional capacity data
├── price_day_before.py       # Day-ahead electricity price scraper
├── upload_prediction.py      # Automated prediction upload utility
│
├── OIBC_presentation.pdf     # Final project presentation
└── README.md                 # Project description (this file)
