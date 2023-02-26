from pathlib import Path
from pyshell.backends.backend import IBackend
from pyshell.core.command_metadata import CommandMetadata
from pyshell.core.command_result import CommandResult

class DockerBackend(IBackend):
    """
    Backend that executes commands in a docker container.
    @ingroup backends
    """

    def run(self,
        metadata: CommandMetadata,
        cwd: Path) -> CommandResult:
        """
        Runs the specified command on the backend.
        @param metadata Metadata for the command to run.
        @param cwd The working directory to use for the command. Will always be
          an absolute path.
        @return The output of the command.
        """
        raise NotImplementedError()