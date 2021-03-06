-- Generated by Oracle SQL Developer Data Modeler 20.2.0.167.1538
--   at:        2020-10-27 18:25:10 EDT
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE leaderboards (
    player_name       VARCHAR2(4000) NOT NULL,
    title             CHAR(3 CHAR),
    country           VARCHAR2(4000),
    date_of_birth     DATE,
    birthplace        VARCHAR2(4000),
    world_rank        INTEGER,
    rapid_rating      INTEGER,
    blitz_rating      INTEGER,
    classical_rating  INTEGER,
    retired           VARCHAR2(20 CHAR),
    date_collected    DATE
);

ALTER TABLE leaderboards ADD CONSTRAINT leaderboards_pk PRIMARY KEY ( player_name );

CREATE TABLE matches (
    matchid         INTEGER NOT NULL,
    format          VARCHAR2(4000) NOT NULL,
    moves           INTEGER NOT NULL,
    result          VARCHAR2(4000) NOT NULL,
    white_title     CHAR(3 CHAR),
    white_player    VARCHAR2(4000 CHAR) NOT NULL,
    white_rating    INTEGER,
    white_accuracy  NUMBER,
    white_country   VARCHAR2(4000),
    black_title     CHAR(3 CHAR),
    black_player    VARCHAR2(4000 CHAR) NOT NULL,
    black_rating    INTEGER,
    black_accuracy  NUMBER,
    black_country   VARCHAR2(4000),
    date_played     DATE NOT NULL,
    date_collected  DATE,
    time            VARCHAR2(4000)
);

ALTER TABLE matches ADD CONSTRAINT matches_pk PRIMARY KEY ( matchid );

CREATE TABLE players (
    username        VARCHAR2(4000) NOT NULL,
    legal_name      VARCHAR2(4000),
    title           CHAR(3 CHAR),
    diamond_member  CHAR(1),
    country         VARCHAR2(4000),
    city            VARCHAR2(4000),
    date_joined     DATE NOT NULL,
    profile_views   INTEGER NOT NULL,
    followers       INTEGER NOT NULL,
    points          INTEGER NOT NULL,
    blitz           INTEGER,
    bullet          INTEGER,
    rapid           INTEGER,
    puzzle_rush     INTEGER,
    puzzles         INTEGER,
    daily_960       INTEGER,
    daily           INTEGER,
    live_960        INTEGER,
    "3Check"        INTEGER,
    koth            INTEGER,
    crazyhouse      INTEGER,
    bughouse        INTEGER,
    url             VARCHAR2(4000),
    last_online     VARCHAR2(4000),
    date_collected  DATE,
    time_collected  VARCHAR2(4000)
);

ALTER TABLE players ADD CONSTRAINT players_pk PRIMARY KEY ( username );

ALTER TABLE matches
    ADD CONSTRAINT matches_players_fk FOREIGN KEY ( white_player )
        REFERENCES players ( username );

ALTER TABLE matches
    ADD CONSTRAINT matches_players_fkv2 FOREIGN KEY ( black_player )
        REFERENCES players ( username );



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              5
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0



--DROP TABLE MATCHES;
--DROP TABLE PLAYERS;
--DROP TABLE LEADERBOARDS;

