def check_suspect_email(email: dict):
    if map(lambda sentence: sentence.str.contains('hostage'), email['sentences']):
        return 'hostage'
    if map(lambda sentence: sentence.str.contains('explos'), email['sentences']):
        return 'explosive'
    else:
        return 'clear'
