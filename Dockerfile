FROM phusion/baseimage:0.9.10

MAINTAINER trent@trenthauck.com

ENV HOME /root

RUN apt-get update && \
    apt-get install -y python-dev \
    python-pip \
    libpq-dev

RUN pip install tornado psycopg2 planout

#add planout
ADD planoutapi /planoutapi

# expose the port that the api listens on
EXPOSE 8999

#setup service and add files
RUN mkdir /etc/service/planoutapi
ADD planoutapi/scripts/run.sh /etc/service/planoutapi/run

CMD ["/sbin/my_init"]
