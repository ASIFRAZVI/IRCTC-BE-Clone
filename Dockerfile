#importing python latest image from Docker
FROM python:latest 

#creationg one working directry with the name of app
WORKDIR /app  

#adding our all folders to app(workdirectory) from to whare i need to copy fro . to my app
COPY . /app

#install the all requirement txt
RUN pip install -r requirements.txt

#choose the port whare our app is exposed
EXPOSE 8000

#give run command to the cmd terminal
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#commands 
# to check the which images are present
# 1. docker image

# to check which image is exposed or running
# 2.docker ps

# to build the image (. =path, -t = tag )
# 3.docker build . -t "name of the image "  or docker build -t anakin .

# to remove image
# 4.docker rmi <image iD"

# to run the docker image
# 5.docker run --network="host" <inmage ID> --name="name for our app (optional)" or docker run -p 8000:8000 anakin

# to run in detach mode (means contineus running after closing of terminals)
# 6.docker run -d --network="host" <image ID> --name="name for our app (optional)" or

#additionally we have to create dockerignore file and add all secrate and unnessesory files



