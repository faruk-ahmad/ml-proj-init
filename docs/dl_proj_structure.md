Deep Learning Project Structure
----------------------------------------------


```bash
.
├── data
│   ├── links.json
│   ├── processed
│   └── raw
├── Dockerfile
├── docs
├── LICENSE
├── MANIFEST.in
├── ml_structure.md
├── notebooks
├── README.md
├── reports
│   ├── comparisions
│   └── figures
├── requirements.txt
├── setup.py
└── src
    ├── dataset
    │   ├── dataloader.py
    │   ├── prepare_dataset.py
    │   └── preprocess_dataset.py
    ├── features
    │   └── generate_features.py
    ├── __init__.py
    ├── __main__.py
    ├── models
    │   ├── predict_model.py
    │   └── train_model.py
    ├── tests
    └── visualize
        ├── visualize_dataset.py
        ├── visualize_features.py
        └── visualize_performance.py
```