## 🧪 Reliability & Testing

To ensure the system works reliably, the following methods are implemented:

- **Clear Structured Outputs:**  
  The AI generates organized troubleshooting steps in a consistent format.

- **Logging:**  
  All inputs and generated outputs are recorded locally for debugging and traceability.

- **Human Evaluation:**  
  Outputs are manually reviewed to confirm whether suggested causes and tests are realistic and useful.

### Testing Results

- Produces accurate and relevant troubleshooting steps
- System performs best when user input is clear and detailed
- Provides consistent, well-structured responses
- Significantly faster than verification-based approaches


## ⚠️ Responsible AI Reflection

### Limitations & Biases
This system relies on a general-purpose language model, which means its responses are based on learned patterns rather than true understanding. As a result, it can sometimes produce overly generic or incomplete diagnoses, especially when user input lacks detail. The system is also biased toward common circuit problems, meaning it may not perform as well on highly specialized or uncommon scenarios.

### What Surprised Me
One surprising result during testing was how much the quality of the input affected the output. When the input was clear and specific, the AI performed very well and produced accurate troubleshooting steps. However, vague inputs led to weaker and more generalized responses, highlighting the importance of context in AI systems.

### Collaboration with AI
Throughout this project, I used AI as a collaborator rather than a decision-maker.

- **Helpful instance:**  
  AI was effective at quickly generating structured troubleshooting steps and organizing them into clear categories (causes, tests, verification), which helped speed up development.

Overall, this project showed me that AI is most useful when guided and integrated into a structured system.
