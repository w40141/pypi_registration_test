class Gender():

    def __init__(self, gender):
        self.genter = self._change(gender)

    def _change(self, flag):
        if isinstance(flag, bool):
            return self._change_bool(flag)
        elif isinstance(flag, str):
            return self._change_str(flag)
        else:
            raise TypeError('error')

    def _change_bool(self, flag):
        if flag:
            return 'Male'
        else:
            return 'Female'

    def _change_str(self, letter):
        letter = letter.lower()
        if letter == 'm':
            return 'Male'
        elif letter == 'f':
            return 'Female'
        else:
            raise ValueError('error')
