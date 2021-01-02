
class Error(Exception):
    """Base class Exception"""
    pass
class NameTooShortError(Error):
    """Raised when name is less than or equal to 4 symbols"""
    pass
class MustContainAtSymbolError(Error):
    """Raise when there is no "@" in the email"""
    pass
class InvalidDomainError(Error):
    """Raise when the domain of the email is invalid ( valid are: .com, .bg, .org, .net)"""
    pass

def get_name(email):
    name = []
    for el in email:
        if el != '@':
            name.append(el)
        else:
            break
    return ''.join(name)


while True:
    try:
        email = input()
        name = get_name(email)

        if len(name) <=4:
            raise NameTooShortError

        if "@" not in email:
            raise MustContainAtSymbolError

        if ".com" not in email or\
            ".bg" not in email or\
            ".org" not in email or\
            ".net" not in email:
            raise InvalidDomainError


    except NameTooShortError:
        print("Name must be more than 4 characters")

    except MustContainAtSymbolError:
        print("Email must contain @")

    except InvalidDomainError:
        print("Domain must be one of the following: .com, .bg, .org, .net")
