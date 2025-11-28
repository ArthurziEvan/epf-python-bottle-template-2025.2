<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amigo Oculto - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>

    <header class="main-header">
        <div class="container">
            <nav style="display: flex; justify-content: space-between; align-items: center;">
                <a href="/" style="color: white; text-decoration: none; font-size: 1.5em; font-weight: bold;">Amigo Oculto</a>
                <div>
                    % if defined('user_login') and user_login:
                        <span style="color: white; margin-right: 15px;">
                            Olá, <strong>{{user_login.name}}</strong>
                        </span>
                        <a href="/rooms" class="btn btn-sm btn-edit" style="color: black;"><i class="fas fa-users"></i> Salas</a>
                        <a href="/logout" class="btn btn-sm btn-danger"><i class="fas fa-sign-out-alt"></i> Sair</a>
                    % else:
                        <a href="/rooms" class="btn btn-sm btn-edit" style="color: black;"><i class="fas fa-users"></i> Salas</a>
                        <a href="/login" class="btn btn-sm btn-edit" style="color: black;"><i class="fas fa-sign-in-alt"></i> Login</a>
                        <a href="/register" class="btn btn-sm btn-primary"><i class="fas fa-user-plus"></i> Cadastro</a>
                    % end
                </div>
            </nav>
        </div>
    </header>

    <div class="container">
        % if defined('success_message') and success_message:
            <div class="alert alert-success" role="alert"><i class="fas fa-check-circle"></i> {{success_message}}</div>
        % end
        
        % if defined('error_message') and error_message:
            <div class="alert alert-danger" role="alert"><i class="fas fa-exclamation-triangle"></i> {{error_message}}</div>
        % end
        
        % if defined('info_message') and info_message:
            <div class="alert alert-info" role="alert"><i class="fas fa-info-circle"></i> {{info_message}}</div>
        % end

        {{!base}}
    </div>

    <footer>
        </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>
