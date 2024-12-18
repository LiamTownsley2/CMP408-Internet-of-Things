import curses
from time import sleep
from Util.general import log_queue


def view_rfid_logs(stdscr):
    return curses.wrapper(_generate_page, stdscr)


def _generate_page(stdscr):
    global log_queue
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()

    stdscr.addstr(0, 0, "Log Viewer (Press 'q' to quit):")

    log_lines = []
    while True:
        try:
            key = stdscr.getkey()
            if key == "q":
                break
        except curses.error:
            pass

        while not log_queue.empty():
            log_lines.append(log_queue.get())

        log_lines = log_lines[-20:]

        for idx, line in enumerate(log_lines, start=1):
            stdscr.addstr(idx, 0, line.strip())

        stdscr.refresh()
        sleep(0.1)
