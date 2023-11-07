CREATE DATABASE "chift-db"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE IF NOT EXISTS public.contact
(
    id   smallint NOT NULL,
    name character varying(50),
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.contact
    OWNER to postgres;
