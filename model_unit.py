class Unit:
    # Unit class for administrative unit

    def __init__(self, woj, pow, gmi, rgmi, name, unit_type):
        """

        :param woj: str: woj id from csv
        :param pow: str: pow id from csv
        :param gmi: str: gmi id from csv
        :param rgmi: str: rgmi id from csv
        :param name: str: name of unit
        :param unit_type: administrative type of unit
        """
        self.woj = woj
        self.pow = pow
        self.gmi = gmi
        self.rgmi = rgmi
        self.name = name
        self.unit_type = unit_type

    def __repr__(self):
        """
        :return: string: information about object
        """
        return "{} {}".format(self.name, self.unit_type)
