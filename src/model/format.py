from enum import Enum


class Format(Enum):
    EBOOK = 'eBook'
    AUDIOBOOK = 'Audiobook'
    # TODO: add paperback and hardcover once the csv file has been updated to include them also
