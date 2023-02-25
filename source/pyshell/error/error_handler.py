from abc import ABC, abstractmethod
from pyshell.core.command_result import CommandResult

class IErrorHandler(ABC):
    """
    Represents an error handler for PyShell commands.
    """
    @abstractmethod
    def handle(self, result: CommandResult) -> None:
        """
        Handles a command that returned a non-zero exit code.
        @param result Data for the command that was run.
        """
        raise NotImplementedError()