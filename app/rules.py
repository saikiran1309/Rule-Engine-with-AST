from app.models import ASTNode
import re

# Create-Rule
def create_rule(rule_string: str) -> ASTNode:
    # Validate the rule string
    if not re.match(r'^[a-zA-Z0-9\s()><=]+$', rule_string):
        raise ValueError("Invalid rule string syntax")
    # Tokenize the rule string
    tokens = re.split(r'(\s+|\(|\))', rule_string)
    tokens = [token.strip() for token in tokens if token.strip()]
    root = parse_tokens_to_ast(tokens)
    return root

# Parse-token for Create-Rule
def parse_tokens_to_ast(tokens):
    if not tokens:
        return None
    # Build an AST based on tokens
    root = ASTNode(node_type='operator', operator='AND')
    for i in range(0, len(tokens), 2):  # Process tokens in pairs
        left_child = ASTNode(node_type='operand', value=tokens[i])  # Example
        right_child = ASTNode(node_type='operand', value=tokens[i + 2])  # Example
        root.left = left_child
        root.right = right_child
    return root

# Combine-Rule
def combine_rules(rules: list, operator: str) -> ASTNode:
    root = None
    for rule in rules:
        ast = create_rule(rule)
        if root:
            root = ASTNode(node_type='operator', operator=operator, left=root, right=ast)
        else:
            root = ast
    return root

# Evaluate-Rule
def evaluate_rule(ast: ASTNode, data: dict) -> bool:
    if ast.node_type == "operator":
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.operator == "AND":
            return left_eval and right_eval
        elif ast.operator == "OR":
            return left_eval or right_eval
    elif ast.node_type == "operand":
        # Comparison logic
        attr_value = data.get(ast.value)
        if ast.operator == ">":
            return attr_value > 30  # Replace with actual comparison logic
        elif ast.operator == "=":
            return attr_value == "Sales"  # Replace with actual comparison logic
    return False
