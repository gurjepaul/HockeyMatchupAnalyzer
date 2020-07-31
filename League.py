from HockeyTeam import HockeyTeam
from sportsreference.nhl.teams import Teams


class League(object):
    """ League class that contains the information of 31 NHL teams """

    # Dictionary that contains team names in an alphabetical order
    _team_names = {1: "Anaheim Ducks",
                   2: "Arizona Coyotes",
                   3: "Boston Bruins",
                   4: "Buffalo Sabres",
                   5: "Calgary Flames",
                   6: "Carolina Hurricanes",
                   7: "Chicago Blackhawks",
                   8: "Colorado Avalanche",
                   9: "Columbus Blue Jackets",
                   10: "Dallas Stars",
                   11: "Detroit Red Wings",
                   12: "Edmonton Oilers",
                   13: "Florida Panthers",
                   14: "Los Angeles Kings",
                   15: "Minnesota Wild",
                   16: "Montreal Canadiens",
                   17: "Nashville Predators",
                   18: "New Jersey Devils",
                   19: "New York Islanders",
                   20: "New York Rangers",
                   21: "Ottawa Senators",
                   22: "Philadelphia Flyers",
                   23: "Pittsburgh Penguins",
                   24: "St. Louis Blues",
                   25: "San Jose Sharks",
                   26: "Tampa Bay Lightning",
                   27: "Toronto Maple Leafs",
                   28: "Vancouver Canucks",
                   29: "Vegas Golden Knights",
                   30: "Washington Capitals",
                   31: "Winnipeg Jets"}

    # Dictionary that will hold Hockey_Team objects for every team in the NHL
    _teams = {}

    def __init__(self, season=2020):
        """
        Calls the create_league function to generate the league
        """
        # Fills our instance variable with teams
        self.create_league(season)

    def create_league(self, year: int):
        """
        Generates NHL teams using web scraper and stores them in a dictionary

        :param year: Year of the season to be analyzed
        """
        # Getting information for each team from sportsreference library
        teams = Teams(year)

        # Putting Hockey_Team objects for each team in our dictionary
        for team in teams:
            self._teams[team.name.upper()] = HockeyTeam(team)

    def retrieve_team(self, user_input: str) -> HockeyTeam:
        """
        Searches through the HockeyTeam dictionary and returns the desired team

        :param user_input: String of user input that corresponds to a team
        :return: HockeyTeam object of the desired team
        """
        # If the selection is in _team_names
        if user_input in str(self._team_names.keys()):
            # returning team in _teams using key from _team_names
            return self._teams[self._team_names[int(user_input)].upper()]

        # Checking if they entered a potential team name in _teams
        else:
            # Splitting their input into keywords
            keywords = user_input.upper().split()

            # Check valid input for each str they input
            for word in keywords:

                # Comparing keywords against each team against each team
                for team in self._teams:

                    # Check if keyword got a hit
                    if word in team:
                        # Returning Hockey_Team object
                        return self._teams[team]

        return None

    def display_teams(self):
        """
        Displays all the teams in the league in alphabetical order
        """
        for team_number in range(1, 32):
            print("{:2}. {}".format(team_number, self._team_names[team_number]))


if __name__ == '__main__':
    covid_league = League()
    covid_league.display_teams()
    selection = covid_league.retrieve_team("Vancity")
    print(selection.name())


