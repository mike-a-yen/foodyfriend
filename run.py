from app import app
import os

PORT = int(os.environ['PORT'])
app.run(port=PORT,debug=True)
