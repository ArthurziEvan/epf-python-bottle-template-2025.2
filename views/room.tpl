% rebase('layout.tpl', title='Sala {{room.id}}')

<section class="container room-details">
    <h1><i class="fas fa-gift"></i> Detalhes do Grupo: {{room.name}}</h1>

    <p><strong>ID:</strong> {{room.id}}</p>
    <p><strong>Dono (Host ID):</strong> {{room.host_id}}</p>
    <p><strong>Status do Sorteio:</strong> {{'Sorteado' if room.sorted else 'Pendente'}}</p>

    <h2 style="margin-top: 20px;">Participantes ({{len(room.members)}})</h2>
    <ul>
        % for member_id in room.members:
            <li>Usuário ID: {{member_id}}</li>
        % end
    </ul>
    
    <div class="actions" style="justify-content: flex-start;">
        
        <a href="/rooms/{{room.id}}/add_member" class="btn btn-edit"><i class="fas fa-user-plus"></i> Adicionar Participante</a>

        <a href="/rooms" class="btn btn-cancel"><i class="fas fa-arrow-left"></i> Voltar para Grupos</a>
        
        <a href="/rooms/{{room.id}}/sort" class="btn btn-primary"><i class="fas fa-random"></i> Realizar Sorteio</a>
    </div>
</section>