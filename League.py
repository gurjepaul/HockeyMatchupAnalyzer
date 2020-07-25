# import Hockey_Team and sportsreference

class League(object):
    __team_names__ = {1: "Anaheim Ducks",
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

    __teams__ = {}

    # Constructor
    def __init__(self):
        self.season = 2020

    # Creates dictionary of Hockey_Team objects
    def create_league(self):
        pass

    # Finds and returns a Hockey_Team object in the teams dictionary
    def retrieve_team(self, selection):
        # Typecasting to an int if selection is a number
        if selection in str(__team_names__.keys()):
            team_selection = int(selection)
            team_selection = __teams__[__team_names__[team_selection].upper()]
        # Checking if they inputted a valid str
        elif type(selection) == str:
            selections = selection.split()
            selection = None
            # Check valid input for each str they input
            for word in selections:
                # Break if we already got a hit
                if valid_selection:
                    break
                # Comparing against each team
                for team in __teams__:
                    # Check if we got a hit
                    if word in team:
                        # Get the team object
                        team_selection = __teams__[team]
                        # Set to true so it break the loop
                        valid_selection = True
                        break
        return None

    # Displays the name of every team in the league alphabetically
    def display_teams(self):
        pass