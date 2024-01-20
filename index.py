#!/usr/bin/python3

from __future__ import print_function
import os
from os import path
import sys
# sys.stdout = open("/var/www/html/slamsim/debug.log", "a")  # Append to a log file
import html

# Get list of wrestler files in the wrestlers directory
wrestler_files = [
    f for f in os.listdir("/var/www/html/slamsim/wrestlers/") if path.splitext(f)[1] == ".py"
]
# ...

def application(environ, start_response):
    # Generate the wrestler options for the dropdown box
    wrestler_options = ""
    for wrestler_file in wrestler_files:
        wrestler_name = path.splitext(wrestler_file)[0]
        print("Debug - wrestler_name: ", wrestler_name)
        wrestler_options += f'\n<option value="{wrestler_file}">{html.escape(wrestler_name)}</option>'

    # Print the HTML content
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Wrestling Game</title>
    </head>
    <body>
        <h1>Wrestling Game</h1>
        <form action="runmatch.py" method="post">
            <label for="wrestler1">Wrestler 1:</label>
            <select id="wrestler1" name="wrestler1">
                {wrestler_options}
            </select>
            <br>
            <label for="wrestler2">Wrestler 2:</label>
            <select id="wrestler2" name="wrestler2">
                {wrestler_options}
            </select>
            <br>
            <label for="wrestler3">Wrestler 3:</label>
            <select id="wrestler3" name="wrestler3">
                <option value="none">None</option>
                {wrestler_options}
            </select>
            <br>
            <label for="wrestler4">Wrestler 4:</label>
            <select id="wrestler4" name="wrestler4">
                <option value="none">None</option>
                {wrestler_options}
            </select>
            <br>
            
            <input type="submit" value="Run Match">
        </form>
    </body>
    </html>
    """

    return [html_content.encode('utf-8')]
