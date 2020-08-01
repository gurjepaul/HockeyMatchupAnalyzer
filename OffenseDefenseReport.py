from TeamReport import TeamReport
from HockeyTeam import HockeyTeam
from sportsreference.nhl.teams import Teams


class OffenseDefenseReport(TeamReport):
    """"  """

    def __init__(self, team: HockeyTeam):
        """
        Constructor that initializes/calls methods to generate the report
        """
        super().__init__(team)

    def generate_rating(self) -> int:
        pass

    def generate_takeaways(self) -> []:
        pass

    def display_report(self):
        pass
