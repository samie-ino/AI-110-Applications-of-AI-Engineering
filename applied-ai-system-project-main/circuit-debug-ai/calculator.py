# Common resistor values (E12 series)
RESISTOR_VALUES = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]

def get_resistors_for_voltage(voltage, current_ma=10):
    """
    Calculate recommended resistor values for a given voltage and desired current.
    Assumes LED with ~2V forward voltage drop.
    
    Args:
        voltage: Supply voltage in volts
        current_ma: Desired current in milliamps (default 10mA for LEDs)
    
    Returns:
        List of (resistor_value, multiplier) tuples
    """
    # Subtract LED forward voltage
    voltage_drop = voltage - 2.0
    
    if voltage_drop <= 0:
        return []
    
    # Calculate target resistance using Ohm's law
    target_resistance = (voltage_drop * 1000) / current_ma
    
    recommendations = []
    
    # Find best matches in standard resistor values
    for multiplier in [1, 10, 100, 1000, 10000]:
        for base_value in RESISTOR_VALUES:
            resistor_value = base_value * multiplier
            actual_current = (voltage_drop * 1000) / resistor_value
            error_percent = abs(actual_current - current_ma) / current_ma * 100
            
            if error_percent < 30:  # Within 30% of desired current
                recommendations.append({
                    'value': resistor_value,
                    'current_ma': actual_current,
                    'error': error_percent
                })
    
    # Sort by error and return top 5
    recommendations.sort(key=lambda x: x['error'])
    return recommendations[:5]


def calculate_series_resistance(resistors):
    """
    Calculate total resistance for resistors in series.
    
    Args:
        resistors: List of resistor values
    
    Returns:
        Total resistance
    """
    return sum(resistors)


def calculate_parallel_resistance(resistors):
    """
    Calculate total resistance for resistors in parallel.
    
    Args:
        resistors: List of resistor values
    
    Returns:
        Total resistance
    """
    if not resistors or any(r == 0 for r in resistors):
        return 0
    
    reciprocal_sum = sum(1/r for r in resistors)
    return 1 / reciprocal_sum


def format_resistance(ohms):
    """
    Format resistance value with appropriate units.
    
    Args:
        ohms: Resistance in ohms
    
    Returns:
        Formatted string
    """
    if ohms >= 1000000:
        return f"{ohms / 1000000:.2f} MΩ"
    elif ohms >= 1000:
        return f"{ohms / 1000:.2f} kΩ"
    else:
        return f"{ohms:.2f} Ω"


def get_connection_advice(config_type, num_resistors):
    """
    Get advice on how to connect resistors.
    
    Args:
        config_type: 'series' or 'parallel'
        num_resistors: Number of resistors
    
    Returns:
        String with advice
    """
    if config_type == "series":
        return f"Connect {num_resistors} resistors end-to-end in a line. The total resistance will be the sum of all individual resistances. Good for increasing resistance."
    else:
        return f"Connect {num_resistors} resistors so all their leads touch the same two points (like branches). The total resistance will be lower than any individual resistor. Good for spreading current load."
