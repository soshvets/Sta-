FROM python:3.9-slim 

# Install Postgres client (needed for connection with db)

RUN apt-get update && apt-get install -y alien libaio1 postgresql-client wget



WORKDIR /app

# Copy requirements.txt first to reduce image build time

COPY backend/requirements.txt ./

# RUN pip wheel --no-cache-dir --no-deps psycopg2-binary==2.9.2 
# Install all, required dependencies
# --no-deps is tricky because requirements.txt should contains all dependencies in this case
# --install-option="--prefix=/install"
RUN  python -m pip install --no-cache-dir -r requirements.txt


COPY backend ./


EXPOSE 8000

