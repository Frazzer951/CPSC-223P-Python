
class Bass:
    """A general representation of a bass."""
    def __init__(self, amplification, year, maker):
        """Initialize attributes to describe the bass."""
        self.amplification = amplification
        self.year = year
        self.maker = maker
        

    def get_bass_description(self):

        """Return a neatly formatted descriptive name."""
        long_name = f"This bass was built by {self.maker.title()} in {self.year}.  It uses {self.amplification} amplification."

        return long_name


