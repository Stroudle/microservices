# Microsserviço REST - FastAPI

Este projeto é um microsserviço simples para manipulação de contatos, desenvolvido em Python utilizando FastAPI. Ele permite cadastrar, consultar e listar contatos, armazenando os dados em memória.

---

## Funcionalidades

- **Cadastrar contato**: Adiciona um novo contato.
- **Consultar contato**: Busca um contato pelo nome.
- **Listar contatos**: Retorna todos os contatos cadastrados.

## Modelo de Contato

Cada contato possui os seguintes campos:

- `nome`: Nome do contato (string)
- `numero_telefone`: Número de telefone (string)
- `tipo_telefone`: Tipo do telefone (enum: `movel`, `fixo`, `comercial`, `indefinido`)
- `categoria_contato`: Categoria do contato (enum: `familia`, `amigos`, `comercial`, `outro`, `indefinido`)

## Execução

1. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Execute o servidor:**
   ```sh
   uvicorn src.app:app --reload
   ```

3. **Acesse a documentação automática:**
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

4. **Teste via script:**
   ```sh
   python teste.py
   ```

---

**Observação:**  
Os dados são armazenados apenas em memória, ou seja, ao reiniciar o servidor os contatos cadastrados serão perdidos.