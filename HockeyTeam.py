from sportsreference.nhl.teams import Teams


class HockeyTeam(object):
    """ HockeyTeam object that will hold information/generate reports for teams """

    # Constructor takes in organization obj from library
    def __init__(self, organization):
        """
        Initializes the organization/team for the class

        :param organization: NHL team whom the instance will be about
        """
        self.organization = organization

    def name(self) -> str:
        """
        Getter method for team name

        :return: String containing teams name
        """
        return self.organization.name

    def age(self) -> float:
        """
        Getter method for teams average age

        :return: Float of the average age of the team
        """
        return self.organization.average_age

    def games_played(self) -> int:
        """
        Getter method for teams games played so far in the season

        :return: Int of the number of games played
        """
        return self.organization.games_played

    def wins(self) -> int:
        """
        Getter method for teams wins so far in the season

        :return: Int of the number of wins
        """
        return self.organization.wins

    def losses(self) -> int:
        """
        Getter method for teams losses so far in the season

        :return: Int of the number of losses
        """
        return self.organization.losses

    def overtime_losses(self) -> int:
        """
        Getter method for teams overtime losses so far in the season

        :return: Int of the number of overtime losses
        """
        return self.organization.overtime_losses

    def points(self) -> int:
        """
        Getter method for teams number of points so far in the season

        :return: Int of the number of points
        """
        return 2 * self.wins() + self.overtime_losses()

    def points_percentage(self) -> float:
        """
        Getter method for teams current points percentage

        :return: Float of the teams current points percentage
        """
        return self.points() / (2 * self.games_played())

    def league_standing(self) -> int:
        """
        Getter method for teams current league standing

        :return: Int of the teams current rank
        """
        return self.organization.rank

    def goals_for(self) -> int:
        """
        Getter method for teams goals for

        :return: Int of the teams goals for
        """
        return self.organization.goals_for

    def goals_against(self) -> int:
        """
        Getter method for teams goals against

        :return: Int of the teams goals against
        """
        return self.organization.goals_against

    def goal_differential(self) -> int:
        """
        Getter method for teams goals differential

        :return: Int of the teams goals differential
        """
        return self.organization.goals_for - self.organization.goals_against

    def goals_per_game(self) -> float:
        """
        Getter method for teams average goals per game

        :return: Float of the average goals per game
        """
        return self.goals_for() / self.games_played()

    def shooting_percentage(self) -> float:
        """
        Getter method for teams current shooting percentage

        :return: Float of the current shooting percentage
        """
        return self.organization.shooting_percentage

    def save_percentage(self) -> float:
        """
        Getter method for teams current save percentage

        :return: Float of the current save percentage
        """
        return self.organization.save_percentage

    # I DONT THINK THIS IS CORRECT
    def pdo(self) -> float:
        """
        Getter method for teams PDO (advance analytic)

        :return: Float of the teams PDO
        """
        return self.organization.shooting_percentage \
               + (100 * self.organization.save_percentage)

    def pp_opportunities(self) -> int:
        """
        Getter method for teams power play opportunities

        :return: Int of the teams power play opportunities
        """
        return self.organization.power_play_opportunities

    def pp_goals_for(self) -> int:
        """
        Getter method for teams power play goals for

        :return: Int of the power play goals for
        """
        return self.organization.power_play_goals

    def pp_goals_against(self) -> int:
        """
        Getter method for teams power play goals against

        :return: Int of the power play goals against
        """
        return self.organization.power_play_goals_against

    def st_goal_differential(self) -> int:
        """
        Getter method for teams special teams goal differential

        :return: Int of the special teams goal differential
        """
        return self.organization.power_play_goals \
               - self.organization.power_play_goals_against

    def pp_percentage(self) -> float:
        """
        Getter method for teams current power play percentage

        :return: Float of the power play percentage
        """
        return self.organization.power_play_percentage

    def pk_percentage(self) -> float:
        """
        Getter method for teams current penalty kill percentage

        :return: Float of the penalty kill percentage
        """
        return self.organization.penalty_killing_percentage

    def team_season_report(self):
        """
        Outputs the teams current general statistics in the form of a report
        """
        print("{} Team Record Report:".format(self.name()))
        print("=" * 39)

        # Games played
        print(" Games played: {}".format(self.games_played()))
        # Wins
        print(" Wins: {}".format(self.wins()))
        # Losses
        print(" Losses: {}".format(self.losses()))
        # OT Losses
        print(" OT Losses: {}".format(self.overtime_losses()))
        # Points
        print(" Points: {}".format(self.points()))
        # Points percentage
        print(" Points Percentage: {:.1%}"
              .format(self.points_percentage()))
        # League standing
        print(" League Standing: {}/31\n"
              .format(self.league_standing()))

        self._team_takeaways()
        print()

    def offense_defense_report(self):
        """
        Outputs the teams current offensive/defensive statistics in the form of
        a report
        """
        print("{} Offense/Defense Report:".format(self.name()))
        print("=" * 43)

        # Goals for
        print(" Goals for: {}".format(self.goals_for()))

        if self.goals_against() is not None:
            # Goals against
            print(" Goals against: {}".format(self.goals_against()))
            # Goal differential
            print(" Goal Differential: {}"
                  .format(self.goal_differential()))
        # Goals per game
        print(" Goals per Game: {:.3}".format(self.goals_per_game()))
        # Shooting percentage
        print(" Shooting percentage (SP%): {}%"
              .format(self.shooting_percentage()))
        # Save percentage
        print(" Save percentage (SV%): {:.1%}"
              .format(self.save_percentage()))
        # PDO
        print(" PDO (SPSV%): {}\n".format(self.pdo()))

        self._offense_defense_takeaways()
        print()

    def special_teams_report(self):
        """
        Outputs the teams current special teams statistics in the form of a report
        """
        print("{} Special Teams Report:".format(self.name()))
        print("=" * 41)

        # Games played
        print(" Power Play Opportunities: {}"
              .format(self.pp_opportunities()))
        # Wins
        print(" Power Play Goals For: {}".format(self.pp_goals_for()))
        # Losses
        print(" Power Play Goals Against: {}"
              .format(self.pp_goals_against()))
        # OT Losses
        print(" Special Teams Goal Differential: {}"
              .format(self.pp_goals_for() - self.pp_goals_against()))
        # Points
        print(" Power Play Percentage: {}%"
              .format(self.pp_percentage()))
        # points percentage
        print(" Penalty Kill Percentage: {}%\n"
              .format(self.pk_percentage()))

        self._special_teams_takeaways()
        print()

    def analyze_matchup(self, opposing_team):
        pass

    # def _team_takeaways(self):
    #     """
    #     Outputs key takeaways regarding the teams general statistics
    #     """
    #     key_takeaways = []
    #
    #     # Checking points percentage
    #     # Points percentage above 65%
    #     if self.points_percentage() >= .650:
    #         key_takeaways \
    #             .append(" (+) Team has one of the highest point percentages in the league")
    #     # Points percentage above 57.5%
    #     elif self.points_percentage() >= .575:
    #         key_takeaways.append(" (+) Team has a strong points percentage")
    #     # Points percentage below 45%
    #     elif self.points_percentage() <= .450:
    #         key_takeaways \
    #             .append(" (-) Team has one of the lowest point percentages in the league")
    #     # Points percentage below 50%
    #     elif self.points_percentage() <= .500:
    #         key_takeaways.append(" (-) Team has a weak points percentage")
    #
    #     # Checking team rank
    #     # Top 5 team in the league
    #     if self.league_standing() <= 5:
    #         key_takeaways.append(" (+) One of the top teams in the league")
    #     # Top 10 team in the league
    #     elif self.league_standing() <= 10:
    #         key_takeaways.append(" (+) Team has a high league standing")
    #     # bottom 6 team in the league
    #     elif self.league_standing() >= 25:
    #         key_takeaways.append(" (-) One of worst teams in the league")
    #     # Bottom 11 team in the league
    #     elif self.league_standing() >= 20:
    #         key_takeaways.append(" (-) Team has a low league standing")
    #
    #     print("Key Takeaways:")
    #
    #     # If key_takeaways is empty their stats are average
    #     if len(key_takeaways) == 0:
    #         print(" (+/-) Pretty average team all around the board")
    #     # Output takeaways found earlier
    #     else:
    #         # Outputting contents of key_takeaways
    #         for point in key_takeaways:
    #             print(point)

    def _offense_defense_takeaways(self):
        """
        Outputs key takeaways regarding the teams offensive/defensive statistics
        """

        key_takeaways = []

        # Checking goals per game
        # One of the top GPG teams
        if self.goals_per_game() >= 3.5:
            key_takeaways \
                .append(" (+) Team has one of the highest goals per game average in the league")
        # Good PPG team
        elif self.goals_per_game() >= 3.2:
            key_takeaways.append(" (+) Team has a strong goals per game average")
        # Bad PPG team
        elif self.goals_per_game() <= 2:
            key_takeaways.append(" (-) Team has a weak goals per game average")
        # One of the bottom PPG teams
        elif self.goals_per_game() <= 2.7:
            key_takeaways \
                .append(" (-) Team has one of the lowest goals per game average in the league")

        # Checking shooting percentage
        # One of the top SP% teams
        if self.shooting_percentage() >= 11:
            key_takeaways \
                .append(" (+) Team has one of the highest shooting percentages in the league")
        # Good SP% teams
        elif self.shooting_percentage() >= 9.5:
            key_takeaways.append(" (+) Team capitalizes on their shots")
        # Bad SP% teams
        elif self.shooting_percentage() <= 8.3:
            key_takeaways.append(" (-) Team doesn't capitalizes on their shots")
        # One of the bottom SP% teams
        elif self.shooting_percentage() <= 8.8:
            key_takeaways \
                .append(" (-) Team has one of the lowest shooting percentages in the league")

        # Checking save percentage
        # One of the top SV% teams
        if self.save_percentage() >= 0.92:
            key_takeaways \
                .append(" (+) Team has one of the highest save percentages in the league")
        # Good SV% teams
        elif self.save_percentage() >= 0.91:
            key_takeaways.append(" (+) Teams saves a good save percentage")
        # Bad SV% teams
        elif self.save_percentage() <= 0.895:
            key_takeaways.append(" (-) Team has a weak save percentage")
        # One of the bottom SV% teams
        elif self.save_percentage() <= 0.9:
            key_takeaways \
                .append(" (-) Team has one of the lowest save percentages in the league")

        # Checking pdo (how lucky a team is)
        # Lucky team
        if self.pdo() >= 102:
            key_takeaways.append(" (+/-) Lucky team. Stats may be inflated")
        # Unlucky team
        elif self.pdo() <= 98:
            key_takeaways \
                .append(" (+/-) Unlucky team. Team may be better than they appear")

        print("Key Takeaways:")

        # If key_takeaways is empty their stats are average
        if len(key_takeaways) == 0:
            print(" (+/-) Average offense")
            print(" (+/-) Average defense")
        # Output takeaways found earlier
        else:
            # Outputting contents of key_takeaways
            for point in key_takeaways:
                print(point)

    def _special_teams_takeaways(self):
        """
        Outputs key takeaways regarding the teams special teams statistics
        """

        key_takeaways = []

        # Checking power play percentage
        # One of the top PP% teams
        if self.pp_percentage() >= 25:
            key_takeaways.append(" (+) Team is deadly on the power play")
        # Good PP% teams
        elif self.pp_percentage() >= 21:
            key_takeaways.append(" (+) Team has a strong power play unit")
        # One of the bottom PP% teams
        elif self.pp_percentage() <= 15:
            key_takeaways.append(" (-) Team is not a threat on the power play")
        # Bad PP% teams
        elif self.pp_percentage() <= 18:
            key_takeaways.append(" (-) Team has a weak power play unit")
        # If none of the above, stat is average for this category
        else:
            key_takeaways.append(" (+/-) Team has an average power play unit")

        # Checking penalty kill percentage
        # One of the top PK% teams
        if self.pk_percentage() >= 84:
            key_takeaways \
                .append(" (+) Team is highly efficient at killing penalties")
        # Good PK% teams
        elif self.pk_percentage() >= 82:
            key_takeaways.append(" (+) Team has a strong penalty killing unit")
        # One of the bottom PK% teams
        elif self.pk_percentage() <= 78:
            key_takeaways.append(" (-) Team cannot kill penalties")
        # Bad PK% teams
        elif self.pk_percentage() <= 75:
            key_takeaways.append(" (-) Team has a weak penalty killing unit")
        # If none of the above, stat is average for this category
        else:
            key_takeaways \
                .append(" (+/-) Team has an average penalty killing unit")

        print("Key Takeaways:")

        # If key_takeaways is empty their stats are average
        if len(key_takeaways) == 0:
            print(" (+/-) Average offense")
            print(" (+/-) Average defense")
        # Output takeaways found earlier
        else:
            # Outputting contents of key_takeaways
            for point in key_takeaways:
                print(point)


if __name__ == '__main__':
    teams = Teams(2020)

    teams_dictionary = {}

    for team in teams:
        teams_dictionary[team.name.upper()] = HockeyTeam(team)

    nhl_team = teams_dictionary["PITTSBURGH PENGUINS"]

    print(type(nhl_team))

    # testing all the class getter methods
    print(nhl_team.name())
    print(nhl_team.age())
    print(nhl_team.games_played())
    print(nhl_team.wins())
    print(nhl_team.losses())
    print(nhl_team.overtime_losses())
    print(nhl_team.points())
    print(nhl_team.points_percentage())
    print(nhl_team.league_standing())
    print(nhl_team.goals_for())
    print(nhl_team.goals_against())
    print(nhl_team.pdo())
    print(nhl_team.pp_opportunities())
    print(nhl_team.pp_goals_for())
    print(nhl_team.pp_goals_against())
    print(nhl_team.st_goal_differential())
    print(nhl_team.pp_percentage())
    print(nhl_team.pk_percentage())

    nhl_team.team_season_report()
    nhl_team.offense_defense_report()
    nhl_team.special_teams_report()

    print(nhl_team.pdo())
    print(nhl_team.shooting_percentage())
    print(nhl_team.save_percentage())
