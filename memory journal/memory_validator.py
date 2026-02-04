from custom_error import TextTooShortError
MIN_LENGTH = 200

def text_validator(text:str):
    if len(text) < MIN_LENGTH:
        raise TextTooShortError(
            f"Text should be at least {MIN_LENGTH} characters."
        )