FROM node:20-alpine

WORKDIR /app

RUN corepack enable

COPY apps/frontend/package.json /app/package.json
RUN pnpm install

COPY apps/frontend /app

EXPOSE 5173

CMD ["pnpm", "dev"]
