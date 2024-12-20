import curses
import traceback
from queue import Queue
from time import sleep

log_queue = Queue()


def view_rfid_logs(stdscr):
    return curses.wrapper(_generate_page)


def _generate_page(stdscr):
    global log_queue
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()

    stdscr.addstr(0, 0, "Log Viewer (Press 'q' to quit):")

    log_lines = []
    while True:
        try:
            key = stdscr.getch()
            if key == ord("q"):
                return

            while not log_queue.empty():
                log_lines.append(log_queue.get())

            log_lines = log_lines[-20:]

            for idx, line in enumerate(log_lines, start=1):
                stdscr.addstr(idx, 0, line.strip())
            stdscr.refresh()
            sleep(0.1)
        except Exception:
            traceback.print_exc()
            sleep(10)
