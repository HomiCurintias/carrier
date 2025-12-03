def _check(file):
    if not file.endswith(".carrier"):
        raise ValueError("Expected: .carrier")

def body(file, data):
    _check(file)

    with open(file, "r") as reader:
        lines = reader.readlines()

    data = data + ":"

    for i in range(len(lines)):
        if lines[i].strip() == data:
            if i + 1 < len(lines):
                prox = lines[i + 1].strip()

                try:
                    return int(prox)
                except:
                    return prox

    return "Not found"


def ncar(file, name, value):
    _check(file)

    with open(file, "w") as arq:
        arq.write(f"{name}:\n\t{value}")


def apd(file, name, value):
    _check(file)

    with open(file, "a") as arq:
        arq.write(f"\n{name}:\n\t{value}")


def cng(file, data, value):
    _check(file)

    with open(file, "r") as reader:
        lines = reader.readlines()

    data = data + ":"

    for i in range(len(lines)):
        if lines[i].strip() == data:
            if i + 1 < len(lines):
                lines[i + 1] = f"\t{value}\n"
                break

    with open(file, "w") as writer:
        writer.writelines(lines)