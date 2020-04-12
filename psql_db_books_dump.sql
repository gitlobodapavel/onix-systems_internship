--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-0ubuntu0.19.04.1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-0ubuntu0.19.04.1)

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

SET default_with_oids = false;

--
-- Name: tbl_books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbl_books (
    b_id character varying(17),
    b_name character varying(255) NOT NULL,
    b_author character varying(255),
    b_topic smallint,
    b_price numeric(10,2),
    CONSTRAINT tbl_books_b_topic_check CHECK (((b_topic >= 0) AND (b_topic <= 127)))
);


ALTER TABLE public.tbl_books OWNER TO postgres;

--
-- Name: tbl_topics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbl_topics (
    topic_id smallint NOT NULL,
    topic_name character varying(100),
    CONSTRAINT tbl_topics_topic_id_check CHECK (((topic_id >= 0) AND (topic_id <= 127)))
);


ALTER TABLE public.tbl_topics OWNER TO postgres;

--
-- Name: tbl_topics_topic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tbl_topics ALTER COLUMN topic_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tbl_topics_topic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: tbl_books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbl_books (b_id, b_name, b_author, b_topic, b_price) FROM stdin;
SBINCODE	Book name	Book author	1	3.99
SBINCODE	Book name	Book author	1	4.00
SBINCODE	Book name	Book author	1	33.45
\.


--
-- Data for Name: tbl_topics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbl_topics (topic_id, topic_name) FROM stdin;
1	Classical literature
2	Science literature
\.


--
-- Name: tbl_topics_topic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbl_topics_topic_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

