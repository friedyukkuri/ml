def FindStringInFile(lines: list, string: str) -> list:
    results = []
    for line in lines:
        if string in line:
            results.append(line)
    return results

def FindStringInFileIgnoreCase(lines: list, string: str) -> list:
    results = []
    for line in lines:
        if string in line.lower():
            results.append(line)
    return results

if __name__ == "__main__":

    # Test the functions
    lines = ["Hello, World!", "Python is awesome", "Hello, Python!"]
    string = "Hello"
    results = FindStringInFile(lines, string)
    assert results == ["Hello, World!", "Hello, Python!"]