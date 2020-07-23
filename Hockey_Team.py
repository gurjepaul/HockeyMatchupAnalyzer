from sportsreference.nhl.teams import Teams


class Hockey_Team(object):
    # Constructor takes in organization obj from library
    def __init__(self, organization):
        self.organization = organization

    # Returns team name
    def name(self) -> str:
        return self.organization.name

    # Returns average age of players on the roster
    def age(self) -> float:
        return self.organization.average_age

    # Returns teams number of games played
    def games_played(self) -> int:
        return self.organization.games_played

    # Returns teams number of wins
    def wins(self) -> int:
        return self.organization.wins

    # Returns teams number of losses
    def losses(self) -> int:
        return self.organization.losses

    # Returns teams number of overtime losses
    def overtime_losses(self) -> int:
        return self.organization.overtime_losses

    # Returns teams number of points
    def points(self) -> int:
        return 2 * self.wins() + self.overtime_losses()

    # Returns teams points percentage
    def points_percentage(self) -> float:
        return self.points() / (2 * self.games_played())

    # Returns teams league standing
    def league_standing(self) -> int:
        return self.organization.rank

    # Returns teams number of goals scored
    def goals_for(self) -> int:
        return self.organization.goals_for

    # Returns teams number of goals against
    def goals_against(self) -> int:
        return self.organization.goals_against

    # Returns teams goal differential
    def goal_differential(self) -> int:
        return self.organization.goals_for \
               - self.organization.goals_against

    # Returns teams average goals per game
    def goals_per_game(self) -> float:
        return self.goals_for() / self.games_played()

    # Returns teams shooting percentage
    def shooting_percentage(self) -> float:
        return self.organization.shooting_percentage

    # Returns teams save percentage
    def save_percentage(self) -> float:
        return self.organization.save_percentage

    # Returns teams spsv% (pdo) I DONT THINK THIS IS CORRECT
    def pdo(self) -> float:
        return self.organization.shooting_percentage \
               + (100 * self.organization.save_percentage)

    # Returns teams number of powerplay opportunities
    def pp_opportunities(self) -> int:
        return self.organization.power_play_opportunities

    # Returns teams number of powerplay goals for
    def pp_goals_for(self) -> int:
        return self.organization.power_play_goals

    # Returns teams number of powerplay against
    def pp_goals_against(self) -> int:
        return self.organization.power_play_goals_against

    # Returns teams special teams goal differential
    def st_goal_differential(self) -> int:
        return self.organization.power_play_goals \
               - self.organization.power_play_goals_against

    # Returns teams powerplay percentage
    def pp_percentage(self) -> float:
        return self.organization.power_play_percentage

    # Returns teams penalty kill percentage
    def pk_percentage(self) -> float:
        return self.organization.penalty_killing_percentage

    # Outputs the teams current statistics regarding standings
    def team_season_report(self):
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

        key_takeaways = []

        # Checking points percentage
        # Points percentage above 65%
        if self.points_percentage() >= .650:
            key_takeaways\
                .append(" (+) Team has one of the highest point percentages in the league")
        # Points percentage above 57.5%
        elif self.points_percentage() >= .575:
            key_takeaways.append(" (+) Team has a strong points percentage")
        # Points percentage below 45%
        elif self.points_percentage() <= .450:
            key_takeaways\
                .append(" (-) Team has one of the lowest point percentages in the league")
        # Points percentage below 50%
        elif self.points_percentage() <= .500:
            key_takeaways.append(" (-) Team has a weak points percentage")

        # Checking team rank
        # Top 5 team in the league
        if self.league_standing() <= 5:
            key_takeaways.append(" (+) One of the top teams in the league")
        # Top 10 team in the league
        elif self.league_standing() <= 10:
            key_takeaways.append(" (+) Team has a high league standing")
        # bottom 6 team in the league
        elif self.league_standing() >= 25:
            key_takeaways.append(" (-) One of worst teams in the league")
        # Bottom 11 team in the league
        elif self.league_standing() >= 20:
            key_takeaways.append(" (-) Team has a low league standing")

        print("Key Takeaways:")

        # If key_takeaways is empty their stats are average
        if len(key_takeaways) == 0:
            print(" (+/-) Pretty average team all around the board")
        # Output takeaways found earlier
        else:
            # Outputting contents of key_takeaways
            for point in key_takeaways:
                print(point)

        print()

    # Outputs the teams current statistics regarding standings
    def offense_defense_report(self):
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

        key_takeaways = []

        # Checking goals per game
        # One of the top GPG teams
        if self.goals_per_game() >= 3.5:
            key_takeaways\
                .append(" (+) Team has one of the highest goals per game average in the league")
        # Good PPG team
        elif self.goals_per_game() >= 3.2:
            key_takeaways.append(" (+) Team has a strong goals per game average")
        # Bad PPG team
        elif self.goals_per_game() <= 2:
            key_takeaways.append(" (-) Team has a weak goals per game average")
        # One of the bottom PPG teams
        elif self.goals_per_game() <= 2.7:
            key_takeaways\
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
            key_takeaways\
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

        print()

    # Outputs the teams current statistics regarding standings
    def special_teams_report(self):
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

        key_takeaways = []

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

        print()

    # Outputs the teams current statistics regarding standings
    def analyze_matchup(self, opposing_team):
        pass


# unit testing
teams = Teams(2020)

teams_dictionary = {}

for team in teams:
    teams_dictionary[team.name.upper()] = Hockey_Team(team)

nhl_team = teams_dictionary["DETROIT RED WINGS"]

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


