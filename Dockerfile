FROM python:3.11-bookworm

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app
# Copy project
COPY . .

RUN mkdir /app/static && \
  pip install -r requirements.txt && \
  chmod +x run.sh
  

EXPOSE 8000

ENTRYPOINT ["bash", "./run.sh"]
# runs the production server
CMD ["gunicorn", "-b", "0.0.0.0:8000", "kioskadmin.wsgi"]