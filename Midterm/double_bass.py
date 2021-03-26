from bass import Bass


class Double_Bass(Bass):
    def __init__(self, amplification, year, maker, bow_type, extension=None):
        super().__init__(amplification, year, maker)
        self.bow_type = bow_type
        self.extension = extension

    def get_bass_description(self):
        if self.extension:
            long_name = f"This bass was built by {self.maker.title()} in {self.year}.  It uses {self.amplification} amplification. It has a {self.extension} extension"
        else:
            long_name = f"This bass was built by {self.maker.title()} in {self.year}.  It uses {self.amplification} amplification."

        return long_name

    def get_bow_type(self):
        return self.bow_type