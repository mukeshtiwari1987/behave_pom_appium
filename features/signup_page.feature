Feature: Sign Up page should have login & sign up component and should not accept invalid email

  Scenario: User should be unable to create an account with an already registered email id
      Given I visit url "https://www.pefin.com/signup"
      When I enter "junocastiel@gmail.com" in email address form
      And I enter "Tork123!" in password form
      And I click Terms of Use
      And I click Submit button
      Then I should see "A user with this email address has already been created. Please login from the home page using your email and password." error


  Scenario: User can see the Login and Sign Up button on sign up page
      Given I visit url "https://www.pefin.com/plan/home"
      Then title should be "Pefin - World's first AI financial advisor."
      When I click Hamburger Icon
      Then "Log In" button exists
      Then "SIGN UP FOR FREE" button should exists
      When I click on X icon
      Then "Continue With Email" button should also exists


  Scenario Outline: User should see message 'Please enter a valid email' on entering invalid email
      Given I visit url "https://www.pefin.com/plan/home"
      When I click Continue With Email button
      When I enter "<invalidEmail>" in email placeholder
      Examples:
            | invalidEmail            |
            | onlyUsername            |
            | onlyDomain.com          |
            | @onlyDomain.com         |
      When I click on Continue button
      Then I should see "Please enter a valid email" message
