# DS605 Lab 7 - Image Representation, PCA, Eigenfaces and Face Recognition

Face recognition on the **AT&T (ORL) Database of Faces** (40 subjects x 10 images, 112x92 grayscale).
All PCA / eigenface computations are implemented with **NumPy linear algebra** (`np.linalg.eigh`, `np.linalg.svd`).
Scikit-learn is used **only** in Part D for the classifiers, cross-validation and grid search.

## Repository contents
| Path | Description |
|---|---|
| `Lab7_PCA_Eigenfaces_Face_Recognition.ipynb` | Complete runnable notebook (Parts A-D) |
| `figures/` | Sample faces, mean face, explained variance, eigenfaces, reconstructions, accuracy curves, matches, model comparison |
| `results/` | `summary.md`, `ml_comparison.csv/.md`, `similarity_matching_results.csv`, `reconstruction_quality.csv`, split indices |
| `requirements.txt` | Python dependencies |

## How to run
1. Put the dataset in `./archive` (folders `s1 ... s40`, each with `1.pgm ... 10.pgm`), or set the environment variable `ORL_DATA_DIR` to its location. The notebook also tries the local path `C:\Users\HP\Documents\DS605-Fundamentals-of-Machine-Learning\LAB07\archive`.
2. `pip install -r requirements.txt`
3. `jupyter notebook Lab7_PCA_Eigenfaces_Face_Recognition.ipynb` -> Run All (a few minutes; the Part D grid search is the slowest step).

## Approach
**Part A - Representation.** Images read as grayscale matrices (112x92, values 0-255), flattened to 10,304-dim vectors, scaled to [0,1], stacked into a 400 x 10,304 matrix with subject labels. Stratified, seeded split: 8 train / 2 test images per subject, so all 40 subjects appear in both sets.

**Part B - PCA.** Mean face from training data only, then centering. Principal directions computed two ways: (1) eigendecomposition of the covariance matrix, using the n x n dual (Gram) matrix because the 10,304 x 10,304 covariance is too large (eigenvectors mapped back via `u = A^T v`; a full-covariance check on downsampled images is included), and (2) SVD of the centred matrix. Eigenvalues and directions agree; SVD is the basis used afterwards. The minimum number of components giving >= 90 % variance (K90) is read from the cumulative-variance curve. Eigenfaces are reshaped to 112x92 images. Faces are projected to K90 dimensions, stored (`results/pca_model_K*.npz`), reconstructed, and compared with raw pixels in terms of MSE / PSNR and number of stored values.

**Part C - Similarity matching.** Each test face is projected with the training mean/basis and matched to its nearest training face (Euclidean; cosine also reported). Raw-pixel matching is run as the baseline. Correct and incorrect matches are visualised, and accuracy is plotted against the number of components.

**Part D - Traditional ML.** KNN, Logistic Regression, linear SVM and RBF SVM on PCA features. The NumPy PCA is wrapped as a scikit-learn transformer so it is refitted inside each fold of a 4-fold stratified CV (no leakage). Searched: number of components, whitening, and each model's hyper-parameters. The test set is used only for the final reported accuracy. A "compact" variant (smallest k within 1 point of the best CV score) shows the accuracy/size trade-off.

## Results and observations
> Fill this section from your own run - the notebook writes all numbers to `results/summary.md` and the figures to `figures/`.

* K90 (components for >= 90 % variance): _..._
* Storage / compression: _..._
* 1-NN accuracy, raw pixels vs PCA: _..._
* ML comparison table: see `results/ml_comparison.md`
* Observations: see the last section of the notebook.
