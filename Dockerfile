FROM postgres

COPY ./.pg_service.conf /configs

RUN export PGSERVICE_FILE=/configs/.pg_service.conf

CMD ["systemctl", "restart", "postgres"]