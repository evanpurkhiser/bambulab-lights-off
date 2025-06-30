from os import environ
import time
import bambulabs_api as bl
from bambulabs_api.states_info import GcodeState

finished_states = [
    GcodeState.IDLE,
    GcodeState.FINISH,
    GcodeState.FAILED,
]

if __name__ == "__main__":
    printer = bl.Printer(
        environ.get("PRINTER_IP"),
        environ.get("PRINTER_ACCESS_CODE"),
        environ.get("PRINTER_SERIAL"),
    )
    printer.connect()
    time.sleep(2)

    # Turn off light
    if printer.get_state() in finished_states:
        printer.turn_light_off()

    printer.disconnect()
