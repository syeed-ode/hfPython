
def search4vowles(phrase:str) -> set:
    """Returns the set of vowels found in phrase"""
    return set('aeiof').intersection(set(phrase))


def search4letters(prhase:str, letters:str = 'aeiou') -> set:
    """Returns the set of letters found in phrase, defaults to vawels"""
    return set(prhase).intersection(set(letters))