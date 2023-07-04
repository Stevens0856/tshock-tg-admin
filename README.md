# TShock tg-admin
Simple Telegram bot that allows you to administer a [TShock](https://github.com/Pryaxis/TShock) server for Terraria.

## Currently available
- Creating tokens
- Switching accounts
- Server/world informaton
- Broadcast
- Execute command
- All/online users
- English/russian localizations

## Installation
1. Rename `.env.example` to `.env`, fill it with your data (`POSTGRES_DSN` data should contain `DB_USER`, `DB_PASS`, `DB_NAME`)
2. Make directories for your postgres and redis data
3. Rename `docker-compose.example.yml` to `docker-compose.yml`
4. Replace `/path/to/postgres-data`, `/path/to/redis-data` with your postgres and redis data paths in `docker-compose.yml`
5. Run `docker compose up -d`
