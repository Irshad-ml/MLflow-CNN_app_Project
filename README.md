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
```
conda create --prefix ./env python=3.7 -y
source activate ./env
pip install -r requirements.txt
conda env export > conda.yaml
```

### After excuting above then excute 
```
conda activate ./env
```
# command to list down the package installed in the current environment
```
pip freeze
```
# or 
```
pip list
```

###### if u want to create multiple directory that means parent plus child directory then excute below command:
###### -------     mkdir -p src/util ---------

# if you want to create the file inside directory execute below command from terminal of current environment(where we want the file)
#  ------------------- touch src/example.py src/util/example2.py ----------------

# setup.py file helps us to install anything as a package

# if we want to  copy the file inside same directory or other director then execcute below command
#  -------------cp src/stage_00_template.py src/stage_01_base_model.py----------------------------

#### To run the mlflow execute the code at the terminal
```
    mlflow run . --no-conda
```

#### To run the mlflow with parameters execute the code at the terminal below " . " means current directory

```
    mlflow run . -e entry_point_name -P configs/config2.yaml --no-conda
    Ex:
        mlflow run . -e get_data -P configs/config2.yaml --no-conda
       
```