# Machine Learning for Cyber Threat Detection

## Overview
This project explores the application of machine learning techniques for detecting cybersecurity threats in network traffic data. The objective is to classify connections as normal or malicious using a real-world dataset and evaluate the effectiveness of different models.

## Objectives
- Apply machine learning algorithms to cybersecurity data
- Compare multiple models for threat detection
- Evaluate classification performance using standard metrics
- Analyze model behavior and generalization capability

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib

## Dataset
This project uses the **NSL-KDD dataset**, a widely recognized benchmark for intrusion detection research.

## Methodology
- Data preprocessing and feature encoding using one-hot encoding
- Conversion of categorical features into numerical representations
- Splitting data into training and testing sets (70/30)
- Training multiple machine learning models:
  - Random Forest
  - Decision Tree
  - Support Vector Machine (SVM)
- Evaluating model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

## Results
The Random Forest model achieved the best overall performance, followed closely by the Decision Tree. The SVM model provided an alternative approach based on margin maximization.

## Analysis
The Random Forest model demonstrated superior performance, indicating that ensemble methods offer better generalization for cybersecurity threat detection tasks.

The Decision Tree showed slightly lower performance, suggesting possible overfitting to training data.

The SVM model provides a different classification perspective and may perform better depending on feature distribution and scaling.

Overall, the results highlight the importance of selecting appropriate models for intrusion detection systems.

## Model Comparison

![Model Comparison](model_comparison.png)

## Project Structure
Cyber_Threat_Detection_com_Machine_Learning/
│
├── data/
│ └── KDDTrain+.txt
├── main.py
├── results.txt
├── model_comparison.png
├── requirements.txt
├── README.md


## How to Run

1. Clone the repository:
```bash
git clone https://github.com/raoniabreu/Cyber_Threat_Detection_com_Machine_Learning.git
```
2. Navigate to the project folder:
```bash
cd Cyber_Threat_Detection_com_Machine_Learning
```
3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```
4. Run the project:
```bash
python main.py
```

## Reproducibility

The experiments use a fixed random state to ensure reproducibility of results.

## Future Improvements
Test additional machine learning models (e.g., Neural Networks)
Improve feature engineering techniques
Apply deep learning approaches
Perform hyperparameter tuning
Use more recent cybersecurity datasets

## Author

Miqueias Raoni de Abreu
