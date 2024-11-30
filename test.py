def valid_csv_line(input: str, expected_columns: int) -> tuple[bool, str]:
    values = input.split(",")

    if len(values) != expected_columns:
        return False, ""
    
    if any(value == "" for value in values):
        return False, ""

    if expected_columns == 3:
        try: int(values[2])
        except ValueError: return False, ""

    new_input = ",".join(value.replace(" ", "") for value in values)
    return True, new_input
    
test = [
    "asdsa d `,  as d s ad, 12323213   ",
    "adsasd,asasd",
    "adadas,asdsd"
]
A = "12311313"
print(A[0:2])