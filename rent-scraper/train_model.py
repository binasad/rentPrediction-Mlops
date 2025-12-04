import pandas as pd

# 1. Load the data
df = pd.read_csv('housing.csv')

# --- PREPROCESSING FUNCTIONS ---
def clean_price(price_text):
    if not isinstance(price_text, str): return price_text
    parts = price_text.split()
    number = float(parts[0])
    unit = parts[1]
    
    if unit == "Crore":
        return number * 10000000
    elif unit == "Lakh":
        return number * 100000
    return number

def clean_area(area_text):
    if not isinstance(area_text, str): return area_text
    parts = area_text.split() 
    number = float(parts[0])
    unit = parts[1]
    
    if unit == "Kanal":
        return number * 20  # <--- The logic you just solved!
        
    return number # Assumes it's already Marla

# --- APPLYING THE CLEANING ---
df['Price'] = df['Price'].apply(clean_price)
df['Area'] = df['Area'].apply(clean_area)

# Remove any rows that failed to clean (just in case)
df = df.dropna()

print("Data is clean! Here are the first 5 rows:")
print(df.head())

# ... (Previous cleaning code) ...

# 5. One-Hot Encoding
# This converts 'Location' into multiple numerical columns
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# 6. Verify the final data
print("--------------------------------")
print("Data is ready for training!")
print(df.head())
print("--------------------------------")
print(f"Total columns: {len(df.columns)}")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib # To save the model file

# 1. Separate Features (X) and Target (y)
# X = The input data (Area, Beds, Location_...)
# y = The answer we want to predict (Price)
X = df.drop('Price', axis=1) 
y = df['Price']

# 2. Split the data
# test_size=0.2 means 20% is saved for the exam
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} houses. Testing on {len(X_test)} houses.")

# 3. Train the Model! 🧠
model = LinearRegression()
model.fit(X_train, y_train)

print("Model has been trained!")

# ... (Previous training code) ...

# 4. Save the Model
joblib.dump(model, 'model.pkl')
print("Model saved to 'model.pkl'")

# 5. Save the Column Names (Crucial for the API!)
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Model columns saved to 'model_columns.pkl'")