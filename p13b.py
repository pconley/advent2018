
rows = [ # first example
    "/->-\\        ",
    "|   |  /----\\",
    "| /-+--+-\\  |",
    "| | |  | v  |",
    "\\-+-/  \\-+--/",
    "  \\------/   ",
]

rows = [ # real problem
    "                                     /---------------------------------------------------------------------------------------------------\\            ",
    "                             /-------+---------------------\\                                                                             |            ",
    "   /--------------------\\ /--+-------+---------------------+----------------------------------------------\\                              |            ",
    "/--+--------------\\     | |  |       |    /----------------+-\\              /---------------------\\  /----+---------\\                    |            ",
    "|  |              |     | |  |       |    |  /-------------+-+------\\       |     /---------------+--+----+---------+--------------------+--------\\   ",
    "|  |              |     | |  |       |    |  |          /--+-+------+-------+-----+---------------+--+----+---\\     |                    |        |   ",
    "|  |              |     | |  |      /+----+--+----------+--+-+------+-------+-----+---------------+--+----+---+-----+---------------\\    |        |   ",
    "|  |              |     | |  |      ||    |  |          |  | |/-----+-------+-----+---------------+--+----+---+-----+---------------+----+--------+-\\ ",
    "|  |              | /---+-+--+------++----+\\ |          |  | ||     |       | /---+----------\\    |  |    |   |     |               |    |        | | ",
    "|  |              | |   | |  |      ||    || |     /----+--+-++---->+-------+-+---+----------+----+--+----+---+----\\|/--------------+----+-------\\| | ",
    "|  |              | | /-+-+--+------++----++-+-----+----+--+-++-----+-------+-+---+----------+----+--+----+---+----+++---------\\    |  /-+------\\|| | ",
    "|  |              | | | | |  v      ||    || |     |    |  | ||     |       | |   |  /-------+----+-\\|    |   |    |||         |    |  | |      ||| | ",
    "|  |   /----------+-+-+-+-+--+------++----++-+-----+----+--+-++-----+-------+-+---+--+-------+----+-++----+\\  |    |||         |    |  | |      ||| | ",
    "|  |   |          | | | | |  |      ||    || |     |    |  | ||     |       | |   |  |       |    | ||    ||  |    |||         |    |  | |      ||| | ",
    "|  |   |          | | | | |  |      ||    || |     |    \\--+-++-----+-------+-+---+--+-------+----+-++----++--/    |||         |    |  | |      ||| | ",
    "|  |   |        /-+-+-+-+-+--+------++----++-+-----+-------+-++-----+-------+-+---+--+-----\\ |    | ||    ||       |||         |    |  | |      ||| | ",
    "|  |   |        | | | | | |  |      ||    || |     |       | ||     |       | |   |  |     | |    | ||    ||       |||         |    |  | |      ||| | ",
    "|/-+---+--------+-+-+-+-+-+--+------++----++-+-----+-----\\ | ||   /-+-------+-+---+--+-----+-+----+-++----++-------+++---------+----+--+\\|      ||| | ",
    "|| |   |        | | | | | |  |      ||    || | /---+-----+-+-++---+-+-------+-+---+--+-----+-+\\   | ||    ||       |||   /-----+----+--+++-----\\||| | ",
    "|| |   |        | | | | | |  |      ||    || | |  /+-----+-+-++---+-+-------+-+---+--+-----+-++---+-++----++-------+++---+-----+----+--+++-\\   |v|| | ",
    "|| |   |        | | | | | |  |      || /--++-+-+--++-----+-+-++---+-+-------+-+---+--+-----+-++---+-++-\\  ||       |||   |     |    |  ||| |   |||| | ",
    "|| |   |        | | \\-+-+-+--+------++-+--+/ | |  ||     | | ||   | |       | |   |/-+-----+-++---+-++-+--++-------+++---+-----+----+--+++-+---++++\\| ",
    "|| |   |        | |   | | |  |      || |  |  | |  ||     | | ||   | |      /+-+---++-+---\\ | ||   | || |  ||       |||   |    /+----+--+++-+-\\ |||||| ",
    "|| |   |        | |   | | | /+------++-+--+--+-+--++-----+-+-++---+-+------++-+---++-+---+-+-++---+-++-+--++-------+++---+---\\||    |  ||| | | |||||| ",
    "|| |   |        \\-+---+-+-+-++-<----++-+--+--+-+--++-----+-+-++---+-+------++-+---++-+---+-/ ||   | || |  ||       |||   |   |||    |  ||| | | |||||| ",
    "|| |   |          |   | | | ||      || |  |  | |  ||     | | ||   | |      || \\---++-+---+---/|   | || |  ||       |||   |   |||    |  ||| | | |||||| ",
    "||/+---+----------+---+-+-+-++----\\ || |  |  | |  ||     | | ||   | | /----++-----++-+---+-\\  |   | || |  || /-----+++-\\ |   |||    |  ||| | | |||||| ",
    "||||   |          |   | | | ||    | || |  |  | |  ||     | | ||   | | |   /++-----++-+---+-+-\\|   | || |  || |     ||| | |   |||    |  ||| | | |||||| ",
    "||||   |          |   | | | ||  /-+-++-+--+--+-+--++-----+-+-++---+-+-+---+++-----++-+---+-+-++---+-++-+--++-+-----+++-+-+---+++----+\\ ||| | | |||||| ",
    "||||   |          |   | | | ||  | | || |  |  | |  ||     | | ||   | | |  /+++-----++-+---+-+-++---+-++-+--++-+-----+++-+>+---+++---\\|| ||| | | |||||| ",
    "||||   |      /---+---+-+-+-++--+-+-++-+--+--+-+--++-----+-+-++---+-+-+--++++-----++-+-\\ | | ||   | || |  || |     ||| | |   |||   ||| ||| | | |||||| ",
    "||||   |      |   |   | | | ||  | | || |  \\--+-+--++-----+-+-/|   | | |  ||||     \\+-+-+-+-+-++---+-++-+--++-+-----+++-+-+---+++---+++-+++-+-+-+++/|| ",
    "||||   |      |   |   | |/+-++--+-+-++-+-\\   | |  ||     | |  |   | |/+--++++------+-+-+-+-+-++---+-++-+--++-+-----+++-+-+---+++\\  ||| ||| | | ||| || ",
    "||||   |      |   |   \\-+++-++--+-+-++-+-+---+-+--++-----+-+--+---+-+++--++++------+-+-+-+-+-++---+-++-+--++-+-----+++-+-+---++/|  |||/+++-+-+-+++\\|| ",
    "||||   |      |/--+-----+++-++--+-+-++-+-+---+-+--++-----+-+--+---+-+++--++++------+-+-+-+-+-++-\\ | || |  || |     ||| | |   || |  ||||||| | | |||||| ",
    "|\\++---+------++--+-----+++-++--+-+-++-+-+---+-+--++-----/ |  |/--+-+++--++++------+-+-+-+-+-++-+-+-++-+--++-+-----+++-+-+---++-+-\\||||||| | | |||||| ",
    "| ||   |      ||  | /---+++-++--+-+-++-+-+---+-+--++-------+-\\||  | |||  ||||      | | | |/+-++-+-+-++-+--++\\|     ||| | |   || | |||||||| | | |||||| ",
    "| ||   |      ||  | |   ||| ||  | | || | | /-+-+--++-------+-+++--+-+++--++++------+-+-+-+++-++-+-+-++-+--++++-----+++-+-+-\\ || | |||||||| | | |||||| ",
    "| ||   |      ||  | |   |||/++--+-+-++-+-+-+-+-+--++-------+-+++--+-+++--++++----\\ | | | ||| || | | || |  ||||     ||| | | | || | |||||||| | | |||||| ",
    "| ||   |      ||  | |/--++++++--+-+-++-+-+-+-+-+--++-------+-+++--+-+++--++++----+-+-+-+-+++-++-+-+\\|| |  |||\\-----+++-/ | | || | |||||||| | | |||||| ",
    "| ||   |      ||  | ||  ||||||  | | || |/+-+-+-+--++-------+-+++--+-+++--++++----+-+-+-+-+++-++-+-++++-+--+++-\\    |||   | | || | |||||||| | | |||||| ",
    "| ||   |      ||  | ||  ||||||  | | || ||| | | |  ||       | |||  | |||  ||||    | | | | ||| || | |||| |  ||| |    |||   | | || | |||||||| | | |||||| ",
    "| ||   |      ||  | ||  |||||| /+-+-++-+++-+-+-+\\ ||       | |||  | |||  ||||    | \\-+-+-+++-++-+-++++-+--+++-+----+++---+-+-++-+-++++++++-+-+-++++/| ",
    "| ||   |      ||  |/++--++++++-++-+-++-+++-+-+-++-++-------+-+++--+-+++--++++----+---+-+-+++-++-+-++++-+--+++-+\\   |||   | | || | |||||||| | | |||| | ",
    "| ||   | /----++--++++--++++++-++-+-++-+++-+-+-++-++-------+-+++--+-+++--++++----+---+-+-+++-++-+-++++-+--+++-++\\  |||   | | || | |||||||| | | |||| | ",
    "| ||   | |    ||  ||||  |||||| || | ||/+++-+-+-++-++-------+-+++--+-+++--++++----+---+-+-+++-++-+-++++-+--+++-+++--+++--\\| | || | |||||||| | | |||| | ",
    "| \\+---+-+----++--++++--++++++-++-/ |||||| | | || ||       | |||  | |||  ||||    |   | | ||| || | |||| |  ||| |||  ||\\--++-+-++-+-++++++++-+-+-++/| | ",
    "|  |   | |    ||  ||||  |||||\\-++---++++++-+-+-++-++-------/ |||  | |||  |\\++----+---+-+-+++-/| | |||| |  ||| |||  || /-++-+-++-+-++++++++-+-+\\|| | | ",
    "|  |   | |  /-++--++++--+++++\\ ||   |||||| | | \\+-++---------+++--+-+++--+-++----+---+-+-+++--//+-++++-+-\\||| |||  || | || | || | |||||||| | |||| | | ",
    "|  |/--+-+--+-++--++++--++++++-++---++++++-+-+--+-++---------+++--+-+++\\ | ||    |   | | |||   || |||\\-+-++++-+++--+/ | || | || | |||||||v | |||| | | ",
    "|  ||  | |  | ||  ||||  |||||| ||   |||||| | |  | ||   /-----+++\\ | |||| | ||    |   | | |||   || |||  | |||| |||  |  | || | || | |||||||| | |||| | | ",
    "|  ||/-+-+--+-++--++++--++++++-++---++++++-+-+\\ | ||   |     |||| v |||| | ||    |   | | |||   || |||  | |||| |||  |  | || | || | |||||||| | |||| | | ",
    "|  ||| | |  | ||  ||||  ||||\\+-++---++++++-+-++-+-++---+-----++++-+-++++-+-++----+---+-+-+++---++-+++--+-++++-+++--+--+-++-+-/| | |||||||| | |||| | | ",
    "|  ||| | | /+-++--++++--++++-+-++---++++++-+-++-+-++---+-----++++-+-++++-+-++----+---+-+-+++---++-+++--+-++++-+++--+--+\\|| |  \\-+-++++++++-+-/||| | | ",
    "|  ||| | | || ||  ||||  |||| | ||   |||||| | || | ||   |    /++++-+-++++-+-++-\\  |   | | |||   || |||  | |||| |||  |  |||| |    | |||||||| |  ||| | | ",
    "|  ||| | | || ||  ||||  |||| | ||   |||||| | || | ||   |    ||||| | |||| | || |  |   | ^ |||   || |||  | |||| |||  |  |||| |    | |||||||| |  ||| | | ",
    "|  ||| | \\-++-++--++++--++++-+-++---++++++-+-++-+-++---+----+++++-+-++++-+-++-+--+---+-+-+++---++-+++--+-++++-++/  |  |||| |    | |||||||| |  ||| | | ",
    "|  \\++-+---++-++--++++--/||| | ||   |||||| | || | ||   |    ||||| | |||| | || |  |   | | |||   || |||  | |||| ||   |  ||||/+----+-++++++++\\|  ||| | | ",
    "|   || |   || ||  ||||   \\++-+-++---+++++/ | || | ||   |    ||||| | |||| | || |  |   | | |||   || |||  | |||| ||   |  ||||||    | ||||||||||  ||| | | ",
    "|   || |   || ||  |||\\----++-+-++---+++++--+-++-+-++---+----+++++-+-++++-+-++-+--+---+-+-+++---++-+/|  | |||| ||   |  ||||||    | ||||||||||  ||| | | ",
    "|   || |   || ||  |||     || | ||   |||||  | || | ||   |    ||||| | |||| \\-++-+--+---+-+-+++---++-+-+--+-++++-++---+--++++++----+-+/||||||||  ||| | | ",
    "|   || |   || ||  |||     || | ||   |||\\+--+-++-+-++---+----+++++-+-++++---++-+--+---+-+-+++---++-+-+--/ |||| ||   |  ||||||    | | ||||||||  ||| | | ",
    "|   || |   || ||  |||     || | ||   ||| |/-+-++-+-++---+----+++++-+-++++---++-+--+---+-+-+++---++-+-+----++++-++---+--++++++----+-+-++++++++--+++-+-+\\",
    "|   || |   || ||  |||     || | ||   ||| || | || | ||   |    ||||| | ||||   || |  |   | | |||   || | |    |||| ||   |  ||||||    | | ||||||||  ||| | ||",
    "|   || |   || ||  |||     || | ||   ||| || | ||/+-++---+----+++++-+-++++---++-+--+---+-+-+++---++-+-+----++++-++---+--++++++---\\| | ||||||||  ||| | ||",
    "|   || |   || ||  |||     |\\-+-++---+++-++-+-++++-++---+----+++++-+-++++---++-+--/   | | |||   || | |    |||| ||   |  ||||||   || | ||||||||  ||| | ||",
    "|   || |   || ||  |||     |  | ||   ||| || |/++++-++---+----+++++-+\\||||   || |      | | |\\+---++-+-+----+++/ ||   |  ||||||   || | ||||||||  ||| | ||",
    "|   || |   || ||  |||     |  | ||   ||| || |||||| ||   |    ||||| ||||||   || |      | | | |   || | |    |||  ||   |  ||||||   || | ||||||||  ||| | ||",
    "|   || |   || ||  |||     \\--+-++---+++-++-++++++-++---+----+++++-++++++---++-+------+-+-+-+---++-+-+----+/|  ||   |  ||||||   || | ||||||||  ||| | ||",
    "|  /++-+---++-++--+++--------+-++---+++-++-++++++-++---+----+++++-++++++---++-+------+-+-+-+---++-+-+----+-+\\ ||   |  ||||||   || | ||||||||  ||| | ||",
    "|  ||| |   || ||/-+++--------+\\||   ||| || ||||||/++---+----+++++-++++++---++-+------+-+-+-+---++-+-+----+-++-++---+--++++++--\\|| | ||\\+++++--+++-/ ||",
    "|  ||| |   || ||| |||        ||||   ||| || |||||||||   |    ||||| ||||||   || |      | | | |   || | |    | || ||   |  ||||||  ||| | || |||||  |||   ||",
    "|  ||| |   || ||| |||        ||||   ||| || |||||||||   |   /+++++-++++++---++\\|      | | | |   || | |    | || ||   |  ||||||  ||| | || |||||  |||   ||",
    "|  ||| |   || ||| |||        ||||   ||| || |||||||||   |   |||||| ||||||   ||||    /-+-+-+-+---++-+-+----+-++\\||   |  ||||||  ||| | || |||||  |||   ||",
    "|  ||| |   || ||| |||    /---++++---+++\\|| ||\\++++++---+---++++++-++/|||   |\\++----+-+-+-+-+---++-/ |    | |||||   |  ||||||  ||| | || |||||  |||   ||",
    "|  ||| |   || |||/+++----+---++++---++++++-++-++++++---+---++++++-++-+++---+-++----+-+-+-+\\|   ||   |    | |||||   |  ||||||  ||| | || |||||  |||   ||",
    "|  ||| |   || |||||||    |   ||||   |||||| || ||||||   |  /++++++-++-+++---+-++----+-+-+-+++---++---+----+-+++++---+--++++++--+++-+-++-+++++--+++\\  ||",
    "|  ||| |   || |||||||    |   ||||   |||||| || ||||||   |  ||||||| || |||   | ||    | | | |||   ||   |    | |||||   |  ||||||  ||| | || |||||  ||||  ||",
    "|  ||| |   || |||||||    |   ||||   |||||| || ||||||   |  |||||||/++-+++---+-++----+-+-+-+++---++---+----+-+++++---+--++++++--+++-+-++-+++++\\ ||||  ||",
    "|  |||/+---++-+++++++\\   |   ||||   |||||| |\\-++++++---+--+++++++++/ |||   | ||    | | | |||   ||   |    | |||||   |  ||||||  ||| | || |||||| ||||  ||",
    "|  |||||   || ||||||||   |   ||||   |||||| |  |||||\\---+--+++++++++--+++---+-++----+-+-+-+++---++---+----+-+++++---/  ||||||  ||| | || |||v|| ||||  ||",
    "|  |||||   || ||||||||   |   ||||   |||||| |  |||||    |  |||||||||  |||   | ||    | \\-+-+++---++<--/    | |||||      ||||||  ||| | || |||||| ||||  ||",
    "|  |||||   || ||||||\\+---+---++++---++++++-+--+++++----+--+++/|||||  |||   | ||   /+---+-+++---++\\       | |||||      ||||||  ||| | || |||||| ||||  ||",
    "|  |||||   || |||||| |   |   ||||   \\+++++-+--+++++----+--+++-+++++--+++---+-++---++---+-+++---+++-------+-+++++------++++++--+++-+-/| |||||| ||||  ||",
    "|  |||||   || |||||| |  /+---++++----+++++-+<-+++++----+--+++-+++++\\ |||   | ||   ||   | |||   |||       | |||||      ||||||  ||| |  | |||||| ||||  ||",
    "|  |||||   || |||||| |  ||   ||\\+----+++++-+--++/||    |  ||| |||||| |||   | ||   ||   | |||   |||       |/+++++------++++++--+++-+--+-++++++\\||||  ||",
    "|  |||||   || |||||| |/-++---++-+----+++++-+--++-++----+--+++-++++++-+++---+-++---++---+-+++---+++-------+++++++-----\\||||||  ||| |  | |||||||||||  ||",
    "|  |||||   || |||||| || ||   || |    ||||| |  || \\+----+--+++-++++++-+++---+-++---++---+-+++---+++-------+++++++-----+++++++--/|| |  | |||||||||||  ||",
    "|  |||||   || |||||| || ||   || | /--+++++-+--++--+----+--+++-++++++-+++---+-++\\  ||   | |||   |||       |||||||     |||||||   || |  | |||||||||||  ||",
    "|  |||||   || |||||\\-++-++---++-+-+--+++++-+--++--+----+--+++-++++++-+++---+-+++--++---+-+++---+++-------++++++/     |||||||   || |  | |||||||||||  ||",
    "|  |||||   || |||||  || ||   || | |  ||||| |  ||  |    |  |||/++++++-+++---+-+++--++---+-+++---+++\\      ||||||      |||||||   || |  | \\++++++++/|  ||",
    "|  |||||   || |\\+++--++-++---++-+-+--+++++-+--++--+----+--++++++++++-+++---+-+++--++---+-+++---+/||      |||||| /----+++++++\\  || |  |  |||||||| |  ||",
    "|  |||||   || | |||  || ||   || \\-+--+++++-+--++--+----+--++++++++++-+++---+-+++--++---+-+++---+-++------++++++-+----++++++++--++-+--/  |||||||| |  ||",
    "|  |||||   || | |||  || || /-++---+--+++++-+--++--+----+--++++++++++-+++---+-+++--++---+\\|||   | ||      |||||| |    ||||||||  || |     |||||||| |  ||",
    "|  |||||   || | |||  || || | ||   |  ||||| |  ||  |    |  |||||||||| |||   | |||  ||/--+++++---+-++------++++++-+----++++++++--++-+-----++++++++-+-\\||",
    "|/-+++++---++-+-+++--++-++-+-++---+--+++++-+--++--+-\\  |  ||||||||\\+-+++---+-+++--+++--+++++---+-++------++++++-+----++++++++--++-+-----/||||||| | |||",
    "|| |||||   || | |||  || || | ||  /+--+++++-+--++--+-+--+--++++++++-+-+++---+-+++--+++--+++++---+-++----\\ |||||| |    ||||||||  || |      ||||||| | |||",
    "|| |||||   || | |||  || || | ||  ||  ||||\\-+--++--+-+--+--++++++++-+-+++---+-+++--+++--+++++---+-++----+-++++++-+----++++++++--++-+------+++++++-+-++/",
    "|| |||||   || | |||  || || | ||  ||  ||||  |  ||  | |  | /++++++++-+-+++--\\| |||  |||  |||||   | ||    | |||||| |    ||||||||  || |      ||||||| | || ",
    "|| |\\+++---++-+-+++--++-++-+-++--++--++++--+--++--+-+--+-+++++++++-+-++/  || |||  |||  |||||   | ||    | |||||| |    ||||||||  || |      ||||||| | || ",
    "|| | |||   |\\-+-+++--++-++-+-/|  ||/-++++--+\\ ||  | |  | ||||||||| | ||   || |||  |||  |||||   | ||    | |||||| |    ||||||||  || |      ||||||| | || ",
    "|| | |||/--+--+-+++\\ || || |  |  ||| ||||  || ||  \\-+--+-+++++++++-+-++---++-+++--+++--+++++---+-++----+-++++++-+----++++++++--++-+------++/|||| | || ",
    "|| | ||||  |  | |||| || || |  |  ||| \\+++--++-++----+--+-+++++++++-+-++---++-+++--+++--+++++---+-++----+-++++++-+----++++++++--++-+------/| |||| | || ",
    "\\+-+-++++--+--+-++/| || || |  |  |||  |||  || ||    |  | ||||||||| | ||   |\\-+++--+++--++/||   | ||    | |||||| |    ||||||||  || |       | |||| | || ",
    " | | ||||  |  | || | || || |  |  |||  |||  || || /--+--+-+++++++++-+-++---+--+++--+++--++-++---+-++----+-++++++-+----++++++++--++-+----\\  | |||| | || ",
    " | | ||||  |  | || | || || |  |  |||  |||  || || |  |  | |||\\+++++-+-++---+--+/|  |||  || ||   | ||    | |\\++++-+----++++++++--++-+----+--+-+/|| | || ",
    " |/+-++++--+--+-++-+-++-++-+--+--+++--+++--++-++\\|  |  | ||| ||||| | ||   |  | |  |||  || ||/--+-++---\\| | |||| |    ||||||||  || |    |  | | || | || ",
    " ||| ||||  |  | || | || || |  |  |||  |||  || ||||  |  | ||| ||||| | |\\---+--+-+--+++--++-+/|  | ||   || | |||| |    ||||||||  || |    |  | | || | || ",
    " ||| ||||  |  | || |/++-++-+--+--+++--+++-\\|| ||||  |  | ||| ||||| | |    |  | |  |||  || | |  | ||   || | |||| |    ||||||||  || |    |  | | || | || ",
    " ||| ||||  |  | || |||| || |  |  |||  ||| |\\+-++++--+--+-+++-+++++-+-+----+--+-+--+++--++-+-+--+-++---++-+-++++-+----++++++/|  || |    |  | | || | || ",
    " ||| |||\\--+--+-++-/||| || |  |  |||  ||\\-+-+-++++--+--+-+++-+++++-+-+----+--+-+--+++--++-+-+--+-++---++-+-+++/ |    |||||| |  || |    |  | | || | || ",
    " ||| |||   |  | \\+--+++-++-+--/  |||  ||  | | ||||  |  | ||| ||||| | |    |  | |  |||  || | |  | ||   || | |||  |    ||||\\+-+--++-+----+--+-+-+/ | || ",
    " ||| |||   |  |  |  ||| || |     |||  ||  | | |\\++--+--+-+++-+++++-+-+----+--+-+--+++--++-+-+--+-++---++-+-+++--+----++++-+-+--/| |    |  | | |  | || ",
    " ||| |||   |  |  |  ||| || |     |||  ||  | | | ||  |  | ||| ||||| | \\----+--+-+--+++--++-+-+--+-++---++-+-+++--+----++++-+-+---/ |    |  | | |  | || ",
    " ||| |||   |  |  |  ||| || |     |||  ||  | | | ||  |  | ||| |\\+++-+------+--+-+--+++--++-+-+--+-++---++-+-+++--+----++++-+-+-----+----+--+-+-+--+-+/ ",
    " ||| |||   |  |  |  ||| || |     |||  ||  | | | ||  |  | ||| | ||\\-+------+--+-+--+++--++-+-+--+-++---++-+-+++--+----++++-+-+-----+----+--+-/ |  | |  ",
    " ||| |||   |  |  |  ||| || |     |||  ||  | | | ||  |  | ||| | ||  |      |  | |  ||| /++-+-+--+-++---++-+-+++--+--\\ |||| | |     |    |  |   |  | |  ",
    " ||| |||   |  \\--+--+++-++-+-----+++--++--+-+-+-++--+--+-+++-+-++--+------+--+-+--+++-+/| | |  | ||   || | |||  |  | |||| | |     |    |  |   |  | |  ",
    " ||| |||   |     |  ||| || |     |||  ||  | | | ||  |  | ||| | ||  |      |  | |  \\++-+-+-+-+--+-/|   || | |||  |  | |||| | |     |    |  |   |  | |  ",
    " ||| ||\\---+-----+--+++-++-+-----+++--++--+-+-+-++--+--+-+++-+-++--+------+--+-+---++-+-+-+-+--+--+---++-+-/||  \\--+-++++-+-/     |    |  |   |  | |  ",
    " ||| ||    |/----+--+++-++-+--\\  |||  ||  | | | ||  |  | \\++-+-++--+------/  | |   || | | | |  |  |   || |  ||     | |||| |       |    |  |   |  | |  ",
    " ||| ||    ||    |  ||| || |  |  |||  ||  | | | ||  |  |  || \\-++--+---------+-+---++-+-+-+-+--+--/   || |  ||     | |||| \\-------+---<+--/   |  | |  ",
    " ||| |\\----++----+--+/| |\\-+--+--+++--+/  | | | ||  |  |  ||   ||  |         | |   || | | | |  |      || |  ||     | ||||         |    |      |  | |  ",
    " ||| |     ||    |  | | |  |/-+--+++--+---+-+-+-++--+--+--++---++--+---------+-+---++-+-+-+-+--+------++-+--++-----+-++++-----\\   |    |      |  | |  ",
    " ||| |     ||    |  | | |  || |  ||\\--+---+-/ | ||  |  |  ||   ||  |         | |   |\\-+-+-+-+--+------++-+--++-----+-++++-----+---+----+------+--+-/  ",
    " ||| |     ||    |  | | |  || |  \\+---+---+---+-++--+--+--++---++--+---------+-+---+--+-+-+-+--+------+/ |  ||     | ||||     |   |    |      |  |    ",
    " ||| |     ||    |  \\-+-+--++-+---+---+---/   | |\\--+--+--++---++--+---------+-+---+--+-+-+-+--+------+--+--++-----+-++++-----+---+----/      |  |    ",
    " ||| |     ||    |    | |  || |   |   \\-------+-+---+--+--++---++--+---------+-+---+--+-+-+-+--+------+--+--++-----+-+++/     |   |           |  |    ",
    " ||| |     \\+----+----+-+--++-+---+-----------+-+---+--+--++---++--+---------+-+---+--+-+-+-+--+------+--+--++-----+-++/      |   |           |  |    ",
    " ||| |      |    |    | \\--++-+---+-----------+-+---+--+--++---++--/         | |   |  | | | |  |      |  |  ||     | ||       |   |           |  |    ",
    " ||| |      |    |    |    \\+-+---+-----------+-+---+--+--++---++----<-------+-+---+--+-/ | |  |      |  |  ||     | ||       |   |           |  |    ",
    " ||| |      |    |    |     | |   |           | |   |  |  ||   ||       /----+-+---+--+---+-+--+------+--+--++-----+-++------\\|   |           |  |    ",
    " ||| |      |    \\----+-----+-+---+-----------+-+---+--+--++---++-------+----+-+---+--+---/ |  |      |  |  ||     | v|   /--++---+-----------+--+\\   ",
    " ||| |      |         |     | |   |           | |   |  |  ||   ||       |    | |   |  |     |  \\------+--/  ||     | ||   |  ||   |           |  ||   ",
    " |\\+-+------+---------+-----+-+---+-----------+-/   |  |  \\+---++--<----+----+-+---+--+-----+---------+-----++-----+-++---+--++---+-----------+--/|   ",
    " | | |      \\---------+-----+-/   | /---------+-----+--+--\\|   \\+-------+----+-+---+--+-----+---------+-----++-----+-++---+--++---/           |   |   ",
    " | | |                |     |     | |         |     |  |  ||    |       |    | |   |  |     |         |     ||     | ||   |  ||               |   |   ",
    " | | |                |     |     | |         |     |  |  |\\----+-------+----/ |   |  |     |         |     ||     | ||   |  ||               |   |   ",
    " | | |                |     \\-----+-+---------+-----+--+--+-----+-------+------+---+--+-----+---------+-----++-----+-++---+--+/               |   |   ",
    " | | |                |   /-------+-+---------+-----+--+--+-----+-----\\ |      |   |  |     |         |     ||     | ||   |  ^                |   |   ",
    " | | |                |   |       | |         |     |  |  |     |     | \\------+---+--+-----+---------+-----++-----+-++---+--/                |   |   ",
    " | | |                \\---+-------+-+---------+-----+--+--+-----+-----+--------+---+--+-----+---------+-----++-----+-/|   |                   |   |   ",
    " | | |                    |       | |         |     |  |  |     |     |        |   |  |     |         |     ||     |  |   \\-------------------+---/   ",
    " \\-+-+--->----------------+-------+-+---------+-----/  |  |     |     |        |   |  |     \\---------/     ||     |  |                       |       ",
    "   \\-+--------------------+-------+-+---------+--------+--+-----+-----+--------+---+--+---------------------/|     |  \\-----------------------/       ",
    "     |                    |       | |         |        \\--+-----/     |        |   |  |                      |     |                                  ",
    "     \\--------------------+-------+-+---------/           |           |        |   |  |                      |     |                                  ",
    "                          |       \\-+---------------------+-----------+--------/   |  |                      |     |                                  ",
    "                          |         \\---------------------/           |            |  \\----------------------+-----/                                  ",
    "                          \\-------------------------------------------/            \\-------------------------/                                        ",
]

xrows = [ # second example
    "/>-<\\  ",
    "|   |  ",
    "| /<+-\\",
    "| | | v",
    "\\>+</ |",
    "  |   ^",
    "  \\<->/",
]

SLASH = '/'
BACKSLASH = '\\'
VERTICAL = '|'
HORIZONTAL = '-'
UP = '^'
DN = 'v'
LEFT = '<'
RIGHT = '>'
CROSS = '+'
CAR_CHARS = [UP, DN, LEFT, RIGHT]
VER_CHARS = [UP, DN]

class Car:
    def __init__(self,id,r,c,direction):
        self.id = id
        self.r = r
        self.c = c
        self.direction = direction
        self.next_turn = 0 # 0,1,2
        self.crashed = False

map = []
cars = []

id = 900
for r in range(len(rows)): 
    map.append(list(rows[r]))
    for c in range(len(rows[r])) :
        if map[r][c] in CAR_CHARS :
            dir = map[r][c]
            cars.append(Car(id,r,c,dir))
            w = VERTICAL if dir in VER_CHARS else HORIZONTAL
            map[r][c] = w
            id += 10
    print("".join(map[r]))

def turn_right(dir):
    if dir == UP : return RIGHT
    if dir == RIGHT : return DN
    if dir == DN : return LEFT
    if dir == LEFT : return UP
    raise ValueError

def turn_left(dir):
    if dir == UP : return LEFT
    if dir == LEFT : return DN
    if dir == DN : return RIGHT
    if dir == RIGHT : return UP
    raise ValueError

def value(r,c):
    try :
        if r<0 or c<0 : return ' '
        return map[r][c]
    except :
        return ' '

def same(_r, _c, r, c):
    return _r == r and _c == c

def corner_turn(corner, source):
    # if you encounter X from direcion Y... proceed in W (X,Y):W
    directions = {
        (SLASH,UP): RIGHT,
        (SLASH,DN): LEFT,
        (SLASH,LEFT): DN,
        (SLASH,RIGHT): UP,
        (BACKSLASH,UP): LEFT,
        (BACKSLASH,DN): RIGHT,
        (BACKSLASH,LEFT): UP,
        (BACKSLASH,RIGHT): DN,
    }
    target = directions.get((corner, source), None)
    if target == None :
        raise ValueError
    # print("corner turn:", corner, source, ">>", target)
    return target

def move(car):
    _r = car.r
    _c = car.c
    _d = car.direction
    if car.direction == UP :
        car.r -= 1
    elif car.direction == DN :
        car.r += 1
    elif car.direction == LEFT :
        car.c -= 1
    else : # direction is RIGHT
        car.c += 1

    icon = map[car.r][car.c]
    # so now set the direction based on the map icon
    if icon in [SLASH,BACKSLASH] :
        # turn in the direction of the corner
        car.direction = corner_turn(icon, _d)

    elif icon == CROSS :
        if car.next_turn == 0 : # LEFT
            car.direction = turn_left(car.direction)
        elif car.next_turn == 1 : # STRAIGHT
            pass # no direction change
        elif car.next_turn == 2 : # RIGHT
            car.direction = turn_right(car.direction)
        else:
            raise ValueError
        car.next_turn = (car.next_turn+1)%3

    else :
        pass # no change to the direction

    # print("car {}:{} moved from ({},{}) to ({},{}) == {}  {}".format(car.id, _d, _r,_c, car.r,car.c, icon, car.direction))

def crashed(car):
    for i in range(len(cars)):
        c = cars[i]
        if c.crashed : continue
        if c.id == car.id : continue
        if same(c.r,c.c,car.r,car.c):
            # print("crash")
            return i
    return None
        
import copy
import time
from operator import attrgetter

def sorter(car): 
    return car.r
  
def main(stdscr):
    # crash = False

    for m in range(20000):
        if m > 0 : 
            # after first - move the cars
            cars.sort(key=attrgetter('r','c'))
            for car in cars : 
                if car.crashed : continue
                move(car)
                # print(m,"moved {} to {},{} ".format(car.id,car.r,car.c))
                # Important: find crash immediately after a single car moves
                # otherwise if you wait until after the all cars move they can miss
                index = crashed(car) # car crashed into cars[index]
                if index != None : 
                    print(m, "crash", index, car.id, "into", cars[index].id, "({},{})".format(car.r,car.c))
                    car.crashed = True
                    cars[index].crashed = True
                
        if m < 10 or m > 8276 :
            remaining = [car for car in cars if not car.crashed]
            car_text = " ".join([ "{}:({},{})".format(car.id,car.r,car.c) for car in remaining])
            print("after move {}: {} cars at: {}".format(m, len(remaining), car_text))
        if len(remaining) == 1 :
            return remaining[0]

last_car = main(0)
print("Last Car at {},{}".format(last_car.c, last_car.r))

