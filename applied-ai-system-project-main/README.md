# ⚡ Circuit Debugging AI Assistant

## 📌 Original Project (Modules 1–3)
This project builds on my work from Modules 1–3, where I learned to debug AI-generated code, design structured systems, and understand how AI models make decisions. The original goal was to use AI as a collaborator while maintaining control through testing and verification. This project extends those ideas into a practical tool that diagnoses and validates electronic circuit issues.

## 🚀 Title & Summary
**Circuit Debugging AI Assistant** is a lightweight AI-powered tool that helps users troubleshoot electronic circuits. It analyzes a user’s problem, generates possible causes and testing steps, and then verifies its own reasoning to improve reliability.

This project demonstrates how AI can be used responsibly by combining **generation + verification**, rather than relying on a single response.

## 🧠 Architecture Overview
The system uses a **streamlined AI agent workflow**:

- **User Input** → User describes a circuit issue  
- **AI Agent (Diagnosis Engine)** → Generates possible causes and troubleshooting steps  
- **Output Formatter** → Structures results into readable sections  
- **Logger** → Records inputs and outputs for reliability  
- **Final Output** → Displays a structured debug report  
- **Human-in-the-loop** → User reviews results and provides feedback  

## 🚀 Advanced Features

- Implemented a Retrieval-Augmented Generation (RAG) system using a custom knowledge base
- Added agentic reasoning with step-by-step analysis
- Specialized the AI for electrical engineering problem-solving
- Fast diagnosis without unnecessary verification overhead


## ⚙️ Setup Instructions

### 1. Clone the repository
    git clone https://github.com/yourusername/circuit-debug-ai.git
    cd circuit-debug-ai

### 2. Install dependencies
    pip install google-generativeai python-dotenv streamlit

### 3. Set up environment variables
Create a `.env` file:
    GEMINI_API_KEY=your_api_key_here

### 4. Run the Streamlit app
    cd circuit-debug-ai
    streamlit run app.py

## 💬 Sample Interactions

### Example 1
Input:
    My op-amp output is stuck high

Output:
    ⚠️ Possible Causes:
    - Op-amp saturation
    - Missing negative power rail
    - Feedback loop disconnected

    🧪 Suggested Tests:
    - Measure supply voltages
    - Check feedback connections

    🧠 Verification:
    Diagnosis is consistent with common op-amp failure modes.
    📊 Confidence: 88%
    📊 Confidence: 88%

### Example 2
Input:
    No current flowing in my circuit

Output:
    ⚠️ Possible Causes:
    - Open circuit
    - Incorrect wiring
    - Dead power source

    🧪 Suggested Tests:
    - Check continuity
    - Measure voltage across components

    🧠 Verification:
    No contradictions found. Causes align with expected electrical behavior.

    📊 Confidence: 91%

### Example 3
Input:
    Signal looks noisy on oscilloscope

Output:
    ⚠️ Possible Causes:
    - External interference
    - Poor grounding
    - Signal integrity issues

    🧪 Suggested Tests:
    - Check grounding connections
    - Reduce nearby noise sources

    🧠 Verification:
    Diagnosis matches common signal noise issues.

    📊 Confidence: 85%

## ⚖️ Design Decisions

- Agent + Evaluator Workflow:  
  A two-step AI process (diagnose → verify) improves reliability.

- Structured Output:  
  Information is organized into clear sections for usability.

- Lightweight Design:  
  No database is used; logs are stored locally to keep the system simple.

Trade-offs:
- Simplicity over scalability  
- Faster development over advanced features  
- Approximate confidence scoring instead of formal evaluation  

## 🧪 Testing Summary

What worked:
- AI generated useful troubleshooting steps  
- Verification improved trust in outputs  
- Structured format improved readability  

What didn’t:
- Some responses were too general  
- Confidence scores are not mathematically rigorous  

What I learned:
- AI outputs must be verified, not blindly trusted  
- System design matters more than prompt quality alone  
- Adding evaluation layers significantly improves reliability  

## 🔍 Reflection

This project taught me that AI should be used as part of a controlled system, not as a standalone solution. I learned how to design workflows where AI generates ideas, but those ideas are validated and structured.

It reinforced skills in:
- critical thinking with AI  
- system design  
- building reliable, testable tools  

## 📈 Future Improvements
- Add real circuit data input (oscilloscope/sensors)  
- Implement Retrieval-Augmented Generation (RAG)  
- Improve verification with rule-based checks  
- Build a web interface for better user experience  

## 🎬Demo Video 
https://www.loom.com/share/ae14d75ef00248bdb825d41ba3ec6e9b
