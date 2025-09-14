# Gamma Ray Classifier 🚀

This repository contains a Flask web application that predicts whether a telescope event is a **Gamma Ray Event (Signal)** or a **Hadron Event (Background Noise)**.

## Project Files

- **app.py** → Main Flask application that serves the web interface and handles predictions.
- **Knn_model.pkl** → Pre-trained KNN model used for classifying events.
- **requirements.txt** → Python dependencies required to run the app.
- **Procfile** → For deployment (used by Render or Heroku).
- **README.md** → This file, describing the project.
- **templates/index.html** → HTML template for the web interface.
- **Gamma_Ray_Analysis.ipynb** → Jupyter Notebook containing the data analysis, EDA, and model building steps.

## Dataset

The dataset used for training the model is **not included** in this repository due to size constraints.  

You can download it here:  
[Download Dataset](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope)

> After downloading, place the dataset in the root folder `Gamma_Ray_Classifier/` so that the Jupyter Notebook and `app.py` can access it.

## Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt

