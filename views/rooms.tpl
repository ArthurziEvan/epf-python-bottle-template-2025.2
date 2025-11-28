% rebase('layout.tpl', title='Grupos')

<section class="container">
    <div class="section-header">
        <h1><i class="fas fa-users"></i> Gestão de Grupos</h1>
    </div>

    <div class="actions" style="justify-content: flex-end; margin-bottom: 20px">
        <a class="btn btn-primary" href="/rooms/add"><i class="fas fa-plus"></i> Criar Grupo</a>
        <a class="btn btn-edit" href="/rooms/join"><i class="fas fa-search"></i> Entrar em um Grupo</a>
        <br>
    </div>

    <div class="table-container">
        <table class="styled-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Dono (Host)</th>
                    <th><i class="fas fa-user-friends"></i> Participantes</th>
                    <th>Status</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % for room in rooms:
                <tr>
                    <td>{{room.id}}</td>
                    <td>{{room.name}}</td>
                    <td>{{room.host_name}}</td>
                    <td>{{len(room.members)}}</td>
                    <td>{{'Sorteado' if room.sorted else 'Pendente'}}</td>
                    <td class="actions">
                        <a href="/rooms/{{room.id}}" class="btn btn-sm btn-edit"><i class="fas fa-door-open"></i> Acessar</a>
                        % if user.id == room.host_id:
                            <form action="/rooms/delete/{{room.id}}" method="post" onsubmit="return confirm('Tem certeza que deseja deletar o grupo {{room.name}}?')">
                                <button type="submit" class="btn btn-sm btn-danger"><i class="fas fa-trash-alt"></i> Excluir</button>
                            </form>
                        % end
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>

    <div class="form-actions">
            <a href="/home" class="btn btn-cancel"><i class="fas fa-arrow-left"></i> Voltar</a>
    </div>
</section>