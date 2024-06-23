#import necessary python library
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from category_encoders import TargetEncoder
from sklearn.preprocessing import LabelEncoder, StandardScaler

# import dataset
df = pd.read_csv("D:/Machine Learning Intern/RestuartantRecommdendation/dataset.csv")
df.head()

#remove null rows
df_cleaned = df.dropna(subset = ['Cuisines', 'Average Cost for two'])
df_cleaned.reset_index(drop = True)
df_cleaned.shape

#Categorical value into numerical 
Target_encode = TargetEncoder()
Label_enode = LabelEncoder()

#split the cuisines
cuisines_split = df_cleaned['Cuisines'].str.split(', ')
unique_cuisines = set(c for sublist in cuisines_split for c in sublist)
unique_cuisines_list = list(unique_cuisines)
cuisines_encoded = pd.DataFrame(0, index = df_cleaned.index, columns = unique_cuisines_list)
                      
for idx, cuisine_list in zip(df_cleaned.index, cuisines_split):
    unique_cuisine_list = list(set(cuisine_list))
    cuisines_encoded.loc[idx, unique_cuisine_list] =1

#rearrange the dataset
df_with_cuisines = pd.concat([df_cleaned, cuisines_encoded], axis =1)
df_with_cuisines.drop('Cuisines', axis=1, inplace = True)
print(df_with_cuisines.head())

#Implement content Based filtering
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#Normalize the 'Average Cost for two; column to ensure equal importance
df_with_cuisines['Average Cost for two'] = (df_with_cuisines['Average Cost for two'] - df_with_cuisines['Average Cost for two'].min())/(df_with_cuisines['Average Cost for two'].max() - df_with_cuisines['Average Cost for two'].min())

#define feature
features = unique_cuisines_list + ['Average Cost for two']
features_matrix = df_with_cuisines[features].values
cosine_sim = cosine_similarity(features_matrix)
                      
#function to get recommendation based on restaurant name
def get_recommendations(restaurant_name, cosine_sim = cosine_sim, num_recommendations = 10):
    idx_list = df_with_cuisines.index[df_with_cuisines['Restaurant Name'] == restaurant_name].tolist()
    if not idx_list:
        print(f"Restaurant '{restaurant_name}' not found.")
        return pd.DataFrame()
    idx =idx_list[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:num_recommendations+1]
    restaurant_indices = [i[0] for i in sim_scores]
    return df_with_cuisines.iloc[restaurant_indices][['Restaurant Name', 'Average Cost for two'] + unique_cuisines_list]
print("The model build successfully!")

#Test

# Get recommendations for a sample restaurant
sample_restaurant = str(input("Enter your Favourite food item:"))
recommended_restaurants = get_recommendations(sample_restaurant)
print(recommended_restaurants)

# Checking if the recommendations are not empty
if not recommended_restaurants.empty:
    # Extract similarity scores for plotting
    sample_index = df_with_cuisines.index[df_with_cuisines['Restaurant Name'] == sample_restaurant].tolist()[0]
    sim_scores = cosine_similarity(features_matrix[sample_index].reshape(1, -1), features_matrix)
    sim_scores = sim_scores[0][recommended_restaurants.index]
    recommended_restaurants['Similarity Score'] = sim_scores

    print(recommended_restaurants)
else:
    print(f"No recommendations available for '{sample_restaurant}'.")

# 1.Scatter plot of Average Cost for two vs. Similarity Score
if not recommended_restaurants.empty:
    plt.figure(figsize=(10, 6))
    plt.scatter(recommended_restaurants['Average Cost for two'], recommended_restaurants['Similarity Score'], c='blue', alpha=0.5)
    plt.title('Average Cost for Two vs. Similarity Score')
    plt.xlabel('Average Cost for Two')
    plt.ylabel('Similarity Score')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


# 2.Bar plot of top recommended restaurants by similarity score
if not recommended_restaurants.empty:
    top_recommendations = recommended_restaurants[['Restaurant Name', 'Similarity Score']].sort_values(by='Similarity Score', ascending=False)

    plt.figure(figsize=(12, 6))
    plt.barh(top_recommendations['Restaurant Name'], top_recommendations['Similarity Score'], color='orange')
    plt.xlabel('Similarity Score')
    plt.title('Top Recommended Restaurants')
    plt.gca().invert_yaxis()  # Highest score at the top
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()
