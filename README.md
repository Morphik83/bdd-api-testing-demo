# BDD API Testing Demo

This project demonstrates BDD (Behavior Driven Development), API testing, and mocking in Python using `behave`, `pytest`, and `requests`.

## Features
- BDD scenarios with `behave`
- API testing with `requests`
- Mocking with `unittest.mock`

## Getting Started

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run Behave tests:
   ```sh
   behave
   ```
3. Run Pytest tests:
   ```sh
   pytest
   ```

## Target System
- https://automationintesting.online/


## Postman & Newman Integration

This project includes API test automation using [Postman](https://www.postman.com/) and [Newman](https://www.npmjs.com/package/newman) for running API collections from the command line.

### How to Use
1. **Install Newman (Node.js required):**
   ```sh
   npm install -g newman
   ```
2. **Open the included Postman collection:**
   - File: `postman/room_api_tests.postman_collection.json`
   - Import into Postman to view and edit requests or assertions.
3. **Run the collection with Newman:**
   ```sh
   cd postman
   newman run "room_api_tests.postman_collection.json"
   ```
4. **Review test results** in your terminal (assertions are defined in the collection's scripts).

### Notes
- You can add or edit tests in Postman, then export the updated collection to the same file.
- Advanced usage: Try the [Postman CLI](https://learning.postman.com/docs/postman-cli/cli-overview/) for more reporting and CI/CD integration.

