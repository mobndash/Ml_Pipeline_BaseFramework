End 2 End ML pipeline project has below features :

Pre - Setup project with Github, Logger, Exceptions

    1. Data Ingestion
    2. Data Transformation
    3. Model Trainer
    4. Model Evaluation
    5. Model Deployment

CI/CD Pipelines - Github Actions
Deployment - AWS


************************************************************************************************************************************************************************************
setup.py

This file is essential for packaging and distributing a Python project. It defines your project’s metadata and dependencies, and allows tools like pip to install it.

************************************************************************************************************************************************************************************

```
ML_Pipeline_E2E
├─ artifacts
│  ├─ model.pkl
│  ├─ preprocessor.pkl
│  ├─ raw_data.csv
│  ├─ test.csv
│  └─ train.csv
├─ catboost_info
│  ├─ catboost_training.json
│  ├─ learn
│  │  └─ events.out.tfevents
│  ├─ learn_error.tsv
│  ├─ time_left.tsv
│  └─ tmp
├─ logs
├─ notebook
│  ├─ catboost_info
│  │  ├─ catboost_training.json
│  │  ├─ learn
│  │  │  └─ events.out.tfevents
│  │  ├─ learn_error.tsv
│  │  ├─ time_left.tsv
│  │  └─ tmp
│  ├─ data
│  │  └─ StudentsPerformance.csv
│  ├─ EDA.ipynb
│  └─ model_training.ipynb
├─ README.md
├─ requirements.txt
├─ setup.py
└─ src
   ├─ components
   │  ├─ data_ingestion.py
   │  ├─ data_transformation.py
   │  ├─ model_trainer.py
   │  └─ __init__.py
   ├─ exception.py
   ├─ logger.py
   ├─ pipeline
   │  ├─ prediction_pipeline.py
   │  ├─ training_pipeline.py
   │  └─ __init__.py
   ├─ utils.py
   └─ __init__.py

```