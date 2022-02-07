Feature:Amazon

@all @smoke
Scenario: Verify login functionality
      Given Launch the App
      When Verify page title
      And close the browser

      @all @sanity
      Scenario: Verify login
      Given Launch the App
      When Enter login
      And close the browser

@all @abcd
Scenario: Verify search
      Given Launch the App
      When Search product
      And close the browser
