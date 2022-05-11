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


#### Notes
##### We can execute below command one by one also by executing in the terminal or we can create one init_setup.sh file by using touch 
# filename.sh in the terminal and
# write everything here and it will automatically execute everything one by one 

# conda create --prefix ./env python=3.7 -y
# source activate ./env
# pip install -r requirements.txt
# conda env export > conda.yaml

# After excuting above then excute conda activate ./env
# pip freeze --->command to list down the package installed in the current environment

# if u want to create multiple directory that means parent plus child directory then excute below command:
# -------     mkdir -p src/util ---------

# if you want to create the file inside directory execute below command from terminal of current environment(where we want the file)
#  ------------------- touch src/example.py src/util/example2.py ----------------

# setup.py file helps us to install anything as a package