from datetime import datetime

def log_interaction(user_input, diagnosis, evaluation, confidence):
    with open("log.txt", "a") as f:
        f.write(f"\n--- {datetime.now()} ---\n")
        f.write(f"Input: {user_input}\n")
        f.write(f"Diagnosis: {diagnosis}\n")
        f.write(f"Evaluation: {evaluation}\n")
        f.write(f"Confidence: {confidence}\n")
