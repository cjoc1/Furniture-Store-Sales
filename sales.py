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

# Given data for Average Purchase Frequency by Country
country_data = {'country': ['Australia', 'Belgium', 'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'India', 'Ireland',
                             'Israel', 'Italy', 'Luxembourg', 'Moldova', 'Netherlands', 'Norway', 'South Africa', 'Spain',
                             'Sweden', 'Switzerland', 'United Arab Emirates', 'United Kingdom', 'United States'],
                'average_purchase_frequency': [1] * 22}

# Create a Pandas DataFrame
country_df = pd.DataFrame(country_data)

# Create subplots
plt.subplot(3, 2, 1)  # 3 rows, 2 columns, position 1
plt.bar(df['Product'], df['Total_Revenue'], color='skyblue')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')

plt.subplot(3, 2, 2)  # 3 rows, 2 columns, position 2
plt.bar(payment_df['payment_type'], payment_df['average_order_value'], color='lightgreen')
plt.title('Average Order Value by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Average Order Value')

plt.subplot(3, 2, 3)  # 3 rows, 2 columns, position 3
plt.bar(state_data['state'], state_data['number_of_customers'], color='lightcoral')
plt.title('Number of Customers by State')
plt.xlabel('State')
plt.ylabel('Number of Customers')

plt.subplot(3, 2, 4)  # 3 rows, 2 columns, position 4
plt.bar(sales_df['product'], sales_df['sales_volume'], color='lightcoral')
plt.title('Sales Volume by Product')
plt.xlabel('Product')
plt.ylabel('Sales Volume')

plt.subplot(3, 2, 5)  # 3 rows, 2 columns, position 5
plt.bar(country_df['country'], country_df['average_purchase_frequency'], color='lightblue')
plt.title('Average Purchase Frequency by Country')
plt.xlabel('Country')
plt.ylabel('Average Purchase Frequency')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plots
plt.show()
