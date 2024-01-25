🗓️ <h1>Django Agenda</h1>
Descrição

Esta aplicação Django foi desenvolvida para facilitar a administração de compromissos, permitindo o cadastro de eventos com informações detalhadas, como Título, Descrição, Data e Hora. A principal funcionalidade é a apresentação dos compromissos em um calendário anual/mensal, onde as datas contendo compromissos são exibidas como links. Ao clicar em uma data com compromisso, o usuário é redirecionado para uma página de detalhes específica desse compromisso.
Funcionalidades:
<ul>
<li><b>Cadastro de Compromissos:</b> Adicione facilmente seus compromissos, fornecendo informações essenciais como Título, Descrição, Data e Hora.</li>
<li><b>Visualização no Calendário:</b> Os compromissos são exibidos de forma intuitiva em um calendário anual/mensal, facilitando a identificação de datas ocupadas.</li>
<li><b>Detalhes do Compromisso:</b> Ao clicar em uma data com compromisso, você é redirecionado para uma página de detalhes que apresenta todas as informações cadastradas para aquele compromisso específico.</li>
<li><b>Pesquisa de Compromissos:</b> Utilize a função de pesquisa para encontrar rapidamente compromissos específicos com base em títulos, datas ou outras informações relevantes.</li></ul>

## Como Iniciar

# Requisitos:
* Certifique-se de ter o Python e o Django instalados em seu ambiente de desenvolvimento.

# Configuração do Ambiente Virtual:
* Recomenda-se criar e ativar um ambiente virtual para isolar as dependências do projeto. Você pode usar o seguinte comando para criar um ambiente virtual:
<table>
<tr>
<td>✅ python -m venv venv</td>
</tr>
</table>


## Instalação das Dependências:
* Instale as dependências do projeto usando o seguinte comando:
<table>
<tr>
<td>✅ pip install -r requirements.txt</td>
</tr>
</table>

# Migrações do Banco de Dados:
* Execute as migrações do banco de dados para criar as tabelas necessárias:
  
<table>
<tr>
<td>✅ python manage.py migrate</td>
</tr>
</table>

# Execução do Servidor:
* Crie os Usuarios como o comando:
  
<table>
<tr>
<td>✅ python manage.py createsuperuser</td>
</tr>
</table>

* Inicie o servidor de desenvolvimento Django:

<table>
<tr>
<td>✅ python manage.py runserver</td>
</tr>
</table>

# Acesso à Aplicação:
* Acesse a aplicação no navegador através do link http://localhost:8000/ e comece a administrar seus compromissos!

# Contribuições
* Contribuições são bem-vindas! Se você encontrar problemas, bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Licença
* Este projeto é distribuído sob a licença MIT.
