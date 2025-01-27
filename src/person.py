class Person:

    def __init__(self, email_address):
        # I know there is a method called email() for fetching email_address but in case of python
        # it's a bit redundant and not really aligned with python philosophy, so I skipped it.
        self.email_address = email_address
