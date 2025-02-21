# VivaFit API

API REST desenvolvida em Django para gerenciamento de academia, dietas e treinos. O sistema permite o gerenciamento de clientes, nutricionistas, personal trainers, além do acompanhamento de dietas, treinos e progresso dos clientes.

## Funcionalidades Principais

- Gestão de Usuários (Clientes, Nutricionistas e Personal Trainers)
- Gerenciamento de Dietas e Refeições
- Controle de Treinos e Exercícios
- Acompanhamento de Progresso
- Relatórios de Consumo e Treinos

## Estrutura do Projeto

O projeto está organizado nos seguintes módulos principais:

- `VivaFit_app/models/`: Modelos de dados do sistema
- `VivaFit_app/views/`: Views e ViewSets da API
- `VivaFit_app/serializers/`: Serializadores para os modelos
- `VivaFit_app/tests/`: Testes automatizados

## Requisitos

- Python 3.x
- Django 5.1.6
- Django REST Framework 3.14.0

## Instalação

1. Clone o repositório:
```
git clone <url-do-repositorio>
cd Fitness_Api
```

2. Crie um ambiente virtual e ative-o:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:
```
python manage.py makemigrations VivaFit_app
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

## Endpoints da API

### Usuários
- `POST /api/clientes/`: Criar novo cliente
- `GET /api/clientes/`: Listar clientes
- `GET /api/clientes/{id}/`: Detalhes do cliente
- `PUT /api/clientes/{id}/`: Atualizar cliente
- `DELETE /api/clientes/{id}/`: Remover cliente

Similar para nutricionistas (`/api/nutricionistas/`) e personais (`/api/personais/`)

### Dietas e Refeições
- `POST /api/dietas/`: Criar nova dieta
- `GET /api/dietas/{id}/`: Detalhes da dieta
- `POST /api/dietas/{id}/adicionar_refeicao/`: Adicionar refeição à dieta
- `GET /api/dietas/{id}/verificar_progresso/`: Verificar progresso da dieta
- `GET /api/dietas/{id}/gerar_relatorio/`: Gerar relatório da dieta

### Treinos
- `POST /api/rotinas-treino/`: Criar nova rotina de treino
- `GET /api/treinos/`: Listar treinos
- `POST /api/treinos/{id}/adicionar_exercicio/`: Adicionar exercício ao treino

### Relatórios
- `GET /api/relatorios-consumo/`: Relatórios de consumo
- `GET /api/relatorios-treinos/`: Relatórios de treinos
- `GET /api/registros-progresso/`: Registros de progresso

## Exemplos de Uso

### Criar um Cliente
```
curl -X POST http://localhost:8000/api/clientes/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 2,
    "nome": "WALLACY",
    "email": "wallacy@gmail.com",
    "telefone": "84998151018",
    "data_nascimento": "2020-02-11",
    "peso": "80.00",
    "altura": "1.80",
    "objetivo_principal": "emagrecer",
    "nivel_atividade_fisica": "médio",
    "restricoes_alimentares": "Nenhuma",
    "meta_peso": "70.00",
    "meta_calorias": 90
  }'
```

## Testes

Para executar os testes:
```
python manage.py test VivaFit_app -v 2  
```

## Desenvolvimento

O projeto segue as melhores práticas de desenvolvimento Django e REST Framework:

- Modelos bem definidos com relacionamentos apropriados
- ViewSets para operações CRUD
- Serializers para validação e transformação de dados
- Testes automatizados para modelos e views
- Documentação clara dos endpoints

## Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Suporte

Para reportar bugs ou sugerir melhorias, por favor abra uma issue no repositório.