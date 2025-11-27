# Facebook Ads Performance Analysis – Agentic AI System

## 1️⃣ Overview

This project analyzes a synthetic Facebook Ads dataset for an undergarments brand and automatically produces two outputs:

- **reports/insights.json** → Key performance insights  
- **reports/creatives.json** → Recommended creative ideas and targeting strategy  

The analysis is performed using a lightweight agentic workflow implemented in Python.

---

## 2️⃣ Dataset Summary

Dataset file: `data/synthetic_fb_ads_undergarments.csv`

Metrics included:
| Metric | Meaning |
|--------|---------|
| spend | Total ad spend |
| impressions | Times ad was viewed |
| clicks | User interactions |
| purchases | Conversions |
| revenue | Value generated |
| roas | Return On Ad Spend |

Additional attributes analyzed:
- platform (FB/IG)
- country (UK/IN/US)
- audience_type (Retargeting/Broad/Lookalike etc.)
- creative_type (UGC/Video/Image etc.)

---

## 3️⃣ Approach Used

| Component | Function |
|----------|----------|
| PlannerAgent | Defines analysis steps |
| AnalystAgent | Loads dataset, computes metrics & generates insights |
| run.py | Executes analyst to produce final JSON outputs |

Metrics calculated:
- **CPC** = spend / clicks  
- **CPM** = spend / impressions × 1000  
- **CVR** = purchases / clicks  

---

## 4️⃣ Key Findings

📌 *Based on mean & aggregate performance across dataset:*

| Category | Best Performer | Why |
|---------|----------------|-----|
| Campaign | MEN PREMIUM - ODAL | Highest ROAS |
| Platform | Facebook | Best revenue contribution |
| Country | UK | Strongest conversion behavior |
| Creative Type | UGC | Best ROAS & engagement |
| Audience Targeting | Retargeting | Lowest CPC |

---

## 5️⃣ Recommendations

To improve performance further:
- Focus spend on **Facebook** over Instagram
- Expand **UGC creatives** with real testimonials
- Prioritize **UK retargeting audiences**
- Increase ads related to the **MEN PREMIUM - ODAL** product line

These are programmatically generated in `creatives.json`.

---

## 6️⃣ How to Run

From project root, run:

```bash
python3 src/run.py
