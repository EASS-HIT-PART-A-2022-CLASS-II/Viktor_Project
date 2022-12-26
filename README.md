# Viktor_Project

# Worker Management Microservices

## This project uses microservices with API requests to allow you to manage workers. 
You can : 

-delete
-add random
-show
-create users with missing information

The project works with Docker and contains two microservices: two for the backend and one for the frontend, which is built with React.

The frontend sends requests to the main service, and if needed, the main service can send API requests to the second service if there is missing information.

## Diagram:

***************************************************************************
    +------------+            +------------+
    |            |            |            |
    |  Frontend  |            |    Main    |
    |            |            |            |
    +------------+            +------------+
          |                         |
          | API request             |  API request
          |                         |
          +-------------------------+
                                    |
                                    | API request
                                    |
                                    v
                         +----------------+
                         |                |
                         | NamesGenerator |
                         |                |
                         +----------------+

*******************************************************

## Running the project

- Clone the repository and navigate to the project directory

- Build and start the docker containers: docker-compose up

This will start the backend and frontend services in separate containers. 

The frontend will be available at http://localhost:3000
