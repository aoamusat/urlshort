# URL Shortening Service

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/aoamusat/urlshort/create-release.yml) ![GitHub Release](https://img.shields.io/github/v/release/aoamusat/urlshort)

This is a URL shortening service implemented using FastAPI, Python, PostgreSQL, and Docker.

## Table of Contents

- [URL Shortening Service](#url-shortening-service)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Configuration](#configuration)
    - [Usage](#usage)
    - [API Documentation](#api-documentation)
- [Docker Support](#docker-support)
- [Contributing](#contributing)
- [License](#license)

## Overview

This URL shortening service allows users to shorten long URLs into concise, easy-to-share short links. It is built on the FastAPI framework, uses PostgreSQL as the database, and is containerized with Docker for easy deployment.

## Features

- Shorten long URLs into short links.
- Retrieve original URLs using short links.
- FastAPI-based RESTful API.
- PostgreSQL database for persistent storage.
- Docker support for containerized deployment.

## Prerequisites

Make sure you have the following installed on your system:

- Docker
- Docker Compose
- Python 3.8 or higher

## Getting Started

### Installation

- Clone the repository:

   ```bash
   git clone https://github.com/aoamusat/urlshort.git
   cd urlshort
   ```
- Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

- Run database migrations:

   ```bash
   alembic upgrade head
   ```
### Configuration


- Set environment variables:

   ```bash
    export DATABASE_URL=postgresql://user:password@host/db
    export BASE_URL=URL # Optional
    ```

## Run the FastAPI development server
```bash
uvicorn main:app --reload --port 80
```
Visit http://localhost/docs in your browser to access the Swagger documentation.

### Usage
Use the API documentation to interact with the service.
Shorten long URLs and retrieve original URLs using the provided API endpoints.
### API Documentation
The API documentation is available at http://localhost/docs.


# Docker Support
The service can be containerized using Docker. Use the provided Dockerfile for deployment.

```bash
# Build the Docker image
docker build -t url-shortener .
```

Alternatively, you can pull the Docker image from the Docker public repository
```bash
docker pull akeemamusat511/urlshorter:latest
```

# Contributing
Feel free to contribute to the project. Fork the repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License.