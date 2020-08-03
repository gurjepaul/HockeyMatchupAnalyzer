from TeamReport import TeamReport
from HockeyTeam import HockeyTeam
from sportsreference.nhl.teams import Teams


class OffenseDefenseReport(TeamReport):
    """  """

    def __init__(self, team: HockeyTeam):
        """
        Constructor that initializes/calls methods to generate the report
        """
        super().__init__(team)

    def generate_rating(self) -> int:
        pass

    def generate_takeaways(self) -> []:
        """
        Outputs key takeaways regarding the teams offensive/defensive statistics
        """
        key_takeaways = []

        # Checking goals per game
        # One of the top GPG teams
        if self.team.goals_per_game() >= 3.5:
            key_takeaways \
                .append(" (+) Team has one of the highest goals per game average in the league")
        # Good PPG team
        elif self.team.goals_per_game() >= 3.2:
            key_takeaways.append(" (+) Team has a strong goals per game average")
        # Bad PPG team
        elif self.team.goals_per_game() <= 2:
            key_takeaways.append(" (-) Team has a weak goals per game average")
        # One of the bottom PPG teams
        elif self.team.goals_per_game() <= 2.7:
            key_takeaways \
                .append(" (-) Team has one of the lowest goals per game average in the league")

        # Checking shooting percentage
        # One of the top SP% teams
        if self.team.shooting_percentage() >= 11:
            key_takeaways \
                .append(" (+) Team has one of the highest shooting percentages in the league")
        # Good SP% teams
        elif self.team.shooting_percentage() >= 9.5:
            key_takeaways.append(" (+) Team capitalizes on their shots")
        # Bad SP% teams
        elif self.team.shooting_percentage() <= 8.3:
            key_takeaways.append(" (-) Team doesn't capitalizes on their shots")
        # One of the bottom SP% teams
        elif self.team.shooting_percentage() <= 8.8:
            key_takeaways \
                .append(" (-) Team has one of the lowest shooting percentages in the league")

        # Checking save percentage
        # One of the top SV% teams
        if self.team.save_percentage() >= 0.92:
            key_takeaways \
                .append(" (+) Team has one of the highest save percentages in the league")
        # Good SV% teams
        elif self.team.save_percentage() >= 0.91:
            key_takeaways.append(" (+) Teams saves a good save percentage")
        # Bad SV% teams
        elif self.team.save_percentage() <= 0.895:
            key_takeaways.append(" (-) Team has a weak save percentage")
        # One of the bottom SV% teams
        elif self.team.save_percentage() <= 0.9:
            key_takeaways \
                .append(" (-) Team has one of the lowest save percentages in the league")

        # Checking pdo (how lucky a team is)
        # Lucky team
        if self.team.pdo() >= 102:
            key_takeaways.append(" (+/-) Lucky team. Stats may be inflated")
        # Unlucky team
        elif self.team.pdo() <= 98:
            key_takeaways \
                .append(" (+/-) Unlucky team. Team may be better than they appear")

        return key_takeaways

    def display_report(self):
        """
        Outputs the teams current offensive/defensive statistics in the form of
        a report
        """
        print("{} Offense/Defense Report:".format(self.team.name()))
        print("=" * 43)

        # Goals for
        print(" Goals for: {}".format(self.team.goals_for()))

        if self.team.goals_against() is not None:
            # Goals against
            print(" Goals against: {}".format(self.team.goals_against()))
            # Goal differential
            print(" Goal Differential: {}"
                  .format(self.team.goal_differential()))
        # Goals per game
        print(" Goals per Game: {:.3}".format(self.team.goals_per_game()))
        # Shooting percentage
        print(" Shooting percentage (SP%): {}%"
              .format(self.team.shooting_percentage()))
        # Save percentage
        print(" Save percentage (SV%): {:.1%}"
              .format(self.team.save_percentage()))
        # PDO
        print(" PDO (SPSV%): {}\n".format(self.team.pdo()))

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

    report = OffenseDefenseReport(nhl_team)

    report.display_report()