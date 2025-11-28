# Data Folder

This folder contains datasets used by the agentic FB Ads analysis pipeline.

## Files

- `synthetic_fb_ads_undergarments.csv`  
  Full dataset provided in the assignment.

- `sample_fb_ads.csv`  
  A smaller subset (~200 rows) used when `use_sample_data: true` in `config/config.yaml`.

## Usage

The system will automatically select the dataset based on configuration:

- Full dataset:
  ```yaml
  use_sample_data: false