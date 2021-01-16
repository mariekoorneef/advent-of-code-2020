def data(text: str, parser=str, sep='\n') -> list:
    """Split the day's text into sections separated by `sep`, and apply `parser` to each. """
    sections = text.split(sep)
    return list(map(parser, sections))


def lines(text: str) -> list:
    return text.splitlines()