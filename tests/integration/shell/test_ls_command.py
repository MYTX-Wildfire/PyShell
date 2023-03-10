from pathlib import Path
from pyshell import PyShell, PyShellOptions, AbortOnFailure, AllowAll, \
    KeepGoing, NativeBackend, ConsoleLogger
from pyshell.modules.shell import Shell

def test_ls_command_with_no_arg():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        ConsoleLogger(),
        AllowAll(),
        AbortOnFailure(),
        PyShellOptions(),
        cwd=Path(__file__).parent
    )

    # Run some commands
    result = Shell.ls(pyshell=pyshell)
    assert result.success

    # Verify that the output is correct
    curr_file = Path(__file__).name
    assert curr_file in result.output


def test_ls_command_with_arg():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        ConsoleLogger(),
        AllowAll(),
        AbortOnFailure(),
        PyShellOptions(),
        cwd=Path(__file__).parent
    )

    # Run some commands
    result = Shell.ls(Path(__file__).parent, pyshell=pyshell)
    assert result.success

    # Verify that the output is correct
    curr_file = Path(__file__).name
    assert curr_file in result.output


def test_ls_command_on_non_existent_dir():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        ConsoleLogger(),
        AllowAll(),
        KeepGoing(),
        PyShellOptions(),
        cwd=Path(__file__).parent
    )

    # Run some commands
    result = Shell.ls("/foo", pyshell=pyshell)
    assert not result.success
