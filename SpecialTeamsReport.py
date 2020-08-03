from TeamReport import TeamReport
from HockeyTeam import HockeyTeam
from sportsreference.nhl.teams import Teams


class SpecialTeamsReport(TeamReport):
    """"  """

    def __init__(self, organization: HockeyTeam):
        """
        Constructor that initializes/calls methods to generate the report
        """
        super().__init__(organization)

    def generate_rating(self) -> int:
        pass

    def generate_takeaways(self) -> []:
        """
        Outputs key takeaways regarding the teams special teams statistics
        """
        key_takeaways = []

        # Checking power play percentage
        # One of the top PP% teams
        if self.team.pp_percentage() >= 25:
            key_takeaways.append(" (+) Team is deadly on the power play")
        # Good PP% teams
        elif self.team.pp_percentage() >= 21:
            key_takeaways.append(" (+) Team has a strong power play unit")
        # One of the bottom PP% teams
        elif self.team.pp_percentage() <= 15:
            key_takeaways.append(" (-) Team is not a threat on the power play")
        # Bad PP% teams
        elif self.team.pp_percentage() <= 18:
            key_takeaways.append(" (-) Team has a weak power play unit")
        # If none of the above, stat is average for this category
        else:
            key_takeaways.append(" (+/-) Team has an average power play unit")

        # Checking penalty kill percentage
        # One of the top PK% teams
        if self.team.pk_percentage() >= 84:
            key_takeaways \
                .append(" (+) Team is highly efficient at killing penalties")
        # Good PK% teams
        elif self.team.pk_percentage() >= 82:
            key_takeaways.append(" (+) Team has a strong penalty killing unit")
        # One of the bottom PK% teams
        elif self.team.pk_percentage() <= 78:
            key_takeaways.append(" (-) Team cannot kill penalties")
        # Bad PK% teams
        elif self.team.pk_percentage() <= 75:
            key_takeaways.append(" (-) Team has a weak penalty killing unit")
        # If none of the above, stat is average for this category
        else:
            key_takeaways \
                .append(" (+/-) Team has an average penalty killing unit")

        return key_takeaways

    def display_report(self):
        """
        Outputs the teams current special teams statistics in the form of a report
        """
        print("{} Special Teams Report:".format(self.team.name()))
        print("=" * 41)

        # Games played
        print(" Power Play Opportunities: {}"
              .format(self.team.pp_opportunities()))
        # Wins
        print(" Power Play Goals For: {}".format(self.team.pp_goals_for()))
        # Losses
        print(" Power Play Goals Against: {}"
              .format(self.team.pp_goals_against()))
        # OT Losses
        print(" Special Teams Goal Differential: {}"
              .format(self.team.pp_goals_for() - self.team.pp_goals_against()))
        # Points
        print(" Power Play Percentage: {}%"
              .format(self.team.pp_percentage()))
        # points percentage
        print(" Penalty Kill Percentage: {}%\n"
              .format(self.team.pk_percentage()))

        print("Key Takeaways:")

        # If key_takeaways is empty their stats are average
        if len(self.takeaways) == 0:
            print(" (+/-) Average offense")
            print(" (+/-) Average defense")
        # Output takeaways found earlier
        else:
            # Outputting contents of key_takeaways
            for point in self.takeaways:
                print(point)


if __name__ == '__main__':
    teams = Teams(2020)

    teams_dictionary = {}

    for team in teams:
        teams_dictionary[team.name.upper()] = HockeyTeam(team)

    nhl_team = teams_dictionary["PITTSBURGH PENGUINS"]

    report = SpecialTeamsReport(nhl_team)

    report.display_report()
