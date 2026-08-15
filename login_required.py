from functools import wraps
from flask import session, redirect

def login_required(f):
    # yes, @wraps is a decorator inside a decorator!
    # it preserves the original function's name, which Flask needs
    @wraps(f)
    # new function, wraps the original func so some code
    # can be executed before and / or after
    #args poand kwargs (key word arguments like dictionary)
    def decorated_function(*args, **kwargs):
        # code that runs BEFORE the original function
        # you can return early here to prevent it from running
        # call the original function and capture its return value
        if "user_id" not in session:
            return redirect("/sessions/new")
        return f(*args, **kwargs)
    return decorated_function