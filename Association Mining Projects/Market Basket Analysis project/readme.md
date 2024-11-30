# **Market Basket Analysis Using Association Rule Mining**  
This project focuses on performing Market Basket Analysis using association rule mining to identify patterns in customer purchasing behavior. The goal is to leverage these insights for enhancing retail strategies such as cross-selling, product placement, and targeted promotions.  

---

## **Table of Contents**  
- [Project Overview](#project-overview)  
- [Key Features](#key-features)  
- [Dataset](#dataset)  
- [Methodology](#methodology)  
- [Results](#results)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## **Project Overview**  
Market Basket Analysis is a data mining technique used to uncover relationships between products purchased together. This project applies association rule mining to identify high-lift combinations, frequently purchased products, and behavioral patterns to inform business decisions in retail.  

---

## **Key Features**  
- Analysis of top product combinations based on support, confidence, and lift.  
- Identification of cross-selling and upselling opportunities.  
- Recommendations for store layout and targeted marketing campaigns.  

---

## **Dataset**  
The dataset used contains transactional records with information such as:  
- Product names  
- Purchase frequency  
- Association between products  

---

## **Methodology**  
1. **Data Preprocessing:**  
   - Cleaning and organizing transactional data for analysis.  
2. **Association Rule Mining:**  
   - Extracting rules using metrics like support, confidence, and lift.  
3. **Result Interpretation:**  
   - Visualizing and interpreting the top 10 rules based on lift for actionable insights.  

---

## **Results**  
### **Key Findings:**  
- "Whole milk" emerged as a frequently purchased product with strong associations.  
- Complementary products like "Other vegetables" and "Bottled water" show high lift values.  

### **Recommendations:**  
- Implement cross-selling strategies and optimize store layouts for increased sales.  

---

## **Installation**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/ajaywhite/market-basket-analysis.git

2. Navigate to the project directory:
   ```bash
   cd market-basket-analysis  
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## **Dependencies** ##
The following Python libraries are required for this project:

- pandas: Data manipulation and analysis
- mlxtend: Association rule mining (apriori algorithm and rule generation)
- matplotlib: Visualization of results
- seaborn: Enhanced data visualization
- numpy: Numerical computations

## **License** ##
- This project is licensed under the MIT License. See the LICENSE file for more details.


## **Contact** ##
For any questions or feedback, feel free to reach out:

- GitHub: ajaywhite
- Email: ajay09official@gmail.com
