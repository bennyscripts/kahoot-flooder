import subprocess
import sys

class Notifier:
    def __init__(self):
        pass

    def send(self, title, text):
        if sys.platform == "win32":
            import win10toast
            toast = win10toast.ToastNotifier()
            toast.show_toast(title, text, duration=5)
        elif sys.platform == "linux":
            subprocess.Popen(["notify-send", title, text])
        elif sys.platform == "darwin":
            cmd = '''on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run'''
            subprocess.call(['osascript', '-e', cmd, title, text])