# Viktor_Project

# Worker Management Microservices




https://user-images.githubusercontent.com/70378430/216985667-f5f094f1-cc19-4c14-a778-c796f8238a2f.mp4




### This project uses microservices with API requests to allow you to manage workers. 

### You can : 

-delete

-add random

-show

-create users with missing information


### The project works with Docker and contains three microservices: 

three for the backend and one for the frontend, which is built with React.

The frontend sends requests to the main service, and if needed, the main service can send API requests to the second service if there is missing information. (such as  Password,role or Name)


## Diagram:

***************************************************************************
    +------------+            +------------+           +------------+ 
    |            |API request |            |API request|            |
    |  Frontend  |- - - - - > |    Main    |- - - - - >|  Password  |
    |            |            |            |           |            |
    +------------+            +------------+           +------------+
                                    |
                                    |  API request
                                    |
                                    |
                                    | 
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
