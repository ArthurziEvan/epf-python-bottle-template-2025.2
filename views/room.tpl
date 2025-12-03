% rebase('layout.tpl', title='Sala {{room.id}}')

% if room.sorted:

    <section class="container room-details">
        <h2><i class="fas fa-gift"></i> Seu Amigo Oculto: </h2>
        <h1>{{users[room.chosen[str(user.id)]]}}</h1>

        % if user.id == room.host_id:
            <a href="/rooms/email/{{room.id}}" class="btn btn-primary"><i class="fas fa-envelope"></i> Mandar Resultados por Email</a>
        % end
    </section>

% else:

    <section class="container room-details">
        <h1><i class="fas fa-gift"></i> Detalhes do Grupo: {{room.name}}</h1>

        <p><strong>ID:</strong> {{room.id}}</p>
        <p><strong>Dono (Host):</strong> {{room.host_name}}</p>
        <p><strong>Status do Sorteio:</strong> **{{'Sorteado' if room.sorted else 'Pendente'}}**</p>

        <h2 style="margin-top: 20px;">Participantes ({{len(room.members)}})</h2>
        <ul>
            % for member_id in room.members:
                <li><strong>{{users[member_id]}}</strong></li>
            % end
        </ul>

        <div class="actions" style="justify-content: flex-start;">

            <a href="javascript:void(0)"onclick="copyPasta('{{room.id}}')"class="btn btn-edit"><i class="fas fa-user-plus"></i> Convidar ao Grupo</a>
            <p id="copy-message" style="display:none; color:green;"></p>
            <a href="/rooms" class="btn btn-cancel"><i class="fas fa-arrow-left"></i> Voltar para Grupos</a>
            % if user.id == room.host_id:
                <a href="/rooms/sort/{{room.id}}" class="btn btn-primary"><i class="fas fa-random"></i> Sortear</a>
            % end
        </div>
    </section>

% end