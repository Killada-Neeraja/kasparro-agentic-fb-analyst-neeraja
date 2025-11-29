# Data Description

This folder contains the datasets used by the Agentic Facebook Performance Analyst.

---

## Datasets
- `synthetic_fb_ads_undergarments.csv`  
  Full synthetic dataset provided in the assignment. Used for complete analysis runs.
- `sample_fb_ads.csv`  
  Smaller subset of the full dataset, used for faster development and testing.

---

## Dataset Switching

The dataset is controlled via `config/config.yaml`:
- `use_sample_data: true` → use `sample_fb_ads.csv`
- `use_sample_data: false` → use `synthetic_fb_ads_undergarments.csv`

You can also adjust:
- `sample_fraction` → how much of the full dataset to keep when sampling (if used in code).
---

## Columns Overview
Both files share the same schema, including:
- `campaign_name`, `adset_name`, `date`
- `spend`, `impressions`, `clicks`
- `ctr`, `purchases`, `revenue`, `roas`
- `creative_type`, `creative_message`
- `audience_type`, `platform`, `country`
