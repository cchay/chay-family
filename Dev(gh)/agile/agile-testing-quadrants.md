# 4 Agile Testing Quadrants
|                     |  Business Facing  |  Business Facing  |                  |
| Supporting the Team |         Q2        |       Q3          | Critique Product |
| Supporting the Team |         Q1        |       Q4          | Critique Product |
|                     | Technology Facing | Technology Facing |                  |

# Q1 
  1. Unit Test
    * xUnit test framework
      * TestBox for ColdFusion
      * dbUnit for database (need to investigate)
    * Required at every level of application
    * Test atomic & isolated code w/o interaction with other layers or units
    * Other layers/units are mocked (see below)
  2. Mocking Framework
    * Eliminate dependency on other layers/units (db, 3rd system ...)
  3. Integration Test
    * Multiple layers

## Unit Test Levels
  * Adv: 
  * Int: 
  * Basic: 
  * Foundation: 
 
# Q2
  1. User story tests
    * Given/When/Then format should be used for user story
  2. Examples
    * Start with "Happy Path", then permutations, then edge cases
    * Visual example
  3. Simulations
    * Wizard of Oz Testing w/ visual layout of interface (mockup)
    * Lead plays the part of the wizard (the system)
      * Resolves and interactions
    * Users talk through interactions and their expections
    * Developers observe and learn (do not speak)

## Questions
  1. Permutations of given/when:
    * Science/Art
    * Consider breaking into multiple US the further it deviates from the happy path 

# Q3: 
  * Exploratory Testing
    * Write exploratory testing charters
    * Go off the beaten path (do the unexpected/break the system)
  * End User Testing = UAT validation
  * Alpha/Beta Testing
    * Done in PROD in small scale

## Questions
  1. PCF/OpenShift: How does a/b testing work in a containerized environment where the same image is deployed?
    * Send Shawn an email for introduction to Arsoni Jerkins for dockers/a/b/blue/green deployment/env/setup.

# Q4: 
  * Performance Testing
    * QUPER
  * Security Testing
    * Sonar Cube (+Fortify)
  * *ility Testing

## Questions
  1. Is security requirement (cannot go forward unless it passes)
  2. "Negative testing" is something that shouldn't happen (null, does/can't exist)... 
  3. We juse JMeter, which is great for front end; can it be use for backend?  Or any open source tool for stress testing backend (db ...)?

