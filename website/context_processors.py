import datetime
def add_variable_to_context(request):
    return {
        'year': datetime.datetime.now().year
    }