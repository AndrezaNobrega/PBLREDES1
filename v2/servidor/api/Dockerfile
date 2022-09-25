FROM python:latest

ADD api.py /api/
ADD getData.py /api/
ADD client_secret.json /api/
ADD token.json /api/
ADD telas.py /api/

EXPOSE 5002

WORKDIR /api/

RUN pip install --upgrade pip
RUN pip install google-api-python-client
RUN pip install python-google-spreadsheet
RUN pip install google-auth
RUN pip install google-auth-oauthlib
RUN pip install requests 

CMD ["python3", "/api/api.py"]