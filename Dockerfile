FROM ubuntu:20.04

RUN apt-get update 
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y curl

RUN pip3 install fastapi
RUN pip3 install uvicorn
EXPOSE 8080
WORKDIR /root
RUN git clone https://github.com/yaminsu5674/2022_oss_assignment3.git
WORKDIR /root/oss_assignment3
CMD ["uvicorn", "minsu_program:app", "--reload","--host", "0.0.0.0", "--port", "8080"]