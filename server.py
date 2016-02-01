from flask import Flask, request
from random import choice, randint


COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]
DISSES = ["slimey", "a ferret", "curdled", "goop"]

app = Flask(__name__)


@app.route('/')
def index():
    # return "<html><body><h1>I am the landing page</h1></body></html>"
    # To escape string, can do:
    # return "<html><body><a href=\"/hello\"><h1>I am the landing page</h1></a></body></html>"
    # Or:
    return "<html><body><a href='/hello'><h1>I am the landing page</h1></a></body></html>"


@app.route('/hello')
def say_hello():
    # return "Hello!"
    # dropdown and radio button
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Hello!</title>
      </head>
      <body>
        <h1>Hello, </h1>
        <form action="/greet">
          <select name="person">>
            <option value="Smartie" name="person">Smartie</option>
            <option value="Clever Girl">Clever Girl</option>
            <option value="Tenacious One">Tenacious One</option>
            <option value="Awesome">Awesome</option>
            <option value="Pythonic person">Pythonic person</option>
          </select>
          <input type="submit">
        </form>

        <form action="/greet">
          <input type="radio" name="person" value="Smartie"> Smartie <br>
          <input type="radio" name="person" value="Clever Girl"> Clever <br>
          <input type="radio" name="person" value="Tenacious One"> Tenacious One <br>
          <input type="radio" name="person" value="Awesome"> Awesome <br>
          <input type="radio" name="person" value="Pythonic Person"> Pythonic Person <br>
        </ul>
        <input type="submit">
        </form>

        <label for="diss">To be dissed:</label>
        <form action="/diss" id="diss">
          <select name="person">
            <option value="Smartie" name="person">Smartie</option>
            <option value="Clever Girl">Clever Girl</option>
            <option value="Tenacious One">Tenacious One</option>
            <option value="Awesome">Awesome</option>
            <option value="Pythonic person">Pythonic person</option>
          </select>
          <input type="submit">
        </form>
      </body>
    </html>
    """

@app.route('/lucky')
def lucky_number():
    lucky_num = randint(1, 10)
    lucky_message = "Your lucky number is %d" % (lucky_num)
    return "<html><body><h1>%s</h1></body></html>" % (lucky_message)


@app.route('/form')
def show_form():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name?
          <input type="text" name="person">
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def offer_greeting():
    player = request.args.get("person")
    nice_thing = choice(COMPLIMENTS)
    # print x
    return """
      <!DOCTYPE html>
      <html>
        <head>
          <title>A Compliment</title>
        </head>
        <body>
          Hi %s, I think you're %s!
        </body>
      </html>
      """ % (player, nice_thing)

@app.route('/diss')
def offer_dissing():
  player = request.args.get("person")
  mean_thing = choice(DISSES)

  return """
        <!DOCTYPE html>
      <html>
        <head>
          <title>A Compliment</title>
        </head>
        <body>
          Hi %s, I don't want to be mean but the example wants me to diss you, so I think you're %s!
        </body>
      </html>
      """ % (player, mean_thing)

if __name__ == "__main__":
  app.run(debug=True)
    # app.run(debug=False)
