Feature: color detection via the camera
 
  @xfail
  Scenario: Ask for color of a physical object
    Given an english speaking user
     When the user says "what is the color code of this thing"
     Then the camera should activate
      And a dominant color should be selected
      And mycroft should reply with dialog from "report-color.dialog"
