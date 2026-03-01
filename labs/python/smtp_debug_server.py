from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging
import signal

controller = Controller(Debugging(), hostname="127.0.0.1", port=1025)
controller.start()
print("SMTP Debug Server listening on 127.0.0.1:1025 (Ctrl+C to stop)")

try:
    signal.pause()
except KeyboardInterrupt:
    pass
finally:
    controller.stop()
