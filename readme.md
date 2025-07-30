# Windows Automation MCP

A Model Context Protocol (MCP) server that provides Windows automation capabilities, allowing AI assistants to interact with the Windows operating system through various automation tools.

## Features

- **Command Execution**: Run Windows command-line commands
- **Program Management**: Open and close applications
- **Text Input**: Type text and execute keyboard shortcuts
- **Screenshot Capture**: Take screenshots of the desktop
- **Browser Control**: Open URLs in specific browsers
- **Web Interaction**: Type text on websites and press keys
- **Timing Control**: Add delays between operations

## Prerequisites

- Python 3.7 or higher
- Windows operating system
- Required Python packages (see Installation)

## Installation

1. Clone or download the MCP server files
2. Install the required dependencies:

```bash
pip install mcp pyautogui psutil
```

3. Place the server files in your desired directory
4. Configure your MCP client to use this server

## Configuration

### For LM Studio

Add the following configuration to your `lmstudio.json` file:

```json
{
  "name": "windows-automation-mcp",
  "version": "0.0.1",
  "schema": "v1",
  "mcpServers": {
    "local": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

### For Other MCP Clients

Configure your MCP client to run the server with:
- Command: `python`
- Arguments: `["server.py"]`
- Working directory: Path to the server files

## Available Tools

### `run_command(command: str)`
Executes a Windows command-line command and returns the output.

**Example**: `run_command("dir C:\\")`

### `open_program(program_name: str)`
Launches a Windows program or application.

**Example**: `open_program("notepad.exe")`

### `close_program(program_name: str)`
Terminates processes matching the given program name.

**Example**: `close_program("notepad")`

### `type_text(text: str)`
Types the specified text at the current cursor position.

**Example**: `type_text("Hello, World!")`

### `keyboard_shortcut(keys: list[str])`
Executes a keyboard shortcut combination.

**Example**: `keyboard_shortcut(["ctrl", "c"])`

### `screenshot()`
Captures a screenshot and saves it to the system's temporary directory.

**Returns**: Path to the saved screenshot file

### `open_browser(url: str, browser: str = "chrome")`
Opens a URL in the specified browser.

**Supported browsers**: chrome, edge, firefox
**Example**: `open_browser("https://google.com", "chrome")`

### `wait_seconds(seconds: float = 3.0)`
Pauses execution for the specified number of seconds.

**Example**: `wait_seconds(2.5)`

### `type_on_website(text: str)`
Types text on a website (same as type_text but with contextual naming).

**Example**: `type_on_website("search query")`

### `press_key(key: str)`
Presses a single key.

**Example**: `press_key("enter")`

## Security Considerations

⚠️ **Important Security Notes**:

- This MCP server can execute arbitrary commands on your Windows system
- It can control your mouse and keyboard
- It can open programs and access files
- Only use this server in trusted environments
- Be cautious when sharing or deploying this server
- Consider implementing additional authentication if needed

## Usage Examples

### Basic Automation Workflow
1. Take a screenshot to see the current state
2. Open a program (e.g., notepad)
3. Wait for the program to load
4. Type some text
5. Save the file using keyboard shortcuts

### Web Automation
1. Open a browser with a specific URL
2. Wait for the page to load
3. Type in search fields
4. Press Enter to submit forms

## Troubleshooting

### Common Issues

**Permission Errors**: 
- Run your MCP client as administrator if you encounter permission issues
- Some system programs may require elevated privileges to control

**PyAutoGUI Fail-Safe**:
- PyAutoGUI has a fail-safe feature that stops execution if you move the mouse to the top-left corner
- This is a safety feature to prevent runaway automation

**Process Not Found**:
- When closing programs, ensure you use the correct process name
- Check Task Manager for the exact process name if needed

**Browser Path Issues**:
- The server uses default installation paths for browsers
- Modify the browser paths in the code if your browsers are installed elsewhere

### Error Handling

All tools include error handling and will return descriptive error messages if operations fail. Check the returned messages for troubleshooting information.

## Dependencies

- **mcp**: Model Context Protocol implementation
- **pyautogui**: GUI automation library
- **psutil**: System and process utilities
- **subprocess**: Built-in Python module for running commands
- **time**: Built-in Python module for timing operations

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this MCP server.

## License

This project is provided as-is for educational and automation purposes. Use responsibly and at your own risk.

## Disclaimer

This software can perform actions on your computer automatically. The authors are not responsible for any damage or unintended consequences resulting from its use. Always test in a safe environment first.