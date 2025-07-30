import os
import subprocess
import time
import pyautogui
import psutil
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

mcp = FastMCP("Windows Automation MCP")

@mcp.tool()
def run_command(command: str) -> str:
    try:
        output = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            encoding='cp850'
        )
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

@mcp.tool()
def open_program(program_name: str) -> str:
    try:
        subprocess.Popen(program_name)
        return f"Program '{program_name}' started successfully."
    except Exception as e:
        return f"Error opening program '{program_name}': {str(e)}"

@mcp.tool()
def close_program(program_name: str) -> str:
    closed = []
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and program_name.lower() in proc.info['name'].lower():
            try:
                proc.terminate()
                closed.append(proc.info['name'])
            except Exception:
                continue
    if closed:
        return f"Processes terminated: {', '.join(closed)}"
    return f"No process matching '{program_name}' was found."

@mcp.tool()
def type_text(text: str) -> str:
    try:
        pyautogui.write(text, interval=0.05)
        return "Text typed successfully."
    except Exception as e:
        return f"Error typing text: {str(e)}"

@mcp.tool()
def keyboard_shortcut(keys: list[str]) -> str:
    try:
        pyautogui.hotkey(*keys)
        return f"Shortcut {' + '.join(keys)} executed."
    except Exception as e:
        return f"Error executing shortcut: {str(e)}"

@mcp.tool()
def screenshot() -> TextContent:
    try:
        path = os.path.join(os.environ["TEMP"], "screenshot.png")
        pyautogui.screenshot(path)
        return TextContent(
            type="text",
            text=f"Screenshot saved at: {path}"
        )
    except Exception as e:
        return TextContent(
            type="text",
            text=f"Error capturing screenshot: {str(e)}"
        )

@mcp.tool()
def open_browser(url: str, browser: str = "chrome") -> str:
    try:
        if browser == "chrome":
            path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        elif browser == "edge":
            path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        elif browser == "firefox":
            path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        else:
            import webbrowser
            webbrowser.open(url)
            return f"Default browser opened {url}"
        subprocess.Popen([path, url])
        return f"{browser} opened {url}"
    except Exception as e:
        return f"Error opening browser: {str(e)}"

@mcp.tool()
def wait_seconds(seconds: float = 3.0) -> str:
    time.sleep(seconds)
    return f"Waited for {seconds} seconds."

@mcp.tool()
def type_on_website(text: str) -> str:
    try:
        pyautogui.write(text, interval=0.05)
        return "Text typed successfully on the website."
    except Exception as e:
        return f"Error typing on website: {str(e)}"

@mcp.tool()
def press_key(key: str) -> str:
    try:
        pyautogui.press(key)
        return f"Key '{key}' pressed."
    except Exception as e:
        return f"Error pressing key: {str(e)}"

if __name__ == "__main__":
    mcp.run("stdio")
