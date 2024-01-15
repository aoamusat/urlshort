FROM python:3.11-slim

COPY ./requirements.txt /urlshorter/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /urlshorter/requirements.txt

COPY . /urlshorter

WORKDIR /urlshorter

COPY entrypoint.sh /urlshorter/entrypoint.sh
RUN chmod +x /urlshorter/entrypoint.sh

EXPOSE 80

# Run migrations at runtime
ENTRYPOINT ["/urlshorter/entrypoint.sh"]

# Run the application server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]