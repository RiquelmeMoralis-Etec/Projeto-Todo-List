Os comandos a seguir serão utilizados pelo terminal presente no VS Code, garanta que esteja no local correto para executar os seguintes comandos.

Execute o seguinte comando antes de testar lembre-se de estar na dentro da pasta \FrontEnd no terminal antes de executar 
(utilize apenas se a pasta \node_modulos não estiver presente na pasta \FrontEnd).

```
npm install
```

Após isso execute o seguinte comando estando na pasta \FrontEnd (este comando executará o frontend do projeto).

```
npm run dev
```
Agora iremos instalar a máquina virtual venv, para isto estejá dentro da pasta \BackEnd
```
python -m venv venv
```

Para executar o backend esteja na pasta \BackEnd e entre na máquina virtual(o comando executará um ambiente virtual caso sejá necessário em sua máquina).
```
.venv\Scripts\activate
```

Após entrar na máquina virtual instale as dependências a seguir.
```
pip install flask_cors

pip install flask_session

pip install pymongo
```

Após esses comandos execute o comando a seguir (este comando irá executar o backend do projeto).

```
python.exe app.py
```

Detalhe, este projeto utiliza mongoDB como banco de dados.
