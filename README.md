# BiotechFunding-repo

### Authorship
Grace Samuel

---

## Project Overview

### Research Question
Do factors such as therapeutic area, indication, technology type, and phase of development influence the funding a company receives?

### Context
Many biotech companies rely on investor funding for a decade or more before generating revenue. Understanding which types of companies are attracting funding is valuable to executive recruiters and strategic advisors. This analysis provides directional insight to guide stakeholder focus.

As Adam (2024) notes:
> “Unlike other industries, biotech startups often require substantial initial capital to support extensive research and development (R&D), clinical trials, and regulatory approvals before generating any revenue.”

### Stakeholders
- Two firm partners (non-technical decision-makers)
- Four-person research team (technical audience)
- Head of Data Science (project lead and analyst)

Model insights help categorize companies into high, medium, and low likelihood tiers of funding success.

---

## Hypothesis & Prediction

**Hypothesis**  
Historical data reveals patterns that allow us to predict funding amounts based on company characteristics.

**Prediction**  
Companies aligned with popular therapeutic areas, technology types, and development stages will raise more funding.

---

## Data Sources

- **DealForma (2025)**: Biopharma deals and funding history  
- **Federal Reserve**: Federal funds rate and 10-year treasury yield  

### Filters Applied
- U.S.-based public (small/medium) and private biopharma only  
- Excluded device, diagnostic, manufacturing sectors  

---

## Data Dictionary (Post-EDA)

| Variable               | Description                           | Notes                            |
|------------------------|---------------------------------------|----------------------------------|
| amount                | Funding amount (USD, log-transformed) | Imputed w/ Random Forest (target) |
| round                 | Funding round                         | Count encoded                    |
| completed_year        | Deal year                             | Median imputed                   |
| federal_fund_effective_rate | Macroeconomic rate             | Numeric                          |
| stage_at_funding      | Drug development stage                | Top 6 + "Other"                  |
| primary_ta            | Therapeutic area                      | Collapsed & encoded              |
| indications           | Indication type                       | Top 10 + "Other"                 |
| primary_tech          | Technology type                       | Top 19 + "Other"                 |
| company_type          | Public small/medium/private           | Encoded                          |
| location              | State                                 | Top 5 + "Other"                  |
| business_model        | Business model                        | Encoded                          |
| public_private        | Public (0) vs Private (1)             | Binary encoded                   |

---

## Methods

### Preprocessing
- Dropped high-missingness and collinear features
- Count encoding for categorical variables
- Median and model-based imputation
- Log transformation and standard scaling

### Modeling Techniques

#### Unsupervised Learning
- PCA for dimensionality reduction
- K-Means Clustering for profiling

#### Supervised Learning
- Linear Regression (baseline)
- Random Forest Regressor
- XGBoost Regressor (best performer)
- MLP Neural Network

### Hyperparameter Tuning
Conducted GridSearchCV and RandomizedSearchCV across:
- `max_depth`, `n_estimators`, `learning_rate` (XGBoost)
- `hidden_layer_sizes`, `alpha`, `activation` (MLP)

Improved XGBoost MAE by ~3 million through tuning. Test MAE: ~$43 million.

### Evaluation Metrics
- MAE, MSE, R² (for regression)
- Silhouette Score (clustering)
- Explained Variance Ratio (PCA)

### Validation
- 5-fold cross-validation
- Train/test split before imputation and transformation
- Repeated testing on multiple platforms

---

## Results

- XGBoost performed best, balancing interpretability and accuracy.
- High funding amounts were associated with companies in gene therapy and oncology.
- Directional insight is more important than exact dollar predictions for stakeholders.
- Final test MAE: ~$43 million

---

## Tools Used

- Python 3.12
- pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn
- Jupyter Notebook + GitHub

---

## Custom Functions

Defined in `main.py` or `utils.py`:

```python
def count_encode(train_col, test_col):
    freq = train_col.value_counts()
    return train_col.map(freq).fillna(0), test_col.map(freq).fillna(0)

def model_impute_missing_values(X_train, y_train, X_missing):
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    return rf.predict(X_missing)
```

---

## How to Reproduce

### Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run Script

```bash
git clone https://github.com/gsamuel24/DSE6311-repo.git
cd DSE6311-repo
python main.py
```

This will:
- Load and preprocess data
- Apply transformations
- Run PCA, clustering, and tuned models
- Output evaluation results and visuals

---

## Testing & Validation

- Self-tested (Windows, Python 3.12)  
- User-tested (MacOS, Python 3.10)  
- Comments in code denote transformation checkpoints

Random seeds (`random_state=42`) used to ensure reproducibility.

---

## References

- Adam, J. (2024, July 5). *The ABC of biotech startup funding*. [Labiotech.eu](https://www.labiotech.eu/expert-advice/biotech-startup-funding/)
- Gatlin, A. (2025, Jan 13). *Biotech stocks prepare for action in 2025*. [Investor's Business Daily](https://www.investors.com/news/technology/biotech-stocks-2025-weight-loss-drugs-ai-trump/)
- [DealForma](https://www.dealforma.com)
- [Federal Reserve](https://www.federalreserve.gov/datadownload/)
