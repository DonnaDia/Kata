SELECT 
  senshi_name as sailor_senshi, 
  real_name_jpn as real_name, 
  cats.name as cat, school as school
FROM sailorsenshi 
LEFT JOIN cats ON cat_id = cats.id
LEFT JOIN schools ON school_id = schools.id