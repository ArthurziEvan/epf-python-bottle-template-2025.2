% rebase('layout.tpl', title='Grupos')

<header>
    <h1>Grupos</h1>
    <a class="btn primary" href="/rooms/add">Criar Grupo</a>
</header>

<main class="container">
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Dono</th>
                <th>Participantes</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for room in rooms:
            <tr>
                <td>{{room.id}}</td>
                <td>{{room.name}}</td>
                <td>{{room.host_id}}</td>
                <td>{{len(room.members)}}</td>
                <td>
                    <a href="/rooms/{{room.id}}">Acessar</a> |
                    <a href="/rooms/{{room.id}}/edit">Editar</a> |
                    <a href="/rooms/{{room.id}}/delete">Deletar</a>
                </td>
            </tr>
            % end
        </tbody>
    </table>
</main>