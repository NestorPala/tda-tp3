SEPARATOR = ","


def read_guerreros_file(filename, separator=SEPARATOR):
    try:
        with open(filename, "r") as groups:
            lines = [line for line in groups if not line.startswith("#")]
    except:
        print("Error opening groups file!")
        return None, None
    
    group_count = int(lines[0].strip())
    
    guerreros = []
    for line in lines[1:]:
        name, power = line.strip().split(separator)
        guerreros.append((name, int(power)))
    
    return group_count, guerreros
