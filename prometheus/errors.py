""" Module to setup error handler """


@app.errorhandler(404)
def not_found_error(error):
    """ 
    Display a specific webpage when page is not found

    Returns:
        str: Template for the error 
    """
    return render_template("errors/404.html")


@app.errorhandler(405)
def wrong_method_error(error):
    """405 error"""
    return render_template("errors/405.html")


@app.errorhandler(500)
def server_error(error):
    """500 error"""
    return render_template("errors/500.html")