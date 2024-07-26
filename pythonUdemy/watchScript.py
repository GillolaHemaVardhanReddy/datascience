import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = r"C:\Users\bittu\Desktop\datascience\pythonUdemy"  # Raw string for the directory path

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    last_modified = None

    @staticmethod
    def on_modified(event):
        if event.src_path.endswith(".py"):
            current_time = time.time()
            if Handler.last_modified is None or current_time - Handler.last_modified > 1:
                print(f"{event.src_path} has been modified")
                # Use quotation marks to handle spaces and special characters in the path
                os.system(f'python "{event.src_path}"')
                Handler.last_modified = current_time

if __name__ == '__main__':
    w = Watcher()
    w.run()
