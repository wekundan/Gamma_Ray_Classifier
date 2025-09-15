# Gamma Ray Classifier

Flask app that predicts whether a telescope event is:  
- **Gamma Ray Event (Signal)**  
- **Hadron Event (Background Noise)**  

---

## Project Files

| File | Description |
|------|-------------|
| `app.py` | Main Flask app for prediction |
| `Knn_model.pkl` | Trained KNN model for classification |
| `Gamma_Rays_Classifier.ipynb` | Jupyter notebook with data exploration, model building, and analysis |
| `templates/index.html` | Frontend template for the Flask app |
| `requirements.txt` | Python dependencies |
| `Procfile` | Config for deployment (Render) |
| `README.md` | Project description and instructions |
| `.gitattributes` | File to control Git behavior for line endings and languages |

---

## Dataset

The dataset is **not included in the repo** due to size, but you can download it from:  
[Download Dataset](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope)

---

## Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```
## Technologies Used

[![Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-ff9900?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)


## SnapShots
<img width="1536" height="706" alt="image" src="https://github.com/user-attachments/assets/d1e93cb2-0666-4f6a-8fbe-57ad880b412a" />
<img width="1654" height="657" alt="image" src="https://github.com/user-attachments/assets/e404ac0b-4cbc-4c06-9e9b-71562dec14d4" />



## Future Scope
- Use multiple Algorithms
- Optimize Flask app.py
- Front-End






