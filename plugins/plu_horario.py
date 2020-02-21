#
# Copyright (c) 2020 Murilo Ijanc' <mbsd@m0x.ru>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import re
import urllib.request

# URL horários
URL = 'https://www.invertexto.com/horariosengenharia'
# timeout do request
TIMEOUT = 5
# user agent
USER_AGENT = 'Dolores request/0.1'
# regex para pegar o conteúdo da textarea
REGEX_TEXTAREA = r'<textarea.*">(.*)<\/textarea>'


def get_content():
    """Função para obter o conteúdo da página."""
    req = urllib.request.Request(URL)
    req.add_header('User-Agent', USER_AGENT)
    r = urllib.request.urlopen(req, timeout=TIMEOUT)
    if r.status != 200:
        print("Falha na conexão: %s", r.reason)
        return None
    content = r.read().decode('utf-8')
    # replace all new lines to <br>
    content = content.replace('\n', '<br>')
    content = re.findall(REGEX_TEXTAREA, content)
    if len(content) == 0:
        print("Não foi encontrado nenhum conteúdo.")
        return None
    # replace all &agrave;s to -
    content = content[0].replace('&agrave;s', '-')
    return content


def get_horarios(update, content):
    """Função que retorna os horários das aulas."""
    text = ""
    content = None
    content = get_content()
    # caso nao retorne nada
    if content is None:
        update.message_reply_text('Op\'s, falha ao consegui os horários.')
    num_max_horarios = len(content.split('<br><br>')) - 1
    # iteramos sobre as "linhas"
    for num, horario in enumerate(content.split('<br><br>')):
        # troco <br> por \n
        t = horario.replace('<br>', '\n')
        text += t
        if num != num_max_horarios:
            text += '\n\n'
    # enviamos o texto
    update.message.reply_text(text)


if __name__ == '__main__':
    get_horarios(None, None)
