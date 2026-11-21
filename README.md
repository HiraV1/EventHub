# EventHub

Sistema distribuído de gerenciamento de eventos e inscrições, desenvolvido com arquitetura de microsserviços e tecnologias heterogêneas.

## Sobre o projeto

O EventHub é uma aplicação baseada em arquitetura de microsserviços, desenvolvida com o objetivo de demonstrar comunicação entre serviços independentes, descentralização de dados, conteinerização, roteamento centralizado e observabilidade.

A aplicação é composta por dois microsserviços:

- **Microsserviço de Eventos:** responsável pelo gerenciamento dos eventos, desenvolvido em Java com Spring Boot.
- **Microsserviço de Inscrições:** responsável pelo gerenciamento das inscrições dos participantes, desenvolvido em Python com FastAPI.

Os serviços possuem bancos de dados independentes e se comunicam por meio de APIs REST utilizando JSON.

## Arquitetura

A arquitetura do EventHub utiliza os seguintes componentes:

| Componente | Tecnologia | Responsabilidade |
|---|---|---|
| Microsserviço de Eventos | Java / Spring Boot | Gerenciamento de eventos |
| Microsserviço de Inscrições | Python / FastAPI | Gerenciamento de inscrições |
| Banco de Eventos | PostgreSQL | Persistência dos eventos |
| Banco de Inscrições | PostgreSQL | Persistência das inscrições |
| API Gateway | NGINX | Roteamento das requisições |
| Coleta de métricas | Prometheus | Monitoramento dos microsserviços |
| Visualização de métricas | Grafana | Dashboards de monitoramento |
| Orquestração | Docker Compose | Gerenciamento dos containers |

### Comunicação entre os microsserviços

O microsserviço de Inscrições realiza requisições HTTP ao microsserviço de Eventos para verificar a existência, o status e a disponibilidade de vagas antes de cadastrar uma inscrição.

Cada microsserviço acessa exclusivamente seu próprio banco de dados, respeitando o princípio Database per Service.

## Tecnologias utilizadas

- Java 25
- Spring Boot
- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL 17
- Docker e Docker Compose
- NGINX
- Prometheus
- Grafana
- Git e GitHub

## Funcionalidades

### Eventos

- Cadastrar eventos;
- Consultar eventos;
- Listar eventos;
- Atualizar informações dos eventos;
- Encerrar eventos;
- Cancelar eventos;
- Excluir eventos logicamente;
- Controlar o status e a capacidade dos eventos.

### Inscrições

- Cadastrar inscrições;
- Consultar inscrições;
- Listar inscrições;
- Atualizar dados dos participantes;
- Cancelar inscrições logicamente;
- Consultar disponibilidade e capacidade dos eventos;
- Impedir inscrições duplicadas para o mesmo evento;
- Liberar vagas após o cancelamento de inscrições.

## Pré-requisitos

Para executar o projeto, é necessário ter instalado:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Docker Compose (disponível no Docker Desktop)
- Git

## Configuração do ambiente

### 1. Clonar o repositório

```bash
git clone [URL_DO_REPOSITORIO](https://github.com/HiraV1/EventHub)
```

Entre na pasta do projeto:

```bash
cd EventHub
```

### 2. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como referência.

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Preencha as variáveis com as credenciais locais dos bancos de dados

## Executando a aplicação

Na raiz do projeto, execute:

```bash
docker compose up -d --build
```

Esse comando constrói as imagens necessárias e inicia os containers dos microsserviços, bancos de dados, API Gateway e ferramentas de monitoramento.

## Endpoints e acessos

### API Gateway

As requisições podem ser encaminhadas pelo NGINX:

| Serviço | Endpoint |
|---|---|
| Eventos | `http://localhost/api/eventos` |
| Inscrições | `http://localhost/api/inscricoes` |

### Acesso direto aos microsserviços

| Serviço | Endereço |
|---|---|
| API de Eventos | `http://localhost:8080/api/eventos` |
| API de Inscrições | `http://localhost:8000/api/inscricoes` |
| Documentação Swagger de Inscrições | `http://localhost:8000/docs` |
| Saúde do serviço de Eventos | `http://localhost:8080/actuator/health` |
| Métricas de Eventos | `http://localhost:8080/actuator/prometheus` |
| Métricas de Inscrições | `http://localhost:8000/metrics` |

### Monitoramento

| Ferramenta | Endereço |
|---|---|
| Prometheus | `http://localhost:9090` |
| Grafana | `http://localhost:3000` |

No Grafana, a fonte de dados Prometheus deve utilizar o endereço interno:

```text
http://prometheus:9090
```

## Testando a aplicação

Com os containers em execução, é possível validar as funcionalidades por meio das APIs.

As requisições utilizadas durante o desenvolvimento estão organizadas na pasta `postman/`.

## Persistência dos dados

Cada microsserviço possui seu próprio banco de dados PostgreSQL:

- `eventhub_eventos`: utilizado exclusivamente pelo microsserviço de Eventos.
- `eventhub_inscricoes`: utilizado exclusivamente pelo microsserviço de Inscrições.

Os dados são armazenados em volumes Docker independentes, permitindo sua persistência mesmo após a interrupção dos containers.

## Observabilidade

O EventHub utiliza Prometheus para coletar métricas dos microsserviços e Grafana para apresentar essas informações em dashboards.

## Autores

Higor Morais Vieira
Projeto acadêmico desenvolvido para a disciplina de Sistemas Distribuídos.
