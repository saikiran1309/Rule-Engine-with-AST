# Rule Engine with AST ( Abstract Syntax Tree )

## Objective
The goal of this project is to develop a simple 3-tier rule engine application comprising a user interface, API, and backend, along with data management. This application will determine user eligibility based on various attributes such as age, department, income, and spending. By leveraging an Abstract Syntax Tree (AST), the system will enable the dynamic creation, combination, and modification of conditional rules, making it flexible and adaptable to changing requirements.

## Project Structure
```csharp
    Rule Engine with AST/
    │
    ├── app/
    │   ├── __init__.py           # Initializes the app package.
    │   ├── crud.py               # CRUD operations for rules and users.
    │   ├── main.py               # Entry point for the FastAPI app.
    │   ├── models.py             # Database models and schemas.
    │   └── rules.py              # Logic for rule handling and AST.
    │
    ├── static/
    │   ├── style.css             # CSS styles for the UI.
    │   └── main.js               # JavaScript for client-side logic.
    │
    ├── templates/
    │   └── index.html            # Main HTML template.
    │
    ├── requirements.txt          # Required Python packages.
    └── README.md                 # Project overview and instructions.

```
## API Design & Features
- **create_rule**: This function takes a string representing a rule and returns a Node object that represents the corresponding Abstract Syntax Tree (AST).<br><br>
![Create Rule](https://github.com/user-attachments/assets/5e15ce9c-109a-42c2-beba-f7aa25303c05)
  
- **combine_rules**: This function accepts a list of rule strings and merges them into a single AST, focusing on efficiency and reducing redundant checks. It returns the root node of the combined AST.<br><br>
![Combine Rules](https://github.com/user-attachments/assets/2fed90c4-9d11-4514-8adc-8e0f8035420b)

- **evaluate_rule**: This function evaluates the combined AST against provided attribute data (e.g., age, department, salary, experience). It returns True if the user meets the criteria defined by the rule; otherwise, it returns False.<br><br>
![Evaluate Rule](https://github.com/user-attachments/assets/e69e97bf-c757-4842-9d0d-b4d681912652)

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
You can implement and execute tests to verify that everything functions properly.
```
Created By : Sai Kiran
