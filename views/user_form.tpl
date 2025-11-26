% rebase('layout.tpl', title='Formulário Usuário') 
<section class="form-section">
    <h1><i class="fas fa-user-plus"></i> {{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required 
                   value="{{user.name if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required 
                   value="{{user.email if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" 
                   value="{{user.password if user else ''}}" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn btn-submit"><i class="fas fa-save"></i> Salvar</button>
            <a href="/users" class="btn btn-cancel"><i class="fas fa-times-circle"></i> Voltar</a>
        </div>
    </form>
</section>