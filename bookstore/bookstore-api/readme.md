# Exercitando o que vimos | 01

1. Gerar e comparar hashes com o bcrypt.
   - [Exemplo de hashing](https://github.com/angeloevangelista/fiap-shift-fullstack-python/tree/main/bookstore/bookstore-api/routers/auth.py#L30)
   - [Exemplo de comparação](https://github.com/angeloevangelista/fiap-shift-fullstack-python/tree/main/bookstore/bookstore-api/routers/auth.py#L61)
2. Gerar token JWT com expiração.
   - [Exemplo de geração de token](https://github.com/angeloevangelista/fiap-shift-fullstack-python/tree/main/bookstore/bookstore-api/routers/auth.py#L69)
   - Use o [JWT.io](https://jwt.io/) para acessar as informações do token gerado

---

# Exercitando o que vimos | 02

1. Fazer uma função que retorne retorne um generator com o `yield` e percorrer os itens.

   - [Exemplo de função retornando um generator](https://github.com/angeloevangelista/fiap-shift-fullstack-python/tree/main/bookstore/bookstore-api/exemplos/yield/main.py#L1)

2. Injetar algum valor em uma rota usando o `Depends`

   - [Usando a injeção de dependência do FastAPI](https://github.com/angeloevangelista/fiap-shift-fullstack-python/tree/main/bookstore/bookstore-api/main.py#L16)

3. Acessar os headers enviados para alguma rota

   - [Acessando o header `authorization`](https://github.com/angeloevangelista/fiap-shift-fullstack-python/tree/main/bookstore/bookstore-api/dependencies/__init__.py#L11)

4. Refazer o CRUD de books (livros)

5. Fazer o CRUD de alguma outra entidade/tipo: authors, categories ou publishers
