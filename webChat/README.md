# Atlas WebChat

Frontend simples (React + TypeScript + Vite) para testar o backend do Atlas: enviar um PDF e conversar sobre o conteúdo dele.

## Pré-requisitos

- Node.js 18+ instalado
- Backend do Atlas rodando em `http://localhost:8000` (`docker compose up -d` ou `make run`, na raiz do projeto)

## Rodando

### Opção 1 — Docker (junto com o resto do projeto)

Na raiz do projeto:

```bash
docker compose up -d --build
```

Isso sobe Postgres, API e o Vite juntos. Abre em `http://localhost:5173`.

### Opção 2 — Local

```bash
cd webChat
npm install
npm run dev
```

Abre em `http://localhost:5173`.

## Configuração (opcional)

Por padrão, aponta para `http://localhost:8000`. Se o backend estiver em outra URL, copie `.env.example` para `.env` e ajuste `VITE_API_URL`.

## Notas

- O chat não mantém histórico de conversa no backend — cada pergunta é uma consulta RAG independente (o Atlas ainda não suporta múltiplos turnos). O histórico que você vê na tela é só visual, do lado do cliente.
- Não existe um endpoint para listar documentos já enviados — a tela só mostra o último upload feito na sessão atual.
