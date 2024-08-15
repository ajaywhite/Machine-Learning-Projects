===================================
Movie Genre Classification Using LSTM and NLP
===================================

Project Overview
----------------
This project focuses on classifying movies into various genres based on their descriptions.
It leverages Natural Language Processing (NLP) techniques and Long Short-Term Memory (LSTM) networks
to build a robust classification model.

- Objective: Develop a model that can accurately classify movies into genres using their textual descriptions.
- Dataset: The project uses a dataset containing movie descriptions and their corresponding genres.
- Approach: Implemented text preprocessing techniques such as tokenization and TF-IDF vectorization, followed by
  building and training an LSTM-based model.

Key Features
------------
- Text Preprocessing: Utilized `Tokenizer` and `TfidfVectorizer` for feature extraction from movie descriptions.
- LSTM Model: Developed an LSTM model with an embedding layer to capture the sequential information in the text.
- Model Evaluation: Achieved an accuracy of 44% on the validation set. The model performance can be further improved with
  hyperparameter tuning and additional data augmentation.

Results
-------
- Accuracy: 44% on the validation dataset.
- Challenges: Imbalanced genre distribution and tuning the LSTM model for better performance.

Getting Started
---------------
1. Clone the repository:
   git clone https://github.com/ajaywhite/movie-genre-classification.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the Jupyter Notebook to train the model:
   jupyter notebook genreclassification.ipynb

Contributing
------------
Feel free to fork this repository, make enhancements, and submit pull requests.
Your contributions are highly appreciated!

License
-------
This project is licensed under a free license.
