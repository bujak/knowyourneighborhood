from model import Model
from tabulate import tabulate


class Controler:
    "Controler class to make data for view"
    
    def __init__(self):
        self.model = Model('malopolska.csv')

    def control_statistics(self):
        """
        Gets data from model and prepare them for view
        :return: string to print
        """
        stats = self.model.get_statistics()
        return tabulate(stats, ["MALOPOLSKA", "AMOUNT"])


    def control_get_3cities_with_longest_name(self):
        """
        Gets data from model and prepare them for view
        :return: string to print
        """
        cities = self.model.get_3cities_with_longest_name()
        cities_string = "THREE CITIES WITH LONGEST NAMES: \n"
        for city in cities:
            cities_string += "\t{} \n".format(city)
        return cities_string

    def control_get_largest_county_by_communities(self):
        """
        Gets data from model and prepare them for view
        :return: string to print
        """
        county = self.model.get_largest_county_by_communities()
        return "COUNTY WITH LARGEST NUMBER OF COMMUNITIES: \n\t{}".format(county.upper())

    def control_locations_belongs_to_more_than_one(self):
        """
        Gets data from model and prepare them for view
        :return: string to print
        """
        locations = self.model.get_locations_belongs_more_than_one_cat()
        locations_string = "LOCATIONS BELONGS TO MORE THAN ONE CATEGORY: \n"
        for location in locations:
            locations_string += '\n\t{}'.format(location)
        return locations_string

    def control_advanced_search(self, string):
        """
        Gets data from model and prepare them for view
        :param string: string input by user in console
        :return: string to print, int: number of records found
        """
        results = self.model.advanced_search(string)
        return tabulate(results, ['LOCATION', 'TYPE']), len(results)
