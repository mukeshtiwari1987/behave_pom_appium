Feature: Login functionality

  Scenario: Try login with valid email and invalid password
    Given I visit url "https://www.pefin.com/login"
    When I enter "junocastiel@gmail.com" in email address form
    And I enter "InvalidPassword" in password form
    And I click Login button
    Then I should see error "The email address or password is incorrect. Please try again."

  Scenario: Try login with invalid email and valid password
    Given I visit url "https://www.pefin.com/login"
    When I enter "invalid@gmail.com" in email address form
    And I enter "Tork123!" in password form
    And I click Login button
    Then I should see error "The email address or password is incorrect. Please try again."

  Scenario: Try login with valid email and blank password
    Given I visit url "https://www.pefin.com/login"
    When I enter "junocastiel@gmail.com" in email address form
    And I click Login button
    Then I should see error "The email and password fields cannot be blank."

  Scenario: Try login with blank email and valid password
    Given I visit url "https://www.pefin.com/login"
    When I enter "Tork123!" in password form
    And I click Login button
    Then I should see error "The email and password fields cannot be blank."