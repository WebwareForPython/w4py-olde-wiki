from SitePage import *
from WebKit.HTTPExceptions import *

def d(**kw): return kw

class login(SitePage):

    def setup(self):
        self._formErrors = {}
        if (self.user()
            and self.request().field('_actionLoginUsername_', False)):
            returnTo = self.request().field('returnTo', '')
            self.sendRedirectAndEnd(returnTo
                                    or self.request().adapterName())

    def pageClass(self):
        return 'none'

    def newUsers(self):
        return self.wiki.config.getbool('newusers', True)

    def actions(self):
        if self.newUsers():
            return ['create']
        else:
            return []

    def title(self):
        if self.view() == 'writeCreateForm':
            return 'Create User Account'
        elif self.view() == 'writeSuccess':
            return 'User Created'
        else:
            return 'Login'

    def create(self):
        self.setView('writeCreateForm')
        req = self.request()
        if not req.field('save', ''):
            return
        username = req.field('username', '')
        name = req.field('name', '')
        email = req.field('email', '')
        website = req.field('website', '')
        if not website.startswith('http'):
            website = 'http://' + website
        password = req.field('password')
        errors = self._formErrors
        if not username:
            errors['username'] = 'Username is required'
        elif self.userManager().userExists(username):
            errors['username'] = 'That username is taken'
        if not name:
            errors['name'] = 'Your name is required'
        if not email:
            errors['email'] = 'Your email address is required'
        if not password:
            errors['password'] = 'Please enter a password'
        if password != req.field('confirm_password', ''):
            errors['password'] = 'Your password does not match your confirmation'
        if errors:
            self.writeHTML()
            return
        user = self.userManager().newUser()
        user.setUsername(username)
        user.setEmail(email)
        user.setWebsite(website)
        user.setPassword(password)
        user.setName(name)
        self.setUser(user)
        self.message('User %s created' % username)
        returnTo = req.field('returnTo', '')
        if returnTo:
            self.sendRedirectAndEnd(returnTo)
        else:
            self.setView('writeSuccess')
        self.writeHTML()

    def writeContent(self):
        self.write(self.simpleLoginForm())
        self.write('<p><a href="%s">Forgot your password?</a></p>\n' %
                   self.servletLink('forgotten'))
        if self.newUsers():
            self.write('<h2>Or create a new user account...</h2>\n')
            self.writeCreateForm(self.linkToSelf())

    def writeSuccess(self):
        self.write('User created!')
        
    def writeCreateForm(self, returnTo=''):
        values = {}
        values['action'] = self.servletLink('login')
        for key in 'username name email website password confirm_password returnTo'.split():
            values[key] = self.htmlEncode(self.request().field(key, ''))
            if self._formErrors.has_key(key):
                values['error_%s' % key] = '<span class="formError">%s</span><br>\n' % self._formErrors[key]
            else:
                values['error_%s' % key] = ''
        if returnTo:
            values['returnTo'] = self.htmlEncode(returnTo)

        self.write('''
        <form action="%(action)s" method="POST">
        <p>No email confirmation required; just fill in the values
        and go!</p>
        <input type="hidden" name="_action_" value="create">
        <input type="hidden" name="save" value="yes">
        <input type="hidden" name="returnTo" value="%(returnTo)s">
        <table class="loginForm">
        
        <tr>
        <td>Username:</td>
        <td>%(error_username)s
        <input type="text" name="username" value="%(username)s" size=30></td>
        </tr>

        <tr>
        <td>Full name:</td>
        <td>%(error_name)s
        <input type="text" name="name" value="%(name)s" size=40></td>
        </tr>

        <tr>
        <td>Email address:</td>
        <td>%(error_email)s
        <input type="text" name="email" value="%(email)s" size=40></td>
        </tr>

        <tr>
        <td>Website:</td>
        <td>%(error_website)s
        <input type="text" name="website" value="%(website)s" size=40></td>
        </tr>

        <tr>
        <td>Password:</td>
        <td>%(error_password)s
        <input type="password" name="password" value="%(password)s" size=20></td>
        </tr>

        <tr>
        <td>Confirm:</td>
        <td>%(error_confirm_password)s
        <input type="password" name="confirm_password" value="%(confirm_password)s" size=20></td>
        </tr>

        <tr>
        <td colspan=2 align=center>
        <input type="submit" value="Create user"></td>
        </tr>
        </table>
        '''
                   % values)
    
