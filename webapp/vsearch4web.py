"""This module provides a simple web application using the Flask web server.  It
   provides 5 endpoints by overriding the Flask.route function decorator


   This code uses jinja2 for its template language.  Flask renders template from
   one directory: ./templates/*.html.  Djabgo uses the DTL.  You can specify
   template locations using the Templates engines, configuring them with the
   TEMPLATES setting.

   ***NOTE: debug is enabled*** this allows automatic restarts on save


Available Functions:
   - do_search:     processes the '/search4' endpoint.  This simply provides default string
                    where the vowels of that string are returned
   - hello:         processes the '/hello' endpoint.  This simply provides default string to the
                    user
   - do_view_log:   Called directly by the user.  This method calls the read_log method from
                    the vsearchlog module. Passes that content, other data, and
                    'viewlog.html' to a flask template engine (which uses Jinja2 under the
                    hood).
   - do_view_unformatted_log:   Processes the '/viewunformattedlog' endpoint. Calls
                    read_unformatted_log in the vsearchlog module
   - do_search_web: processes the '/search4web' endpoint.  This is called from the do_entry
                    method.  It collects form data from the Flask request object, and uses
                    that data as input to the search4letters and reender_template functions.
                    The result from search4letters is also pased to the render_template.
   - do_entry:      processes the '/endtry' endpoint.  This endpoint renders the 'entry.html'
                    template.  The HTML takes input from the user and posts that to
                    '/search4web' endpoint

"""
from flask import Flask, render_template, request
from webapp.vsearch_local import search4letters
from webapp.vsearchlog import log_request, read_log, read_unformatted_log
from webapp.vsearchrep import save_request, get_log, total_number_of_requests, highest_letters_requested


app = Flask(__name__)


@app.route('/hello')
def hello() -> str:
    """processes the '/' endpoint.  Base method from root path to prove
       everything works out ok.

       Returns:
           Static string message 'Hello World from Flask!'
    """
    return "Hello World from Flask!"


@app.route('/search4')
def do_search() -> str:
    """Processes the '/search4' endpoint. Executes search4letters with
       defaulted input text of 'life, the universe, and everything in
       between'. The default search text is 'aeiou'.

       Returns:
           Static set of {'u', 'i', 'e', 'a'}
    """
    return str(search4letters('life, the universe, and everything in between'))


@app.route('/entry')
def do_entry() -> 'html':
    """Calls the 'entry.html' file in the template directory.  That file
       calls a POST to the '/search4web' endpoint."""
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/search4web', methods=['POST'])
def do_search_web() -> 'html':
    """Called from 'entry.html' this method calls the 'search4letters' and
       passes the correct result, and arguments to the 'results.html' file,
       a jinja2 template, rended by flaxk's render_template."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    the_results = str(search4letters(phrase, letters))
    log_request(request, the_results)
    save_request(request, the_results)
    template_input = dict(the_phrase=phrase
                          , the_letters=letters
                          , the_results=the_results
                          , the_title='Here are your results'
                          )
    return render_template('results.html', **template_input)


@app.route('/viewlog')
def do_view_log() -> 'html':
    """"Called directly by the user.  This method calls the read_log method
        from the vsearchlog module. Passes that content, other data, and
        'viewlog.html' to a flask template engine (which uses Jinja under
        the hood).

       Returns:
            'viewlog.html' with contents from logfile!!!
    """
    view_log_dict = dict(the_data=read_log()
                         , the_title='Current Log Data'
                         , the_row_titles=['Form Data'
                                           , 'Remote Addr'
                                           , 'User Agent'
                                           , 'Results'
                                           ]
                         )
    return render_template('viewlog.html', **view_log_dict)


@app.route('/dataoutput')
def do_get_data() -> 'html':
    """Process the  /dataoutput' endpoint. It retrieves data from MySql and
       populates the data in a html.

       Returns:
            'viewlog.html' with contents from database!!!
    """
    get_data_dict = dict(the_data=get_log()
                         , the_title='Current Database State'
                         , the_row_titles=['Phrase'
                                           , 'Letters'
                                           , 'Remote Addr'
                                           , 'User Agent'
                                           , 'Results'
                                           ]
                         )
    return render_template('viewlog.html', **get_data_dict)


@app.route('/stats')
def get_statistics() -> 'html':
    """Prints out the statistics that answer the questions:
            how many answered requests

       Returns:
            'stats.html'
    """
    stat_data_dic=dict(total_number_of_requests=total_number_of_requests()
                       ,most_selected_letters=highest_letters_requested())

    statistics_dict = dict(the_title='This is the statistics for the SEARCH4LOG webapp'
                           , table_header='Statistics'
                           , stat_data_dic=stat_data_dic.items())
    return render_template('stats.html', **statistics_dict)


@app.route('/viewunformattedlog')
def do_view_unformatted_log() -> str:
    """"Calls teh read_unformatted_log method from the vsearchlog module."""
    return read_unformatted_log()


if __name__ == '__main__':
    app.run(debug=True)
