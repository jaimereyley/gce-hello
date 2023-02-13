# Must use a Cuda version 11+
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /sanic


ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD server.py .
EXPOSE 80

# Add your custom app code, init() and inference()
ADD app.py .

CMD ["python3", "server.py"]