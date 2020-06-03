import datetime
import time

class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(
            seconds=delay
        )

        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (event for event in self.events if event.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
                time.sleep(0.5)


def format_time(message, *args):
    now = datetime.datetime.now()
    print(f"{now:%I:%M:%S}: {message}")

def one(timer):
    format_time("Called one")

def two(timer):
    format_time("Called two")

def three(timer):
    format_time("Called three")    


class Repeater:
    def __init__(self):
        self.count = 0

    def __call__(self, timer):
        format_time(f"repeat {self.count}")
        self.count += 1
        timer.call_after(5, self)