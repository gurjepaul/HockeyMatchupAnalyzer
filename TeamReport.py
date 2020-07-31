from abc import abstractmethod
from HockeyTeam import HockeyTeam


class TeamReport(object):
    """ Abstract superclass for report objects """

    def __init__(self, team):
        """
        Constructor that initializes/calls methods to generate the report
        """
        self.team = team
        self.rating = self.generate_rating()
        self.takeaways = self.generate_takeaways()

    @abstractmethod
    def generate_rating(self) -> int:
        """
        Abstract method that will generate the team rating for the current report

        :return: Int of the teams rating
        """
        pass

    @abstractmethod
    def generate_takeaways(self) -> []:
        """
        Abstract method that will generate the takeaways for the current report

        :return: List containing the takeaways
        """
        pass

    @abstractmethod
    def display_report(self):
        """
        Abstract method that will output the contents of the report
        """
        pass
