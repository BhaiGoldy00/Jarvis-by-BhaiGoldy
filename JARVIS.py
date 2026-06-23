import subprocess
import sys
import os
import time
import webbrowser

# ─────────────────────────────────────────
#   🤖 JARVIS - by Goldy Bhai
#   Just A Rather Very Intelligent System
# ─────────────────────────────────────────

def speak(text, delay=0.3):
    """Print with Jarvis style and dramatic pause"""
    time.sleep(delay)
    print(f"\n🤖 JARVIS: {text}")

def open_chrome(url="https://www.google.com"):
    speak("Initializing Google Chrome, Sir...", delay=0.4)
    try:
        if sys.platform == "win32":
            paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ]
            opened = False
            for path in paths:
                if os.path.exists(path):
                    subprocess.Popen([path, url])
                    opened = True
                    break
            if not opened:
                webbrowser.open(url)
        else:
            webbrowser.open(url)
        time.sleep(0.5)
        speak("Google Chrome has been launched successfully. ✅")
    except Exception as e:
        speak(f"Unable to launch Chrome, Sir. Error: {e}")

def open_camera():
    speak("Activating camera module, Sir...", delay=0.4)
    try:
        if sys.platform == "win32":
            subprocess.Popen("start microsoft.windows.camera:", shell=True)
            time.sleep(0.5)
            speak("Camera is now active and ready. ✅")
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-a", "Photo Booth"])
            time.sleep(0.5)
            speak("Camera has been launched successfully. ✅")
        else:
            try:
                subprocess.Popen(["cheese"])
                time.sleep(0.5)
                speak("Camera is now active and ready. ✅")
            except:
                speak("Camera application not found. Please install 'cheese' via: sudo apt install cheese")
    except Exception as e:
        speak(f"Failed to activate camera, Sir. Error: {e}")

def open_youtube():
    speak("Launching YouTube, Sir...", delay=0.4)
    time.sleep(0.3)
    open_chrome("https://www.youtube.com")

def open_zerodayx():
    speak("Access granted. Initiating ZeroDayX protocol...", delay=0.5)
    time.sleep(0.6)
    speak("Loading your personal playlist, Sir. Enjoy the session. 🎵🔥")
    time.sleep(0.4)
    webbrowser.open("https://open.spotify.com/playlist/5L6Q87DlqK5RXAmVMwTWVY?si=kPWDuZ1PTMidoLKvwXa38Q")

def open_google(query=None):
    if query:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        speak(f"Searching Google for: '{query}', Sir...", delay=0.4)
        time.sleep(0.3)
        open_chrome(url)
    else:
        open_chrome("https://www.google.com")

def show_help():
    time.sleep(0.3)
    print("""
╔══════════════════════════════════════════╗
║         🤖 JARVIS - COMMAND CENTER      ║
╠══════════════════════════════════════════╣
║  chrome          → Launch Chrome        ║
║  camera          → Activate Camera      ║
║  youtube         → Open YouTube         ║
║  google <query>  → Search on Google     ║
║  ZeroDayX        → 🔐 Classified 🎵    ║
║  help            → Display this menu    ║
║  exit / quit     → Shutdown Jarvis      ║
╚══════════════════════════════════════════╝
""")

def process_command(cmd):
    cmd_original = cmd.strip()
    cmd = cmd_original.lower()

    if not cmd:
        return

    # 🔐 Secret codeword — ZeroDayX (case insensitive)
    if cmd == "zerodayx":
        open_zerodayx()
        return

    if cmd in ["exit", "quit", "bye", "shutdown"]:
        speak("Understood, Sir. Shutting down all systems. Goodbye. 👋", delay=0.4)
        time.sleep(0.5)
        sys.exit(0)

    elif cmd in ["chrome", "browser", "internet"]:
        open_chrome()

    elif cmd in ["camera", "cam", "webcam"]:
        open_camera()

    elif cmd in ["youtube", "yt"]:
        open_youtube()

    elif cmd.startswith("google "):
        query = cmd[7:]
        open_google(query)

    elif cmd in ["help", "commands"]:
        show_help()

    else:
        speak(f"Command not recognized: '{cmd_original}'. Type 'help' to view available commands, Sir.")

def main():
    os.system("cls" if sys.platform == "win32" else "clear")
    time.sleep(0.3)
    print("""
╔══════════════════════════════════════════╗
║   🤖  J.A.R.V.I.S  — by Goldy Bhai     ║
║   Just A Rather Very Intelligent System  ║
╚══════════════════════════════════════════╝
""")
    time.sleep(0.5)
    speak("All systems online. Good to see you, Sir.", delay=0.4)
    time.sleep(0.3)
    speak("Type 'help' to view available commands.")
    print()

    while True:
        try:
            user_input = input("\n🎤 You: ").strip()
            process_command(user_input)
        except KeyboardInterrupt:
            speak("\nEmergency shutdown initiated. Goodbye, Sir. 👋", delay=0.3)
            sys.exit(0)

if __name__ == "__main__":
    main()