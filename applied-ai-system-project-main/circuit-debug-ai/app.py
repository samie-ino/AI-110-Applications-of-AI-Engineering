import streamlit as st
from agent import diagnose
from logger import log_interaction
from calculator import (
    get_resistors_for_voltage,
    calculate_series_resistance,
    calculate_parallel_resistance,
    format_resistance,
    get_connection_advice
)

st.set_page_config(page_title="Circuit Debug AI", layout="wide")

st.title("⚡ Circuit Debugging AI Assistant")

# Create tabs
tab1, tab2 = st.tabs(["🔍 Diagnosis", "⚡ Voltage & Resistor Calculator"])

# Sidebar
st.sidebar.title("⚙️ Options")
show_logs = st.sidebar.checkbox("Show Logs")

# TAB 1: DIAGNOSIS
with tab1:
    st.write("Diagnose and troubleshoot circuit problems using AI.")
    
    # Input
    user_input = st.text_area("Describe your circuit issue:", height=150)
    
    if st.button("Analyze Circuit"):
        if user_input.strip() == "":
            st.warning("Please enter a circuit issue.")
        else:
            with st.spinner("Analyzing..."):
                diagnosis = diagnose(user_input)
                log_interaction(user_input, diagnosis, "", "")
    
            st.success("Analysis Complete")
    
            st.subheader("🔍 Diagnosis")
            st.write(diagnosis)

# TAB 2: RESISTOR CALCULATOR
with tab2:
    st.write("Calculate resistor values and combinations for your circuit.")
    
    calc_mode = st.radio("Choose mode:", ["Voltage → Find Resistors", "Resistor Values → Calculate Total"])
    
    if calc_mode == "Voltage → Find Resistors":
        st.subheader("🔌 Resistor Finder")
        
        col1, col2 = st.columns(2)
        
        with col1:
            voltage = st.number_input("Supply Voltage (V):", min_value=1.0, max_value=48.0, value=5.0, step=0.5)
        
        with col2:
            current_ma = st.number_input("Desired Current (mA):", min_value=1.0, max_value=100.0, value=10.0, step=1.0)
        
        if st.button("Find Suitable Resistors"):
            resistors = get_resistors_for_voltage(voltage, current_ma)
            
            if resistors:
                st.success("✅ Recommended resistors:")
                
                for i, r in enumerate(resistors, 1):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Option {i}:** {format_resistance(r['value'])}")
                    with col2:
                        st.write(f"Current: {r['current_ma']:.2f} mA")
                    with col3:
                        st.write(f"Error: {r['error']:.1f}%")
                
                # Add connection advice
                st.subheader("💡 Connection Options")
                
                best_resistor = resistors[0]['value']
                
                st.write("**If you have these standard resistor values available:**")
                
                # Suggest series combinations
                st.write("**Series (to INCREASE resistance):**")
                for base in [100, 220, 330, 470]:
                    count = round(best_resistor / base)
                    if 2 <= count <= 10:
                        total = count * base
                        st.write(f"  • {count}× {format_resistance(base)} in series = {format_resistance(total)}")
                
                # Suggest parallel combinations
                st.write("**Parallel (to DECREASE resistance):**")
                for base in [1000, 2200, 3300, 4700]:
                    count = round(base / best_resistor)
                    if 2 <= count <= 10:
                        total = base / count
                        st.write(f"  • {count}× {format_resistance(base)} in parallel = {format_resistance(total)}")
            else:
                st.error("❌ No suitable resistors found. Try a higher voltage.")
    
    else:  # Resistor Values → Calculate Total
        st.subheader("🔢 Series/Parallel Calculator")
        
        # Get connection type
        connection = st.radio("Connection Type:", ["Series", "Parallel"], horizontal=True)
        
        # Get number of resistors
        num_resistors = st.slider("Number of resistors:", min_value=1, max_value=10, value=2)
        
        # Input resistor values
        resistor_values = []
        cols = st.columns(min(5, num_resistors))
        
        for i in range(num_resistors):
            with cols[i % 5]:
                r_val = st.number_input(f"R{i+1} (Ω):", min_value=1.0, value=330.0, step=1.0, key=f"r{i}")
                resistor_values.append(r_val)
        
        if st.button("Calculate Total Resistance"):
            if connection == "Series":
                total = calculate_series_resistance(resistor_values)
            else:
                total = calculate_parallel_resistance(resistor_values)
            
            st.success(f"✅ Total Resistance: **{format_resistance(total)}**")
            
            # Show connection advice
            advice = get_connection_advice(connection.lower(), num_resistors)
            st.info(f"💡 {advice}")
            
            # Calculate safe voltages based on power ratings
            st.subheader("⚠️ Safe Voltage Limits")
            
            # Standard power ratings for resistors
            power_ratings = [0.125, 0.25, 0.5, 1.0]  # 1/8W, 1/4W, 1/2W, 1W
            
            for power in power_ratings:
                # P = V²/R → V = √(P*R)
                max_voltage = (power * total) ** 0.5
                st.warning(f"**{power}W resistor:** Max safe voltage = **{max_voltage:.2f}V** (dissipates {power}W at this voltage)")
            
            st.info("💡 **Recommendation:** Choose resistors with power rating suitable for your circuit's operating voltage. When in doubt, use a higher power rating (e.g., 1/2W instead of 1/4W).")
            
            # Visual representation
            st.subheader("Connection Diagram")
            if connection == "Series":
                diagram = " ─── ".join([f"[{format_resistance(r)}]" for r in resistor_values])
            else:
                diagram = " ‖ ".join([f"[{format_resistance(r)}]" for r in resistor_values])
            st.code(diagram, language="text")

# Show logs
if show_logs:
    try:
        with open("log.txt", "r") as f:
            st.text(f.read())
    except:
        st.write("No logs yet.")

st.markdown("---")

# Test button
if st.button("Run System Tests"):
    results, passed, total = run_tests()

    st.subheader("🧪 Test Results")

    for r in results:
        if r["passed"]:
            st.success(f"{r['input']} → Passed ({r['confidence']})")
        else:
            st.error(f"{r['input']} → Failed ({r['confidence']})")

    st.write(f"### {passed}/{total} tests passed")
