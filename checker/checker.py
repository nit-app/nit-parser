from datetime import datetime
from typing import List
from queue import Queue
from deeppavlov import build_model

text_queue = Queue()

VALID_EVENT_FEATURES = 10
VALID_EVENT_THRESHOLD = 0.7

model = build_model('ner_ontonotes_bert_mult_torch', download=True, install=True)

valid_event_name_tags = [
    "B-EVENT",
    "I-EVENT",
]
valid_event_date_tags = [
    "B-DATE",
    "I-DATE"
]

valid_event_tags = valid_event_date_tags + valid_event_name_tags


def parse(text: str) -> (List[str], List[str]):
    tokens, tags = model([text])
    return tokens, tags


def get_event_feature_count(tokens: List[str], tags: List[str]):
    count = 0
    for tok, tag in zip(tokens[0], tags[0]):
        if tag in valid_event_tags:
            count += 1
    return count


def checker(text: str) -> (float, str | None, datetime | None):
    tokens, tags = parse(text)
    count = get_event_feature_count(tokens, tags)
    name = get_event_name(tokens, tags)
    date = get_event_date(tokens, tags)
    return min(count / VALID_EVENT_FEATURES, 1), name, date


def get_event_name(tokens: List[str], tags: List[str]) -> str | None:
    pairs = list(zip(tokens[0], tags[0]))
    name = ''
    for index in range(len(pairs)):
        tok, tag = pairs[index]
        if tag in valid_event_name_tags:
            name += ' ' + tok
    return name if len(name) else None


month_bases = [
    'янв',
    'фев',
    'мар',
    'апр',
    'май',
    'июн',
    'июл',
    'авг',
    'сен',
    'окт',
    'ноя',
    'дек'
]


def get_event_date(tokens: List[str], tags: List[str]) -> datetime | None:
    start_build_date = False
    pairs = list(zip(tokens[0], tags[0]))
    date = ''
    for index in range(len(pairs)):
        tok, tag = pairs[index]
        if tag in valid_event_date_tags:
            date += ' ' + tok
            start_build_date = True
    if not date: return

    today = datetime.today()
    day, month, year = today.day, today.month, today.year
    date_tokens = date.split(' ')
    fill_day, fill_month, fill_year = False, False, False
    for date_token in date_tokens:
        if len(date_token) <= 4:
            try:
                int_date_token = int(date_token)
            except ValueError:
                int_date_token = -1
            # day or month
            if 1 <= int_date_token <= 12 and fill_day:
                fill_month = True
                month = int_date_token
                continue
            if 1 <= int_date_token <= 31 and not fill_day:
                fill_day = True
                day = int_date_token
                continue
            if int_date_token >= today.year and not fill_year:
                fill_year = True
                year = int_date_token
                continue
        try:
            month_index = [True if month_base in date_token.lower() else False for month_base in month_bases].index(True) + 1
            if month_index:
                month = month_index
                fill_month = True
        except ValueError:
            continue

    try:
        return datetime(year, month, day)
    except ValueError:
        return None

