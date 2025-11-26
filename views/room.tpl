% rebase('layout.tpl', title='Sala {{room.id}}')

<h1>Room: {{room.name}}</h1>

<p><strong>ID:</strong> {{room.id}}</p>
<p><strong>Host:</strong> {{room.host_id}}</p>

<a href="/rooms">Voltar</a>