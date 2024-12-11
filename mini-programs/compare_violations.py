import pandas as pd

def compare_violations(csv_file, dict_file):
    # Read the CSV file
    df = pd.read_csv(csv_file, encoding='utf-8')
    
    # Load the dictionary file as a module
    with open(dict_file, 'r', encoding='utf-8') as f:
        exec(f.read(), globals())
    
    # Get unique article codes from CSV
    csv_violations = df[['Article', 'FineReasonText']].drop_duplicates()
    csv_violations = csv_violations[csv_violations['Article'].notna()]
    
    # Convert to dictionary for easier comparison
    csv_dict = dict(zip(csv_violations['Article'], csv_violations['FineReasonText']))
    
    # Get all unique codes
    all_codes = sorted(set(list(csv_dict.keys()) + list(traffic_violations.keys())))
    
    # Print comparison
    print("\n=== Traffic Violations Code Comparison ===")
    print(f"{'Code':<15} {'In CSV':<10} {'In Dict':<10}")
    print("-" * 35)
    
    for code in all_codes:
        in_csv = "✓" if code in csv_dict else "❌"
        in_dict = "✓" if code in traffic_violations else "❌"
        print(f"{code:<15} {in_csv:<10} {in_dict:<10}")
    
    # Print detailed comparison for investigation
    print("\n=== Detailed Comparison ===")
    for code in all_codes:
        print(f"\nCode: {code}")
        if code in csv_dict:
            print(f"CSV  : {csv_dict[code][:100]}...")
        else:
            print("CSV  : Not present")
            
        if code in traffic_violations:
            print(f"Dict : {traffic_violations[code][:100]}...")
        else:
            print("Dict : Not present")
            
    # Print statistics
    print("\n=== Statistics ===")
    print(f"Total unique codes in CSV: {len(csv_dict)}")
    print(f"Total unique codes in Dictionary: {len(traffic_violations)}")
    print(f"Codes in CSV but not in Dictionary: {len(set(csv_dict.keys()) - set(traffic_violations.keys()))}")
    print(f"Codes in Dictionary but not in CSV: {len(set(traffic_violations.keys()) - set(csv_dict.keys()))}")

if __name__ == "__main__":
    compare_violations('unique_articles.csv', 'dictionary.py')