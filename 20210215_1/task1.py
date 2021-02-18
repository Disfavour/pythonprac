import pyfiglet
import bottle


@bottle.get('/login')
def login():
    return bottle.template('''
        <form action="/login" method="post">
            <p>Text: <input name="string" type="text" /></p>
            
            <p>Style: <select name = "style">
            % for item in data:
            <option value={{item}}>{{item}}</option>
            % end
            </select></p>
            
            <p>Colour: <input type="color" name="colour" value="#ff0000" /></p>
            
            <p><input type="submit" value="Submit"></p>
        </form>
    ''', data=pyfiglet.FigletFont.getFonts())


@bottle.post('/login')
def do_login():
    string = bottle.request.forms.get('string')
    style = bottle.request.forms.get('style')
    colour = bottle.request.forms.get('colour')
    print(colour)
    f = pyfiglet.Figlet(font=style)
    text = f.renderText(string)
    return bottle.template('<pre style="color:{{color}}">{{text}}</pre>', text=text, color=colour)


bottle.run(host='localhost', port=8080)

# http://localhost:8080/login
