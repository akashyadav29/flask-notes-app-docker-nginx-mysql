# ----------- Stage 1: Build Stage -----------
FROM python:3.9 AS build

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --user -r requirements.txt


# ----------- Stage 2: Final Stage -----------
FROM python:3.9-slim

WORKDIR /app

COPY --from=build /root/.local /root/.local
COPY app .

ENV PATH=/root/.local/bin:$PATH

RUN apt-get update && apt-get install -y curl
EXPOSE 5000

HEALTHCHECK CMD curl -f http://localhost:5000/ || exit 1

CMD ["python","app.py"]
