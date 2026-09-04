print("=== AI Data Preprocessor ===")
# Try entering something messy like: "   hIRaGana PrAcTiCe" 
raw_data = input("Enter a messy study note (add weird spaces and mixed CaSe): ")

# 1. String Methods: Cleaning the data
clean_data = raw_data.strip().capitalize()
data_length = len(clean_data)
space_count = clean_data.count(" ")

# 2. Conditional Expression (Ternary Operator)
# Categorizing the data in a single line
data_category = "Multi-word phrase" if space_count > 0 else "Single word"

print("\n--- Processing Results ---")
print(f"Original Data : '{raw_data}'")
print(f"Cleaned Data  : '{clean_data}'")
print(f"Total Length  : {data_length} characters")
print(f"Category      : {data_category}")