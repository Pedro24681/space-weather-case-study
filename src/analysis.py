# src/analysis.py

def calculate_storm_statistics(storm_data):
    """
    Calculate statistics for space weather storms.

    Parameters:
    storm_data (list): A list of storm data entries.

    Returns:
    dict: A dictionary containing storm statistics, e.g., average intensity, max intensity.

    Raises:
    ValueError: If storm_data is empty or not a list.
    """
    if not isinstance(storm_data, list) or not storm_data:
        raise ValueError("Invalid input: storm_data must be a non-empty list.")
    
    # Compute statistics (placeholder implementation)
    average_intensity = sum(storm_data) / len(storm_data)
    max_intensity = max(storm_data)
    
    return {
        "average_intensity": average_intensity,
        "max_intensity": max_intensity
    }

def classify_kp_events(kp_index):
    """
    Classify Kp index events.

    Parameters:
    kp_index (float): The Kp index value.

    Returns:
    str: The classification of the Kp index event.

    Raises:
    ValueError: If kp_index is not between 0 and 9.
    """
    if kp_index < 0 or kp_index > 9:
        raise ValueError("Kp index must be between 0 and 9.")
    
    if kp_index <= 3:
        return "Low"
    elif kp_index <= 5:
        return "Moderate"
    elif kp_index <= 7:
        return "High"
    else:
        return "Extreme"

def detect_extreme_events(event_data):
    """
    Detect extreme space weather events.

    Parameters:
    event_data (list): A list of event intensities.

    Returns:
    list: A list of extreme events detected.

    Raises:
    ValueError: If event_data is not a list.
    """
    if not isinstance(event_data, list):
        raise ValueError("Invalid input: event_data must be a list.")
    
    # Detect extreme events (placeholder implementation)
    extreme_threshold = 100  # Example threshold for extreme events
    extreme_events = [event for event in event_data if event > extreme_threshold]
    
    return extreme_events