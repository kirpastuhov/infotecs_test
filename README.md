
# Infotecs Test Task

Simple web application for computing prime factors of a number.

## Getting Started

Get yourself a copy of the project with the command
```
git clone https://github.com/kirpastuhov/infotecs_test.git
```

### Prerequisites

You may need [Docker](https://www.docker.com/products/docker-desktop) installed

###  Run the project with Docker:
In the project directory run:
```
docker-compose build
```
And then:
```
docker-compose up
```
Now the application is running on localhost:8000

To stop application use press CTRL+C  or:
```
docker-compose down
```
###  Run the project without Docker:
In the project directory run:
```
python manage.py runserver
```

To stop application use press CTRL+C
## Running the tests

Run this command to run some simple tests:
```
python manage.py test main
```