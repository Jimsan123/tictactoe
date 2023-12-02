import re

def parseCoordinates(text: str):
    pattern = r"\(([^,]+),([^)]+)\)"
    matches = re.findall(pattern, text)
    coordinates = []
    for match in matches:
        x, y = match
        coordinates.append((x.strip(), y.strip()))  # Stripping to remove any extra whitespace
    return coordinates

# Example usage
text = "Here are some coordinates: (12, 34), (56, 78) and (9,10)."
# Result is: [('12', '34'), ('56', '78'), ('9', '10')]