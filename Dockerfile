FROM balenalib/raspberrypi3-python:2-stretch-run
RUN apt-get update -y
RUN apt-get install gcc
RUN apt-get update -y
RUN pip install serial
RUN pip install pyserial
RUN pip install paho-mqtt
RUN apt-get install libjpeg-dev -y
RUN apt-get install zlib1g-dev -y
RUN apt-get install libfreetype6-dev -y
RUN apt-get install liblcms1-dev -y
RUN apt-get install libopenjp2-7 -y
RUN apt-get install libtiff5 -y
RUN pip install pillow
RUN apt-get install python-picamera
RUN apt-get update -y
COPY ./first_balena_app /first_balena_app/
WORKDIR /first_balena_app
CMD ["python", "balena_publisher.py"]
