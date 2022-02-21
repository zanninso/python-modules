import re

from numpy import isin


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        if (isinstance(account, Account)):
            self.account.append(account)
            # print(dir(account))
        return self

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if (amount < 0):
            return False
        origin = self.get_account(origin)
        dest = self.get_account(dest)
        if (origin is None or dest is None):
            return False
        if (self.__account_corupted(origin) or self.__account_corupted(dest)):
            return False
        if (origin.value < amount):
            return False

        origin.value -= amount
        dest.value += amount
        return True

    def get_account(self, key):
        if (isinstance(key, int)):
            for elm in self.account:
                if (elm.id == key):
                    return elm
        elif (isinstance(key, str)):
            for elm in self.account:
                if (elm.name == key):
                    return elm
        return None

    def __account_corupted(self, account):
        acc_m = dir(account)
        if (len(acc_m) % 2 == 0):
            return True

        if len([n for n in acc_m if re.match('^b', n)]) > 0:
            return True

        if len([n for n in acc_m if re.match('^(zip|addr)', n)]) == 0:
            return True

        if 'name' not in acc_m or 'id' not in acc_m or 'value' not in acc_m:
            return True

        return False

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
        """
        account = self.get_account(account)
        if (account is None):
            return

        acc_m = dir(account)

        for key in acc_m:
            if (key.startswith('b')):
                del account.__dict__[key]

        zip = [n for n in acc_m if re.match('^(zip|addr)', n)]
        if len(zip) == 0:
            account.__dict__['zip'] = ''
        if len(zip) == 2:
            del account.__dict__['addr']

        if 'name' not in acc_m:
            account.__dict__['name'] = 'temp'

        if 'id' not in acc_m:
            account.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1

        if 'value' not in acc_m:
            account.__dict__['value'] = 0

        if (len(dir(account)) % 2 == 0):
            account_attr = ['zip', 'addr', 'name', 'id', 'ID_COUNT', 'value']
            for key in account.__dict__:
                if (key not in account_attr):
                    del account.__dict__[key]
                    return
