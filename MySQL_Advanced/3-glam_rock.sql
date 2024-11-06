-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

USE hbtn_0d_tvshows

SELECT band_name, (split, 2024) - formed AS lifespan FROM metal_bands 
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
