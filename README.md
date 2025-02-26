## Download Conda
https://www.anaconda.com/download/success


## Create new env  

Create a new python environment called hello with python version 3.10.0

```sh
conda create --name hello python=3.10.0 -y
```

## Active environment

```sh
conda activate hello
```


## Get info about current environment

We can see things like where the python environment exists
```sh
conda info
```


## Remove env

We can see things like where the python environment exists
```sh
conda deactivate
```

```sh
conda remove -h openvino --all -y
```


## Install support package

```sh
conda install -c conda-forge pandas
```

```sh
conda install -c conda-forge ipykernel
```