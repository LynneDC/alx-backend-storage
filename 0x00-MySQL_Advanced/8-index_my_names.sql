-- 8-index_my_names.sql

CREATE INDEX idx_name_first ON names(LEFT(name, 1));

