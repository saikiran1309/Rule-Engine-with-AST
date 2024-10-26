# Rule Engine with AST ( Abstract Syntax Tree )

## Overview
This application functions as a rule engine that assesses user eligibility based on factors like age, department, salary, and experience. It employs an Abstract Syntax Tree (AST) to represent and handle conditional rules, enabling the dynamic creation, combination, and evaluation of these rules.

## Project Structure
```csharp
    Rule Engine with AST/
    │
    ├── app/
    |   ├──  __init__.py
    │   ├── crud.py
    │   ├── main.py
    │   ├── models.py
    |   └── rules.py
    |
    ├── static/
    │   ├── style.css
    |   └── main.js
    |
    ├── templates/
    │   └── index.html
    │
    ├── requirements.txt
    └── README.md
```

## Getting Started

### Prerequisites

- Make sure you have **Python** installed on your system.
- confirm by using
  
   ```bash
   python --version
   ```

### Installation
1. **Clone the Repository**
   ```bash
   git clone "https://github.com/saikiran1309/Rule-Engine-with-AST.git"
   cd Rule-Engine-with-AST
   ```

2. **Create a new virtual environment for the project**
   ```bash
   pip install virtualenv
   virtualenv venv         # Create a new venv
   venv\Scripts\activate    # Activate the virtual environment
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **To run the app, use:**
   ```bash
   uvicorn app.main:app 
   ```
## API Endpoints

1. **Create Rule**
   - **Endpoint:** `/api/rules/create_rule`
   - **Method:** POST
   - **Body:**

     ```json
     {
      "rule_name": "Rule1",
      "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
     }
     ```
     
2. **Combine Rules**
   - **Endpoint:** `/api/rules/combine_rules`
   - **Method:** POST
   - **Body:**

     ```json
     {
        "rules": [
          "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
          "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        ],
        "op": "AND"
     }  
     ```
     
3. **Evaluate Rule**
   - **Endpoint:** `/api/rules/evaluate_rule`
   - **Method:** POST
   - **Body:**

     ```json
     {
       "name": "Saikiran", 
       "age": 22,
       "country": "India", 
       "salary": 500000,
       "position": "Developer",
       "experience": 3
      }
     ```
## Running Tests
You can add and run tests to ensure everything is working correctly. 
```
Created By : Sai Kiran
