# Asterisk image Docker file

FROM ubuntu:xenial
MAINTAINER SergeM <sbmatyuniN@gmail.com>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y asterisk 

ENV ASTERISKUSER asterisk

RUN apt-get install -y python

#Copy minimum configuration files so that it can start
COPY configs/etc/* /etc/asterisk/
COPY configs/ /configs/

RUN chown -R $ASTERISKUSER:$ASTERISKUSER /etc/asterisk

# cleain tmp file
RUN rm -rf /tmp/*

#Make asterisk port open
#EXPOSE 5060

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
#CMD ["/usr/sbin/asterisk"]
#CMD ["/etc/init.d/asterisk start"]


