# Pokémon Capstone
<h2> What this project is for </h2>
<p> This application is a Django database, that uses Django's REST package to make an API. the API will use server side rendering to gather input from a user and make API calls and request such as GET, POST, and etc. This API will be for a shoe store demo, the users will be able to make API calls to view and render specific shoes, with information regarding them.
<h2> Dependencies required for this project </h2>
<ul>
  <li>Python 3.8.2</li>
  <li>Poetry</li>
  <li>Linux-based or Mac operating system</li>
  <li>Bash or Zsh shell</li>
  </ul>
<h2> Installation </h2>
<ul>
<p><li>If you're running Windows 10, <a href="https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/">here</a> is a tutorial on how to get a bash terminal running on Windows.</li><p/>
<p><li><a href="https://www.geeksforgeeks.org/how-to-download-and-install-python-latest-version-on-linux/">Here</a> is a guide on how to install the latest version of Python on Linux, and <a href="https://blog.adafruit.com/2020/05/29/installing-the-latest-version-of-python-on-mac-os-catalina-python-mac-apple-catalina-letsbsocial1/">click here</a> for Mac.
  </li>
</p>
  <p><li><a href="https://pypi.org/project/poetry/">How to install Poetry with pip package manager.</a></li></p>
  </ul>
  <p> Now that everything is set up, you can move onto running this project on your machine</p>
  <h2> Set-Up </h2>
  <ol>
  <li> Fork and clone the repo.</li>
  <li> cd into your new directory, and run the command <code>poetry install</code>. This is going to install all of the dependecies required for the project.</li>
  <li> now run <code>poetry shell</code>. This will create a virtual enviornment for your terminal. From here you can run commands off of a file called manage.py. This file holds all of the information for things such as running a server. </li>
  <li>In order to populate database with pokemon data run this command

  <code> python manage.py bootstrap_data</code></li>
  <li> you can run the command <code> python manage.py runserver</code> to run the server.
    <li> Open up the server in the browser, it will be running on localhost port 8000.
  </li>
  </ol>

## REFERENCES:

### Django

https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a

 https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0#:~:text=To%20save%20passwords%20and%20secret,Setting%20click%20on%20Environment%20Variables%20


### React

https://stackoverflow.com/questions/948532/how-do-you-convert-a-javascript-date-to-utc

https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a

# README created by Team Aquamarine.

## Disclaimer
All Pokemon and pokemon related content is property of Pokemon and Nintendo. We do not own any of it, and this is a fan made project.
