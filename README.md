# Viktor_Project

Simple project that uses  microservises with API request That allows you to manage workers


Frontend  --> backend.Main --> NamesGenerator 



******************
HOW TO RUN 

1. Build main from Backend/main.py   
   
   docker build -t server  .

2. Run Ducker as 
    
    docker run -ti -p80:8001 --name server  server

3. Build main from NamesGenerator/main.py   
    
    docker build -t app  .

4. Run Docker as 
    
    docker run -ti -p8080:8080 --name app  app

4. Create nework
    
    docker network create net 

5. Connect both images to the network
    
    docker network connect net server 
    
    docker network connect net app     

6. Congratulations  you can now manage worker Database     
