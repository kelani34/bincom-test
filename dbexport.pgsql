--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3
-- Dumped by pg_dump version 14.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dress_color; Type: TABLE; Schema: public; Owner: kelani
--

CREATE TABLE public.dress_color (
    color character varying,
    frequency integer
);


ALTER TABLE public.dress_color OWNER TO kelani;

--
-- Data for Name: dress_color; Type: TABLE DATA; Schema: public; Owner: kelani
--

COPY public.dress_color (color, frequency) FROM stdin;
GREEN	10
YELLOW	5
BROWN	6
BLUE	30
PINK	5
ORANGE	9
CREAM	2
RED	9
WHITE	16
ARSH	1
BLEW	1
BLACK	1
\.


--
-- PostgreSQL database dump complete
--

