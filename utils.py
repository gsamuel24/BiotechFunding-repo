import pandas as pd

def collapse_categories(series, top_n, other_name="Other"):
    top_categories = series.value_counts().nlargest(top_n).index
    return series.apply(lambda x: x if x in top_categories else other_name)

def count_encode(train_col, test_col):
    freq = train_col.value_counts()
    return train_col.map(freq).fillna(0), test_col.map(freq).fillna(0)

def encode_data(train_df, test_df):
    train_encoded = train_df.copy()
    test_encoded = test_df.copy()

    # Example count encoding (add your full version here)
    train_encoded['round'], test_encoded['round'] = count_encode(train_encoded['round'], test_encoded['round'])

    return train_encoded, test_encoded

def model_impute_missing_values(X_train, y_train, X_missing):
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    return rf.predict(X_missing)
