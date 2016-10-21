from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import Flask,request,abort,redirect,render_template,session,url_for,flash

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hsrd to guess string'

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name != None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))
    
#@app.route('/user/<name>',methods=['GET','POST'])
#def user(name):
    #name = None
    #form = NameForm ()
    #if form.validate_on_submit():
        #name = form.name.data
        #form.name.data = ''
    #return render_template('user.html',form=form,name=name)

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is %s' % user_agent

@app.route('/abor')
def abor():
    #специальный ответ для не удачи
    return abort(404)
    
@app.route('/VK')
def VK():
    #специальный ответ для перехода 
    return redirect('http://vk.com')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
    
@app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('500.html'),500
if __name__ == '__main__':
    app.run()