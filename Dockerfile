FROM python:3.9

WORKDIR /code

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the sources
COPY src/ .

# Run
CMD [ "python", "./server.py" ]