knowledge_base = [
    {"topic": "op amp saturation", "content": "Op-amps saturate when output hits supply rails due to missing rails or high input."},
    {"topic": "no current", "content": "No current usually indicates an open circuit, bad wiring, or no power source."},
    {"topic": "noisy signal", "content": "Noise can be caused by poor grounding, interference, or long wires."}
]

def retrieve_context(problem):
    problem = problem.lower()
    results = []

    for item in knowledge_base:
        if any(word in problem for word in item["topic"].split()):
            results.append(item["content"])

    return "\n".join(results) if results else "No relevant context found."
