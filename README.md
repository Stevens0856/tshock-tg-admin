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
<details>
  <summary>More</summary>
  
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/4291e681-caee-4b58-a85f-6377e8f05c17)
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/36601a3f-18f8-4d60-b04c-c7bd3b4da71d)

![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/5287b2fa-8648-47ce-85c0-a07d8e3210e8)
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/31efeb63-0a6d-4e50-a463-344b67fd5176)
![image](https://github.com/montaq/tshock-tg-admin/assets/53003167/c8f0a936-5be3-4bf5-9ddf-8a11f249ab4d)

</details>
