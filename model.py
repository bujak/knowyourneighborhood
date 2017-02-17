import csv
from model_unit import Unit
from collections import Counter


class Model:
    # Model class to handle data from csv file

    def __init__(self, csv_file):
        """
        :param csv_file: string: filename of csv file with data
        """
        raw_data = self.load_file(csv_file)
        self.data = self.make_objects_list(raw_data)
        self.load_file(csv_file)

    def load_file(self, file_name):
        """
        Read csv file and insert data to list of list

        :param csv_file: string: filename of csv file with data
        :return: list: list with list with data from file
        """
        data = []
        with open(file_name, 'r') as new_file:
            lines = csv.reader(new_file, delimiter='\t')
            for row in lines:
                data.append(row)
        data = data[1:]
        return data

    def make_objects_list(self, data):
        """
        Create objecst of Unit class and store them in list
        :param data: list: list of list with data from file
        :return: list: list with objects
        """
        unit_list = []
        for row in data:
            unit_list.append(Unit(row[0], row[1], row[2], row[3], row[4], row[5]))
        return unit_list

    def get_statistics(self):
        """
        Counts for occurencies of unit type in objects list
        :return: list: list with tuples (unit_type(str): how many units(int))
        """
        types = []
        for unit in self.data:
            types.append(unit.unit_type)
        return Counter(
            types).most_common()  # count occurencies of same unit_type and put data in tuples (unit_type: ocurencies)

    def get_3cities_with_longest_name(self):
        """
        Get list with all cities names, sort them by length and return longest 3
        :return: list: list with longest cities names
        """
        cities = []
        for city in self.data:
            if city.unit_type == "miasto":
                cities.append(city.name)
        sorted_cities = sorted(cities, key=lambda x: len(x), reverse=True)
        return sorted_cities[:3]

    def get_largest_county_by_communities(self):
        """
        Get list with all 'pow' ids, count occurencies, find name of id with largest occurencies
        :return: string: string with name of county
        """
        counties = []
        for unit in self.data:
            counties.append(unit.pow)
        largest_county_id = Counter(counties).most_common(1)[0][
            0]  # count occurencies of county id and assign id to variable

        for item in self.data:  # get name of county by id
            if largest_county_id in item.pow:
                return item.name

    def get_locations_belongs_more_than_one_cat(self):
        """
        Store all names in list then count occurencies of names. If number larger than 1, store name in another list
        :return: list: list with location names
        """
        locations = []
        unit_names = []
        for unit in self.data:
            unit_names.append(unit.name)
        unit_names = Counter(unit_names).most_common()  # list of tuples: (unit_name, occurencies)

        for item in unit_names:
            if item[1] > 1:  # if occurencies higher than 1, append to list
                locations.append(item[0])
        return locations

    def advanced_search(self, string):
        """
        Find string input by user before in units names
        :param string: string typed by user in console
        :return: list with list like [name, type]
        """
        search_list = []
        found = []
        for unit in self.data:
            if string.lower() in unit.name.lower():
                search_list.append(unit)

        sorted_search_list = sorted(sorted(search_list, key=lambda x: x.name), key=lambda x: unit.unit_type)

        for unit in sorted_search_list:
            found.append([unit.name, unit.unit_type])
        return found
