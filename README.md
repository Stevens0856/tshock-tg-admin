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

## Screenshots
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/75de3882-cd77-48f9-8c8f-6d760d041cdf)
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/b215e1e9-b390-476d-b17b-376ab858b000)

![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/5287b2fa-8648-47ce-85c0-a07d8e3210e8)
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/4291e681-caee-4b58-a85f-6377e8f05c17)
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/3148edfb-94a9-4e75-8e55-80c94a1c6aac)
