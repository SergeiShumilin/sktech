#! /bin/bash

sudo docker build -t skoltech .
sudo docker run -d --name skoltech skoltech tail -f /dev/null
sudo docker exec skoltech /home/script.sh /home/dracula.txt /home/
sudo docker exec -it skoltech /bin/bash
