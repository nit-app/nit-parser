import schedule
from parser.tg import run as tg
from parser.itevents import run as itevents
from parser.itc2go import run as itc2go


def run_parsers():
    print('start parsing tg')
    tg()
    print('start parsing itevents')
    itevents()
    print('start parsing itc2go')
    itc2go()


def schedule_parsers():
    schedule.every().day.at("02:00").do(run_parsers)


def main():
    print('start job')
    schedule_parsers()


if __name__ == '__main__':
    main()
