DROP TABLE pets;
DROP TABLE owners;
DROP TABLE vets;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  emergency_contact TEXT
);

CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  dob DATE,
  Phone VARCHAR(255),
  address TEXT,
  vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  dob DATE,
  type VARCHAR(255),
  notes TEXT,
  vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
  owner_id INT REFERENCES owners(id) ON DELETE CASCADE
);