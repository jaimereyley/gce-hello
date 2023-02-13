# Must use a Cuda version 11+
FROM sanicframework/sanic:3.8-latest

WORKDIR /sanic


ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt


# add the entitlements file
ADD service_account.json .

# We add the banana boilerplate here
ADD server.py .
EXPOSE 80

# Add your custom app code, init() and inference()
ADD app.py .


CMD ["python", "server.py"]