INSERT INTO settings (active, version, web, api, user_data)
VALUES (True, '1.0', '{ "visible": { "/categorias": false } }', '{}', '{}');

-- privilegios básicos, agnosticos ao fork
INSERT INTO privilegios (name, created_user, updated_user) VALUES
    ('Administrador', 0, 0), -- 1
    ('Moderador', 0, 0), -- 2
    ('Participante', 0, 0); -- 3


INSERT INTO avatars (avatar, standard)
VALUES ('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',
        true);

-- usuário admin, agnostico ao fork
--      query nao ta errada, se algum intellisense apontar erro é pq a IDE não entende o "OVERRIDING SYSTEM VALUE"
INSERT INTO usuarios (id, type, email, username, password, name, has_accepted_terms, created_user, updated_user, avatar_id)
OVERRIDING SYSTEM VALUE VALUES (0, 1, 'admin@email.com', 'admin', '12345', 'Administrador', False, 0, 0, 1);

INSERT INTO categorias (id, name, created_user, updated_user)
OVERRIDING SYSTEM VALUE VALUES (0, 'Sem Categoria', 0, 0);

-- TESTING INSERTS
INSERT INTO categorias (name, created_date, created_user, updated_date, updated_user)
VALUES ('Orientações', '2022-03-02 10:08:40.420395', 0, '2022-03-02 10:08:40.420395', 0), -- 1
       ('Atividades', '2022-03-02 10:08:40.420395', 0, '2022-03-02 10:08:40.420395', 0), -- 2
       ('Interação Social', '2022-03-02 10:08:40.420395', 0, '2022-03-02 10:08:40.420395', 0), -- 3
       ('Sintomas Atípicos', '2022-03-02 10:08:40.420395', 0, '2022-03-02 10:08:40.420395', 0) -- 4
;

INSERT INTO categorias (name, created_date, created_user, updated_date, updated_user)
VALUES ('Categoria Teste', '2022-03-02 10:08:40.420395', 0, '2022-03-02 10:08:40.420395', 0); -- 5

INSERT INTO postagens (categoria, titulo, texto, selo, created_date, created_user, updated_date, updated_user)
VALUES (0, 'Post 1', 1, 'false', '2022-03-02 14:31:21.414159', 0, '2022-03-02 14:31:21.414159', 0); -- 1
INSERT INTO postagens (categoria, titulo, texto, selo, created_date, created_user, updated_date, updated_user)
VALUES (0, 'Post 2', 2, 'true', '2022-03-02 14:31:21.414159', 0, '2022-03-02 14:31:21.414159', 0); -- 2
INSERT INTO postagens (categoria, titulo, texto, selo, created_date, created_user, updated_date, updated_user)
VALUES (1, 'Post 3', 3, 'true', '2022-03-02 14:31:21.414159', 0, '2022-03-02 14:31:21.414159', 0); -- 3


SELECT * FROM settings;

SELECT * FROM usuarios;
SELECT * FROM privilegios;

SELECT * FROM categorias;
SELECT * FROM postagens ORDER BY created_date DESC;
SELECT * FROM comentarios;

UPDATE usuarios SET data = NULL WHERE id = 0