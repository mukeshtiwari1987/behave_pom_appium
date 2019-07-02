Feature: Testing functionality of Let's plan for your new home page

    Scenario: User is entering valid information
      Given I visit url "https://www.pefin.com/plan/home"
      When I click Continue With Email button
      When I enter "junocastiel@gmail.com" in email placeholder
      When I click on Continue button
      Then I should see "Let’s plan for your new home"
      When I click Select "New York" state
      And  I type "NEW YORK" in city
      And  I type "10001" in Zip code
      And  I type "062020" in future date
      And  I click "Excellent: 750+"
      And  I click in Upfront Amount
      And  I type "100000"
      And  I click in Monthly spending
      And  I type in "5000"
      And  I click Get My Plan
      Then I should see "Your new home plan" page

    Scenario: User is entering invalid information
      Given I visit url "https://www.pefin.com/plan/home"
      When I click Continue With Email button
      When I enter "junocastiel@gmail.com" in email placeholder
      When I click on Continue button
      Then I should see "Let’s plan for your new home"
      When I click Select "New York" state
      And  I type "NEW YORK" in city
      And  I type "ABCDE" in Zip code
      And  I type "062018" in future date
      And  I click "Excellent: 750+"
      And  I click in Upfront Amount
      And  I type "-1"
      And  I click in Monthly spending
      And  I type in "-1"
      And  I click Get My Plan
      Then I should see "Please enter a valid zipcode" in zipcode
      Then I should see "Please enter a future date" in date
      Then I should see "Please enter your expected down payment" in upfront amount
      Then I should see "Please enter your expected monthly payment" in monthly spending
