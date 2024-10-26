# app/crud.py
from app.models import ASTNode
import re
from typing import List

# Parse Expression
def parse_expression(expression):
    expression = expression.strip()
    if expression.startswith('(') and expression.endswith(')'):
        expression = expression[1:-1].strip()
    for op in ['AND', 'OR']:
        parts = split_expression(expression, op)
        if len(parts) > 1:
            return ASTNode(
                node_type="operator",
                operator=op,
                left=parse_expression(parts[0]),
                right=parse_expression(' '.join(parts[1:]))
            )
    # Print the expression being matched
    print(f"Matching expression: {expression}")

    pattern = r"(\w+)\s*([<>=!]+)\s*('[^']*'|\"[^\"]*\"|\w+)"
    match = re.match(pattern, expression)
    if match:
        left_operand = ASTNode(node_type="operand", value=match.group(1))
        right_operand = ASTNode(node_type="operand", value=match.group(3))
        return ASTNode(node_type="operator", operator=match.group(2), left=left_operand, right=right_operand)
    raise ValueError("Invalid rule string format")

# Split Expression
def split_expression(expression: str, operator: str) -> List[str]:
    parts = []
    depth = 0
    current_part = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for token in tokens:
        if token == '(':
            depth += 1
            current_part.append(token)
        elif token == ')':
            depth -= 1
            current_part.append(token)
        elif depth == 0 and token.upper() == operator:
            parts.append(' '.join(current_part).strip())
            current_part = []
        else:
            current_part.append(token)
    if current_part:
        parts.append(' '.join(current_part).strip())
    return parts

# Create Rule
def create_rule_ast(rule_string: str) -> ASTNode:
    return parse_expression(rule_string)

# Combine Rule
def combine_rule_asts(rules: List[str], operator: str):
    combined_structure = {
        "operation": operator,
        "nodes": []
    }
    # Split rules into AST nodes
    for rule in rules:
        conditions = rule.split(" AND ")  # Adjust if necessary for your parsing
        and_nodes = []
        for condition in conditions:
            and_nodes.append({
                "operation": "AND",
                "nodes": [{"condition": condition.strip()}]
            })
        combined_structure["nodes"].append({
            "operation": operator,
            "nodes": and_nodes
        })
    return combined_structure

# Evaluate Rule
def evaluate_rule(ast: ASTNode, data: dict) -> bool:
    if ast.node_type == "operator":
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.operator == "AND":
            return left_eval and right_eval
        elif ast.operator == "OR":
            return left_eval or right_eval
    elif ast.node_type == "operand":
        key = ast.value  # Adjust this based on your AST implementation
        operator = ast.operator  
        # Handle value processing if it is string
        value = ast.value  
        if isinstance(value, str) and (value[0] == "'" and value[-1] == "'"):
            value = value[1:-1]
        
        # Perform the comparison based on operator
        if operator == ">":
            return data[key] > float(value)  # Ensure correct type comparison
        elif operator == "<":
            return data[key] < float(value)
        elif operator == ">=":
            return data[key] >= float(value)
        elif operator == "<=":
            return data[key] <= float(value)
        elif operator == "==":
            return data[key] == value
        elif operator == "!=":
            return data[key] != value
        elif operator == "=":  # Assuming '=' is the same as '=='
            return data[key] == value
    return False

# Evaluate Rule
def evaluate_rule_ast(rule_ast: ASTNode, user_attributes: dict) -> bool:
    return evaluate_rule(rule_ast, user_attributes)

