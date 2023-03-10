from pathlib import Path
from pyshell import PyShell, PyShellOptions, AbortOnFailure, AllowAll, \
    KeepGoing, NativeBackend, NullLogger, ConsoleLogger
from pyshell.commands.external_command import ExternalCommand
from unit.tracing.get_caller_line_number import get_caller_line_number

def test_run_external_executable_on_path():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        NullLogger(),
        AllowAll(),
        AbortOnFailure(),
        PyShellOptions()
    )

    # Run the commands
    cmd = ExternalCommand(
        "ls",
        "/usr/bin"
    )
    result = cmd(pyshell)
    assert result.success


def test_run_external_executable_not_on_path():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        ConsoleLogger(),
        AllowAll(),
        AbortOnFailure(),
        PyShellOptions()
    )

    # Get the path to the test script to invoke
    curr_path = Path(__file__).parent
    script_path = curr_path / "test.sh"

    # Run the commands
    msg = "foo"
    cmd = ExternalCommand(
        script_path,
        msg,
        locate_executable=True
    )
    result = cmd(pyshell)
    assert result.success
    assert result.output == f"{msg}\n"


def test_run_external_executable_not_on_path_with_no_locate():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        ConsoleLogger(),
        AllowAll(),
        AbortOnFailure(),
        PyShellOptions()
    )

    # Get the path to the test script to invoke
    curr_path = Path(__file__).parent
    script_path = curr_path / "test.sh"

    # Run the commands
    msg = "foo"
    cmd = ExternalCommand(
        script_path,
        msg,
        locate_executable=False
    )
    result = cmd(pyshell)
    assert result.success
    assert result.output == f"{msg}\n"


def test_run_external_executable_not_on_path_fails():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        NullLogger(),
        AllowAll(),
        KeepGoing(),
        PyShellOptions()
    )
    script_path = "foo.sh"

    # Run the commands
    msg = "foo"
    cmd = ExternalCommand(
        script_path,
        msg,
        locate_executable=True
    )
    result = cmd(pyshell)
    assert not result.success


def test_run_external_executable_not_on_path_with_no_locate_fails():
    # Initialize a PyShell instance for running commands
    pyshell = PyShell(
        NativeBackend(),
        ConsoleLogger(),
        AllowAll(),
        AbortOnFailure(),
        PyShellOptions()
    )

    # Get the path to the test script to invoke
    curr_path = Path(__file__).parent
    script_path = curr_path / "foo.sh"

    # Run the commands
    msg = "foo"
    cmd = ExternalCommand(
        script_path,
        msg,
        locate_executable=False
    )
    result = cmd(pyshell)
    assert not result.success


def test_command_returns_full_command():
    # Create the command
    cmd_name = "echo"
    cmd_args = ["foo", "bar"]
    cmd = ExternalCommand(
        cmd_name,
        cmd_args
    )

    assert cmd.command_name == cmd_name
    assert cmd.args == cmd_args
    assert cmd.full_command == ([cmd_name] + cmd_args)


def test_full_command_without_args():
    # Create the command
    cmd_name = "echo"
    cmd = ExternalCommand(
        cmd_name
    )

    assert cmd.command_name == cmd_name
    assert cmd.args == []
    assert cmd.full_command == [cmd_name]


def test_command_captures_origin():
    # Create the command
    cmd = ExternalCommand("echo", "foo")
    expected_line_number = get_caller_line_number() - 1

    assert cmd.origin.file_path == Path(__file__)
    assert cmd.origin.line_number == expected_line_number
