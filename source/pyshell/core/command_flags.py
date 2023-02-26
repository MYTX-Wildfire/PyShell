from enum import IntEnum

class CommandFlags(IntEnum):
    """
    Flags that identify various properties of a command.
    """
    # Standard command, no special properties.
    STANDARD = 0x0

    # The command's trigger condition has not been met.
    # Inactive commands should not be run.
    INACTIVE = 0x1

    # Command is a command that should be run even if a failure occurs.
    CLEANUP = 0x2