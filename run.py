from market import app
import os
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 5000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
