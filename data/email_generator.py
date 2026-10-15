import uuid

def generate_email() -> str:
    return f"test_{uuid.uuid4().hex[:10]}@example.com"