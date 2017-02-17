from controller import Controler
from os import system

class View:
    def __init__(self):
        self.controller = Controler()

    @staticmethod
    def enter_to_continue():
        """
        Input for stoping console screen
        """
        input("\nEnter to continue\n")

    def view_statistics(self):
        """
        Get string from controler and print it
        """
        print(self.controller.control_statistics())

    def view_3_cities(self):
        """
        Get string from controler and print it
        """
        print(self.controller.control_get_3cities_with_longest_name())

    def view_locations_belongs_to_more_than_one(self):
        """
        Get string from controler and print it
        """
        print(self.controller.control_locations_belongs_to_more_than_one())

    def view_control_get_largest_county_by_communities(self):
        """
        Get string from controler and print it
        """
        print(self.controller.control_get_largest_county_by_communities())

    def view_advanced_search(self, string):
        """
        Get string from controler and print it
        """
        results = self.controller.control_advanced_search(string)
        if results[1] == 0:
            print("\nNone results found for '{}' ".format(string))
        else:
            print("\nFound {} results for term '{}'\n\n{}".format(results[1], string,results[0]))

    def show_menu(self):
        """
        Main menu
        """
        while True:
            system("clear")
            print("What would you like to do:\n"
                  "(1) List statistics\n"
                  "(2) Display 3 cities with longest names\n"
                  "(3) Display county's name with the largest number of communities \n"
                  "(4) Display locations, that belong to more than one category\n"
                  "(5) Advanced search\n"
                  "(0) Exit program\n")

            option = input("Option: ")
            if option == "1":
                self.view_statistics()
                self.enter_to_continue()
            elif option == "2":
                self.view_3_cities()
                self.enter_to_continue()
            elif option == "3":
                self.view_control_get_largest_county_by_communities()
                self.enter_to_continue()
            elif option == "4":
                self.view_locations_belongs_to_more_than_one()
                self.enter_to_continue()
            elif option == "5":
                term = input("Searching for: ")
                self.view_advanced_search(term)
                self.enter_to_continue()
            elif option == "0":
                break