from AppOpener import run


def runner(app):
    if "youtube" in app:
        return -1
    list = run(app)
    if(list=='null'):
        return -1
    if(list!=None):
        run(list[0])
    

