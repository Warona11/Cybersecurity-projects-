# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:  # Changed from k to key, as k was not defined.
        print(dictionary[key])  # Corrected to use key instead of k.

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",
    "maggie": "(Pacifier Suck)"
}

# Corrected to pass keys as a list
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
