from app import app

@app.route('/')
def homePage():
    return {
        'test': 'hi'
    }


@app.route('/contact')
def contactPage():
    return {
        'yo' : [
            'shoha', 'brandt', 'aubrey'
        ]
    }


