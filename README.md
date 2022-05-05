# Mlflow-project-template
Mlflow project template

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```


### STEP 05- create the conda.yaml
```bash
conda env export > conda.yaml
```

### STEP 06- commit and push the changes to the remote repository