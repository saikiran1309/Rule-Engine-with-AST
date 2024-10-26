from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.crud import create_rule_ast, combine_rule_asts, evaluate_rule_ast
from typing import List
from pydantic import BaseModel

app = FastAPI()

class RuleCreate(BaseModel):
    rule_name: str
    rule_string: str

class CombineRulesRequest(BaseModel):
    rules: List[str]
    op: str

class EvaluateRuleRequest(BaseModel):
    ast: str
    data: dict

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rule-Create
@app.post("/api/rules/create_rule")
async def create_rule(request: RuleCreate):
    try:
        created_ast = create_rule_ast(request.rule_string)  
        formatted_ast = format_ast(created_ast)
        return {"formatted_tree": formatted_ast, "ruleName": request.rule_name}
    except ValueError as e:
        print(f"ValueError: {str(e)}") 
        raise HTTPException(status_code=400, detail=f"Invalid rule string format: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")  
        raise HTTPException(status_code=500, detail=str(e))


# Combine-Rules-Request
@app.post("/api/rules/combine_rules")
async def combine_rules(request: CombineRulesRequest):
    try:
        combined_ast = combine_rule_asts(request.rules, request.op)  # Make sure you're using 'op'
        formatted_ast = format_ast(combined_ast)  # Format the AST for display
        return {"formatted_tree": formatted_ast, "ruleName": "Combined Rule"}
    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging line to log the error
        raise HTTPException(status_code=400, detail=str(e))

# Format-AST
def format_ast(ast) -> str:
    def recurse(node, level=0):
        indent = "│   " * level + "├── "
        if "operation" in node:
            result = indent + node["operation"] + "\n"
            for child in node.get("nodes", []):
                result += recurse(child, level + 1)
        elif "condition" in node:
            result = indent + node["condition"] + "\n"
        else:
            result = indent + "<unknown node format>\n"
        return result
    return recurse(ast).strip()

# Evaluate-Rule-Request
@app.post("/api/rules/evaluate_rule")
async def evaluate_rule(request: EvaluateRuleRequest):
    try:
        # Here you would have your logic to evaluate the AST against the data
        # For demonstration, let's assume the evaluation is successful:
        evaluation_result = evaluate_rule_ast(request.ast, request.data)  # Your function here
        return {"result": evaluation_result}  # Return the evaluation result
    except Exception as e:
        # Instead of raising an HTTPException, return a result of false
        return {"result": False}




