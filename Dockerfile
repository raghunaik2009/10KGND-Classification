FROM python:3.8.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

#CMD [ "./startup.sh" ]
#ENTRYPOINT ["sh","./startup.sh"]
CMD [ "flask", "run" , "--host", "0.0.0.0", "-p", "5000"]
