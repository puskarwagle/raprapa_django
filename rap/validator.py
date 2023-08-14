from django.core.exceptions import ValidationError
from datetime import datetime
import re

def validate_phone_number(value):
    # Regular expression to match a valid phone number format
    pattern = r'^\d{10}$'
    
    if not re.match(pattern, value):
        raise ValidationError("Enter a valid 10-digit phone number.")

def validate_nullable_integer(value):
    # print(f"Value received: {value}") 
    
    if value is None or value == "":
        # print("Value is None or empty")
        return None
    
    if isinstance(value, str):
        # print("Value is a string")
        
        if value.strip() == "":
            # print("Value is a blank string")
            return None
    
    try:
        int_value = int(value)
        # print(f"Value successfully converted to int: {int_value}") 
        return int_value
    except (ValueError, TypeError):
        # print("Value conversion to int failed")
        raise ValidationError("Enter a valid integer or leave it blank.")


# def parse_and_validate_date(input_date):
#     if not input_date:
#         return None  # Return None for empty input
    
#     try:
#         # Parse input date in MM-DD-YYYY format
#         parsed_date = datetime.strptime(input_date, '%m-%d-%Y')
#         # Convert parsed date to YYYY-MM-DD format
#         formatted_date = parsed_date.strftime('%Y-%m-%d')
#         return formatted_date
#     except ValueError:
#         return None
