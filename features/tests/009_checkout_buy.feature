# Created by rapid at 2/2/2021
Feature: # Verify Contact=email text is here and Ship to=address text is here

  Scenario: # Verify Contact=email text is here and Ship to=address text is here
    Given Loginpage
    Then Verify Contact=email(randomized) and Ship to=address '2124 NE 182nd St North Miami Beach, Fl 33162' are here