from pyshell.commands.command_result import CommandResult
from pyshell.error.error_handler import IErrorHandler

class AbortOnFailure(IErrorHandler):
    """
    Error handler that stops a PyShell script if a command fails.
    @ingroup error
    """
    def handle(self, result: CommandResult) -> None:
        """
        Handles a command that returned a non-zero exit code.
        @param result The result of the command.
        """
        raise RuntimeError(
            f"Command '{result.command}' failed with exit code " + \
                f"{result.exit_code}.\n" +
            f"Note: Full command was '{result.full_command}'."
        )
