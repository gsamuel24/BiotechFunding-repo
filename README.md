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

### Data Dictionary (Post-EDA)

| Variable Name                  | Description                                  | Details                                           | Role            |
|-------------------------------|----------------------------------------------|--------------------------------------------------|-----------------|
| `amount`                      | Funding amount (USD)                         | Log-transformed; imputed via Random Forest       | Target Variable |
| `round`                       | Funding round                                | Count encoded; 16 levels                         | Predictor       |
| `completed_year`              | Year the deal closed                         | Numeric; median imputed                          | Predictor       |
| `federal_fund_effective_rate` | Federal fund rate at time of funding         | Numeric; median imputed                          | Predictor       |
| `stage_at_funding`            | Drug development stage                       | Top 6 + 'Other'; count encoded                   | Predictor       |
| `primary_ta`                  | Primary therapeutic area                     | Collapsed + count encoded                        | Predictor       |
| `indications`                 | Indication targeted                          | Top 10 + 'Other'; count encoded                  | Predictor       |
| `primary_tech`                | Core technology used                         | Top 19 + 'Other'; count encoded                  | Predictor       |
| `company_type`                | Company classification                       | Count encoded (3 nominal categories)             | Predictor       |
| `location`                    | Headquarters state                           | Top 5 states + 'Other'; count encoded            | Predictor       |
| `business_model`              | Business model description                   | Count encoded (12 nominal categories)            | Predictor       |
| `public_private`              | Public vs. Private                           | Binary encoded (0 = Public, 1 = Private)         | Predictor       |

---

### Analysis Plan

**Preprocessing Steps:**
- Dropped high-missingness predictors (`lead_investor_this_round`, `lead_investor_co_type`)
- Dropped highly collinear variables (`total_raised_all_rounds`, `10yr_treasury_yield`)
- Removed Public Large companies (skewed and not relevant to stakeholders)
- Count encoding for nominal categorical variables
- Median imputation for skewed numerical predictors
- Random Forest imputation for target variable (`amount`)
- Log transformation of `amount`
- StandardScaler applied to all features

**Modeling Techniques:**
- **Unsupervised Learning:**
  - PCA for dimensionality reduction
  - K-Means clustering to identify company profiles

- **Supervised Learning:**
  - Linear Regression (baseline)
  - Random Forest Regressor
  - Neural Network (basic and regularized)

**Evaluation Metrics:**
- MAE, MSE, R² for regression
- Silhouette Score for clustering
- Explained variance ratio for PCA

**Validation:**
- 5-fold cross-validation
- Hyperparameter tuning via grid or random search

**Success Criteria:**
- The hypothesis will be supported if models can accurately predict funding amounts on unseen data.

---

### Tools

- Python  
- pandas, numpy, scikit-learn, seaborn, matplotlib  
- GitHub for version control

---

### Project Repo

[GitHub Project Link](http://github.com/gsamuel24)

---

### References

- Adam, J. (2024, July 5). *The ABC of biotech startup funding*. Labiotech.eu. https://www.labiotech.eu/expert-advice/biotech-startup-funding/  
- Gatlin, A. (2025, January 13). *Biotech stocks prepare for action in 2025: Weight-loss drugs, AI, and Trump 2.0 are the catalysts.* Investor's Business Daily. https://www.investors.com/news/technology/biotech-stocks-2025-weight-loss-drugs-ai-trump/  
- DealForma. https://www.dealforma.com  
- Federal Reserve. https://www.federalreserve.gov/datadownload/

---

### Reproducibility & Setup Instructions

This project is written entirely in **Python 3.12+** and is structured to allow others to reproduce the analysis from start to finish.

### Requirements

The following packages are required to run the code:

```bash
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

You can install them using pip:

```bash
pip install -r requirements.txt
```

### How to Run the Analysis

1. Clone the repo:

```bash
git clone https://github.com/gsamuel24/DSE6311-repo.git
cd DSE6311-repo
```

2. Upload or place the cleaned dataset in the same folder as the script file.
3. Run the script file to execute the full pipeline:

```bash
python main.py
```

This will:
- Load and preprocess the dataset
- Apply encoding, imputation, normalization, and transformation
- Run PCA, clustering, and multiple regression models
- Output visualizations and model metrics

---

### Custom Functions

Several custom helper functions were written for this project and can be found in the `utils.py` file (if separated) or defined within `main.py`.

### Example Functions

```python
def count_encode(train_col, test_col):
    """
    Apply count encoding to a categorical column.

    Parameters:
    train_col (pd.Series): Training set column
    test_col (pd.Series): Test set column

    Returns:
    Tuple[pd.Series, pd.Series]: Encoded training and test columns
    """
    freq = train_col.value_counts()
    return train_col.map(freq).fillna(0), test_col.map(freq).fillna(0)
```

```python
def model_impute_missing_values(X_train, y_train, X_missing):
    """
    Impute missing target values using a Random Forest Regressor.

    Parameters:
    X_train (pd.DataFrame): Features for known targets
    y_train (pd.Series): Known target values
    X_missing (pd.DataFrame): Features where target is missing

    Returns:
    np.ndarray: Imputed target values
    """
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    return rf.predict(X_missing)
```
---

### Reproducibility Notes

- Random seed is set using `np.random.seed(42)` and `random_state=42` in model calls
- Test/train split occurs before any transformation or imputation to prevent data leakage
- Log transformation, standardization, and encoding follow best practices to ensure validity

---

---

### Code Testing & Validation

All code for this project has been both **self-tested** and **user-tested** to ensure it runs smoothly on multiple environments.

- **Self-Tested**: The full pipeline was run locally using Python 3.12 on a Windows machine. No runtime errors occurred, and all expected outputs (transformed datasets, model performance metrics, and visualizations) were generated successfully.

- **User-Tested**: The same scripts were run on a MacOS machine by another user (non-author). The project executed without modification or error, confirming platform independence.

```python
# TEST PASSED: Dataset loaded and preprocessed without missing values.
# TEST PASSED: Count encoding matches expected category frequency.
# TEST PASSED: Log transformation and StandardScaler applied correctly.
# TEST PASSED: Models trained and evaluated without errors.
```

This validation process ensures that the project is reproducible, stable, and portable across systems.

---
