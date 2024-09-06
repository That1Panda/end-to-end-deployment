
# Script to build and run the Docker container

# Define variables
IMAGE_NAME="nlp_model_image"
CONTAINER_NAME="nlp_model_container"
PORT=8000

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Check if a container with the same name is already running and stop it
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    echo "Stopping existing container..."
    docker stop $CONTAINER_NAME
fi

# Remove any existing container with the same name
if [ $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
    echo "Removing existing container..."
    docker rm $CONTAINER_NAME
fi

# Run the Docker container
echo "Running Docker container..."
docker run -d -p $PORT:8000 --name $CONTAINER_NAME $IMAGE_NAME

# Confirm the container is running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    echo "Container is up and running on port $PORT."
else
    echo "Failed to start the container."
fi
