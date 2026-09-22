# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API in Python using FastAPI, including route creation, request validation, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Set up the FastAPI app

#### Descrição
Create a FastAPI application that serves a simple API for managing a list of items or records.

#### Requisitos
O programa concluído deve:

- initialize a FastAPI app with a descriptive title
- create a root endpoint that returns a welcome message
- run the app locally with a development server command
- confirm the API responds correctly in a browser or via HTTP client

### 🛠️ Build the CRUD endpoints

#### Descrição
Implement the main REST endpoints for listing, creating, updating, and deleting resources.

#### Requisitos
O programa concluído deve:

- add an endpoint to list all items
- add an endpoint to retrieve one item by its identifier
- add an endpoint to create a new item
- add an endpoint to update an existing item
- add an endpoint to delete an item
- return JSON responses with consistent payloads

### 🛠️ Validate input and handle errors

#### Descrição
Improve the API with data validation and clear responses for invalid input or missing resources.

#### Requisitos
O programa concluído deve:

- define a Pydantic model for request data validation
- reject invalid input with clear validation errors
- handle missing item IDs gracefully
- return appropriate HTTP status codes for successful and failed requests
- keep the API organized and readable with simple function and model structure
