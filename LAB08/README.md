DS605 Lab Assignment 8: Decision Trees and Support Vector Machines
Overview
This assignment studies classification using Decision Trees and Support
Vector Machines (SVMs). It implements selected algorithms from scratch,
compares them with Scikit-learn implementations, visualizes decision
boundaries, and evaluates model performance.
Dataset
Dataset: UCI Banknote Authentication Dataset
File: data_banknote_authentication.txt
Samples: 1,372
Input features: 4 numerical features
Target: Binary banknote class (0 or 1)

The dataset columns are:
1. variance
2. skewness
3. curtosis
4. entropy
5. class --- target label
Dataset path

Assignment Objectives
- Explore the dataset and inspect feature distributions and class
  balance.
- Implement Decision Tree splitting using Gini impurity and entropy.
- Build a recursive Decision Tree classifier from scratch.
- Implement a Linear SVM from scratch.
- Compare manual implementations with Scikit-learn models.
- Explore linear, polynomial, and RBF SVM kernels.
- Visualize decision boundaries on two selected features and on a
  synthetic nonlinear dataset.
- Compare model performance using classification metrics and execution
  time.
Sections Covered
Part A --- Decision Tree from Scratch
- Gini impurity and entropy
- Finding the best feature-threshold split
- Recursive tree construction and stopping conditions
- Prediction and comparison with Scikit-learn's
  DecisionTreeClassifier
Part B --- Linear SVM from Scratch
- Linear decision boundary and margin-based classification
- Manual model training and prediction
- Comparison with Scikit-learn's SVM implementation
Part C --- Kernel SVM and Nonlinear Boundaries
- Linear, polynomial, and RBF kernels
- Nonlinear decision boundaries using a synthetic make_moons dataset
- Experiments with the regularization parameter C
- Evaluation of model performance
Part D --- Final Model Comparison
- Train models using all four banknote features
- Compare accuracy, precision, recall, F1-score, training time, and
  prediction time
- Visualize model scores and the confusion matrix for the
  best-performing final SVM
Tools and Libraries
- Python
- Jupyter Notebook
- NumPy
- pandas
- Matplotlib
- scikit-learn
Setup and Execution
1. Install Python and VS Code or Jupyter Notebook.
2. Install the required libraries:
   pip install numpy pandas matplotlib scikit-learn jupyter
3. Download or copy data_banknote_authentication.txt into the dataset
   location specified in the notebook.
4. Open 202618003_Lab8_optimized.ipynb.
5. Select the Python environment where the dependencies are installed.
6. Run all cells in order, from top to bottom.
The notebook uses a reproducible train-test split with an 80:20 ratio,
random_state=42, and stratification for the banknote classes. The
two-feature visualizations use variance and skewness; final model
comparisons use all four features. SVM inputs are standardized using
statistics calculated from the training set.
Reported Findings
The notebook's conclusion reports the following results for its tested
configurations:
- The manual and Scikit-learn Decision Trees achieved 99.27%
  accuracy and an F1-score of 99.19% in the final four-feature
  comparison.
- The manual Linear SVM achieved 88.00% accuracy, while
  Scikit-learn's Linear SVM achieved 97.45% accuracy.
- On the synthetic make_moons dataset, the RBF SVM achieved 96.50%
  accuracy in the tested configuration.
- In the final banknote comparison, the Scikit-learn RBF SVM achieved
  100% accuracy and an F1-score of 1.00 on the held-out test
  set.
These are results reported by the notebook and may depend on the code,
library versions, and configuration used when it is run.
Notes
- The dataset file is not embedded in this README; ensure it is
  available locally before running the notebook.
- The configured dataset path is specific to one Windows computer and
  must be changed if your directory differs.
- The test set is used for final evaluation; model comparisons should
  be interpreted in the context of this single train-test split.
