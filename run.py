from bingewatch.app import app

#for heroku, might delete later if it doesn't work
server = app.server

if __name__ == '__main__':
   app.run_server(debug=True)

