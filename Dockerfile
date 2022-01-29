##################Dockerfile##################
FROM openjdk:8

RUN apt-get update
RUN apt-get install -y bzip2 
RUN apt-get install -y wget
RUN apt-get install -y gcc 
RUN apt-get install -y git 
RUN apt-get install -y curl

RUN apt-get update
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

RUN pip3 install gdown==3.12.2
RUN pip3 install requests==2.24.0
RUN pip3 install pandas==1.1.3
RUN pip3 install elasticsearch==7.11.0
RUN pip3 install pyspark==3.1.1
RUN pip3 install esdk-obs-python==3.20.11 --trusted-host pypi.org
RUN pip3 install Pillow==8.2.0
RUN pip3 install xlrd==1.1.0
RUN pip3 install xlsxwriter==1.4.3

RUN apt-get install -y zip 

RUN mkdir /yan/
RUN chmod 777 /yan/ 

RUN useradd -u 8877 yan
USER yan

######

USER yan
WORKDIR /yan/

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512
RUN shasum -a 512 -c elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 
RUN tar -xzf elasticsearch-7.13.4-linux-x86_64.tar.gz

######

USER yan
WORKDIR /yan/

RUN curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.13.4-linux-x86_64.tar.gz
RUN curl https://artifacts.elastic.co/downloads/kibana/kibana-7.13.4-linux-x86_64.tar.gz.sha512 | shasum -a 512 -c - 
RUN tar -xzf kibana-7.13.4-linux-x86_64.tar.gz

######

COPY elasticsearch_dbpedia_arabic.tar.gz /yan/
RUN tar -xzvf /yan/elasticsearch_dbpedia_arabic.tar.gz
RUN rm elasticsearch_dbpedia_arabic.tar.gz

######

ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3

RUN echo "sd1g6s1g52d0g5"

WORKDIR /yan/
RUN git clone https://github.com/liang6261515/jessica_kibana_docker.git
RUN mv jessica_kibana_docker/* ./
RUN rm -r jessica_kibana_docker

WORKDIR /yan/
RUN git clone https://github.com/yanliang12/dbpedia_query_arabic.git
RUN mv dbpedia_query_arabic/* ./
RUN rm -r dbpedia_query_arabic

##################Dockerfile##################