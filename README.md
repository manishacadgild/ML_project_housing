## Housing Price Prediction

``` bash 
conda create -p venv python==3.9 -y
conda activate venv/

```
``` bash 
pip install -r requirements.txt

```
BUILD DOCKER IMAGES
```
docker build -t <image_name>:<tagname> .
```
Note: Image name for docker must be lower case

```
docker images
```
Run docker images
```
docker rum -p 5000:5000 -e PORT=5000
```

```