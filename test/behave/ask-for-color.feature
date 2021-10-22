Feature: Get information about a color
 
  Scenario Outline: Ask for specific color by name
    Given an english speaking user
     When the user says "<request a color>"
     Then mycroft reply should contain "<color name> has a hex value of <hex-value>. In RGB this is Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color
      | request a color | color name | hex-value | red-value | green-value | blue-value |
      | show me the color red | red | ff0000 | 255 | 0 | 0 |
      | what does yellow look like | yellow | ffff00 | 255 | 255 | 0 |
      | show me dark salmon | dark salmon | e9967a | 233 | 150 | 122 |
      | what does light goldenrod yellow look like | light goldenrod yellow | fafad2 | 250 | 250 | 210 |

# TODO Remove unused values from example tables

  Scenario Outline: Ask for color by hex value with known name
    Given an english speaking user
     When the user says "<request by hex>"
     Then mycroft reply should contain "That is <color name>. Its RGB values are, Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color by hex
      | request by hex | color name | red-value | green-value | blue-value |
      | what color has a hex code of ff0000 | red | 255 | 0 | 0 |

  @xfail
  Scenario Outline: FAILING - color name reported with no spaces
    Given an english speaking user
     When the user says "<request by hex>"
     Then mycroft reply should contain "That is <color name>. Its RGB values are, Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color by hex
      | request by hex | color name | red-value | green-value | blue-value |
      | what color has a hex code of e9967a | dark salmon | 233 | 150 | 122 |

  Scenario Outline: Ask for color by hex value with unknown name
    Given an english speaking user
     When the user says "<request by hex>"
     Then mycroft reply should contain "The RGB values for this color are, Red <red-value>, Green <green-value>, Blue <blue-value>"

    Examples: requesting a color by hex
      | request by hex | red-value | green-value | blue-value |
      | what color has a hex code of ff0001 | 255 | 0 | 1 |
      | what color has a hex code of fadfad | 250 | 223 | 173 |

  # Scenario Outline: Ask for color by RGB values with known name
  
  # Scenario Outline: Ask for color by RGB values with unknown name

