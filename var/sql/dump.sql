--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: app_adv; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_adv (
    id integer NOT NULL,
    date_from timestamp with time zone NOT NULL,
    date_to timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL,
    title text NOT NULL,
    link character varying(200) NOT NULL,
    code text NOT NULL,
    bg character varying(255) NOT NULL,
    place_id integer NOT NULL,
    picture character varying(100),
    is_enabled boolean NOT NULL,
    date_created timestamp with time zone NOT NULL,
    date_changed timestamp with time zone NOT NULL
);


ALTER TABLE public.app_adv OWNER TO astrikov;

--
-- Name: app_adv_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_adv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_adv_id_seq OWNER TO astrikov;

--
-- Name: app_adv_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_adv_id_seq OWNED BY app_adv.id;


--
-- Name: app_adv_section; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_adv_section (
    id integer NOT NULL,
    adv_id integer NOT NULL,
    advsection_id integer NOT NULL
);


ALTER TABLE public.app_adv_section OWNER TO astrikov;

--
-- Name: app_adv_section_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_adv_section_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_adv_section_id_seq OWNER TO astrikov;

--
-- Name: app_adv_section_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_adv_section_id_seq OWNED BY app_adv_section.id;


--
-- Name: app_advplace; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_advplace (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    slug character varying(50) NOT NULL,
    is_enabled boolean NOT NULL
);


ALTER TABLE public.app_advplace OWNER TO astrikov;

--
-- Name: app_advplace_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_advplace_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_advplace_id_seq OWNER TO astrikov;

--
-- Name: app_advplace_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_advplace_id_seq OWNED BY app_advplace.id;


--
-- Name: app_advsection; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_advsection (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    is_enabled boolean NOT NULL
);


ALTER TABLE public.app_advsection OWNER TO astrikov;

--
-- Name: app_advsection_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_advsection_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_advsection_id_seq OWNER TO astrikov;

--
-- Name: app_advsection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_advsection_id_seq OWNED BY app_advsection.id;


--
-- Name: app_cmsmodule; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_cmsmodule (
    id integer NOT NULL,
    group_id character varying(50) NOT NULL,
    name character varying(64) NOT NULL,
    sort integer NOT NULL,
    description text NOT NULL,
    slug character varying(50) NOT NULL,
    is_enabled boolean NOT NULL
);


ALTER TABLE public.app_cmsmodule OWNER TO astrikov;

--
-- Name: app_cmsmodule_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_cmsmodule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_cmsmodule_id_seq OWNER TO astrikov;

--
-- Name: app_cmsmodule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_cmsmodule_id_seq OWNED BY app_cmsmodule.id;


--
-- Name: app_cmsmodulegroup; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_cmsmodulegroup (
    id integer NOT NULL,
    slug character varying(50) NOT NULL,
    name character varying(64) NOT NULL,
    fa character varying(50) NOT NULL,
    sort integer NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.app_cmsmodulegroup OWNER TO astrikov;

--
-- Name: app_cmsmodulegroup_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_cmsmodulegroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_cmsmodulegroup_id_seq OWNER TO astrikov;

--
-- Name: app_cmsmodulegroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_cmsmodulegroup_id_seq OWNED BY app_cmsmodulegroup.id;


--
-- Name: app_feed; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_feed (
    id integer NOT NULL,
    type_id integer NOT NULL,
    name character varying(255) NOT NULL,
    slug character varying(50) NOT NULL
);


ALTER TABLE public.app_feed OWNER TO astrikov;

--
-- Name: app_feed_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_feed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_feed_id_seq OWNER TO astrikov;

--
-- Name: app_feed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_feed_id_seq OWNED BY app_feed.id;


--
-- Name: app_feeditem; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_feeditem (
    id integer NOT NULL,
    feed_id integer NOT NULL,
    name character varying(1024) NOT NULL,
    slug character varying(50) NOT NULL,
    short_text text NOT NULL,
    full_text text NOT NULL,
    picture character varying(100) NOT NULL,
    views_count integer NOT NULL,
    seo_keywords text NOT NULL,
    seo_description text NOT NULL,
    is_visible boolean NOT NULL,
    date_published timestamp with time zone NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.app_feeditem OWNER TO astrikov;

--
-- Name: app_feeditem_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_feeditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_feeditem_id_seq OWNER TO astrikov;

--
-- Name: app_feeditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_feeditem_id_seq OWNED BY app_feeditem.id;


--
-- Name: app_feedtype; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_feedtype (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    slug character varying(50) NOT NULL
);


ALTER TABLE public.app_feedtype OWNER TO astrikov;

--
-- Name: app_feedtype_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_feedtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_feedtype_id_seq OWNER TO astrikov;

--
-- Name: app_feedtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_feedtype_id_seq OWNED BY app_feedtype.id;


--
-- Name: app_file; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_file (
    id integer NOT NULL,
    folder_id integer NOT NULL,
    path character varying(100) NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.app_file OWNER TO astrikov;

--
-- Name: app_file_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_file_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_file_id_seq OWNER TO astrikov;

--
-- Name: app_file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_file_id_seq OWNED BY app_file.id;


--
-- Name: app_folder; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_folder (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.app_folder OWNER TO astrikov;

--
-- Name: app_folder_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_folder_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_folder_id_seq OWNER TO astrikov;

--
-- Name: app_folder_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_folder_id_seq OWNED BY app_folder.id;


--
-- Name: app_page; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_page (
    id integer NOT NULL,
    parent_id integer,
    title character varying(255) NOT NULL,
    header character varying(255) NOT NULL,
    menu_name character varying(255) NOT NULL,
    menu_url character varying(255) NOT NULL,
    slug character varying(50) NOT NULL,
    url character varying(512) NOT NULL,
    sort integer NOT NULL,
    module_id integer NOT NULL,
    module_params character varying(128),
    before_content text NOT NULL,
    after_content text NOT NULL,
    date_created timestamp with time zone NOT NULL,
    date_changed timestamp with time zone NOT NULL,
    keywords text NOT NULL,
    description text NOT NULL,
    adv_section_id integer NOT NULL,
    is_enabled boolean NOT NULL,
    is_in_menu boolean NOT NULL,
    is_locked boolean NOT NULL
);


ALTER TABLE public.app_page OWNER TO astrikov;

--
-- Name: app_page_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_page_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_page_id_seq OWNER TO astrikov;

--
-- Name: app_page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_page_id_seq OWNED BY app_page.id;


--
-- Name: app_pagemodule; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_pagemodule (
    id integer NOT NULL,
    slug character varying(50) NOT NULL,
    name character varying(64) NOT NULL,
    is_enabled boolean NOT NULL
);


ALTER TABLE public.app_pagemodule OWNER TO astrikov;

--
-- Name: app_pagemodule_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_pagemodule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_pagemodule_id_seq OWNER TO astrikov;

--
-- Name: app_pagemodule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_pagemodule_id_seq OWNED BY app_pagemodule.id;


--
-- Name: app_project; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_project (
    id integer NOT NULL,
    project_type_id integer NOT NULL,
    name character varying(1024) NOT NULL,
    url character varying(200) NOT NULL,
    slug character varying(50) NOT NULL,
    short_text text NOT NULL,
    full_text text NOT NULL,
    picture character varying(100) NOT NULL,
    page_preview_picture character varying(100) NOT NULL,
    seo_keywords text NOT NULL,
    seo_description text NOT NULL,
    is_visible boolean NOT NULL,
    date_published timestamp with time zone NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.app_project OWNER TO astrikov;

--
-- Name: app_project_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_project_id_seq OWNER TO astrikov;

--
-- Name: app_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_project_id_seq OWNED BY app_project.id;


--
-- Name: app_projecttype; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_projecttype (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    slug character varying(50) NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.app_projecttype OWNER TO astrikov;

--
-- Name: app_projecttype_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_projecttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_projecttype_id_seq OWNER TO astrikov;

--
-- Name: app_projecttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_projecttype_id_seq OWNED BY app_projecttype.id;


--
-- Name: app_sitesettings; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE app_sitesettings (
    id integer NOT NULL,
    site_title character varying(255) NOT NULL,
    site_description text NOT NULL,
    footer_content text NOT NULL
);


ALTER TABLE public.app_sitesettings OWNER TO astrikov;

--
-- Name: app_sitesettings_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE app_sitesettings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_sitesettings_id_seq OWNER TO astrikov;

--
-- Name: app_sitesettings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE app_sitesettings_id_seq OWNED BY app_sitesettings.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO astrikov;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO astrikov;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO astrikov;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO astrikov;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO astrikov;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO astrikov;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO astrikov;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO astrikov;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO astrikov;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO astrikov;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO astrikov;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO astrikov;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO astrikov;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO astrikov;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO astrikov;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO astrikov;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO astrikov;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO astrikov;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO astrikov;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO astrikov;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO astrikov;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: watson_searchentry; Type: TABLE; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE TABLE watson_searchentry (
    id integer NOT NULL,
    engine_slug character varying(200) NOT NULL,
    content_type_id integer NOT NULL,
    object_id text NOT NULL,
    object_id_int integer,
    title character varying(1000) NOT NULL,
    description text NOT NULL,
    content text NOT NULL,
    url character varying(1000) NOT NULL,
    meta_encoded text NOT NULL
);


ALTER TABLE public.watson_searchentry OWNER TO astrikov;

--
-- Name: watson_searchentry_id_seq; Type: SEQUENCE; Schema: public; Owner: astrikov
--

CREATE SEQUENCE watson_searchentry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.watson_searchentry_id_seq OWNER TO astrikov;

--
-- Name: watson_searchentry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astrikov
--

ALTER SEQUENCE watson_searchentry_id_seq OWNED BY watson_searchentry.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_adv ALTER COLUMN id SET DEFAULT nextval('app_adv_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_adv_section ALTER COLUMN id SET DEFAULT nextval('app_adv_section_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_advplace ALTER COLUMN id SET DEFAULT nextval('app_advplace_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_advsection ALTER COLUMN id SET DEFAULT nextval('app_advsection_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_cmsmodule ALTER COLUMN id SET DEFAULT nextval('app_cmsmodule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_cmsmodulegroup ALTER COLUMN id SET DEFAULT nextval('app_cmsmodulegroup_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_feed ALTER COLUMN id SET DEFAULT nextval('app_feed_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_feeditem ALTER COLUMN id SET DEFAULT nextval('app_feeditem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_feedtype ALTER COLUMN id SET DEFAULT nextval('app_feedtype_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_file ALTER COLUMN id SET DEFAULT nextval('app_file_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_folder ALTER COLUMN id SET DEFAULT nextval('app_folder_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_page ALTER COLUMN id SET DEFAULT nextval('app_page_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_pagemodule ALTER COLUMN id SET DEFAULT nextval('app_pagemodule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_project ALTER COLUMN id SET DEFAULT nextval('app_project_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_projecttype ALTER COLUMN id SET DEFAULT nextval('app_projecttype_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_sitesettings ALTER COLUMN id SET DEFAULT nextval('app_sitesettings_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY watson_searchentry ALTER COLUMN id SET DEFAULT nextval('watson_searchentry_id_seq'::regclass);


--
-- Data for Name: app_adv; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_adv (id, date_from, date_to, name, title, link, code, bg, place_id, picture, is_enabled, date_created, date_changed) FROM stdin;
\.


--
-- Name: app_adv_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_adv_id_seq', 1, false);


--
-- Data for Name: app_adv_section; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_adv_section (id, adv_id, advsection_id) FROM stdin;
\.


--
-- Name: app_adv_section_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_adv_section_id_seq', 1, false);


--
-- Data for Name: app_advplace; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_advplace (id, name, slug, is_enabled) FROM stdin;
1	Баннер	banner_place	t
\.


--
-- Name: app_advplace_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_advplace_id_seq', 1, true);


--
-- Data for Name: app_advsection; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_advsection (id, name, is_enabled) FROM stdin;
1	Не главная	t
2	Главная	t
\.


--
-- Name: app_advsection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_advsection_id_seq', 2, true);


--
-- Data for Name: app_cmsmodule; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_cmsmodule (id, group_id, name, sort, description, slug, is_enabled) FROM stdin;
1	admin	Пользователи CMS	1		cms-users	t
2	admin	Метрика	2		metrics	t
3	content	Структура сайта	1		pagemap	t
4	content	Новости и статьи	2		feeds	t
5	content	Проекты	2		projects	t
6	adv	Рекламные баннеры	1		adv	t
7	adv	Рекламные места	2		adv-places	t
8	adv	Рекламные разделы	3		adv-sections	t
\.


--
-- Name: app_cmsmodule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_cmsmodule_id_seq', 8, true);


--
-- Data for Name: app_cmsmodulegroup; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_cmsmodulegroup (id, slug, name, fa, sort, description) FROM stdin;
1	admin	Администрирование	fa-flag	1	
2	content	Контент	fa-file	2	
3	adv	Реклама на сайте	fa-rocket	3	
\.


--
-- Name: app_cmsmodulegroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_cmsmodulegroup_id_seq', 3, true);


--
-- Data for Name: app_feed; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_feed (id, type_id, name, slug) FROM stdin;
\.


--
-- Name: app_feed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_feed_id_seq', 1, false);


--
-- Data for Name: app_feeditem; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_feeditem (id, feed_id, name, slug, short_text, full_text, picture, views_count, seo_keywords, seo_description, is_visible, date_published, date_created) FROM stdin;
\.


--
-- Name: app_feeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_feeditem_id_seq', 1, false);


--
-- Data for Name: app_feedtype; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_feedtype (id, name, slug) FROM stdin;
1	Новости	news
2	Статьи	articles
\.


--
-- Name: app_feedtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_feedtype_id_seq', 2, true);


--
-- Data for Name: app_file; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_file (id, folder_id, path, date_created) FROM stdin;
\.


--
-- Name: app_file_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_file_id_seq', 1, false);


--
-- Data for Name: app_folder; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_folder (id, name, date_created) FROM stdin;
\.


--
-- Name: app_folder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_folder_id_seq', 1, false);


--
-- Data for Name: app_page; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_page (id, parent_id, title, header, menu_name, menu_url, slug, url, sort, module_id, module_params, before_content, after_content, date_created, date_changed, keywords, description, adv_section_id, is_enabled, is_in_menu, is_locked) FROM stdin;
1	\N	Главная страница	Главная страница				/	1	1	\N			2014-12-07 23:29:49.05332+07	2014-12-07 23:29:49.05333+07			2	t	t	f
\.


--
-- Name: app_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_page_id_seq', 1, true);


--
-- Data for Name: app_pagemodule; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_pagemodule (id, slug, name, is_enabled) FROM stdin;
1	home	Главная страница	f
2	pagemap	Статическая страница	t
3	feeds	Ленты	t
\.


--
-- Name: app_pagemodule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_pagemodule_id_seq', 3, true);


--
-- Data for Name: app_project; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_project (id, project_type_id, name, url, slug, short_text, full_text, picture, page_preview_picture, seo_keywords, seo_description, is_visible, date_published, date_created) FROM stdin;
1	1	TeamsTree.ru	http://teamstree.ru/	teamstreeru	<p>Сервис для совместной работы над проектами</p>	<p>Сервис для совместной работы над проектами</p>	feeds/2014/12/11/teamstree-logo.png	feeds/2014/12/11/TeamsTree___TeamsTree.png			t	2014-12-18 23:01:07+07	2014-12-11 23:01:43.645564+07
2	1	MyWebWedding	http://mywebwedding.ru/	mywebwedding	<p>Конструктор свадебных сайтов</p>	<p>Конструктор свадебных сайтов</p>	feeds/2014/12/11/mww.png	feeds/2014/12/11/start-screen-bg.jpg			t	2014-12-25 00:15:43+07	2014-12-11 23:17:31.249173+07
3	1	DartCMS	http://astrikov.ru/	dartcms	<p>Система управления контентом на Django</p>	<p>Система управления контентом&nbsp;на Django</p>	feeds/2014/12/11/dartcms.png	feeds/2014/12/11/dartcms_5h4HTYS.png			t	2014-11-26 00:00:36+07	2014-12-11 23:21:30.885183+07
\.


--
-- Name: app_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_project_id_seq', 3, true);


--
-- Data for Name: app_projecttype; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_projecttype (id, name, slug, date_created) FROM stdin;
1	Собственные	own	2014-12-11 21:58:51.370459+07
2	Сайты	sites	2014-12-11 21:59:02.661359+07
\.


--
-- Name: app_projecttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_projecttype_id_seq', 2, true);


--
-- Data for Name: app_sitesettings; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY app_sitesettings (id, site_title, site_description, footer_content) FROM stdin;
\.


--
-- Name: app_sitesettings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('app_sitesettings_id_seq', 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add log entry	4	add_logentry
11	Can change log entry	4	change_logentry
12	Can delete log entry	4	delete_logentry
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add search entry	8	add_searchentry
23	Can change search entry	8	change_searchentry
24	Can delete search entry	8	delete_searchentry
25	Can add Группа модулей CMS	9	add_cmsmodulegroup
26	Can change Группа модулей CMS	9	change_cmsmodulegroup
27	Can delete Группа модулей CMS	9	delete_cmsmodulegroup
28	Can add Модуль CMS	10	add_cmsmodule
29	Can change Модуль CMS	10	change_cmsmodule
30	Can delete Модуль CMS	10	delete_cmsmodule
31	Can add папка	11	add_folder
32	Can change папка	11	change_folder
33	Can delete папка	11	delete_folder
34	Can add file	12	add_file
35	Can change file	12	change_file
36	Can delete file	12	delete_file
37	Can add site settings	13	add_sitesettings
38	Can change site settings	13	change_sitesettings
39	Can delete site settings	13	delete_sitesettings
40	Can add рекламное место	14	add_advplace
41	Can change рекламное место	14	change_advplace
42	Can delete рекламное место	14	delete_advplace
43	Can add рекламный раздел	15	add_advsection
44	Can change рекламный раздел	15	change_advsection
45	Can delete рекламный раздел	15	delete_advsection
46	Can add рекламный баннер	16	add_adv
47	Can change рекламный баннер	16	change_adv
48	Can delete рекламный баннер	16	delete_adv
49	Can add Функциональный модуль	17	add_pagemodule
50	Can change Функциональный модуль	17	change_pagemodule
51	Can delete Функциональный модуль	17	delete_pagemodule
52	Can add страница	18	add_page
53	Can change страница	18	change_page
54	Can delete страница	18	delete_page
55	Can add Тип ленты	19	add_feedtype
56	Can change Тип ленты	19	change_feedtype
57	Can delete Тип ленты	19	delete_feedtype
58	Can add категория новостей	20	add_feed
59	Can change категория новостей	20	change_feed
60	Can delete категория новостей	20	delete_feed
61	Can add запись ленты	21	add_feeditem
62	Can change запись ленты	21	change_feeditem
63	Can delete запись ленты	21	delete_feeditem
64	Can add тип проекта	22	add_projecttype
65	Can change тип проекта	22	change_projecttype
66	Can delete тип проекта	22	delete_projecttype
67	Can add проект	23	add_project
68	Can change проект	23	change_project
69	Can delete проект	23	delete_project
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('auth_permission_id_seq', 69, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$12000$WWgZI9DC5ySI$1KDQB0PCqvTPVAKAB0HawquD1A4WDU2CqEwRgfKqhsk=	2014-12-11 23:20:16.706476+07	t	admin			atrikov.d@gmail.com	t	t	2014-12-07 23:18:45.675361+07
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2014-12-07 23:26:37.585187+07	1	Администрирование	1		9	1
2	2014-12-07 23:26:51.520038+07	2	Контент	1		9	1
3	2014-12-07 23:27:01.010833+07	3	Реклама на сайте	1		9	1
4	2014-12-07 23:27:20.33113+07	1	Администрирование / Пользователи CMS	1		10	1
5	2014-12-07 23:27:35.93497+07	2	Администрирование / Метрика	1		10	1
6	2014-12-07 23:27:47.554977+07	3	Контент / Структура сайта	1		10	1
7	2014-12-07 23:27:58.079372+07	4	Контент / Новости и статьи	1		10	1
8	2014-12-07 23:28:15.777779+07	5	Контент / Проекты	1		10	1
9	2014-12-07 23:28:46.140883+07	6	Реклама на сайте / Рекламные баннеры	1		10	1
10	2014-12-07 23:28:58.134726+07	7	Реклама на сайте / Рекламные места	1		10	1
11	2014-12-07 23:29:14.65834+07	8	Реклама на сайте / Рекламные разделы	1		10	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 11, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	log entry	admin	logentry
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	search entry	watson	searchentry
9	Группа модулей CMS	app	cmsmodulegroup
10	Модуль CMS	app	cmsmodule
11	папка	app	folder
12	file	app	file
13	site settings	app	sitesettings
14	рекламное место	app	advplace
15	рекламный раздел	app	advsection
16	рекламный баннер	app	adv
17	Функциональный модуль	app	pagemodule
18	страница	app	page
19	Тип ленты	app	feedtype
20	категория новостей	app	feed
21	запись ленты	app	feeditem
22	тип проекта	app	projecttype
23	проект	app	project
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('django_content_type_id_seq', 23, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2014-12-07 23:18:24.842042+07
2	auth	0001_initial	2014-12-07 23:18:25.629721+07
3	admin	0001_initial	2014-12-07 23:18:25.774576+07
4	sessions	0001_initial	2014-12-07 23:18:25.90272+07
5	sites	0001_initial	2014-12-07 23:18:26.198233+07
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('django_migrations_id_seq', 5, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
buymai5oqgy31zt17oy54mpiz5y1htx4	YjVkMzg4ZmQyYTAxM2FjNjg4M2E2N2Q1ZjEyYjc0ZTE1NWQyZWRmZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImUzYzM0OTkwODkwMzU0OGIxZjA1ZjI5ODczZDdmYzcwYzM2NTU3NzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJsaWIuYmFja2VuZHMuYWRtLmF1dGguQXV0aEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoxfQ==	2014-12-25 23:21:32.346107+07
nx08e27qeb3922csetjvflk19xj9mzii	YzkzYzIwMDc1N2I5YjM3MTkwMTlmNzU3Njc0YTRhZTZhNjBmOThmOTp7fQ==	2014-12-25 23:23:28.648268+07
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY django_site (id, domain, name) FROM stdin;
1	astrikov.dev	astrikov.dev
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: watson_searchentry; Type: TABLE DATA; Schema: public; Owner: astrikov
--

COPY watson_searchentry (id, engine_slug, content_type_id, object_id, object_id_int, title, description, content, url, meta_encoded) FROM stdin;
\.


--
-- Name: watson_searchentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astrikov
--

SELECT pg_catalog.setval('watson_searchentry_id_seq', 1, false);


--
-- Name: app_adv_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_adv
    ADD CONSTRAINT app_adv_pkey PRIMARY KEY (id);


--
-- Name: app_adv_section_adv_id_advsection_id_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_adv_section
    ADD CONSTRAINT app_adv_section_adv_id_advsection_id_key UNIQUE (adv_id, advsection_id);


--
-- Name: app_adv_section_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_adv_section
    ADD CONSTRAINT app_adv_section_pkey PRIMARY KEY (id);


--
-- Name: app_advplace_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_advplace
    ADD CONSTRAINT app_advplace_pkey PRIMARY KEY (id);


--
-- Name: app_advplace_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_advplace
    ADD CONSTRAINT app_advplace_slug_key UNIQUE (slug);


--
-- Name: app_advsection_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_advsection
    ADD CONSTRAINT app_advsection_pkey PRIMARY KEY (id);


--
-- Name: app_cmsmodule_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_cmsmodule
    ADD CONSTRAINT app_cmsmodule_pkey PRIMARY KEY (id);


--
-- Name: app_cmsmodule_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_cmsmodule
    ADD CONSTRAINT app_cmsmodule_slug_key UNIQUE (slug);


--
-- Name: app_cmsmodulegroup_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_cmsmodulegroup
    ADD CONSTRAINT app_cmsmodulegroup_pkey PRIMARY KEY (id);


--
-- Name: app_cmsmodulegroup_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_cmsmodulegroup
    ADD CONSTRAINT app_cmsmodulegroup_slug_key UNIQUE (slug);


--
-- Name: app_feed_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_feed
    ADD CONSTRAINT app_feed_pkey PRIMARY KEY (id);


--
-- Name: app_feed_type_id_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_feed
    ADD CONSTRAINT app_feed_type_id_slug_key UNIQUE (type_id, slug);


--
-- Name: app_feeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_feeditem
    ADD CONSTRAINT app_feeditem_pkey PRIMARY KEY (id);


--
-- Name: app_feeditem_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_feeditem
    ADD CONSTRAINT app_feeditem_slug_key UNIQUE (slug);


--
-- Name: app_feedtype_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_feedtype
    ADD CONSTRAINT app_feedtype_pkey PRIMARY KEY (id);


--
-- Name: app_file_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_file
    ADD CONSTRAINT app_file_pkey PRIMARY KEY (id);


--
-- Name: app_folder_name_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_folder
    ADD CONSTRAINT app_folder_name_key UNIQUE (name);


--
-- Name: app_folder_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_folder
    ADD CONSTRAINT app_folder_pkey PRIMARY KEY (id);


--
-- Name: app_page_module_id_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_page
    ADD CONSTRAINT app_page_module_id_slug_key UNIQUE (module_id, slug);


--
-- Name: app_page_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_page
    ADD CONSTRAINT app_page_pkey PRIMARY KEY (id);


--
-- Name: app_pagemodule_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_pagemodule
    ADD CONSTRAINT app_pagemodule_pkey PRIMARY KEY (id);


--
-- Name: app_pagemodule_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_pagemodule
    ADD CONSTRAINT app_pagemodule_slug_key UNIQUE (slug);


--
-- Name: app_project_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_project
    ADD CONSTRAINT app_project_pkey PRIMARY KEY (id);


--
-- Name: app_project_slug_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_project
    ADD CONSTRAINT app_project_slug_key UNIQUE (slug);


--
-- Name: app_projecttype_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_projecttype
    ADD CONSTRAINT app_projecttype_pkey PRIMARY KEY (id);


--
-- Name: app_sitesettings_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY app_sitesettings
    ADD CONSTRAINT app_sitesettings_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: watson_searchentry_pkey; Type: CONSTRAINT; Schema: public; Owner: astrikov; Tablespace: 
--

ALTER TABLE ONLY watson_searchentry
    ADD CONSTRAINT watson_searchentry_pkey PRIMARY KEY (id);


--
-- Name: app_adv_place_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_adv_place_id ON app_adv USING btree (place_id);


--
-- Name: app_adv_section_adv_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_adv_section_adv_id ON app_adv_section USING btree (adv_id);


--
-- Name: app_adv_section_advsection_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_adv_section_advsection_id ON app_adv_section USING btree (advsection_id);


--
-- Name: app_advplace_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_advplace_slug_like ON app_advplace USING btree (slug varchar_pattern_ops);


--
-- Name: app_cmsmodule_group_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_cmsmodule_group_id ON app_cmsmodule USING btree (group_id);


--
-- Name: app_cmsmodule_group_id_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_cmsmodule_group_id_like ON app_cmsmodule USING btree (group_id varchar_pattern_ops);


--
-- Name: app_cmsmodule_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_cmsmodule_slug_like ON app_cmsmodule USING btree (slug varchar_pattern_ops);


--
-- Name: app_cmsmodulegroup_fa; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_cmsmodulegroup_fa ON app_cmsmodulegroup USING btree (fa);


--
-- Name: app_cmsmodulegroup_fa_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_cmsmodulegroup_fa_like ON app_cmsmodulegroup USING btree (fa varchar_pattern_ops);


--
-- Name: app_cmsmodulegroup_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_cmsmodulegroup_slug_like ON app_cmsmodulegroup USING btree (slug varchar_pattern_ops);


--
-- Name: app_feed_slug; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feed_slug ON app_feed USING btree (slug);


--
-- Name: app_feed_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feed_slug_like ON app_feed USING btree (slug varchar_pattern_ops);


--
-- Name: app_feed_type_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feed_type_id ON app_feed USING btree (type_id);


--
-- Name: app_feeditem_feed_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feeditem_feed_id ON app_feeditem USING btree (feed_id);


--
-- Name: app_feeditem_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feeditem_slug_like ON app_feeditem USING btree (slug varchar_pattern_ops);


--
-- Name: app_feedtype_slug; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feedtype_slug ON app_feedtype USING btree (slug);


--
-- Name: app_feedtype_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_feedtype_slug_like ON app_feedtype USING btree (slug varchar_pattern_ops);


--
-- Name: app_file_folder_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_file_folder_id ON app_file USING btree (folder_id);


--
-- Name: app_page_adv_section_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_page_adv_section_id ON app_page USING btree (adv_section_id);


--
-- Name: app_page_module_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_page_module_id ON app_page USING btree (module_id);


--
-- Name: app_page_parent_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_page_parent_id ON app_page USING btree (parent_id);


--
-- Name: app_page_slug; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_page_slug ON app_page USING btree (slug);


--
-- Name: app_page_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_page_slug_like ON app_page USING btree (slug varchar_pattern_ops);


--
-- Name: app_pagemodule_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_pagemodule_slug_like ON app_pagemodule USING btree (slug varchar_pattern_ops);


--
-- Name: app_project_project_type_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_project_project_type_id ON app_project USING btree (project_type_id);


--
-- Name: app_project_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_project_slug_like ON app_project USING btree (slug varchar_pattern_ops);


--
-- Name: app_projecttype_slug; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_projecttype_slug ON app_projecttype USING btree (slug);


--
-- Name: app_projecttype_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX app_projecttype_slug_like ON app_projecttype USING btree (slug varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: watson_searchentry_content_type_id; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX watson_searchentry_content_type_id ON watson_searchentry USING btree (content_type_id);


--
-- Name: watson_searchentry_engine_slug; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX watson_searchentry_engine_slug ON watson_searchentry USING btree (engine_slug);


--
-- Name: watson_searchentry_engine_slug_like; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX watson_searchentry_engine_slug_like ON watson_searchentry USING btree (engine_slug varchar_pattern_ops);


--
-- Name: watson_searchentry_object_id_int; Type: INDEX; Schema: public; Owner: astrikov; Tablespace: 
--

CREATE INDEX watson_searchentry_object_id_int ON watson_searchentry USING btree (object_id_int);


--
-- Name: adv_id_refs_id_26a2e8fc; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_adv_section
    ADD CONSTRAINT adv_id_refs_id_26a2e8fc FOREIGN KEY (adv_id) REFERENCES app_adv(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_adv_place_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_adv
    ADD CONSTRAINT app_adv_place_id_fkey FOREIGN KEY (place_id) REFERENCES app_advplace(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_adv_section_advsection_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_adv_section
    ADD CONSTRAINT app_adv_section_advsection_id_fkey FOREIGN KEY (advsection_id) REFERENCES app_advsection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_cmsmodule_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_cmsmodule
    ADD CONSTRAINT app_cmsmodule_group_id_fkey FOREIGN KEY (group_id) REFERENCES app_cmsmodulegroup(slug) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_feed_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_feed
    ADD CONSTRAINT app_feed_type_id_fkey FOREIGN KEY (type_id) REFERENCES app_feedtype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_feeditem_feed_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_feeditem
    ADD CONSTRAINT app_feeditem_feed_id_fkey FOREIGN KEY (feed_id) REFERENCES app_feed(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_file_folder_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_file
    ADD CONSTRAINT app_file_folder_id_fkey FOREIGN KEY (folder_id) REFERENCES app_folder(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_page_adv_section_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_page
    ADD CONSTRAINT app_page_adv_section_id_fkey FOREIGN KEY (adv_section_id) REFERENCES app_advsection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_page_module_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_page
    ADD CONSTRAINT app_page_module_id_fkey FOREIGN KEY (module_id) REFERENCES app_pagemodule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_page_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_page
    ADD CONSTRAINT app_page_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES app_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_project_project_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY app_project
    ADD CONSTRAINT app_project_project_type_id_fkey FOREIGN KEY (project_type_id) REFERENCES app_projecttype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: astrikov
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

