import requests
from adal.adal_error import AdalError
from azure.cli.core._profile import Profile
from adal.adal_error import AdalError
from azure.cli.core.prompting import prompt_pass, NoTTYException
import azure.cli.core.azlogging as azlogging

from azure.cli.core._util import CLIError
def login(username, password, service_principal, tenant):
    """Log in to access Azure subscriptions"""
    interactive = False
    profile = Profile()
    try:
        subscriptions = profile.find_subscriptions_on_login(
            interactive,
            username,
            password,
            service_principal,
            tenant)
    except AdalError as err:
        # try polish unfriendly server errors
        msg = str(err)
        suggestion = "For cross-check, try 'az login' to authenticate through browser."
        if ('ID3242:' in msg) or ('Server returned an unknown AccountType' in msg):
            raise CLIError("The user name might be invalid. " + suggestion)
        if 'Server returned error in RSTR - ErrorCode' in msg:
            raise CLIError("Logging in through command line is not supported. " + suggestion)
        raise CLIError(err)
    except requests.exceptions.ConnectionError as err:
        raise CLIError('Please ensure you have network connection. Error detail: ' + str(err))
    all_subscriptions = list(subscriptions)
    for sub in all_subscriptions:
        sub['cloudName'] = sub.pop('environmentName', None)
    return all_subscriptions