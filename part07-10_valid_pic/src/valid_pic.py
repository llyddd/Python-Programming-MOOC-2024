from datetime import datetime

def is_it_valid(pic: str):
    control_ref = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    century_ref = {"+": "18", "-": "19", "A": "20"}
    
    # Ensure correct length
    if len(pic) != 11:
        return False
    
    # Extract date components
    day = pic[:2]
    month = pic[2:4]
    year_suffix = pic[4:6]
    century_marker = pic[6]
    personal_identifier = pic[7:10]
    control_character = pic[10]

    # Validate century marker
    if century_marker not in century_ref:
        return False
    
    # Construct full year
    full_year = century_ref[century_marker] + year_suffix

    # Check if the date is valid using datetime
    try:
        datetime.strptime(f"{full_year}-{month}-{day}", "%Y-%m-%d")
    except ValueError:
        return False

    # Compute control character
    nine_digit_number = int(day + month + year_suffix + personal_identifier)
    calculated_control_character = control_ref[nine_digit_number % 31]

    # Check if control character matches
    return calculated_control_character == control_character

if __name__ == "__main__":

    pic = is_it_valid("080842-720N")
    print(pic)