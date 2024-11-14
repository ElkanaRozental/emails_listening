from typing import List


def is_contain_hostage(email: dict):
    return any("hostage" in sentence for sentence in email['sentences'])


def is_contain_explosive(email: dict):
    return any("explos" in sentence for sentence in email['sentences'])


def check_suspect_email(email: dict):
    if map(lambda sentence: sentence.str.contains('hostage'), email['sentences']):
        return 'hostage'
    if map(lambda sentence: sentence.str.contains('explos'), email['sentences']):
        return 'explosive'
    else:
        return 'clear'


def change_sentence_index(email: dict):
    sentences: List[str] = email['sentences']
    sentences = sorted(sentences, key=lambda sentence: 'hostage' in sentence or 'explos' in sentence, reverse=True)
    email['sentences'] = sentences
    return email