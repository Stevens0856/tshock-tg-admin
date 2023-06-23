build:
	docker build --build-arg BUILD_TYPE=production -t tshock-tg-admin:production .
build-dev:
	docker build --build-arg BUILD_TYPE=development -t tshock-tg-admin:development .
run:
	docker run -d --rm --name tshock-tg-admin tshock-tg-admin:production
run-dev:
	docker run -it --name tshock-tg-admin -v './:/code' tshock-tg-admin:development
stop:
	docker stop tshock-tg-admin
rerun-dev:
	docker stop tshock-tg-admin
	docker run -d --rm --name tshock-tg-admin -v './:/code' tshock-tg-admin:development
attach:
	docker attach tshock-tg-admin --sig-proxy=false
exec:
	docker exec -it tshock-tg-admin sh
