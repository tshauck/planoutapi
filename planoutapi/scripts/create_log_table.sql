CREATE TABLE experiments (
    id serial primary key,
    inputs json,
    name varchar(300),
    checksum varchar(50),
    params json,
    time bigint,
    salt varchar(300),
    event varchar(300)
)
