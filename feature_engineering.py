def create_features(df):
    df['Demand'] = df['Rating Count'] * df['Rating']
    df['Discount'] = df['Actual Price'] - df['Discount Price']
    df['Category'] = df['Category'].astype('category').cat.codes

    X = df[['Category', 'Discount Price', 'Actual Price', 'Discount', 'Rating']]
    y = df['Demand']

    return X, y