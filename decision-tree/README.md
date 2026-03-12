# Decision Tree Classification — Balance Scale Dataset

This project implements Decision Tree classifiers using both **Gini Index** and **Entropy** criteria on the UCI Balance Scale dataset.

## Objective
Build and evaluate a decision tree model for classification, then compare performance using two splitting criteria:
- Gini
- Entropy

## Workflow
1. Import dataset
2. Split features and labels
3. Create training and testing sets
4. Train decision tree using Gini
5. Train decision tree using Entropy
6. Make predictions
7. Evaluate with confusion matrix, accuracy, and classification report

## Files
- `decision-tree-tutorial-KennethYeaher.py` — main Python script

## Technologies
- Python
- scikit-learn
- pandas
- numpy
- matplotlib

## Key Concepts
- Decision tree classifiers
- Model evaluation
- Overfitting control with `max_depth` and `min_samples_leaf`
- Comparing splitting criteria