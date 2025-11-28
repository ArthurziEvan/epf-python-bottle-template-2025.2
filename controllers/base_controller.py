from bottle import static_file

from services.user_service import UserService


class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()
        self.user_service = UserService()


    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)


    def home_redirect(self):
        """Redireciona a rota raiz para /home"""
        return self.redirect('/home')


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        from bottle import template as render_template
        from bottle import request

        session = request.environ['beaker.session']

        logged_user = None

        if session and session.get('user_id'):
            user_id = session['user_id']
            logged_user = self.user_service.get_by_id(user_id)

        context['logged_user'] = logged_user

        return render_template(template, **context)


    def redirect(self, path, code=302):
        """Redirecionamento robusto com tratamento de erros"""
        from bottle import HTTPResponse, response as bottle_response

        try:
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            print(f"ERRO NO REDIRECT: {type(e).__name__} - {str(e)}")
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )
