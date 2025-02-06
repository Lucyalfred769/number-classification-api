# Number Classification API 🚀

A simple Flask API to classify numbers.

## Features
- Classify a number as **prime**, **perfect**, **Armstrong**, **odd**, or **even**.
- Provide a **fun fact** about the number using the Numbers API.
- Handle CORS for cross-origin requests.

## API Endpoint

### `GET /api/classify-number`

Classify a given number based on its mathematical properties.

**Query Parameters:**
- `number` (required) - The number you want to classify.

#### Example Request:
GET http://your-digitalocean-ip/api/classify-number?number=371

#### Example Response (200 OK):

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Example Response (400 Bad Request - Invalid Input):

```json
{
    "number": "alphabet",
    "error": true
}
```

## Mathematical Properties
The API checks for the following mathematical properties:

- **Prime**: A number greater than 1 that is divisible only by 1 and itself.
- **Perfect**: A number that is equal to the sum of its proper divisors (excluding the number itself).
- **Armstrong**: A number that is equal to the sum of its own digits each raised to the power of the number of digits.
- **Even/Odd**: Whether the number is even (divisible by 2) or odd.

## CORS Support
The API supports CORS to allow cross-origin requests. This means that you can make API requests from a different domain or port (e.g., a frontend running on http://localhost:3001 can make requests to the API running on http://localhost:3000).

## Installation

Clone the repository:

```sh
git clone https://github.com/your-username/number-classification-api.git
```

Navigate into the project directory:

```sh
cd number-classification-api
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Start the server:

```sh
flask run
```

The API will be available at http://localhost:5000.

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

## Testing the API
You can test the API using any HTTP client (like Postman, Insomnia, or your browser).

Example using curl:

```sh
curl "http://your-digitalocean-ip/api/classify-number?number=371"
```

## Technologies Used
- **Flask**: Python web framework to build the API.
- **Numbers API**: For providing fun facts about numbers.
- **Docker**: To containerize the application.
- **DigitalOcean**: For deployment.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
