import pandas as pd
import matplotlib.pyplot as plt

# Given data for Total Revenue by Product
data = {'Product': ['Bed', 'Chair', 'Couch'],
        'Total_Revenue': [30000, 100800, 43200]}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Given data for Average Order Value by Payment Type
payment_data = {'payment_type': ['Amex', 'Diners', 'Mastercard', 'Visa'],
                'average_order_value': [2785.71, 1418.18, 1872.73, 1573.47]}

# Create a Pandas DataFrame
payment_df = pd.DataFrame(payment_data)

# Given data for Number of Customers by State
state_data = {'state': ['AL', 'AZ', 'Alberta', 'Andhra Pradesh', 'British Columbia', 'Brussels (Bruxelles)', 'CA', 'CO',
                         'Chisinau', 'Cork', 'Dubayy', 'Dublin', 'England', 'FL', 'Frederiksborg', 'GA', 'Gauteng', 'Geneve',
                         'HI', 'IA', 'ID', 'IL', 'Ile-de-France', 'Ita-Suomen Laani', 'Kobenhavn', 'Lombardy', 'Luxembourg',
                         'MD', 'MO', 'Meath', 'Michigan', 'Murcia', 'NC', 'NH', 'NJ', 'NY', 'Noord-Brabant', 'Noord-Holland',
                         'Nordrhein-Westfalen', 'Northern Ireland', 'OH', 'OR', 'Ontario', 'Oslo', 'Queensland', 'Rogaland',
                         'Saskatchewan', 'Stockholm', 'Storstrom', 'TN', 'TX', 'Tel Aviv', 'UT', 'VA', 'VT', 'Vaud', 'Victoria'],
               'number_of_customers': [1, 1, 3, 1, 4, 1, 4, 1, 1, 1, 1, 2, 9, 6, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1,
                                        1, 1, 1, 1, 1, 1, 1, 2, 6, 1, 1, 1, 2, 2, 1, 1, 3, 1, 2, 1, 2, 2, 2, 2, 2, 2, 0, 0]}

# Ensure both lists have the same length
if len(state_data['state']) != len(state_data['number_of_customers']):
    raise ValueError("Error: Lengths of 'state' and 'number_of_customers' must be the same.")

# Given data for Sales Volume by Product
sales_data = {'product': ['Chair', 'Couch', 'Bed'],
              'sales_volume': [84, 12, 4]}

# Create a Pandas DataFrame
sales_df = pd.DataFrame(sales_data)

# Given data for Total Purchases by Country
country_data = {'country': ['Australia', 'Belgium', 'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'India', 'Ireland',
                             'Israel', 'Italy', 'Luxembourg', 'Moldova', 'Netherlands', 'Norway', 'South Africa', 'Spain',
                             'Sweden', 'Switzerland', 'United Arab Emirates', 'United Kingdom', 'United States'],
                'total_purchases': [4, 1, 11, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 3, 10, 48]}

# Create a Pandas DataFrame
country_df = pd.DataFrame(country_data)

# Create subplots
plt.figure(figsize=(15, 12))

plt.subplot(2, 2, 1)
plt.bar(df['Product'], df['Total_Revenue'], color='skyblue')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')

plt.subplot(2, 2, 2)
plt.bar(payment_df['payment_type'], payment_df['average_order_value'], color='lightgreen')
plt.title('Average Order Value by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Average Order Value')

plt.subplot(2, 2, 3)
plt.bar(sales_df['product'], sales_df['sales_volume'], color='lightcoral')
plt.title('Sales Volume by Product')
plt.xlabel('Product')
plt.ylabel('Sales Volume')

plt.subplot(2, 2, 4)
plt.bar(country_df['country'], country_df['total_purchases'], color='lightblue')
plt.title('Total Purchases by Country')
plt.xlabel('Country')
plt.ylabel('Total Purchases')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility

plt.tight_layout()

# Display the plots
plt.show()

