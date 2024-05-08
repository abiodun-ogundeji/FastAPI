# FastAPI Demo
This repository contains a basic demonstration of using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Features
* GET Endpoints: Demonstrates basic GET endpoints for retrieving data.
* POST Endpoint: Illustrates how to create a POST endpoint for adding data.
* Input Validation: Shows how to use Pydantic models for input validation.
* Async Endpoints: Demonstrates both synchronous and asynchronous endpoints.
* Testing: Provides unit tests for the defined endpoints.

## Requirements
* Python 3.7+
* FastAPI
* Pydantic
* Starlette (for testing)

## Usage
1. Install dependencies:
pip install fastapi pydantic starlette
2. Run the FastAPI application:
uvicorn app:app --reload
3. Access the API using the provided endpoints.

## Endpoints
* GET /: Returns a simple "Hello World" message.
* GET /users/{user_id}: Returns a JSON blob containing the user ID.
* POST /items/: Creates a new item with a name and price.
* GET /sleep_slow: Synchronous endpoint that simulates slow processing.
* GET /sleep_fast: Asynchronous endpoint that simulates fast processing.

## Running Tests
Run tests using the following command:
python tests.py
