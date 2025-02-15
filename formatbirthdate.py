from CTkMessagebox import CTkMessagebox

def validate_and_format_birthdate(birthdate):
    months = {
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
    }

    special_month = {"February"}
    thirtyone_days = {
        "January", "March", "May", "July",
        "August", "October", "December"
    }
    thirty_days = {"September", "April", "June", "November"}

    birthdate_parts = str(birthdate).split()
    if len(birthdate_parts) == 3:
        month = str(birthdate_parts[0]).capitalize()
        day = int(str(birthdate_parts[1]).strip(","))
        year = str(birthdate_parts[2])
        if month in months:
            if month in special_month and day > 29:
                CTkMessagebox(title="Error", message = "Invalid day in birthdate.", icon = "warning", sound = True)
            elif month in thirtyone_days and day > 31:
                CTkMessagebox(title="Error", message = "Invalid day in birthdate.", icon = "warning", sound = True)
            elif month in thirty_days and day > 30:
                CTkMessagebox(title="Error", message = "Invalid day in birthdate.", icon = "warning", sound = True)
            else:
                if len(year) == 4:
                    formatted_birthdate = f"{month} {day}, {year}"
                    return formatted_birthdate
                else:
                    CTkMessagebox(title="Error", message = "Invalid year in birthdate.", icon = "warning", sound = True)
        else:
            CTkMessagebox(title="Error", message = "Invalid month in birthdate.", icon = "warning", sound = True)
    else:
        CTkMessagebox(title="Error", message = "Invalid birthdate.", icon = "warning", sound = True)
