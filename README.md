<a id="readme-top"></a>

<div align="center">
  <h1>Patient API</h1>
  <p><strong>Simple patient records with FastAPI and MongoDB.</strong></p>
  <p>A compact CRUD API for creating, listing, retrieving, updating, and deleting patient records.</p>
  <p>
    <a href="#api"><strong>Explore the API »</strong></a>
    <br /><br />
    <a href="#run-locally">Run locally</a>
    &middot;
    <a href="https://github.com/pavan2184/Patient/issues/new">Report a bug</a>
    &middot;
    <a href="https://github.com/pavan2184/Patient/issues/new">Request a feature</a>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&amp;logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&amp;logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&amp;logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&amp;logoColor=white" alt="Docker" />
</p>

## About The Project

This repository is a learning-scale patient-record service backed by a local MongoDB database. It demonstrates basic FastAPI routing, Pydantic request models, MongoDB document conversion, and CRUD operations.

> This is a software prototype, not a production clinical or medical-record system. It does not implement authentication, authorization, audit logging, encryption policy, or healthcare compliance controls.

## API

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `POST` | `/patients` | Create a patient |
| `GET` | `/patients` | List patients |
| `GET` | `/patients/{pid}` | Retrieve a patient |
| `PUT` | `/patients/{pid}` | Update a patient |
| `DELETE` | `/patients/{pid}` | Delete a patient |

## Run Locally

Start MongoDB on `mongodb://localhost:27017`, then install and run the API:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
uvicorn main:app --reload
```

Open the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).
