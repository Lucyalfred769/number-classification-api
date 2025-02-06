# Number Classification API 🚀
A simple Flask API to classify numbers.

## Features
- Detects if a number is **Armstrong, Prime, or Perfect**.
- Provides **math facts** from NumbersAPI.
- Deployed on **DigitalOcean**.

## Usage
```sh
curl "http://your-digitalocean-ip/api/classify-number?number=371"
```

## Docker Setup

### Build Docker image:
```sh
docker build -t number-classification-api .
```

### Run Docker container locally:
```sh
docker run -p 5000:5000 number-classification-api
```

### Push Docker image to Docker Hub:
1. Tag your image:
    ```sh
    docker tag number-classification-api your-dockerhub-username/number-classification-api:latest
    ```
2. Push the image:
    ```sh
    docker push your-dockerhub-username/number-classification-api:latest
    ```

### Deploy on DigitalOcean:

1. SSH into your DigitalOcean droplet.
2. Install Docker (if not installed):
    ```sh
    sudo apt update
    sudo apt install docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    ```
3. Pull and run the image:
    ```sh
    docker pull your-dockerhub-username/number-classification-api:latest
    docker run -d -p 80:5000 your-dockerhub-username/number-classification-api
    ```

Access the API at `http://your_droplet_ip/api/classify-number?number=371`.