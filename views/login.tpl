% rebase('layout.tpl', title='Login')
<section class="form-section">
    <h1><i class="fas fa-sign-in-alt"></i> Login</h1>
    
    % if defined('login_error') and login_error:
        <div class="alert alert-danger" role="alert" style="max-width: 450px; margin: 0 auto 20px;">
            <i class="fas fa-exclamation-circle"></i> {{login_error}}
        </div>
    % end

    <form action="/login" method="post" class="form-container">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required
                       value="{{user_data.get('email') if defined('user_data') and user_data else ''}}">
        </div>

        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn btn-submit"><i class="fas fa-sign-in-alt"></i> Entrar</button>
            <a href="/" class="btn btn-cancel"><i class="fas fa-times-circle"></i> Cancelar</a>
        </div>
    </form>
    <p style="text-align: center; margin-top: 20px;">
        Não tem uma conta? <a href="/register" class="login-link">Cadastre-se aqui</a>.
    </p>
</section>