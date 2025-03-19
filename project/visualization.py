import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the data
data= pd.read_csv("global_energy_consumption.csv")

# Check structure
print(data.info())
print(data.head())
print(data.isnull().sum())
data.fillna(0, inplace=True)

df=data.drop_duplicates()
print(df.describe())
print(df)

plt.scatter(df['Year'], df['Total Energy Consumption (TWh)'],marker='.',alpha=0.6, color='blue')
plt.title("Scatter Plot: Year vs Total Energy")
plt.xlabel("Year")
plt.ylabel("Total Energy")
plt.show()

plt.plot(df['Country'], df['Energy Price Index (USD/kWh)'], marker='.', linestyle='-', color='pink')
plt.title("Line Plot: Year vs Energy Price Index")
plt.xlabel("Year")
plt.ylabel("Energy Price Index (USD/kWh)")
plt.show()


sns.boxplot(x='Country', y='Carbon Emissions (Million Tons)', data=df)
plt.title("Box Plot: Carbon Emissions by Country")
plt.xlabel("Country")
plt.ylabel("Carbon Emissions")
plt.xticks(rotation=45, ha='right')
plt.show()


sns.barplot(x='Country', y='Renewable Energy Share (%)', data=df, ci=None, palette="Blues_d")
plt.title("Bar Plot: Renewable Energy by Country")
plt.xlabel("Country")
plt.ylabel("Renewable Energy (%)")
plt.xticks(rotation=45, ha='right')
plt.show()

sns.pairplot(df, vars=['Energy Price Index (USD/kWh)', 'Carbon Emissions (Million Tons)', 'Renewable Energy Share (%)', 'Fossil Fuel Dependency (%)'], hue='Country', diag_kind="kde")
plt.suptitle("Pair Plot of Energy Data", y=1.02)
plt.show()
