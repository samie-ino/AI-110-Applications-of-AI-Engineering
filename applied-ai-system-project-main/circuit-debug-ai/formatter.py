def format_output(user_input, diagnosis, evaluation, confidence):
    return f"""
══════════════════════════════════
🔍 CIRCUIT DEBUG REPORT
══════════════════════════════════

📥 Input:
{user_input}

──────────────────────────────────
🧠 AI Reasoning + Diagnosis:
{diagnosis}

──────────────────────────────────
🧪 Verification:
{evaluation}

──────────────────────────────────
📊 Confidence:
{confidence}

══════════════════════════════════
"""
