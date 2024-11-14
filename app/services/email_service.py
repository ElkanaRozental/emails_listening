from typing import List


def check_suspect_email(email: dict):
    if map(lambda sentence: sentence.str.contains('hostage'), email['sentences']):
        return 'hostage'
    if map(lambda sentence: sentence.str.contains('explos'), email['sentences']):
        return 'explosive'
    else:
        return 'clear'


def change_sentence_index(email: dict):
    sentences: List[str] = email['sentences']
    sentence_to_move = filter(
        lambda sentence: sentence.str.contains('hostage') or
        sentence.str.contains('explos'),
        sentences
    )
    sentences.remove(sentence_to_move)
    sentences.insert(0, sentence_to_move)
    email['sentences'] = sentences
    return email
