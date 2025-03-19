import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['day_of_week'] = df['hour_beginning'].dt.day_name()

# Q1: Filtering Data for Weekdays and Plotting Pedestrian Counts
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
filtered_df = df[df['day_of_week'].isin(weekdays)]
weekday_counts = filtered_df.groupby("day_of_week")["Pedestrians"].sum()
weekday_counts = weekday_counts.reindex(weekdays)

plt.figure(figsize=(8,5))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o', linestyle='-', color='b')
plt.xlabel("Day of the Week")
plt.ylabel("Total Pedestrian Count")
plt.title("Pedestrian Count for Each Weekday")
plt.grid(True)
plt.show()

# Q2: Tracking Pedestrian Counts on Brooklyn Bridge and Weather Influence
df_2019 = df.loc[(df['hour_beginning'].dt.year == 2019) & (df['location'] == "Brooklyn Bridge")]
df_2019 = df_2019[['weather_summary', 'Pedestrians']]
df_encoded = pd.get_dummies(df_2019, columns=['weather_summary'])
correlation_matrix = df_encoded.corr()

plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Weather and Pedestrian Counts on Brooklyn Bridge (2019)')
plt.show()

# Q3: Categorizing Time of Day and Analyzing Activity Patterns
def categorize_time(hour):
    if 5 <= hour < 11:
        return 'Morning'
    elif 11 <= hour < 16:
        return 'Afternoon'
    elif 16 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df['Time_of_Day'] = df['hour_beginning'].dt.hour.apply(categorize_time)
activity_counts = df['Time_of_Day'].value_counts().reindex(['Morning', 'Afternoon', 'Evening', 'Night'])

plt.figure(figsize=(8,5))
plt.bar(activity_counts.index, activity_counts.values, color=['blue', 'orange', 'green', 'red'])
plt.xlabel("Time of the Day")
plt.ylabel("Pedestrian Activity")
plt.title("Pedestrian Activity throughout the Day")
plt.show()
