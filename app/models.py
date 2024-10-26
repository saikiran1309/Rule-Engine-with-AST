# app/models.py
class ASTNode:
    def __init__(self, node_type: str, operator: str = None, value: str = None, left: 'ASTNode' = None, right: 'ASTNode' = None):
        self.node_type = node_type
        self.operator = operator
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self, visited=None):
        if visited is None:
            visited = set()  # Initialize a new set if this is the first call
        # Use the id of the current instance to track visits
        if id(self) in visited:
            return {"node_type": self.node_type, "operator": self.operator, "value": self.value}
        # Mark this instance as visited
        visited.add(id(self))
        return {
            "node_type": self.node_type,
            "operator": self.operator,
            "value": self.value,
            "left": self.left.to_dict(visited) if self.left else None,
            "right": self.right.to_dict(visited) if self.right else None,
        }
