# Load Balancer Prototype

A load balancer is essential for all applications that aim to scale. When you have thousands of requests per second you need to distribute them between your instances in the most efficient way possible.

This repository aims to create a load balancer using python, it is an exercise in understanding the primary meaning behind a load balancer.

## Set up

You will need to have docker and docker-compose installed in your machine.

After that cloning, run the following commands in the root of the repository:

    docker-compose build

And:

    docker-compose up

The application should be up.

## Using it

To use it is simple, there are two routes available:

    POST -> http://localhost:80
    GET -> http://localhost:80

The post will send a call to be distributed between the available workers and the get will return a summary of how many calls have been sent and distributed.

## Load testing

Execute the following command to send 10 thousand requests and see how they are distributed:

    docker exec -it load-balancer-prototype_load-balancer_1  python3 ./app/load-testing.py