# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.contract_management -t test_contract.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.contract_management.testing.COLLECTIVE_CONTRACT_MANAGEMENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/contract_management/tests/robot/test_contract.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Contract
  Given a logged-in site administrator
    and an add Contracts form
   When I type 'My Contract' into the title field
    and I submit the form
   Then a Contract with the title 'My Contract' has been created

Scenario: As a site administrator I can view a Contract
  Given a logged-in site administrator
    and a Contract 'My Contract'
   When I go to the Contract view
   Then I can see the Contract title 'My Contract'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Contracts form
  Go To  ${PLONE_URL}/++add++Contracts

a Contract 'My Contract'
  Create content  type=Contracts  id=my-contract  title=My Contract

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Contract view
  Go To  ${PLONE_URL}/my-contract
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Contract with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Contract title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
