# 2022_oss_assignment3

# How to build image
Download Dockerfile and go to the directory which includes Dockefile you downloaded just before.
And type below with tag_name you want.
```bash
docker build -t ANY_TAG .
```

# How to run Docker Container
And type below for running Container
```bash
docker run -d -p 8080:8080 ANY_TAG:latest
```

# Use Program
You can freely use this statistics program.

Do not paste all below commands, just type seeing this.

If you want to add number type below. You can put ANY_NUMBER_YOU_WANT.
 
```bash
curl -X POST “http://localhost:8080/numbers?new=ANY_NUMBER_YOU_WANT”
```

If you want to get average from number list of you added.
```bash
curl -X GET “http://localhost:8080/numbers/average”
```

If you want to get sum from number list of you added.
```bash
curl -X GET “http://localhost:8080/numbers/sum”
```

If you want to get standard deviation from number list of you added.
```bash
curl -X GET “http://localhost:8080/numbers/stddev”
```
