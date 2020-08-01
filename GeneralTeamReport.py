from TeamReport import TeamReport
from HockeyTeam import HockeyTeam
from sportsreference.nhl.teams import Teams


class GeneralTeamReport(TeamReport):
    """"  """

    def __init__(self, organization: HockeyTeam):
        """
        Constructor that initializes/calls methods to generate the report
        """
        super().__init__(organization)

    def generate_rating(self) -> int:
        pass

    def generate_takeaways(self) -> []:
        key_takeaways = []

        # Checking points percentage
        # Points percentage above 65%
        if self.team.points_percentage() >= .650:
            key_takeaways \
                .append(" (+) Team has one of the highest point percentages in the league")
        # Points percentage above 57.5%
        elif self.team.points_percentage() >= .575:
            key_takeaways.append(" (+) Team has a strong points percentage")
        # Points percentage below 45%
        elif self.team.points_percentage() <= .450:
            key_takeaways \
                .append(" (-) Team has one of the lowest point percentages in the league")
        # Points percentage below 50%
        elif self.team.points_percentage() <= .500:
            key_takeaways.append(" (-) Team has a weak points percentage")

        # Checking team rank
        # Top 5 team in the league
        if self.team.league_standing() <= 5:
            key_takeaways.append(" (+) One of the top teams in the league")
        # Top 10 team in the league
        elif self.team.league_standing() <= 10:
            key_takeaways.append(" (+) Team has a high league standing")
        # bottom 6 team in the league
        elif self.team.league_standing() >= 25:
            key_takeaways.append(" (-) One of worst teams in the league")
        # Bottom 11 team in the league
        elif self.team.league_standing() >= 20:
            key_takeaways.append(" (-) Team has a low league standing")

        return key_takeaways

    def display_report(self):
        """
        Outputs the teams current general statistics in the form of a report
        """
        print("{} Team Record Report:".format(self.team.name()))
        print("=" * 39)

        # Games played
        print(" Games played: {}".format(self.team.games_played()))
        # Wins
        print(" Wins: {}".format(self.team.wins()))
        # Losses
        print(" Losses: {}".format(self.team.losses()))
        # OT Losses
        print(" OT Losses: {}".format(self.team.overtime_losses()))
        # Points
        print(" Points: {}".format(self.team.points()))
        # Points percentage
        print(" Points Percentage: {:.1%}"
              .format(self.team.points_percentage()))
        # League standing
        print(" League Standing: {}/31\n"
              .format(self.team.league_standing()))

        print("Key Takeaways:")

        # If key_takeaways is empty their stats are average
        if len(self.takeaways) == 0:
            print(" (+/-) Pretty average team all around the board")
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

    report = GeneralTeamReport(nhl_team)

    report.display_report()
