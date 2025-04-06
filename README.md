# DSE6311-repo

## Capstone Course

### Basics
This paper outlines the finalized project proposal for Team Epsilon, which is operated by Grace Samuel who covers all roles of Team Lead, Recorder, and Spokesperson.

---

### Background & Questions

This project is centered around the research question:  
**Do factors such as therapeutic area, indication, technology type, and phase of development influence the funding a company receives?**

In the context of executive recruitment, insight into this question is highly valuable. Many biotech companies rely entirely on investor funding for a decade or more as they progress through the drug development process. As Adam (2024) notes:

> “Unlike other industries, biotech startups often require substantial initial capital to support extensive research and development (R&D), clinical trials, and regulatory approvals before generating any revenue. This high-risk, high-reward environment makes navigating the biotech startup funding landscape particularly complex.”

Investor funding plays a crucial role in the success of any biotech company, and identifying those with strong financial backing serves as an indicator of their ability to grow and hire new employees.

For executive search firms, understanding where investors are focusing allows for more targeted engagement with stable clients. It also supports long-term relationship building and positions the firm to anticipate and respond to market shifts. If a model reveals trends—such as a rise in gene therapy investment that later shifts to cell therapy—the firm can adapt more quickly than competitors and deliver real-time market insights.

Addressing this question has direct implications for business strategy, informing decisions about which companies to prioritize, which conferences to attend, and how to allocate time and resources. This question is considered truly novel, as it reflects a current business challenge being explored within the firm, and no similar models have been identified in previous investigations.

---

### Identified Stakeholders

In this scenario, the Head of Data Science at XYZ Search Partners is the primary analyst, and all stakeholders are internal to the company.

**Stakeholders include:**
- The two partners of the executive search firm (non-technical decision-makers)
- The research team of four (technical, with advanced understanding)

The Head of Data Science will independently develop the model and present a high-level summary to all stakeholders. Moving forward, meetings will be held separately with partners and researchers. The model will be updated as new data is collected, with researchers assisting in long-term maintenance. The partners will receive monthly updates initially, with the frequency adjusted based on need.

---

### Hypothesis & Prediction

**Hypothesis:**  
Historical funding data can predict the amount of funding a biotech company will receive by revealing patterns related to therapeutic area, indication, technology type, stage of development, and other features.

**Prediction:**  
Biotech companies developing treatments in high-interest therapeutic areas, indications, technology types, and stages of development will receive higher funding amounts.

---

### Data & Methods

Most of the data for this project was sourced from DealForma, a biopharma database that provides detailed information on deals and funding activity within the industry.

**Filters Applied:**
- Public biopharma companies (small, medium, large)
- All private biopharma
- Excluded device, diagnostic, and manufacturing sectors
- Excluded non-U.S. companies

**Additional Sources:**
- Federal funds effective rate and ten-year treasury yield from the Federal Reserve
- These macroeconomic indicators were merged into the DealForma dataset to provide context

> As stated in Gatlin (2025): “Biotech stocks could become more attractive with interest rates coming down and inflation being curbed.”

**Citations:**
- DealForma. (2025). Biotech Funding – Custom Export [funding_data]. Retrieved March 22, 2025, from https://www.dealforma.com  
- Federal Reserve Board. (2025). Interest rates – Selected historical data. https://www.federalreserve.gov/datadownload/

---

### Data Dictionary

| Variable Name             | Variable Description                                 | Details                                               | Role in Analysis          |
|--------------------------|------------------------------------------------------|--------------------------------------------------------|----------------------------|
| amount                   | Amount of funding in USD                            | Numeric – float64 (currency)                           | Outcome Variable           |
| company                  | Biopharma company name                              | Category (string label)                                | Identifier                 |
| round                    | Funding round                                       | Category – One-hot encoded                             | Predictor                  |
| completed                | Date the deal was completed                         | Date – datetime.date                                   | Predictor                  |
| federal_fund_effective_rate | Federal fund effective rate at time of funding    | Numeric – float64                                      | Predictor (macroeconomic)  |
| 10yr_treasury_yield      | Ten-year treasury yield at time of funding          | Numeric – float64                                      | Predictor (macroeconomic)  |
| lead_investor_this_round | Lead investor for that funding instance             | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| lead_investor_co_type    | Lead investor type (e.g., private equity, corp vc)  | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| stage_at_funding         | Drug development stage at time of funding           | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| primary_ta               | Primary therapeutic area of the company             | Category – One-hot encoded                             | Predictor                  |
| indications              | Primary indication of the company                   | Category – One-hot encoded                             | Predictor                  |
| primary_tech             | Primary technology of the company                   | Category – One-hot encoded                             | Predictor                  |
| company_type             | Classification of company (e.g., public small)      | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| location                 | State the company is headquartered in               | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| business_model           | Business model (e.g., early stage R&D only)         | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| public_private           | States if company is public or private              | Category – One-hot encoded (includes 'Unknown')        | Predictor                  |
| total_raised_all_rounds  | Amount USA raised in all funding rounds             | Numeric – float64 (currency)                           | Predictor                  |

---

### Analysis Plan

**Outcome variable:** `amount` (funding amount)  
**Predictor variables:** See table above

**Dataset:**
- ~10,000 rows
- 14 features

**Data Cleaning Steps:**
- One-hot encoding categorical variables
- Normalizing continuous variables
- Handling missing values
- Dropping unnecessary fields

> Note: The `indications` column was cleaned to retain only the primary indication.

**Models Used:**
- **Linear Regression** – Baseline model to assess basic relationships
- **Random Forest Regressor** – For capturing complex patterns and feature importance
- **Feedforward Neural Network**
  - Simple version
  - Advanced version (dropout, batch norm, regularization)
- **K-Means Clustering** – To group companies based on traits and funding
- **PCA (Principal Component Analysis)** – Dimensionality reduction + regression

**Evaluation Metrics:**
- **Supervised Models:** MAE, MSE, R-squared, residual plots, learning curves
- **Unsupervised Models:** Silhouette score (K-Means), explained variance (PCA), cluster plots

**Hyperparameter Tuning:** Grid search or random search

**Success Criteria:**  
If models accurately predict funding on unseen data, the hypothesis is supported.

---

### Tools

All work will be done in **Python**.

---

### Project Repo

[GitHub Project Link](http://github.com/gsamuel24)

---

### References

- Adam, J. (2024, July 5). *The ABC of biotech startup funding*. Labiotech.eu. https://www.labiotech.eu/expert-advice/biotech-startup-funding/
- Gatlin, A. (2025, January 13). *Biotech stocks prepare for action in 2025: Weight-loss drugs, AI, and Trump 2.0 are the catalysts.* Investor's Business Daily. https://www.investors.com/news/technology/biotech-stocks-2025-weight-loss-drugs-ai-trump/
