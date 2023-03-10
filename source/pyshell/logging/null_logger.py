from pathlib import Path
from pyshell.commands.command_metadata import CommandMetadata
from pyshell.logging.command_logger import ICommandLogger
from pyshell.logging.logger import ILogger
from pyshell.logging.logger_options import LoggerOptions
from pyshell.logging.null_command_logger import NullCommandLogger

class NullLogger(ILogger):
    """
    Represents a logger for PyShell.
    Loggers are executed after a command is run regardless of the result of the
      command. This allows for logging of both successful and failed commands
      since the logger is executed before an error handler is called to handle
      a failed command.
    @ingroup logging
    """
    def construct_logger(self,
        metadata: CommandMetadata,
        options: LoggerOptions,
        cwd: Path) -> ICommandLogger:
        """
        Constructs a new command logger.
        @param metadata The metadata of the command that will the command logger
          will be used for.
        @param options The options for the command logger.
        @param cwd The current working directory of the command that will the
          command logger will be used for.
        @return A new command logger instance.
        """
        return NullCommandLogger()
