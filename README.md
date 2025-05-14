# Mtcars Flask API

This repository implements a predictive linear regression model on the `mtcars.csv` dataset using a Flask API in Docker and deployed to Google Cloud Run.

## Contents

* `mtcars.csv`: dataset
* `train_model.py`: trains and saves the linear regression model (`mtcars_model.pkl`)
* `app.py`: Flask API for MPG predictions
* `requirements.txt`: Python dependencies
* `Dockerfile`: builds the container image

## Local Setup and Testing

1. **Clone the repository**

   ```bash
   git clone git@github.com:Derek-Wen/Mtcars-Flask-Api.git
   cd Mtcars-Flask-Api
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**

   ```bash
   python train_model.py
   ```

   This creates `mtcars_model.pkl`.

4. **Run the API locally**

   ```bash
   python app.py
   ```

   The server listens on http://localhost:8080.

5. **Test locally**

   ```bash
   curl -X POST "http://localhost:8080/predict" -H "Content-Type: application/json" -d '{"cyl":6,"disp":160.0,"hp":110,"drat":3.90,"wt":2.620,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'
   ```

   Expected response:

   ```json
   {"predicted_mpg":22.599505761262385}
   ```

## Docker Containerization

1. **Build the Docker image**

   ```bash
   docker build -t mtcars-flask-api .
   ```

2. **Run the container locally**

   ```bash
   docker run --rm -p 8080:8080 mtcars-flask-api
   ```

3. **Test in Docker**

   ```bash
   curl -X POST "http://localhost:8080/predict" -H "Content-Type: application/json" -d '{"cyl":6,"disp":160.0,"hp":110,"drat":3.90,"wt":2.620,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'
   ```

## Docker Hub

1. **Tag the image**:

   ```bash
   docker tag mtcars-flask-api:latest derekhwen/mtcars-flask-api:latest
   ```

2. **Push to Docker Hub**

   ```bash
   docker push derekhwen/mtcars-flask-api:latest
   ```

## Google Cloud Run Deployment (Console)

1. Go to the Cloud Run console.
2. Click **Create Service** and select **Artifact Registry / Docker Hub**.
3. For **Container image URL**, enter:

   ```text
   docker.io/derekhwen/mtcars-flask-api:latest
   ```
4. Under **Authentication**, select **Allow unauthenticated invocations**.
5. Under **Container**, set **Port** to `8080`.
6. Click **Deploy**.

After deployment you’ll see a URL:

```
https://mtcars-flask-api-427327765085.us-central1.run.app
```

**Test the live service**:

```bash
curl -X POST "https://mtcars-flask-api-427327765085.us-central1.run.app/predict" -H "Content-Type: application/json" -d '{"cyl":6,"disp":160.0,"hp":110,"drat":3.90,"wt":2.620,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'
```

You should receive the same JSON prediction as mine.
---