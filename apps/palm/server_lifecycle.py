from threading import Thread
import receiver


def on_server_loaded(_server_context):
    # Block the stream connection
    pass
    # t = Thread(target=receiver.stream_receive, daemon=True)
    # t.start()
