from scripts.events.pub_sub_hub import Subscriber


class LoggingHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "logging_handler", event_hub)

    def run(self, event):
        # Note: Does not create a log entry. Doing so causes infinite loops. Don't do that.
        print(event.log_string)