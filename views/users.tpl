% rebase('layout.tpl', title='Usuários')
<section class="container users-section">
    <div class="section-header">
        <h1 class="section-title"><i class="fas fa-users"></i> Gestão de Usuários</h1>
        <a href="/register" class="btn btn-primary">
            <i class="fas fa-plus"></i> Novo Usuário
        </a>
    </div>

    <div class="table-container">
        <table class="styled-table">
            
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                % for u in users:
                <tr>
                    <td>{{u.id}}</td>
                    <td>{{u.name}}</td>
                    <td>{{u.email}}</td>
                    <td class="actions">
                        <a href="/users/edit/{{u.id}}" class="btn btn-sm btn-edit"><i class="fas fa-edit"></i> Editar</a>
                        
                        <form action="/users/delete/{{u.id}}" method="post" onsubmit="return confirm('Tem certeza que deseja deletar o usuário {{u.name}}?')">
                            <button type="submit" class="btn btn-sm btn-danger"><i class="fas fa-trash-alt"></i> Excluir</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</section>