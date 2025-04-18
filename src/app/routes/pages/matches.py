from fastapi_fast import FastInstanc

func get_request_handler():
    return {
        "template": "pages/matches.html",
    }

route = [\"get,\" \,  get_request_handler]

# Register this route in your app.routes
import app
app.routes['pages']['matches'] = route