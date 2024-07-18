# FastAPI CRUD API

This project implements a simple CRUD (Create, Read, Update, Delete) API using FastAPI. It provides endpoints to manage items with an in-memory database.

## Dependencies

- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-crud-api.git
   cd fastapi-crud-api
   ```

2. Install the required dependencies:
   ```
   pip install fastapi uvicorn
   ```

## Running the Application

To run the application, use the following command:

```
python main.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Root Endpoint

- **GET /** - Welcome message
  - Response: `{"message": "Welcome to the FastAPI CRUD API"}`

### Item Endpoints

- **POST /items/** - Create a new item
  - Request body: `{"id": int, "name": string, "description": string}`
  - Response: Created item

- **GET /items/{item_id}** - Get a specific item by ID
  - Response: Item details

- **GET /items/** - Get all items
  - Response: List of all items

- **PUT /items/{item_id}** - Update an existing item
  - Request body: `{"id": int, "name": string, "description": string}`
  - Response: Updated item

- **DELETE /items/{item_id}** - Delete an item
  - Response: `{"message": "Item deleted successfully"}`

## Example Usage

### Create an Item

```bash
curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Example Item", "description": "This is an example item"}'
```

### Get an Item

```bash
curl "http://localhost:8000/items/1"
```

### Get All Items

```bash
curl "http://localhost:8000/items/"
```

### Update an Item

```bash
curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item", "description": "This item has been updated"}'
```

### Delete an Item

```bash
curl -X DELETE "http://localhost:8000/items/1"
```

## Error Handling

The API includes basic error handling:

- 400 Bad Request: When trying to create an item with an ID that already exists
- 404 Not Found: When trying to read, update, or delete an item that doesn't exist

## Future Improvements

- Add authentication and authorization
- Implement a persistent database
- Add input validation and more robust error handling
- Implement pagination for the get all items endpoint
- Add unit tests and integration tests