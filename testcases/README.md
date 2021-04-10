## Step to run
```
$pip install -r requirements.txt
$python sample.py
```

## Build Docker Image and run
```
$docker image build -t sample:0.1 .
$docker container run --rm -e TARGET_HOST=<target host/server> sample:0.1
```
