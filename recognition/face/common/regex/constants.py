class Phone:
    RE = r'^\+?1?\d{9,15}$'
    EXCEPTION_MESSAGE = 'Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'


class StudentCard:
    RE = r'[A-Z]{2} №[0-9]{8}'
    EXCEPTION_MESSAGE = 'Student card must be entered in format: "BB №11111111".'
