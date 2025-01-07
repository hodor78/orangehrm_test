from datetime import datetime

def generate_unique_user_id(prefix="hodor"):
    timestamp = datetime.now().strftime("%m%d%H%M%S")
    unique_id = f"{prefix}{timestamp}"
    return unique_id
