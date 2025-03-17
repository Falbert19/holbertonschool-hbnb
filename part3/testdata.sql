-- Insert Admin User (Password must be pre-hashed)
INSERT INTO users (id, first_name, last_name, email, password, is_admin) VALUES
('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'Admin', 'HBnB', 'admin@hbnb.io', 
'$2b$12$KIX/H3N77.oQ6yx3BZUQdeULaLhD1K7BX8qCf8Hc4yprf2Rx2lv6K', TRUE);

-- Insert Initial Amenities
INSERT INTO amenities (id, name) VALUES
(UUID(), 'WiFi'),
(UUID(), 'Swimming Pool'),
(UUID(), 'Air Conditioning');
