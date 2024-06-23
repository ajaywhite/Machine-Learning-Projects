Restaurant Recommendation System
Overview
This project implements a content-based filtering recommendation system for restaurants. It suggests restaurants based on user preferences, focusing on features such as cuisines offered and the average cost for two people.

Features
Data Preprocessing: Clean and encode categorical data.
Normalization: Normalize numerical features for accurate similarity calculations.
Content-Based Filtering: Recommend similar restaurants using cosine similarity.
Visualization: Visualize recommendations with scatter and bar plots.
Requirements
Ensure you have the following Python libraries installed:

pandas
numpy
matplotlib
category_encoders
scikit-learn
Install these dependencies using the command:


pip install pandas numpy matplotlib category_encoders scikit-learn
Dataset
Your dataset should be in CSV format and include columns such as:

Restaurant Name: The name of the restaurant.
Cuisines: The cuisines offered, separated by commas.
Average Cost for two: The average cost for two people.
Make sure the dataset path in the script is correctly set. Update the path as necessary:


df = pd.read_csv("D:/Machine Learning Intern/RestuartantRecommdendation/dataset.csv")
Setup and Execution
Clone the Repository


git clone https://github.com/your-username/restaurant-recommendation-system.git
cd restaurant-recommendation-system
Install Dependencies
Install the required libraries using the provided requirements.txt:


pip install -r requirements.txt
Run the Script
Execute the script in your Python environment:


python recommendation_system.py
Input and Recommendations
When prompted, enter the name of your favorite restaurant to receive similar restaurant recommendations. The script will display and visualize the results.

Script Details
Data Preprocessing
Removing Null Rows: Drop rows with missing values in the Cuisines or Average Cost for two columns.
Encoding Categorical Features: Split and encode the Cuisines column into binary features for each unique cuisine.
Normalization: Normalize the Average Cost for two column to a range of 0 to 1.
Content-Based Filtering
Cosine Similarity: Calculate cosine similarity between restaurants based on their features.
Recommendations: Generate restaurant recommendations based on user-specified restaurant name.
Visualization
Scatter Plot: Plot the relationship between the average cost for two and the similarity score.
Bar Plot: Display top recommended restaurants sorted by similarity score.
