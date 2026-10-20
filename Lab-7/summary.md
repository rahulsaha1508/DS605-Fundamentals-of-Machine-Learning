# Results summary

* Dataset: 400 images, 40 subjects, 112x92 px (10304 features). Split: 320 train / 80 test (2 test images per subject, seed 42).
* PCA: 100 components retain >= 90% variance (90.09%), i.e. 103x fewer numbers per image. Eigendecomposition and SVD agree (max eigenvalue difference 1.3e-13).
* Training-set storage: 3,297,280 numbers (raw) vs 1,072,704 (scores + basis + mean) = 3.1x smaller.
* Reconstruction at K=100: test PSNR 23.39 dB.
* 1-NN (Euclidean) test accuracy: raw pixels 96.25% vs PCA K=100 96.25%.
* Best traditional model: Logistic Regression - test accuracy 97.5% with k=150 (CV 98.44%); compact version k=30 gives 97.5%.

## Comparison table

| Model | Setting | k | whiten | params | CV acc (%) | Test acc (%) |
|---|---|---|---|---|---|---|
| 1-NN Euclidean, raw pixels | baseline | 10304 | - | {} |  | 96.25 |
| 1-NN Euclidean, PCA K90 | baseline | 100 | False | {} |  | 96.25 |
| KNN | best CV | 150 | False | {'n_neighbors': 1, 'weights': 'uniform'} | 95.0 | 96.25 |
| Logistic Regression | best CV | 150 | False | {'C': 10} | 98.44 | 97.5 |
| SVM (linear) | best CV | 60 | True | {'C': 0.1} | 97.81 | 96.25 |
| SVM (RBF) | best CV | 60 | True | {'C': 1, 'gamma': 'scale'} | 97.5 | 96.25 |
| KNN | compact (<=1pt below best CV) | 20 | False | {'n_neighbors': 1, 'weights': 'uniform'} | 94.06 | 96.25 |
| Logistic Regression | compact (<=1pt below best CV) | 30 | False | {'C': 0.1} | 97.5 | 97.5 |
| SVM (linear) | compact (<=1pt below best CV) | 30 | False | {'C': 0.1} | 96.88 | 97.5 |
| SVM (RBF) | compact (<=1pt below best CV) | 30 | False | {'C': 10, 'gamma': 'scale'} | 96.88 | 97.5 |
