FROM ubuntu:16.04

RUN apt-get update -qqq
RUN whoami

# Will set new entrypoint later
# ENTRYPOINT ["/bin/echo", "hi,", "world"]

# Install python
RUN apt-get install -y python-pip python-dev
 
# Install libraries
RUN pip install numpy pandas scipy statsmodels
 
# Add my script
ADD hie_analysis.py /home/hie_analysis.py
ADD 1-longitudinal-minimal-data-set-V2.csv /home/1-longitudinal-minimal-data-set-V2.csv

ENTRYPOINT ["python", "/home/hie_analysis.py"]