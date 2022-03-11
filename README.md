# flaskapi_mlops

## Getting Started

### Start Serve

Via Docker

- Build the image from Dockerfile
- Run a container from image

Via CMD:

- Goto root folder
- exec `pip install -r requirements.txt`
- exec `python app.py`

### Run

- Make a request to http://{SERVER}:{PORT}/predict

Via Curl

example:
``` curl
curl -X POST http://127.0.0.1:5001/predict -H 'Content-Type: application/json' -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}'
```
Via Postman
- Using the postman collection saved in root of this repository.

### Test

- Below, there is 3 test cases that you can use in this repos

#### iris setosa

``` json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

#### Iris-versicolor
``` json
{
    "sepal_length": 5.5,
    "sepal_width": 2.5,
    "petal_length": 4.0,
    "petal_width": 1.3
}
```

#### Iris-virginica
``` json
{
    "sepal_length": 6.4,
    "sepal_width": 2.8,
    "petal_length": 5.6,
    "petal_width": 2.2
}
```

## Requirements

- Python 3.10+
