% rebase('layout.tpl', title='Entrar em Grupo')
<section class="form-section">
    <h1><i class="fas fa-users"></i> Entrar em um Grupo</h1>

    <form method="post" action="/rooms/join" class="form-container" onsubmit="join()">
        <div class="code-box">
            % for i in range(6):
                <input type="text"
                   maxlength="1"
                   class="code-input"
                   oninput="next(event, this, false)"
                   onkeydown="next(event, this, true)"
                   style="width:40px; height:40px; text-align:center; font-size:20px;"
                   required>
            % end

            <input type="hidden" name="room_id" id="room_id">

            <button type="submit" class="btn btn-submit"><i class="fas fa-arrow-right-to-bracket"></i> Entrar</button>
        </div>
    </form>
</section>