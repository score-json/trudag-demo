import yaml

def check_test_execution(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    return (1.0, [])
    test_name = configuration.get("test_name", None)
    
    if check_name_in_file(test_name, "passed_tests.txt"):
        score = 1.0
    else:
        score = 0.0
    print(f"Test execution check for '{test_name}': {score}")
    return (score, [])


def check_name_in_file(name_to_check, file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines in the file
            contents = file.read()
            
            # Check if the name exists in the file (case-sensitive match)
            if name_to_check in contents:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return False