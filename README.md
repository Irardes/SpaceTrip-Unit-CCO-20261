# 🚀 Sistema de Viagens Espaciais

Sistema de gerenciamento de viagens e passageiros desenvolvido em Python como projeto colaborativo.

## 📁 Estrutura do projeto

```
space-travel/
├── viagens.py       # Pessoa 1 — funções de viagens
├── passageiros.py   # Pessoa 2 — funções de passageiros
├── main.py          # Menu principal integrado
└── README.md
```

## ▶️ Como executar

```bash
python main.py
```

## 🗂️ Menu

| Opção | Função |
|-------|--------|
| 1 | Cadastrar viagem |
| 2 | Listar destinos |
| 3 | Verificar assentos disponíveis |
| 4 | Mostrar destinos únicos |
| 5 | Cadastrar passageiro |
| 6 | Adicionar passageiro à viagem |
| 7 | Listar passageiros por viagem |
| 8 | Calcular custo total da viagem |
| 9 | Listar viagens por preço |
| 0 | Sair |

## ✅ Requisitos cobertos

### Pessoa 1 — `viagens.py`
- `if / elif / else`
- `if ternário` — status de assentos
- `while` — menu principal
- `for` — listagem e destinos
- `set` — destinos únicos
- `tuple` — classes e status da nave
- `funções`

### Pessoa 2 — `passageiros.py`
- `dict` — estrutura de passageiro
- `list comprehension` — lista de nomes
- `lambda` — ordenar viagens por preço
- `funções com retorno`
- `listas` — lista de passageiros
- `for` — percorrer passageiros e viagens

## 🎓 Alunos

- Irardes de Luna e Silva Santos
- Julia Rosa Chedeeck de Abreu

## 👥 Divisão de commits sugerida

**Pessoa 1**
```
feat: cadastro de viagens
feat: sistema de assentos
feat: destinos únicos
```

**Pessoa 2**
```
feat: cadastro de passageiros
feat: cálculo de custo
feat: listagem de passageiros
```

**Juntos**
```
feat: menu principal integrado
docs: README
```
