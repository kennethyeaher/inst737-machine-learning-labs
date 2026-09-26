# INST737 Machine Learning Labs

Two tutorial based Python exercises exploring how training choices affect model evaluation. Built for INST737 at the University of Maryland.

## My work

I implemented the train/test split and model evaluation exercises: a housing regression example and a comparison of Gini and entropy decision trees. These are learning implementations, not production prediction services.

| Exercise | What to inspect |
| --- | --- |
| [Decision trees](decision-tree/decision-tree-tutorial-KennethYeaher.py) | Balance Scale classification, a 70/30 split, depth limited Gini and entropy trees, confusion matrices, classification reports, and tree plots. |
| [Train/test split](split-tutorial-KennethYeaher.py) | California Housing regression, an 80/20 split, training and test R², and ten actual versus predicted values. |

![Classification report from a saved decision tree tutorial run, showing uneven performance across the three classes.](docs/readme/preview.jpg)

A cropped output capture retained in my portfolio. It documents a previous tutorial run, not a new benchmark. The class level report makes errors visible that an overall accuracy score can hide.

## Run locally

With Python 3 available, create an environment from the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas numpy scikit-learn matplotlib
python decision-tree/decision-tree-tutorial-KennethYeaher.py
python split-tutorial-KennethYeaher.py
```

On Windows, activate with `.venv\Scripts\activate`. The scripts fetch datasets from UCI and scikit-learn's California Housing source, so initial runs need network access. The decision tree script opens Matplotlib windows. Dependencies are not pinned, and results can vary by library version.

---

## Author

**Kenneth Yeaher**  
Master of Information Management  
University of Maryland, College Park  
[![LinkedIn: Kenneth Yeaher](https://img.shields.io/badge/LinkedIn-Kenneth_Yeaher-0A66C2?style=flat)](https://www.linkedin.com/in/kennethyeaher/)

`Python` · `Machine Learning` · `Model Evaluation`
