<form action="{{action}}" method="post" class="form-container">
    
    <div class="form-group">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name" required 
            value="{{user.name if defined('user') and 'id' in user else (user.get('name') if defined('user') and user and hasattr(user, 'get') else '')}}">
    </div>
    
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required 
            value="{{user.email if defined('user') and 'id' in user else (user.get('email') if defined('user') and user and hasattr(user, 'get') else '')}}">
    </div>
    
    <div class="form-group">
        <label for="password">Senha: {{'(Mantenha em branco para não alterar)' if defined('user') and user and user.id else ''}}</label>
        <input type="password" id="password" name="password" 
                   placeholder="{{'Deixe em branco para manter a senha atual' if defined('user') and user and user.id else ''}}"
                   required="{{'' if defined('user') and user and user.id else 'required'}}">
    </div>
    
    <div class="form-actions">
        <button type="submit" class="btn btn-submit"><i class="fas fa-save"></i> {{'Atualizar' if defined('user') and user and user.id else 'Salvar'}}</button>
        
        <a href="/users" class="btn btn-cancel"><i class="fas fa-times-circle"></i> Voltar</a>
    </div>
</form>