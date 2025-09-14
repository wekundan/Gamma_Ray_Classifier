# Gamma Ray Classifier 🚀

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
