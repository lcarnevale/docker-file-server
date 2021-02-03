# File Server Microservice
<img src="https://img.shields.io/badge/python-v3-blue" alt="python-v3-blue">

A Python implementation of a simple file server microservice.

# How to use it
Clone the repository and build it locally using the Dockerfile.
```bash
docker build -t lcarnevale/fileserver .
```

Run the image.
```bash
docker run -d --rm --name fileserver \
    -e PORT=8085 \
    -v /mnt/fileshare:/mnt/fileshare \
    -v /var/log/lcarnevale:/opt/app/log \
    -p 8085:8085 \
    --restart unless-stopped \
    lcarnevale/fileserver
```

Open the log file for watching what is going on.
```bash
tail -f /var/log/lcarnevale/fileserver.log
```

Create a file within the mounted directory and download it using Curl.
```bash
curl http://<IP-ADDRESS>:8085/download?filename=<FILENAME> --output <FILENAME>
```