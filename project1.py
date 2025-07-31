def calculate_remaining_due(total_due, payment_made):
    """
    Calculate remaining due amount after payment
    
    Parameters:
    total_due (float): Original amount owed
    payment_made (float): Payment amount received
    
    Returns:
    float: Remaining due amount
    """
    remaining_due = total_due - payment_made
    return max(remaining_due, 0)  # Ensures amount doesn't go negative

# Example usage
original_due = 1000.00
payment = 300.00
new_due = calculate_remaining_due(original_due, payment)
print(f"Remaining due amount: ${new_due:.2f}")