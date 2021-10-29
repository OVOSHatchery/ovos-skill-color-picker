Feature: Give me 3 colors that work with <color>

  @xfail 
  Scenario Outline: Increase color channel
    Given an english speaking user
     When the user says "give me a 3 color palette that includes <input color>"
     Then the skill makes an API request
     Then the palette is read back to the user
      And the palette is displayed on the screen

    Examples: 3-color palettes
      | input color | 3-color palette list |
      | honey dew | honeydew, something, something |
      | #fa8072 | salmon, something, something |