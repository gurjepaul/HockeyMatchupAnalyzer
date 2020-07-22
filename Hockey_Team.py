from sportsreference.nhl.teams import Teams


class Hockey_Team(object):

    # Constructor takes in organization obj from library
    def __init__(self, organization):
        self.organization = organization

    # returns team name
    def name(self) -> str:
        return self.organization.name

    # returns average age of players on the roster
    def age(self) -> float:
        return self.organization.average_age

    # returns teams number of games played
    def games_played(self) -> int:
        return self.organization.games_played

    # returns teams number of wins
    def wins(self) -> int:
        return self.organization.wins

    # returns teams number of losses
    def losses(self) -> int:
        return self.organization.losses

    # returns teams number of overtime losses
    def overtime_losses(self) -> int:
        return self.organization.overtime_losses

    # returns teams number of points
    def points(self) -> int:
        return self.organization.points

    # returns teams points percentage
    def points_percentage(self) -> float:
        return self.organization.points_percentage

    # returns teams league standing
    def league_standing(self) -> int:
        return self.organization.rank

    # returns teams number of goals scored
    def goals_for(self) -> int:
        return self.organization.goals_for

    # returns teams number of goals against
    def goals_against(self) -> int:
        return self.organization.goals_against

    # returns teams goal differential
    def goal_differential(self) -> int:
        return self.organization.goals_for \
               - self.organization.goals_against

    # returns teams average goals per game
    def goals_per_game(self) -> float:
        return self.organization.total_goals_per_game

    # returns teams shooting percentage
    def shooting_percentage(self) -> float:
        return self.organization.shooting_percentage

    # returns teams save percentage
    def save_percentage(self) -> float:
        return self.organization.save_percentage

    # returns teams spsv% (pdo)
    def pdo(self) -> float:
        return self.organization.shooting_percentage \
               + (100 * self.organization.save_percentage) * 10

    # returns teams number of powerplay opportunities
    def pp_opportunities(self) -> int:
        return self.organization.power_play_opportunities

    # returns teams number of powerplay goals for
    def pp_goals_for(self) -> int:
        return self.organization.power_play_goals

    # returns teams number of powerplay against
    def pp_goals_against(self) -> int:
        return self.organization.power_play_goals_against

    # returns teams special teams goal differential
    def st_goal_differential(self) -> int:
        return self.organization.power_play_goals \
               - self.organization.power_play_goals_against

    # returns teams powerplay percentage
    def pp_percentage(self) -> float:
        return self.organization.power_play_percentage

    # returns teams penalty kill percentage
    def pk_percentage(self) -> float:
        return self.organization.penalty_killing_percentage

    # outputs the teams current statistics regarding standings
    def team_season_report(self):
        pass

    # outputs the teams current statistics regarding standings
    def offense_defense_report(self):
        pass

    # outputs the teams current statistics regarding standings
    def special_teams_report(self):
        pass

    # outputs the teams current statistics regarding standings
    def analyze_matchup(self, opposing_team):
        pass


# unit testing
teams = Teams(2020)

teams_dictionary = {}

for team in teams:
    teams_dictionary[team.name.upper()] = Hockey_Team(team)

penguins = teams_dictionary["PITTSBURGH PENGUINS"]

print(type(penguins))

# testing all the class getter methods
print(penguins.name())
print(penguins.age())
print(penguins.games_played())
print(penguins.wins())
print(penguins.losses())
print(penguins.overtime_losses())
print(penguins.points())
print(penguins.points_percentage())
print(penguins.league_standing())
print(penguins.goals_for())
print(penguins.goals_against())
print(penguins.pdo())
print(penguins.pp_opportunities())
print(penguins.pp_goals_for())
print(penguins.pp_goals_against())
print(penguins.st_goal_differential())
print(penguins.pp_percentage())
print(penguins.pk_percentage())

