syms x y z 
F_e = [x^2, 3*x*z^2, -2*x*z]; 
divergence_v_e = divergence(F_e, [x, y, z]) 
curl_v_e = curl(F_e, [x, y, z]) 
syms x y z 
F_b = [x*y, 2*y*z, 3*z*x]; 
divergence_v_b = divergence(F_b, [x, y, z]) 
curl_v_b = curl(F_b, [x, y, z]) 
syms x y z 
r_c = [y^2, (2*x*y + z^2), 2*y*z]; 
divergence_r_c = divergence(r_c, [x, y, z]) 
curl_r_c = curl(r_c, [x, y, z])
