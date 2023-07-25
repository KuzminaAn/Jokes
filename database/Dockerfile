FROM --platform=linux/amd64 postgres:9.6

USER postgres

COPY init_db.sql /docker-entrypoint-initdb.d/
ENV POSTGRES_HOST_AUTH_METHOD=trust

EXPOSE 5432

CMD ["postgres"]