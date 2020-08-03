from sportsreference.nhl.teams import Teams
import GeneralTeamReport
import OffenseDefenseReport
import SpecialTeamsReport


class HockeyTeam(object):
    """ HockeyTeam object that will hold information/generate reports for teams """

    # Constructor takes in organization obj from library
    def __init__(self, team):
        """
        Initializes the organization/team for the class

        :param team: NHL team whom the instance will be about
        """
        self.team = team
        self._general_report = GeneralTeamReport(team)
        self._off_def_report = OffenseDefenseReport(team)
        self._special_report = SpecialTeamsReport(team)

    def name(self) -> str:
        """
        Getter method for team name

        :return: String containing teams name
        """
        return self.team.name

    def age(self) -> float:
        """
        Getter method for teams average age

        :return: Float of the average age of the team
        """
        return self.team.average_age

    def games_played(self) -> int:
        """
        Getter method for teams games played so far in the season

        :return: Int of the number of games played
        """
        return self.team.games_played

    def wins(self) -> int:
        """
        Getter method for teams wins so far in the season

        :return: Int of the number of wins
        """
        return self.team.wins

    def losses(self) -> int:
        """
        Getter method for teams losses so far in the season

        :return: Int of the number of losses
        """
        return self.team.losses

    def overtime_losses(self) -> int:
        """
        Getter method for teams overtime losses so far in the season

        :return: Int of the number of overtime losses
        """
        return self.team.overtime_losses

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
        return self.team.rank

    def goals_for(self) -> int:
        """
        Getter method for teams goals for

        :return: Int of the teams goals for
        """
        return self.team.goals_for

    def goals_against(self) -> int:
        """
        Getter method for teams goals against

        :return: Int of the teams goals against
        """
        return self.team.goals_against

    def goal_differential(self) -> int:
        """
        Getter method for teams goals differential

        :return: Int of the teams goals differential
        """
        return self.team.goals_for - self.team.goals_against

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
        return self.team.shooting_percentage

    def save_percentage(self) -> float:
        """
        Getter method for teams current save percentage

        :return: Float of the current save percentage
        """
        return self.team.save_percentage

    # I DONT THINK THIS IS CORRECT
    def pdo(self) -> float:
        """
        Getter method for teams PDO (advance analytic)

        :return: Float of the teams PDO
        """
        return self.team.shooting_percentage \
               + (100 * self.team.save_percentage)

    def pp_opportunities(self) -> int:
        """
        Getter method for teams power play opportunities

        :return: Int of the teams power play opportunities
        """
        return self.team.power_play_opportunities

    def pp_goals_for(self) -> int:
        """
        Getter method for teams power play goals for

        :return: Int of the power play goals for
        """
        return self.team.power_play_goals

    def pp_goals_against(self) -> int:
        """
        Getter method for teams power play goals against

        :return: Int of the power play goals against
        """
        return self.team.power_play_goals_against

    def st_goal_differential(self) -> int:
        """
        Getter method for teams special teams goal differential

        :return: Int of the special teams goal differential
        """
        return self.team.power_play_goals \
               - self.team.power_play_goals_against

    def pp_percentage(self) -> float:
        """
        Getter method for teams current power play percentage

        :return: Float of the power play percentage
        """
        return self.team.power_play_percentage

    def pk_percentage(self) -> float:
        """
        Getter method for teams current penalty kill percentage

        :return: Float of the penalty kill percentage
        """
        return self.team.penalty_killing_percentage


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
    print(nhl_team.pdo())
    print(nhl_team.shooting_percentage())
    print(nhl_team.save_percentage())

