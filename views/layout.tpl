<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>

    <header class="main-header">
        <div class="container">
            <nav style="display: flex; justify-content: space-between; align-items: center;">
                <a href="/" style="color: white; text-decoration: none; font-size: 1.5em;">Amigo Oculto</a>
                <div>
                    <a href="/rooms" class="btn btn-sm btn-edit" style="color: black;">Salas</a>
                    <a href="/users" class="btn btn-sm btn-edit" style="color: black;">Usuários</a>
                </div>
            </nav>
        </div>
    </header>

    <div class="container">
        {{!base}}
    </div>

    <footer>
        </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>