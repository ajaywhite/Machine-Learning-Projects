Restaurant Recommendation System
# Restaurant Recommendation System
## Overview
This project implements a content-based filtering recommendation system for restaurants. Using a
dataset of restaurants, it recommends restaurants based on user preferences, focusing on cuisines
and average cost for two.
## Features
- Preprocess and encode categorical features.
- Normalize numerical features to ensure equal importance in similarity calculations.
- Implement content-based filtering using cosine similarity.
- Provide recommendations based on user input.
- Visualize recommendations with scatter and bar plots.
## Requirements
Before running the project, ensure you have the following Python packages installed:
- `pandas`
- `numpy`
- `matplotlib`
- `category_encoders`
- `scikit-learn`
You can install these packages using the following command:
```bash
pip install pandas numpy matplotlib category_encoders scikit-learn
```
## Dataset
The dataset should be in CSV format and include the following columns:
- `Restaurant Name`: The name of the restaurant.
- `Cuisines`: The types of cuisines offered by the restaurant, separated by commas.
- `Average Cost for two`: The average cost for two people dining at the restaurant.
Ensure that your dataset is placed at the specified path in the script. You can modify the path to
your dataset as needed:
```python
df = pd.read_csv("D:/Machine Learning Intern/RestuartantRecommdendation/dataset.csv")
```
## Setup and Execution
1. **Clone the Repository**
 ```bash
 git clone https://github.com/ajaywhite/restaurant-recommendation-system.git
 cd restaurant-recommendation-system
 ```
2. **Install Dependencies**
 Make sure all required libraries are installed. You can use the provided `requirements.txt` file for
this:
 ```bash
 pip install -r requirements.txt
 ```
3. **Run the Script**
 Execute the script using a Python environment:
 ```bash
 python recommendation_system.py
 ```
4. **Input and Recommendations**
 When prompted, enter your favorite restaurant name to receive recommendations. The script will
display recommended restaurants and visualize them using scatter and bar plots.
## Script Details
### Data Preprocessing
- **Removing Null Rows:** Rows with missing values in the `Cuisines` or `Average Cost for two`
columns are removed.
- **Encoding Categorical Features:** The `Cuisines` column is split into individual cuisines, and each
cuisine is represented as a binary feature.
- **Normalization:** The `Average Cost for two` column is normalized to a range of 0 to 1.
### Content-Based Filtering
- **Cosine Similarity:** The script calculates the cosine similarity between restaurants based on their
encoded features and the normalized average cost.
- **Recommendations:** Based on the cosine similarity, the script provides recommendations for
similar restaurants.
### Visualization
- **Scatter Plot:** Plots the relationship between the average cost for two and the similarity score of
the recommended restaurants.
- **Bar Plot:** Displays the top recommended restaurants sorted by similarity score.
## Example Usage
Here's an example of how to use the recommendation system:
```python
# Load the dataset
df = pd.read_csv("path/to/your/dataset.csv")
# Clean and preprocess the data
df_cleaned = df.dropna(subset=['Cuisines', 'Average Cost for two'])
df_cleaned.reset_index(drop=True, inplace=True)
# Encode the categorical data and prepare the features
# ...
# Get recommendations for a sample restaurant
sample_restaurant = "Your Favorite Restaurant"
recommended_restaurants = get_recommendations(sample_restaurant)
print(recommended_restaurants)
# Visualize the recommendations
# ...
```
## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes
you would like to make.
